# Data Types

The GUIDE Data Model describes column types at a logical level using the generic data types in each `Objects` record's `GenericDataType` field. The installable PostgreSQL DDL maps each generic type to a concrete PostgreSQL type.

## Mapping table

| Generic type (`GenericDataType`) | PostgreSQL type | Columns in 1.0.0 | Notes |
|---|---|---:|---|
| String (str or text) | `TEXT` | 3,590 | Variable-length string, no length cap. Most identifiers in 1.0.0 are text. |
| Datetime | `TIMESTAMP WITH TIME ZONE` | 1,452 | RFC 3339, time-zone aware. Used for audit timestamps. |
| Integer (bigint) | `BIGINT` | 1,024 | 64-bit signed integer. Used mainly for `CreatedBy`/`UpdatedBy`/`DeletedBy`. |
| Date | `DATE` | 784 | ISO 8601 (YYYY-MM-DD). |
| UUID | `UUID` | 498 | Used for `TenantIdentifier`. |
| Floating point (float) | `NUMERIC` | 250 | Arbitrary precision; preferred over `DOUBLE PRECISION` to preserve precision across transformations. |
| Boolean (bool) | `BOOLEAN` | 221 | True/false. Yes/No enumerations from source standards are modeled as booleans. |
| Integer (int) | `INTEGER` | 124 | 32-bit signed integer. |
| Character (char) | `CHAR(1)` | 0 | Single character. |
| Enumerated type (enum) | `TEXT` | 0 | The model does **not** use SQL enums: they are brittle to extend and can cause data loss. Enumerations from source standards are documented in `ExampleEnumerations` as guidance only. |
| Time | `TIME WITH TIME ZONE` | 0 | RFC 3339 (hh:mm:ss±hh:mm). |
| Timestamp | `BIGINT` | 0 | Unix epoch seconds, stored as an integer to preserve precision. |

The generator matches type names case-insensitively and stops with an error on any type it does not recognize, so a new or misspelled type can never silently become `TEXT`.

## Reference code lists

The `DataTypes` sheet also points to two external code lists used by some columns:

- **Geographic areas:** [BLS QCEW area titles](https://www.bls.gov/cew/classifications/areas/qcew-area-titles.htm)
- **Languages:** [ISO 639-2 language codes](https://www.loc.gov/standards/iso639-2/php/code_list.php)
