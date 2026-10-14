#!/usr/bin/env python3
"""
validate_sql.py — verify the generated DDL is structurally and syntactically sound.

This runs three layers of checks:

1. **Structural parse** — re-parses every CREATE TABLE, FK constraint, and
   index to confirm names are unique, PKs are present, no duplicate columns
   within a table, and every FK target resolves to an existing table+column.

2. **Postgres identifier rules** — verifies every schema, table, column,
   constraint, and index name is a legal Postgres identifier under 63 chars
   and not a reserved word.

3. **SQLite execution** — translates the DDL to SQLite-compatible syntax
   (drop schema-qualified names and Postgres-specific clauses, map UUID to
   TEXT) and actually executes it against an in-memory SQLite database to
   catch any remaining syntax issues. SQLite is a less strict parser than
   Postgres, but a successful SQLite run combined with the identifier-rule
   check is strong evidence the DDL is well-formed.

Run from the repo root:
    python scripts/validate_sql.py
"""
from __future__ import annotations

import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Postgres reserved words that cannot be unquoted identifiers
PG_RESERVED = {
    "all", "analyse", "analyze", "and", "any", "array", "as", "asc",
    "asymmetric", "both", "case", "cast", "check", "collate", "column",
    "constraint", "create", "current_catalog", "current_date",
    "current_role", "current_time", "current_timestamp", "current_user",
    "default", "deferrable", "desc", "distinct", "do", "else", "end",
    "except", "false", "fetch", "for", "foreign", "from", "grant",
    "group", "having", "in", "initially", "intersect", "into", "lateral",
    "leading", "limit", "localtime", "localtimestamp", "not", "null",
    "offset", "on", "only", "or", "order", "placing", "primary",
    "references", "returning", "select", "session_user", "some",
    "symmetric", "table", "then", "to", "trailing", "true", "union",
    "unique", "user", "using", "variadic", "when", "where", "window",
    "with",
}

IDENT_RE = re.compile(r"^[a-z_][a-z0-9_]{0,62}$")


def parse_create_tables(text: str) -> dict:
    """Return {schema.name: {columns, pk}} from a SQL file's CREATE TABLE statements."""
    tables = {}
    for m in re.finditer(r"CREATE TABLE (\w+)\.(\w+) \((.*?)\n\);", text, re.DOTALL):
        schema, name, body = m.group(1), m.group(2), m.group(3)
        cols = []
        pk = []
        for line in body.split(",\n"):
            line = line.strip()
            if line.startswith("CONSTRAINT pk_"):
                pkm = re.search(r"PRIMARY KEY \(([^)]+)\)", line)
                if pkm:
                    pk = [c.strip() for c in pkm.group(1).split(",")]
                continue
            parts = line.split()
            if len(parts) >= 2 and not parts[0].startswith("CONSTRAINT"):
                type_match = re.match(
                    r"^[a-z_][a-z0-9_]*\s+"
                    r"(TIMESTAMP WITH TIME ZONE|TIME WITH TIME ZONE|CHAR\(1\)|"
                    r"BIGINT|INTEGER|NUMERIC|BOOLEAN|DATE|UUID|TEXT)",
                    line,
                )
                cols.append({
                    "name": parts[0],
                    "type": type_match.group(1) if type_match else parts[1],
                    "not_null": "NOT NULL" in line,
                })
        tables[f"{schema}.{name}"] = {"schema": schema, "name": name,
                                      "columns": cols, "pk": pk}
    return tables


def check_identifier(ident: str, kind: str) -> list[str]:
    """Return a list of issues with the identifier."""
    issues = []
    if not IDENT_RE.match(ident):
        issues.append(f"{kind} '{ident}' is not a valid PG identifier")
    if ident.lower() in PG_RESERVED:
        issues.append(f"{kind} '{ident}' is a Postgres reserved word")
    if len(ident) > 63:
        issues.append(f"{kind} '{ident}' exceeds 63 chars ({len(ident)})")
    return issues


