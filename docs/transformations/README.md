# Data Transformation Standards

The GUIDE Data Model is the target of transformations from many different source systems — SIS, CRM, LMS, and others. The quality of the data inside the model depends on those transformations preserving the meaning and precision of the source data.

This directory documents the standards that govern transformations:

- **[Transformation Standards](transformation-standards.md)** — DataKind's approach to data transformation and data quality
- **[Data Quality Tests](https://docs.google.com/document/d/1pn2CgiKAU2QLExp8_AeOeuImBHComDV9eC2PscwcER8/edit)** — an initial approach to AI-assisted data quality tests

## What the transformation standards aim to do

1. **Provide transparency.** Institutions adopting the GUIDE Data Model, or considering adopting it, should know what kinds of changes their data may undergo and what level of deviation is treated as acceptable. This lets each institution make an informed call about whether the model fits its data.
2. **Give examples of transformations to avoid.** Some transformations look reasonable but undermine the data's precision or correctness. Documenting these limits the risk of error in cases where the source data doesn't lend itself to a clean transformation.

Together, these are intended to build trust in the data flowing through the model — but they are only one piece of that trust. Data-quality tests run inside the [Data Observation Toolkit (DOT)](https://github.com/datakind/data-observation-toolkit), and the transformation code will be published in a future release.

## What the transformation standards do *not* do

- They do not eliminate discrepancies in source data — e.g. a student having two different "total credits earned" values across two source systems.
- They do not explain *why* an individual discrepancy exists for a given institution.
- They do not determine whether any specific institution's data is suitable for transformation. That judgment depends on the institution's data availability, format, and quality.

## How transformation fidelity is assured

Three complementary mechanisms:

### 1. Data monitoring and quality tests

The [Data Observation Toolkit (DOT)](https://github.com/datakind/data-observation-toolkit) uses [dbt](https://www.getdbt.com/) and [Great Expectations](https://greatexpectations.io/) to run quality checks against transformed data. Tests specific to the GUIDE Data Model cover identifier completeness, cross-column logic, and chronology.

### 2. Transparency in transformation code

Each transformation is tied to a source-system category (SIS, CRM, LMS) with notes on what the transformation does. Row-level lineage is carried in the model itself through `SourceSystemIdentifier`, `SourceSystemKeyValue`, and the `SourceSystem*Date` columns, and `SourceRaw*` columns preserve ambiguous or lossy source values alongside canonical ones.

### 3. Analytic standards for numeric columns

For numeric columns, we defined a conservative threshold based on power analysis: the magnitude of change that, on a 6,000-student sample, would only approach statistical significance in 20% of repeated random samples. This works out to **0.045 standard deviations**. Transformations exceeding this should be flagged for review.

More sophisticated approaches (distribution-comparison tests, synthetic-data validation) are possible but are highly specific to each transformation and don't generalize well. They're reserved for high-risk transformations.

## Issues unrelated to transformations

Some problems look like transformation issues but aren't:

- Data corruption or row drops during **ingestion**.
- Source data quality issues that **predate** ingestion (data entry errors, columns that should be numeric but contain alphabetic characters).
- Variability across institutions (2 vs. 4 decimal places for raw numeric columns; dates vs. datetimes).
- Misalignment between the data model and the ingested data (e.g. the model expects a date but the institution only provides a month).

These can produce results that look like transformation failures even when transformations are correct, or compromise data quality even when transformations pass every check. They're worth keeping in mind when investigating data issues.
