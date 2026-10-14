# GUIDE Data Model

[Version](VERSION): **1.0.0**

The GUIDE Data Model is an open-source, public-good data model that harmonizes data from the many source systems used in higher education — Student Information Systems (SIS), Customer Relationship Management systems (CRM), Learning Management Systems (LMS), and others — into a single canonical representation that institutions can adopt without licensing fees.

For the motivations behind the data model and where it is going, see [OVERVIEW.md](OVERVIEW.md).

This repository contains everything an institution or implementer needs to understand, install, and contribute to the model:

- The **data model reference**: the `Objects` object in `[guide_data_model_schema_v1.0.0.json](guide_data_model_schema_v1.0.0.json)`, with the authoring workbook `[guide_data_model_schema_v1.0.0.xlsx](guide_data_model_schema_v1.0.0.xlsx)` alongside it
- **Documentation** of entities, columns, data types, and transformation standards under [docs/](docs/)
- The **installable specification** (PostgreSQL DDL) under [spec/](spec/)
- **Tooling** for generation and validation under [scripts/](scripts/)



## Status

**GUIDE Data Model 1.0.0** reflects the mapping of the model against SIS, LMS and CRM data. It defines **500 objects** and **7,943 columns** across **11 entities**, and installs cleanly on PostgreSQL. See [CHANGELOG.md](CHANGELOG.md) for release details.

## The data model reference

The single reference for the data model is the `Objects` object in the model JSON:

```
guide_data_model_schema_v1.0.0.json
└── sheets
    ├── Objects        ← the data model: one record per column (7,943 records)
    ├── ObjectDesc     ← one description per object (500 records)
    ├── DataTypes      ← generic data type definitions
    ├── Decisions      ← key design decisions and the version that added them (132 records)
    └── Index          ← what each sheet contains
```

Each record in `sheets.Objects.records` describes one column of one object:


| Field                             | Meaning                                                        |
| --------------------------------- | -------------------------------------------------------------- |
| `VersionAdded` / `VersionUpdated` | Model version that added or last changed the column            |
| `Entity` / `Sub-Entity`           | Domain grouping; each entity becomes one PostgreSQL schema     |
| `Object`                          | Table name (PascalCase, e.g. `CourseLookup`)                   |
| `Column`                          | Column name (PascalCase, e.g. `CourseIdentifier`)              |
| `Description`                     | What the column holds                                          |
| `Key`                             | `PK`, `FK`, or `PK, FK`                                        |
| `FKReference`                     | Target of a foreign key, as `Table.Column`                     |
| `Nullable`                        | `Y` or `N`                                                     |
| `GenericDataType`                 | Logical type — see [data types](docs/data-model/data-types.md) |
| `Default`                         | Default value, if any                                          |
| `Example` / `ExampleEnumerations` | Illustrative values                                            |
| `Comment`                         | Modeling notes                                                 |


Everything else in this repository — the SQL, the entity reference pages, and the relationship explorer — is generated from `Objects` (plus table descriptions from `ObjectDesc`) by `[scripts/generate_schema.py](scripts/generate_schema.py)` and `[scripts/generate_erd.py](scripts/generate_erd.py)`. The JSON is an export of the workbook; when the two disagree, regenerate the JSON from the workbook rather than editing either by hand.

## Repository layout

```
guide-data-model/
├── README.md                              You are here
├── OVERVIEW.md                            Why the model exists and where it is going
├── CHANGELOG.md                           Version history
├── VERSION                                Single-line current version
├── LICENSE                                Apache License 2.0
├── guide_data_model_schema_v1.0.0.json    Data model reference (sheets.Objects)
├── guide_data_model_schema_v1.0.0.xlsx    Authoring workbook the JSON is exported from
├── docs/                                  Narrative documentation
│   ├── data-model/                        Entity-by-entity reference, data types, ERD
│   └── transformations/                   Standards for transforming source data into the model
├── scripts/                               Generators and validators
├── spec/                                  Installable specification
│   └── sql/                               PostgreSQL DDL (install.sql is the entry point)
└── examples/                              Sample data and queries (placeholder for now)
```



## Quick install

You need **PostgreSQL 14 or newer** (tested on PostgreSQL 16).

```bash
createdb guide-data-model
psql -d guide-data-model -f spec/sql/install.sql
```

`install.sql` runs in a single transaction and stops on the first error, so a failed install leaves nothing behind. It locates its component files relative to itself, so you can run it from any directory.

Verify by listing the schemas:

```bash
psql -d guide-data-model -c "SELECT schema_name FROM information_schema.schemata
                 WHERE schema_name IN ('core','person','engagement','academics',
                       'appointment','advising','finances','learner_success',
                       'supports','workforce','admissions');"
```

You should get 11 rows.

To start over:

```bash
psql -d guide-data-model -f spec/sql/teardown.sql
psql -d guide-data-model -f spec/sql/install.sql
```



## What the data model looks like