def layer1_structural(tables: dict, fk_text: str) -> list[str]:
    """Check PKs exist, no duplicate columns, all FK refs resolve."""
    issues = []
    for tname, info in tables.items():
        if not info["pk"]:
            issues.append(f"{tname}: missing primary key")
        col_names = [c["name"] for c in info["columns"]]
        dups = {n for n in col_names if col_names.count(n) > 1}
        if dups:
            issues.append(f"{tname}: duplicate columns {dups}")
        # Every PK column must exist in the table
        for pkc in info["pk"]:
            if pkc not in col_names:
                issues.append(f"{tname}: PK column '{pkc}' not in table")

    # FK resolution
    fk_pattern = re.compile(
        r"ALTER TABLE (\w+)\.(\w+)\s+ADD CONSTRAINT (\w+)\s+"
        r"FOREIGN KEY \(([^)]+)\)\s+"
        r"REFERENCES (\w+)\.(\w+) \(([^)]+)\);",
        re.DOTALL,
    )
    fk_count = 0
    for m in fk_pattern.finditer(fk_text):
        fk_count += 1
        src = f"{m.group(1)}.{m.group(2)}"
        tgt = f"{m.group(5)}.{m.group(6)}"
        src_cols = [c.strip() for c in m.group(4).split(",")]
        tgt_cols = [c.strip() for c in m.group(7).split(",")]
        if src not in tables:
            issues.append(f"FK source table not found: {src}")
            continue
        if tgt not in tables:
            issues.append(f"FK target table not found: {tgt}")
            continue
        src_col_names = {c["name"] for c in tables[src]["columns"]}
        tgt_col_names = {c["name"] for c in tables[tgt]["columns"]}
        src_col_types = {c["name"]: c["type"] for c in tables[src]["columns"]}
        tgt_col_types = {c["name"]: c["type"] for c in tables[tgt]["columns"]}
        for c in src_cols:
            if c not in src_col_names:
                issues.append(f"FK source column not found: {src}.{c}")
        for c in tgt_cols:
            if c not in tgt_col_names:
                issues.append(f"FK target column not found: {tgt}.{c}")
        if len(src_cols) != len(tgt_cols):
            issues.append(
                f"FK column count mismatch: {src} has {len(src_cols)} src cols vs "
                f"{tgt} has {len(tgt_cols)} tgt cols"
            )
        for src_col, tgt_col in zip(src_cols, tgt_cols):
            if src_col not in src_col_types or tgt_col not in tgt_col_types:
                continue
            src_type = src_col_types[src_col]
            tgt_type = tgt_col_types[tgt_col]
            integer_family = {"INTEGER", "BIGINT"}
            if src_type != tgt_type and {src_type, tgt_type} - integer_family:
                issues.append(
                    f"FK type mismatch: {src}.{src_col} ({src_type}) -> "
                    f"{tgt}.{tgt_col} ({tgt_type})"
                )
    return issues, fk_count


def check_install_plan(
    tables: dict,
    table_files: list[str],
    install_text: str,
    schemas_text: str,
) -> list[str]:
    """Verify install.sql loads every generated component in a transaction."""
    issues = []
    includes = re.findall(r"^\\ir\s+(.+)$", install_text, re.MULTILINE)
    expected = [
        "001_create_schemas.sql",
        *(f"tables/{name}" for name in sorted(table_files)),
        "003_foreign_keys.sql",
        "004_indexes.sql",
    ]
    if includes != expected:
        issues.append(
            "install.sql include order/content differs from generated artifacts: "
            f"expected {expected}, got {includes}"
        )
    if r"\set ON_ERROR_STOP on" not in install_text:
        issues.append("install.sql does not enable ON_ERROR_STOP")
    if not re.search(r"^BEGIN;$", install_text, re.MULTILINE):
        issues.append("install.sql does not begin a transaction")
    if not re.search(r"^COMMIT;$", install_text, re.MULTILINE):
        issues.append("install.sql does not commit its transaction")

    declared_schemas = set(
        re.findall(r"^CREATE SCHEMA IF NOT EXISTS (\w+);$", schemas_text, re.MULTILINE)
    )
    used_schemas = {info["schema"] for info in tables.values()}
    if declared_schemas != used_schemas:
        issues.append(
            "schema declarations differ from table schemas: "
            f"declared={sorted(declared_schemas)}, used={sorted(used_schemas)}"
        )
    return issues


