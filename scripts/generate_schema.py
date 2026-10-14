#!/usr/bin/env python3
"""
generate_schema.py — read the GUIDE Data Model JSON and emit PostgreSQL DDL
plus per-entity Markdown documentation.

The reference for the data model is the "Objects" object inside the JSON
export (``sheets.Objects.records``): one record per column, carrying the
Entity, Object, Column, Key, FKReference, Nullable, GenericDataType, Default,
and Description of that column. Table descriptions come from
``sheets.ObjectDesc.records``.

This is the build script that produces the contents of:
  spec/sql/001_create_schemas.sql
  spec/sql/tables/*.sql
  spec/sql/003_foreign_keys.sql
  spec/sql/004_indexes.sql
  spec/sql/install.sql
  spec/sql/teardown.sql
  docs/data-model/entities/*.md

Run from the repo root:
    python scripts/generate_schema.py [guide_data_model_schema_v1.0.0.json]

It is idempotent and overwrites the generated files.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = (REPO_ROOT / "VERSION").read_text().strip()
MODEL_NAME = "GUIDE Data Model"
DEFAULT_MODEL_JSON = REPO_ROOT / f"guide_data_model_schema_v{SCHEMA_VERSION}.json"

# ---------- Mappings -----------------------------------------------------------

# GenericDataType -> PostgreSQL type.
# - Timestamp (Unix seconds) maps to BIGINT to preserve precision.
# - Enumerated types map to TEXT: the model does not use SQL enums.
PG_TYPE = {
    "Integer (int)": "INTEGER",
    "Integer (bigint)": "BIGINT",
    "Floating point (float)": "NUMERIC",
    "Character (char)": "CHAR(1)",
    "String (str or text)": "TEXT",
    "Boolean (bool)": "BOOLEAN",
    "Enumerated type (enum)": "TEXT",
    "Date": "DATE",
    "Time": "TIME WITH TIME ZONE",
    "Datetime": "TIMESTAMP WITH TIME ZONE",
    "Timestamp": "BIGINT",
    "UUID": "UUID",
}

# Case-insensitive: GenericDataType casing has drifted across versions (e.g.
# "Floating Point" vs "Floating point"). An unknown type raises instead of
# silently falling back to TEXT.
PG_TYPE_CI = {k.casefold(): v for k, v in PG_TYPE.items()}

# Terminology normalization applied to descriptions rendered into SQL comments
# and Markdown. A few descriptions in the model still use the model's former
# name or a vendor-specific term; the published documentation uses the GUIDE
# name and source-system categories instead. Fix these upstream in the model
# workbook when possible, then remove the entries here.
TERMINOLOGY = [
    (re.compile(r"\bUDTS\b"), "GUIDE"),
    (re.compile(r"\bEllucian section\b"), "SIS section"),
]

# Postgres reserved words that need a suffix to be usable as identifiers.
# We add an `_x` suffix rather than quoting so unquoted SQL still works.
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

PG_MAX_IDENT = 63

ENTITY_ORDER = [
    "Core",
    "Person",
    "Engagement",
    "Academics",
    "Appointment",
    "Advising",
    "Finances",
    "Learner Success",
    "Supports",
    "Workforce",
    "Admissions",
]

ENTITY_DESCRIPTIONS = {
    "Core": "Tenancy, organizations, core person records, source systems, and shared reference data.",
    "Person": "Person profiles, demographics, identity, relationships, restrictions, and success plans.",
    "Engagement": "Surveys, forums, matching, streamed learning events, and recruitment attribution.",
    "Academics": "Courses, classes, programs, curriculum, enrollments, credit, transfer, credentials, and assessments.",
    "Appointment": "Appointment scheduling, agendas, and templates.",
    "Advising": "Caseloads, support assignments, early alerts, and intake.",
    "Finances": "Financial aid, scholarships, tuition, charges, and learner financial plans.",
    "Learner Success": "Learner-success plan item types.",
    "Supports": "Resources, wellness, goals, learner supports, housing, and dining.",
    "Workforce": "Career pathways, career plans, industry needs, job postings, employment, and resumes.",
    "Admissions": "Applications, checklist items, decisions, deposits, fees, and reviews.",
}


def safe_ident(name: str, max_len: int = PG_MAX_IDENT) -> str:
    """Make an identifier safe for Postgres: <=63 chars and not reserved."""
    n = name
    if n.lower() in PG_RESERVED:
        n = n + "_x"
    if len(n) > max_len:
        # Keep a recognizable prefix and append an 8-char digest of the original.
        digest = hashlib.md5(name.encode()).hexdigest()[:8]
        n = f"{name[:max_len - 9]}_{digest}"
    return n


def to_snake(name: str) -> str:
    """PascalCase -> snake_case. Handles consecutive caps like 'URL', 'ID'."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def schema_name(entity: str) -> str:
    """Convert an entity label into a legal PostgreSQL schema name."""
    snake = to_snake(entity)
    normalized = re.sub(r"[^a-z0-9_]+", "_", snake).strip("_")
    normalized = re.sub(r"_+", "_", normalized)
    return safe_ident(normalized)