The 1.0.0 model contains **500 objects** organized into **11 entities**:


| Entity            | Tables | Columns | What it holds                                                                                   |
| ----------------- | ------ | ------- | ----------------------------------------------------------------------------------------------- |
| `core`            | 36     | 649     | Tenancy, organizations, core person records, source systems, shared reference data              |
| `person`          | 61     | 1,031   | Profiles, demographics, identity, relationships, restrictions, success plans                    |
| `engagement`      | 31     | 530     | Surveys, forums, matching, streamed learning events, recruitment attribution                    |
| `academics`       | 199    | 2,874   | Courses, classes, programs, curriculum, enrollments, credit, transfer, credentials, assessments |
| `appointment`     | 8      | 133     | Appointment scheduling, agendas, templates                                                      |
| `advising`        | 17     | 330     | Caseloads, support assignments, early alerts, intake                                            |
| `finances`        | 37     | 672     | Financial aid, scholarships, tuition, charges, financial plans                                  |
| `learner_success` | 1      | 12      | Learner-success plan item types                                                                 |
| `supports`        | 60     | 878     | Resources, wellness, goals, learner supports, housing, dining                                   |
| `workforce`       | 33     | 518     | Career pathways, career plans, industry needs, job postings, employment, resumes                |
| `admissions`      | 17     | 316     | Applications, checklist items, decisions, deposits, fees, reviews                               |


Every operational table is scoped by `TenantIdentifier` (a UUID), the data-ownership and security boundary. Most tables use `(TenantIdentifier, <own identifier>)` as their primary key.

`Objects` contains **1,818 foreign-key reference rows**. The generated PostgreSQL DDL emits **1,781 enforceable foreign-key constraints** and **1,200 indexes**. Of the remaining 37 rows, 4 duplicate an existing constraint and 33 are documented and skipped because they reference a revisioned table (`Assessment`, `Competency`, `AssessmentItem`, `LearningResourceLookup`, `LearnerDegreePlan`) without the `RevisionIdentifier` its primary key requires.

Detailed reference:

- [Entity reference](docs/data-model/) — every table, every column
- [Data types](docs/data-model/data-types.md) — how generic types map to PostgreSQL
- [Entity relationship explorer](docs/data-model/ERD--all_entities.html) — interactive, searchable view of objects and their relationships



## Transformations

Data has to be transformed to fit the model, and the transformations themselves must be transparent and trustworthy. See [docs/transformations/](docs/transformations/) for:

- **[Transformation Standards](docs/transformations/transformation-standards.md)** — DataKind's authored standard, including the conservative numeric threshold for acceptable deviation between raw and transformed data and concrete examples of transformations to avoid.
- **AI-assisted Data Quality Tests** — an initial approach maintained outside the repo, linked from [docs/transformations/README.md](docs/transformations/README.md).



## Source systems

The model is the harmonized layer that sits above institutional source systems. Its structure has been refined by mapping it against real source-system schemas: a CRM in 0.2.0 and an SIS in 1.0.0, in addition to a LMS in 0.1.0.

### Approach to mapping

We use a GenAI-assisted, human-reviewed workflow to accelerate mapping and transformation:

1. **AI draft.** An AI-generated first pass between the source schema and the GUIDE Data Model.
2. **SME review.** A subject-matter expert reviews the AI output field by field, assigns each row a mapping status and priority, and adds transformation notes where needed.
3. **Model refinement.** Gaps found during review become changes to the model itself, recorded in the `Decisions` sheet and the [CHANGELOG](CHANGELOG.md).



### Source-system priority

When systems contain overlapping data, the harmonized layer must decide which value to keep. Our approach is to document **field-level provenance with an external reference**: source-system priority and transformation logic for each column are kept in an external, versioned, timestamped table that can be referenced from SQL for lineage. If a column within a row combines data from multiple sources, a `transformation_logic` column can be added and the source system/table/field made multi-value. Within the model itself, `SourceSystemIdentifier`, `SourceSystemKeyValue`, and the `SourceSystem*Date` columns carry row-level lineage.

**Example of an external reference table**


| source_id | mapping_version | target_column | source_system | source_table | source_field | transformation_logic | effective_date |
| --------- | --------------- | ------------- | ------------- | ------------ | ------------ | -------------------- | -------------- |
| a1b2c3d4  | v1.0.0          | first_name    | SIS           | person       | first_name   |                      | 2026-10-13     |




## Versioning


| Version | Date         | Notes                                                                                                                                           |
| ------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0   | May 2026     | First release: 291 objects, 5,420 columns, 10 entities.                                                                                         |
| 0.2.0   | July 2026    | CRM mapping: adds the Admissions entity, shared reference data, and person contact/consent tables (317 objects).                                |
| 1.0.0   | October 2026 | SIS mapping: expands the model to 500 objects and 7,943 columns, introduces the tenant boundary, and makes the model installable on PostgreSQL. |


See [CHANGELOG.md](CHANGELOG.md) for details.