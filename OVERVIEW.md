# GUIDE Data Model — Overview

This file explains the thesis behind the data model, what lives in this repository today, and where it is going. It is intended for institutional researchers, data leaders, ed-tech contributors, and anyone evaluating whether to engage with a unified data model for higher education.

---

## 1. Why a data model

Higher education runs on data that is plentiful but fragmented. A single student's experience is recorded across multiple systems — a Student Information System (SIS), a Customer Relationship Management system (CRM) for recruitment and admissions, a Learning Management System (LMS), advising and support tools, and more. Each platform has its own schema, its own vocabulary, and its own export format. The same concept can be defined differently in each.

The cost of that fragmentation is felt by institutional researchers and data teams, who spend a significant amount of their time reconciling information rather than generating insight that could improve student outcomes. It is also felt by students whose records do not travel cleanly across institutions and systems, which ultimately limits institutions' ability to support learners toward success.

A shared, open data model addresses this by giving institutions a single canonical representation of the higher-education student lifecycle. When source systems are mapped into a common language, the burden of data reconciliation drops, data quality and institutional trust in data improve, and teams can move to faster, more holistic insight.

## 2. Why this approach

There are existing standards in this space, and the GUIDE Data Model is not an attempt to replace them. It is a complementary, public-good artifact with three deliberate design choices.

**Open-source, license-free, community-driven.** Institutions can adopt the model without licensing fees, and can see the rationale and transformation standards transparently. This repository is designed for community engagement and contribution.

**Built-in definitions and governance.** The model is designed for transparency, which includes public documentation of data definitions and field-level provenance. Every column carries a description, and the key design decisions behind the model are recorded with the version that introduced them. Source-system priority, transformation logic, and lineage are designed to be easy to track.

**GenAI-assisted, human-reviewed mappings.** Mapping a source system into a canonical model has historically been a high-effort engagement. The GUIDE Data Model uses GenAI to accelerate field-by-field mapping and transformation drafts, and every mapping goes through expert human review for priority and validation. The intent is to make mappings faster to produce and easier to audit. The model's grouping into high-level entities is intentionally modular so it can evolve iteratively.

## 3. What is covered in this repository

The repository contains everything an institution or implementer needs to understand the model, install it, and contribute back.

**The data model reference** is the `Objects` object in `[guide_data_model_schema_v1.0.0.json](guide_data_model_schema_v1.0.0.json)`. Version 1.0.0 defines 500 objects and 7,943 columns organized into 11 entities; see the [README](README.md) for the entity breakdown and relationship counts.

**The installable specification** under `spec/` is PostgreSQL DDL generated directly from `Objects`: 500 tables in 11 schemas, 1,781 foreign-key constraints, and 1,200 indexes.

**Narrative documentation** under `docs/` provides entity-by-entity reference material — every table, every column type, and relationships — an interactive relationship explorer, and the transformation standards that govern how source data is reshaped into the model.

**Tooling** under `scripts/` generates the SQL and documentation from the model JSON and validates the result, including an end-to-end install into a temporary PostgreSQL cluster.

**Examples** under `examples/` will hold sample datasets and queries in a later release.

## 4. Development timeline


| Version      | Date         | Status   | Scope                                                                                                                                                                                                                                                                                                 |
| ------------ | ------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0.1.0**    | May 2026     | Released | First release of the model: 291 objects and 5,420 columns across 10 entities.                                                                                                                                                                                                                         |
| **0.2.0**    | July 2026    | Released | Model refined against a CRM: Admissions entity (17 tables), shared reference data, person citizenship, immigration, related-contact and communication-consent tables (317 objects).                                                                                                                   |
| **1.0.0**    | October 2026 | Current  | Model refined against an SIS: 500 objects and 7,943 columns; tenant boundary (`TenantIdentifier`); course catalog, academic periods, programs and degree progress, transfer and prior-learning credit, grades, housing and dining, financial-aid funds; installable PostgreSQL DDL and documentation. |
| Beyond 1.0.0 | TBD          | Backlog  | Mapping against additional systems. Fully tested transformation code and validated data-quality tests. Sample datasets that exercise the schema.                                                                                                                                                      |


The current release is best read as an early public version: the model, generated SQL, per-entity documentation, and tooling are in place, while source-system coverage, governance, and validation layers continue to mature.

---

*This document is a high-level companion to the technical [README.md](README.md). For installation, schema reference, and relationship statistics, start there.*