def sql_col_name(name: str) -> str:
    """snake_case + Postgres-safe."""
    return safe_ident(to_snake(name))


def pg_type_for(column: str, generic: str) -> str:
    """Map the model's generic type to a PostgreSQL type."""
    pg_type = PG_TYPE_CI.get((generic or "").strip().casefold())
    if pg_type is None:
        raise ValueError(f"Unsupported GenericDataType {generic!r} for column {column!r}")
    return pg_type


def normalize_terms(text: str) -> str:
    for pattern, replacement in TERMINOLOGY:
        text = pattern.sub(replacement, text)
    return text


def render_default_clause(raw, pg_type: str) -> Optional[str]:
    """Translate the model's SQL Server-flavored defaults to PostgreSQL."""
    if raw is None or (isinstance(raw, str) and not raw.strip()):
        return None
    if isinstance(raw, bool):
        raw = "true" if raw else "false"
    text = str(raw).strip()
    upper = text.upper()

    if upper.startswith("NEXT VALUE FOR"):
        # Sequences only apply to integer identifiers; text identifiers are
        # assigned by the loading process.
        if pg_type not in {"INTEGER", "BIGINT"}:
            return None
        return "GENERATED BY DEFAULT AS IDENTITY"
    if upper.startswith("SYSUTCDATETIME"):
        return "DEFAULT CURRENT_TIMESTAMP"
    if text.startswith("N'") and text.endswith("'"):
        text = text[1:]
    if pg_type == "BOOLEAN":
        v = text.lower()
        if v in {"true", "1", "yes", "y"}:
            return "DEFAULT TRUE"
        if v in {"false", "0", "no", "n"}:
            return "DEFAULT FALSE"
    if pg_type in {"INTEGER", "NUMERIC", "BIGINT"}:
        return f"DEFAULT {text}"
    if text.startswith("'") and text.endswith("'"):
        text = text[1:-1]
    s = text.replace("'", "''")
    return f"DEFAULT '{s}'"


# ---------- Read the model JSON -----------------------------------------------


def load_model(json_path: Path):
    """Return ({table: {entity, columns}}, {table: description}) from the JSON.

    Columns keep the order in which they appear in the Objects records.
    """
    data = json.loads(json_path.read_text(encoding="utf-8"))
    sheets = data["sheets"]

    tables: dict[str, dict] = {}
    for r in sheets["Objects"]["records"]:
        obj, column = r.get("Object"), r.get("Column")
        if not obj or not column:
            continue
        col = {
            "column": column,
            "description": normalize_terms(r.get("Description") or ""),
            "key": (r.get("Key") or "").strip(),
            "fk_ref": (r.get("FKReference") or "").strip(),
            "nullable": (r.get("Nullable") or "").strip().upper(),
            "generic_type": (r.get("GenericDataType") or "").strip(),
            "default": r.get("Default"),
        }
        t = tables.setdefault(obj, {"entity": r.get("Entity"), "columns": []})
        if t["entity"] != r.get("Entity"):
            raise ValueError(f"{obj} has rows in more than one entity")
        t["columns"].append(col)

    descs = {}
    for r in sheets["ObjectDesc"]["records"]:
        obj = r.get("Object")
        if obj and obj not in descs:
            descs[obj] = normalize_terms(r.get("Description") or "")
    return tables, descs


