# Examples

This directory will eventually hold:

- **Sample data** — a small set of synthetic records covering core tables, suitable for a quick install-and-query demo.
- **Example queries** — common SQL patterns against the GUIDE Data Model schema (find a learner's full academic history, compute a course's enrollment over time, etc.).

If you're using the GUIDE Data Model 1.0.0 today and want to load synthetic data, install the schema (see the [README](../README.md#quick-install)) and use the `Objects` records in [`../guide_data_model_schema_v1.0.0.json`](../guide_data_model_schema_v1.0.0.json) and the entity documentation in [`../docs/data-model/entities/`](../docs/data-model/entities/) as field references. Start with `core.tenant`: every tenant-scoped table references it.