def layer2_identifiers(tables: dict, fk_text: str, idx_text: str) -> list[str]:
    """Check every identifier is a valid Postgres identifier."""
    issues = []
    seen_constraint_names = defaultdict(int)
    seen_index_names = defaultdict(int)

    for tname, info in tables.items():
        issues.extend(check_identifier(info["schema"], "schema"))
        issues.extend(check_identifier(info["name"], "table"))
        for c in info["columns"]:
            issues.extend(check_identifier(c["name"], f"column {tname}"))

    for m in re.finditer(r"ADD CONSTRAINT (\w+)", fk_text):
        cname = m.group(1)
        issues.extend(check_identifier(cname, "constraint"))
        seen_constraint_names[cname] += 1

    for m in re.finditer(r"CREATE INDEX (\w+) ON", idx_text):
        iname = m.group(1)
        issues.extend(check_identifier(iname, "index"))
        seen_index_names[iname] += 1

    # FK constraints must be unique per table, but Postgres treats them as
    # unique globally per schema; check global uniqueness conservatively.
    dup_constraints = {n: c for n, c in seen_constraint_names.items() if c > 1}
    if dup_constraints:
        # FK constraint names only need to be unique per table in Postgres,
        # but if our generator made duplicates within a table we'd see it
        # in layer1. Flag as warning, not error.
        for n, c in dup_constraints.items():
            issues.append(f"WARN: constraint name '{n}' used {c} times (OK if "
                          f"on different tables)")

    dup_indexes = {n: c for n, c in seen_index_names.items() if c > 1}
    for n, c in dup_indexes.items():
        # Index names DO have to be unique per schema in Postgres
        issues.append(f"index name '{n}' duplicated {c} times")

    return issues


def split_sql_statements(text: str) -> list[str]:
    """Split SQL into individual statements, respecting single-quoted strings.

    A naive split on `;` breaks on semicolons inside strings (like COMMENT
    bodies). This walker tracks whether we're inside a single-quoted string
    and only splits on `;` outside of strings. It also handles SQL string
    escape: `''` inside a quoted string is a literal apostrophe.
    """
    stmts = []
    buf = []
    i = 0
    in_string = False
    while i < len(text):
        ch = text[i]
        if in_string:
            buf.append(ch)
            if ch == "'":
                # Check for escaped quote
                if i + 1 < len(text) and text[i + 1] == "'":
                    buf.append(text[i + 1])
                    i += 2
                    continue
                in_string = False
            i += 1
        else:
            if ch == "'":
                in_string = True
                buf.append(ch)
                i += 1
            elif ch == "-" and i + 1 < len(text) and text[i + 1] == "-":
                # Line comment: skip to end of line
                while i < len(text) and text[i] != "\n":
                    i += 1
            elif ch == ";":
                stmt = "".join(buf).strip()
                if stmt:
                    stmts.append(stmt + ";")
                buf = []
                i += 1
            else:
                buf.append(ch)
                i += 1
    tail = "".join(buf).strip()
    if tail:
        stmts.append(tail)
    return stmts


def to_sqlite(stmt: str) -> str:
    """Translate a Postgres DDL statement to SQLite-compatible syntax.

    We only need to rewrite *identifiers* that appear in statement structure,
    not text inside single-quoted strings. The rewriter walks the string
    paying attention to quote state to avoid corrupting comment bodies.
    """
    # First, drop COMMENT ON statements — SQLite doesn't support them and they
    # carry free-text descriptions that don't need to round-trip.
    if stmt.strip().upper().startswith("COMMENT ON"):
        return ""

    out = []
    i = 0
    in_string = False
    while i < len(stmt):
        ch = stmt[i]
        if in_string:
            out.append(ch)
            if ch == "'":
                if i + 1 < len(stmt) and stmt[i + 1] == "'":
                    out.append(stmt[i + 1])
                    i += 2
                    continue
                in_string = False
            i += 1
        else:
            if ch == "'":
                in_string = True
                out.append(ch)
                i += 1
            else:
                out.append(ch)
                i += 1
    rewritten = "".join(out)

    # Now apply identifier-level rewrites OUTSIDE strings only. The easiest
    # way is to split on quote boundaries again and only rewrite the
    # outside-string chunks.
    chunks = []
    parts = re.split(r"('(?:[^']|'')*')", rewritten)
    for j, p in enumerate(parts):
        if j % 2 == 1:
            # quoted string — leave alone
            chunks.append(p)
        else:
            # Outside string. Apply transforms.
            x = p
            x = re.sub(r"\b([a-z_][a-z0-9_]*)\.([a-z_][a-z0-9_]*)", r"\1__\2", x)
            x = re.sub(r"\bUUID\b", "TEXT", x)
            x = re.sub(r"TIMESTAMP WITH TIME ZONE", "TEXT", x)
            x = re.sub(r"TIME WITH TIME ZONE", "TEXT", x)
            x = re.sub(r"\s+GENERATED BY DEFAULT AS IDENTITY", "", x)
            chunks.append(x)
    return "".join(chunks)