# ---------- DDL emission ------------------------------------------------------


def _normalize_comment(text: str) -> str:
    """Collapse whitespace and escape quotes for a SQL string literal."""
    return " ".join(str(text).split()).replace("'", "''")


def render_create_table(table: str, info: dict, table_desc: str) -> str:
    """Emit a CREATE TABLE statement (without FK constraints; those come later)."""
    schema = schema_name(info["entity"])
    sql_table = safe_ident(to_snake(table))

    cols = info["columns"]
    pk_cols = [c["column"] for c in cols if "PK" in c["key"].upper()]

    lines = [f"-- {table}"]
    if table_desc:
        lines.append(wrap_comment(table_desc, prefix="-- "))
    lines.append(f"CREATE TABLE {schema}.{sql_table} (")

    col_lines = []
    for c in cols:
        pg = pg_type_for(c["column"], c["generic_type"])
        bits = [f"    {sql_col_name(c['column']):<48} {pg}"]
        if c["nullable"] == "N":
            bits.append("NOT NULL")
        default_clause = render_default_clause(c["default"], pg)
        if default_clause is not None:
            bits.append(default_clause)
        col_lines.append(" ".join(bits))

    if pk_cols:
        pk_sql_cols = ", ".join(sql_col_name(c) for c in pk_cols)
        pk_name = safe_ident(f"pk_{sql_table}")
        col_lines.append(f"    CONSTRAINT {pk_name} PRIMARY KEY ({pk_sql_cols})")

    lines.append(",\n".join(col_lines))
    lines.append(");")

    if table_desc:
        lines.append(f"COMMENT ON TABLE {schema}.{sql_table} IS '{_normalize_comment(table_desc)}';")
    for c in cols:
        if c["description"]:
            lines.append(
                f"COMMENT ON COLUMN {schema}.{sql_table}.{sql_col_name(c['column'])} "
                f"IS '{_normalize_comment(c['description'])}';"
            )

    lines.append("")
    return "\n".join(lines)


def wrap_comment(text: str, prefix: str = "-- ", width: int = 100) -> str:
    """Wrap a long string into SQL line comments."""
    out = []
    line = prefix
    for word in text.split():
        if len(line) + len(word) + 1 > width and line.strip() != prefix.strip():
            out.append(line.rstrip())
            line = prefix + word + " "
        else:
            line += word + " "
    if line.strip() != prefix.strip():
        out.append(line.rstrip())
    return "\n".join(out)


def parse_fk_refs(raw: str) -> list[str]:
    """Split an FKReference cell into its newline/comma-separated Table.Column entries."""
    entries = [e.strip() for e in raw.replace(",", "\n").split("\n")]
    return [e for e in entries if e]


