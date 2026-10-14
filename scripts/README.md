# `scripts/` — generators and validators

Utility scripts that build and verify the GUIDE Data Model specification. All of them read the **`Objects`** object of the model JSON (`sheets.Objects.records`), with table descriptions from `sheets.ObjectDesc.records`.

## What's here

| Script | Purpose |
| ------ | ------- |
| `generate_schema.py` | Read the model JSON and regenerate schemas, table DDL, foreign keys, indexes, install/teardown scripts, and per-entity Markdown. |
| `generate_erd.py` | Build the interactive HTML relationship explorer from the model JSON. |
| `validate_sql.py` | Run structural, PostgreSQL-identifier, FK-type, install-plan, and SQLite execution checks against the generated DDL. |
| `validate_postgres.py` | Install, count-check, tear down, and remove the model in an isolated temporary PostgreSQL cluster. |

## Typical workflow

When the model changes, export the workbook to JSON, bump [`../VERSION`](../VERSION), then from the repository root:

```bash
# 1. Regenerate SQL and entity Markdown docs
python scripts/generate_schema.py guide_data_model_schema_v1.0.0.json

# 2. Regenerate the relationship explorer
python scripts/generate_erd.py

# 3. Validate the DDL statically
python scripts/validate_sql.py

# 4. Verify in a real temporary PostgreSQL cluster
python scripts/validate_postgres.py
```

`generate_schema.py` prints the counts used in the documentation (tables and columns per entity, FK reference rows, constraints emitted, duplicates, skips, and indexes). Update the numbers in the READMEs and CHANGELOG from that output.

The generation commands are idempotent and overwrite their outputs; the validators are read-only.

### Terminology normalization

`generate_schema.py` has a short `TERMINOLOGY` list that rewrites the model's former name and a vendor-specific term in descriptions before they are written to SQL comments, entity pages, and the relationship explorer. The JSON itself is not changed. When those descriptions are fixed in the workbook, remove the entries.

## Dependencies

- Python 3.10+ (standard library only — no packages to install)
- PostgreSQL command-line tools for `validate_postgres.py`: `initdb`, `pg_ctl`, `createdb`, `psql`. Set `PG_BIN` if `initdb`/`pg_ctl` are not on your `PATH`, and run it as a non-root user.

See [`../spec/README.md`](../spec/README.md) for installation details.