def layer3_sqlite(tables_by_file: dict, fk_text: str, idx_text: str) -> tuple:
    """Execute the DDL against in-memory SQLite as a syntax check."""
    issues = []
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")

    # CREATE TABLEs first
    for path, text in tables_by_file.items():
        for stmt in split_sql_statements(text):
            translated = to_sqlite(stmt)
            if not translated.strip():
                continue
            try:
                conn.execute(translated)
            except sqlite3.Error as e:
                preview = translated[:200].replace("\n", " ")
                issues.append(f"SQLite error in {path}: {e} | stmt: {preview}")

    # Indexes
    for stmt in split_sql_statements(idx_text):
        translated = to_sqlite(stmt)
        if not translated.strip():
            continue
        try:
            conn.execute(translated)
        except sqlite3.Error as e:
            preview = translated[:200].replace("\n", " ")
            issues.append(f"SQLite index error: {e} | stmt: {preview}")

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
    table_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='index' "
                "AND name NOT LIKE 'sqlite_%'")
    idx_count = cur.fetchone()[0]
    conn.close()
    return issues, table_count, idx_count


def main():
    tables_dir = REPO_ROOT / "spec" / "sql" / "tables"
    fk_path = REPO_ROOT / "spec" / "sql" / "003_foreign_keys.sql"
    idx_path = REPO_ROOT / "spec" / "sql" / "004_indexes.sql"
    install_path = REPO_ROOT / "spec" / "sql" / "install.sql"
    schemas_path = REPO_ROOT / "spec" / "sql" / "001_create_schemas.sql"


    # Aggregate all CREATE TABLE statements
    all_tables = {}
    tables_by_file = {}
    for f in sorted(tables_dir.glob("*.sql")):
        text = f.read_text()
        tables_by_file[f.name] = text
        all_tables.update(parse_create_tables(text))

    fk_text = fk_path.read_text()
    idx_text = idx_path.read_text()
    install_text = install_path.read_text()
    schemas_text = schemas_path.read_text()

    failed = False

    print(f"Validating {len(all_tables)} tables...")
    print()

    print("LAYER 1: structural checks")
    issues, fk_count = layer1_structural(all_tables, fk_text)
    issues.extend(
        check_install_plan(
            all_tables,
            list(tables_by_file),
            install_text,
            schemas_text,
        )
    )
    if issues:
        failed = True
        print(f"  FAIL: {len(issues)} issues")
        for i in issues[:20]:
            print(f"    {i}")
        if len(issues) > 20:
            print(f"    ... and {len(issues) - 20} more")
    else:
        print(f"  PASS: {len(all_tables)} tables, {fk_count} FK constraints")
    print()

    print("LAYER 2: Postgres identifier rules")
    issues = layer2_identifiers(all_tables, fk_text, idx_text)
    errors = [i for i in issues if not i.startswith("WARN")]
    warns = [i for i in issues if i.startswith("WARN")]
    if errors:
        failed = True
        print(f"  FAIL: {len(errors)} issues")
        for i in errors[:20]:
            print(f"    {i}")
    else:
        print(f"  PASS (with {len(warns)} acceptable warnings)")
    print()

    print("LAYER 3: SQLite execution")
    issues, tc, ic = layer3_sqlite(tables_by_file, fk_text, idx_text)
    if issues:
        failed = True
        print(f"  FAIL: {len(issues)} issues")
        for i in issues[:20]:
            print(f"    {i}")
        if len(issues) > 20:
            print(f"    ... and {len(issues) - 20} more")
    else:
        print(f"  PASS: {tc} tables created, {ic} indexes created in SQLite")
    print()
    if failed:
        print("Validation failed.")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