def render_foreign_keys(tables: dict) -> tuple[str, dict]:
    """Emit PostgreSQL FK constraints from the model's FK references.

    FKReference usually names only the business identifier even though the
    target's PK is tenant-scoped (TenantIdentifier + identifier). When the
    source table carries the remaining target-PK columns under the same name,
    they are added to the emitted FK. References that cannot cover the
    target's complete primary key are skipped and listed at the end of the
    generated file.
    """
    lines = [
        f"-- Foreign key constraints for the {MODEL_NAME} {SCHEMA_VERSION}",
        "-- Generated by scripts/generate_schema.py — do not edit by hand.",
        "",
    ]
    stats = {"fk_rows": 0, "emitted": 0, "duplicates": 0, "skipped": 0}
    seen_constraints = set()
    seen_names = set()
    unresolved_log = []
    pk_by_table = {
        table: [c["column"] for c in info["columns"] if "PK" in c["key"].upper()]
        for table, info in tables.items()
    }

    for table, info in sorted(tables.items()):
        schema = schema_name(info["entity"])
        sql_table = safe_ident(to_snake(table))
        source_cols = {c["column"] for c in info["columns"]}

        for c in info["columns"]:
            if "FK" not in c["key"].upper() or not c["fk_ref"]:
                continue
            stats["fk_rows"] += 1

            entries = parse_fk_refs(c["fk_ref"])
            bad = [e for e in entries if not re.fullmatch(r"\w+\.\w+", e)]
            if bad or not entries:
                unresolved_log.append(f"  -- {table}.{c['column']}: unparseable reference {bad or c['fk_ref']!r}")
                continue
            target_tables = {e.split(".", 1)[0] for e in entries}
            referenced_cols = [e.split(".", 1)[1] for e in entries]

            if len(target_tables) != 1:
                unresolved_log.append(f"  -- {table}.{c['column']}: mixed targets {sorted(target_tables)}")
                continue
            ref_table = target_tables.pop()
            if ref_table not in tables:
                unresolved_log.append(f"  -- {table}.{c['column']}: unknown target table {ref_table}")
                continue

            ref_schema = schema_name(tables[ref_table]["entity"])
            ref_sql_table = safe_ident(to_snake(ref_table))
            target_pk = pk_by_table[ref_table]
            if not target_pk:
                unresolved_log.append(f"  -- {table}.{c['column']}: target {ref_table} has no primary key")
                continue
            if not set(referenced_cols).issubset(target_pk):
                unresolved_log.append(
                    f"  -- {table}.{c['column']}: target columns {referenced_cols} "
                    f"are not part of the PK of {ref_table} ({target_pk})"
                )
                continue

            # Emit columns in target-PK order. The FK row's own column supplies
            # the referenced identifier; remaining PK components must exist
            # under the same name in the source table.
            src_cols = []
            for target_col in target_pk:
                if target_col in referenced_cols:
                    src_cols.append(c["column"])
                elif target_col in source_cols:
                    src_cols.append(target_col)
                else:
                    break
            if len(src_cols) != len(target_pk):
                unresolved_log.append(
                    f"  -- {table}.{c['column']}: source lacks columns required for "
                    f"{ref_table} PK {target_pk}"
                )
                continue

            src_cols_sql = [sql_col_name(s) for s in src_cols]
            tgt_cols_sql = [sql_col_name(t) for t in target_pk]

            sig = (schema, sql_table, tuple(src_cols_sql), ref_schema, ref_sql_table, tuple(tgt_cols_sql))
            if sig in seen_constraints:
                stats["duplicates"] += 1
                continue
            seen_constraints.add(sig)

            # Constraint names only need to be unique per table, but globally
            # unique names are easier to grep.
            cname = safe_ident(f"fk_{sql_table}_{'_'.join(src_cols_sql)}_{ref_sql_table}")
            if cname in seen_names:
                n = 2
                while f"{cname[:60]}_{n}" in seen_names:
                    n += 1
                cname = f"{cname[:60]}_{n}"
            seen_names.add(cname)

            lines.append(
                f"ALTER TABLE {schema}.{sql_table}\n"
                f"    ADD CONSTRAINT {cname}\n"
                f"    FOREIGN KEY ({', '.join(src_cols_sql)})\n"
                f"    REFERENCES {ref_schema}.{ref_sql_table} ({', '.join(tgt_cols_sql)});\n"
            )
            stats["emitted"] += 1

    stats["skipped"] = len(unresolved_log)
    if unresolved_log:
        lines.append("")
        lines.append(f"-- Skipped FK references that cannot cover the target primary key ({len(unresolved_log)}):")
        lines.extend(unresolved_log)
    lines.append("")
    return "\n".join(lines), stats


