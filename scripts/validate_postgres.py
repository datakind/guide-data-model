#!/usr/bin/env python3
"""Install and tear down the GUIDE Data Model in an isolated temporary PostgreSQL cluster.

Run from the repo root:
    python scripts/validate_postgres.py

Requires the PostgreSQL server binaries (initdb, pg_ctl) plus createdb and psql.
If initdb/pg_ctl are not on PATH (Debian/Ubuntu install them under
/usr/lib/postgresql/<version>/bin), set PG_BIN to that directory.
"""

from __future__ import annotations

import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = REPO_ROOT / "spec" / "sql"


def executable(name: str) -> str:
    path = shutil.which(name, path=os.environ.get("PG_BIN")) or shutil.which(name)
    if path is None:
        raise RuntimeError(f"Required PostgreSQL executable not found: {name}")
    return path


def run(command: list[str], *, capture: bool = False) -> str:
    result = subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip() if capture else ""


def available_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def expected_counts() -> tuple[list[str], int, int, int]:
    schemas_text = (SQL_DIR / "001_create_schemas.sql").read_text()
    schemas = re.findall(r"^CREATE SCHEMA IF NOT EXISTS (\w+);", schemas_text, re.M)
    table_count = sum(
        len(re.findall(r"^CREATE TABLE ", path.read_text(), re.M))
        for path in (SQL_DIR / "tables").glob("*.sql")
    )
    fk_count = len(
        re.findall(
            r"^ALTER TABLE ",
            (SQL_DIR / "003_foreign_keys.sql").read_text(),
            re.M,
        )
    )
    index_count = len(
        re.findall(
            r"^CREATE INDEX ",
            (SQL_DIR / "004_indexes.sql").read_text(),
            re.M,
        )
    )
    return schemas, table_count, fk_count, index_count


def main() -> None:
    initdb = executable("initdb")
    pg_ctl = executable("pg_ctl")
    createdb = executable("createdb")
    psql = executable("psql")
    schemas, expected_tables, expected_fks, expected_indexes = expected_counts()

    with tempfile.TemporaryDirectory(prefix="guide-postgres-") as temp:
        temp_path = Path(temp)
        data_dir = temp_path / "data"
        socket_dir = temp_path / "socket"
        socket_dir.mkdir()
        port = available_port()
        started = False
        try:
            run([initdb, "-D", str(data_dir), "--no-locale", "--encoding=UTF8"])
            run([
                pg_ctl,
                "-D",
                str(data_dir),
                "-o",
                f"-F -k {socket_dir} -p {port}",
                "-w",
                "start",
            ])
            started = True
            connection = ["-h", str(socket_dir), "-p", str(port), "-d", "guide_test"]
            run([createdb, "-h", str(socket_dir), "-p", str(port), "guide_test"])
            run([
                psql,
                "-X",
                "-v",
                "ON_ERROR_STOP=1",
                *connection,
                "-f",
                "spec/sql/install.sql",
            ])

            schema_list = ",".join(f"'{schema}'" for schema in schemas)
            query = (
                "SELECT count(*) FROM information_schema.tables "
                f"WHERE table_schema IN ({schema_list}) AND table_type='BASE TABLE';"
                "SELECT count(*) FROM pg_constraint c JOIN pg_namespace n "
                "ON n.oid=c.connamespace "
                f"WHERE c.contype='f' AND n.nspname IN ({schema_list});"
                "SELECT count(*) FROM pg_indexes "
                f"WHERE schemaname IN ({schema_list}) AND indexname LIKE 'idx_%';"
            )
            actual = [
                int(value)
                for value in run([psql, "-X", "-At", *connection, "-c", query], capture=True).splitlines()
            ]
            expected = [expected_tables, expected_fks, expected_indexes]
            if actual != expected:
                raise RuntimeError(f"PostgreSQL counts differ: expected {expected}, got {actual}")

            run([
                psql,
                "-X",
                "-v",
                "ON_ERROR_STOP=1",
                *connection,
                "-f",
                "spec/sql/teardown.sql",
            ])
            remaining = int(run([
                psql,
                "-X",
                "-At",
                *connection,
                "-c",
                f"SELECT count(*) FROM information_schema.schemata WHERE schema_name IN ({schema_list});",
            ], capture=True))
            if remaining:
                raise RuntimeError(f"Teardown left {remaining} GUIDE schemas")

            print(
                f"PASS: PostgreSQL installed and removed {expected_tables} tables, "
                f"{expected_fks} foreign keys, and {expected_indexes} indexes."
            )
        except subprocess.CalledProcessError as error:
            if error.stderr:
                print(error.stderr.strip(), file=sys.stderr)
            raise
        finally:
            if started:
                subprocess.run(
                    [pg_ctl, "-D", str(data_dir), "-m", "fast", "stop"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                )


if __name__ == "__main__":
    main()