def render_indexes(tables: dict) -> tuple[str, int]:
    """Emit indexes on every non-PK FK column. PKs are already indexed by Postgres."""
    lines = [
        f"-- Indexes on foreign key columns for the {MODEL_NAME} {SCHEMA_VERSION}",
        "-- Postgres automatically indexes primary keys; FK columns need explicit",
        "-- indexes to keep join performance reasonable.",
        "",
    ]
    seen = set()
    for table, info in sorted(tables.items()):
        schema = schema_name(info["entity"])
        sql_table = safe_ident(to_snake(table))
        for c in info["columns"]:
            key = c["key"].upper()
            if "FK" not in key or "PK" in key:
                continue
            col_sql = sql_col_name(c["column"])
            idx_name = safe_ident(f"idx_{sql_table}_{col_sql}")
            if idx_name in seen:
                continue
            seen.add(idx_name)
            lines.append(f"CREATE INDEX {idx_name} ON {schema}.{sql_table} ({col_sql});")
    lines.append("")
    return "\n".join(lines), len(seen)


# ---------- Markdown docs -----------------------------------------------------


def render_entity_markdown(entity: str, tables_in_entity: dict, descs: dict) -> str:
    """A single Markdown page documenting every table in an entity."""
    schema = schema_name(entity)
    out = [
        f"# Entity: {entity}",
        "",
        f"This page documents every table that belongs to the **{entity}** entity "
        f"in the {MODEL_NAME} {SCHEMA_VERSION}. Tables are listed alphabetically. Each "
        f"table lists its columns, PostgreSQL types, primary/foreign keys, and "
        f"descriptions, as they appear in the `Objects` records of the model JSON.",
        "",
        f"**Tables in this entity: {len(tables_in_entity)}**",
        "",
        "## Table of contents",
        "",
    ]
    for t in sorted(tables_in_entity):
        out.append(f"- [{t}](#{t.lower()})")
    out += ["", "---", ""]

    for t in sorted(tables_in_entity):
        info = tables_in_entity[t]
        out += [f"## {t}", "", f"**SQL identifier:** `{schema}.{safe_ident(to_snake(t))}`", ""]
        if descs.get(t):
            out += [descs[t], ""]
        out.append("| Column | Type | Key | Nullable | Description |")
        out.append("|---|---|---|---|---|")
        for c in info["columns"]:
            pg = pg_type_for(c["column"], c["generic_type"])
            key = c["key"] or ""
            refs = parse_fk_refs(c["fk_ref"]) if c["fk_ref"] else []
            if refs:
                key = f"{key} → " + ", ".join(f"`{r}`" for r in refs)
            nullable = "No" if c["nullable"] == "N" else "Yes"
            desc = " ".join(c["description"].split()).replace("|", "\\|")
            out.append(f"| `{sql_col_name(c['column'])}` | `{pg}` | {key} | {nullable} | {desc} |")
        out.append("")
    return "\n".join(out)


def ordered_entities(by_entity: dict[str, dict]) -> list[str]:
    """Return stable entity order, preserving any future additions."""
    known = [entity for entity in ENTITY_ORDER if entity in by_entity]
    return known + sorted(set(by_entity) - set(known))


def entity_sql_filename(position: int, entity: str) -> str:
    return f"{position:02d}_{schema_name(entity)}.sql"


def banner(title: str, *extra: str) -> list[str]:
    rule = "-- " + "=" * 76
    return [rule, f"-- {MODEL_NAME} {SCHEMA_VERSION} — {title}",
            "-- Generated by scripts/generate_schema.py — do not edit by hand.",
            *(f"-- {e}" for e in extra), rule, ""]


def render_create_schemas(entities: list[str]) -> str:
    lines = banner("create schemas")
    lines += [f"CREATE SCHEMA IF NOT EXISTS {schema_name(e)};" for e in entities]
    lines.append("")
    for e in entities:
        description = _normalize_comment(ENTITY_DESCRIPTIONS.get(e, f"{MODEL_NAME} {e} entity."))
        lines.append(f"COMMENT ON SCHEMA {schema_name(e)} IS '{description}';")
    lines.append("")
    return "\n".join(lines)


def render_install(entities: list[str]) -> str:
    # \ir resolves paths relative to this file, so install.sql works from any
    # working directory.
    lines = banner("master install script") + [
        r"\set ON_ERROR_STOP on",
        "BEGIN;",
        "",
        r"\echo 'Creating schemas...'",
        r"\ir 001_create_schemas.sql",
        "",
        r"\echo 'Creating tables (entity by entity)...'",
    ]
    lines += [rf"\ir tables/{entity_sql_filename(i, e)}" for i, e in enumerate(entities, start=1)]
    lines += [
        "",
        r"\echo 'Adding foreign key constraints...'",
        r"\ir 003_foreign_keys.sql",
        "",
        r"\echo 'Creating indexes on foreign keys...'",
        r"\ir 004_indexes.sql",
        "",
        "COMMIT;",
        rf"\echo 'Done. {MODEL_NAME} {SCHEMA_VERSION} installed.'",
        "",
    ]
    return "\n".join(lines)


def render_teardown(entities: list[str]) -> str:
    lines = banner("teardown", "DROPs every GUIDE schema and all of its contents. Use with care.")
    lines += ["SET client_min_messages = warning;  -- silence per-object CASCADE notices", ""]
    lines += [f"DROP SCHEMA IF EXISTS {schema_name(e)} CASCADE;" for e in reversed(entities)]
    lines.append("")
    return "\n".join(lines)


# ---------- Main --------------------------------------------------------------


def main(json_path: Path) -> None:
    tables, descs = load_model(json_path)
    column_count = sum(len(t["columns"]) for t in tables.values())
    print(f"Loaded {len(tables)} tables and {column_count} columns from {json_path.name}.")

    by_entity: dict[str, dict] = defaultdict(dict)
    for t, info in tables.items():
        by_entity[info["entity"]][t] = info
    entities = ordered_entities(by_entity)

    sql_dir = REPO_ROOT / "spec" / "sql"
    tables_dir = sql_dir / "tables"
    docs_dir = REPO_ROOT / "docs" / "data-model" / "entities"
    tables_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Remove stale generated entity artifacts before writing the current set.
    for stale in [*tables_dir.glob("*.sql"), *docs_dir.glob("*.md")]:
        stale.unlink()

    def write(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")
        print(f"  wrote {path.relative_to(REPO_ROOT)}")

    write(sql_dir / "001_create_schemas.sql", render_create_schemas(entities))
    for i, entity in enumerate(entities, start=1):
        lines = banner(f"{entity} entity", f"{len(by_entity[entity])} tables")
        for t in sorted(by_entity[entity]):
            lines.append(render_create_table(t, by_entity[entity][t], descs.get(t, "")))
        write(tables_dir / entity_sql_filename(i, entity), "\n".join(lines))

    fk_sql, fk_stats = render_foreign_keys(tables)
    write(sql_dir / "003_foreign_keys.sql", fk_sql)
    idx_sql, idx_count = render_indexes(tables)
    write(sql_dir / "004_indexes.sql", idx_sql)
    write(sql_dir / "install.sql", render_install(entities))
    write(sql_dir / "teardown.sql", render_teardown(entities))

    for entity in entities:
        write(docs_dir / f"{schema_name(entity)}.md",
              render_entity_markdown(entity, by_entity[entity], descs))

    print()
    print(f"Entities: {len(entities)}")
    for entity in entities:
        n_cols = sum(len(t["columns"]) for t in by_entity[entity].values())
        print(f"  {entity:<16} {schema_name(entity):<16} {len(by_entity[entity]):>4} tables {n_cols:>5} columns")
    print(f"FK reference rows: {fk_stats['fk_rows']}")
    print(f"FK constraints emitted: {fk_stats['emitted']} "
          f"(duplicates collapsed: {fk_stats['duplicates']}, skipped: {fk_stats['skipped']})")
    print(f"Indexes: {idx_count}")
    print("\nDone.")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MODEL_JSON)
