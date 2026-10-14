# Changelog

All notable changes to the GUIDE Data Model are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/) and the project adheres to [Semantic Versioning](https://semver.org/).

Counts in this file are computed from the `Objects` records of each version's model JSON.

---

## [1.0.0] — 2026-10-13 — SIS mapping and installable release

### Added

- **183 net new objects** (221 added, 38 removed or renamed): 500 objects and 7,943 columns across 11 entities, up from 317 objects and 5,961 columns.
- **Tenant boundary.** New `Tenant` table; `TenantIdentifier` (UUID) is the data-ownership and security boundary on every operational table, replacing `OrganizationIdentifier` in that role. `OrganizationIdentifier` now identifies a real-world organization within a tenant.
- **Academics:** course and class catalog detail (titles, descriptions, credits, instructional hours and methods, levels, categories, cross-listing, requisite rules), academic catalogs, academic periods and census dates, programs, curriculum and requirements, degree-progress evaluation, recognized academic credit with transfer, test, and prior-learning evaluation, external education, grade definitions and grade changes, academic honors, CIP codes.
- **Person:** identity documents, race and ethnicity with reporting classifications, gender identity, privacy status, service restrictions and their impacts, person-to-person relationships, tag assignments, achievements, organization memberships, success predictions.
- **Core:** `Organization` (replacing `OrganizationLookup`), organization units, relationships, accreditation, classifications, contact points, and tenant-relative organization roles; `PersonIdentification`/`PersonIdentificationSystem`; administrative periods.
- **Supports:** housing (buildings, rooms, rates, requests, occupancy) and dining (meal plans, rates, requests, assignments).
- **Finances:** financial-aid years, funds, award periods, need summaries, satisfactory academic progress, learner account charges.
- **Advising:** a single `PersonSupportReferral` and `PersonSupportAssignment` across advising, early alerts, intake, and coordinated care.
- 38 new key decisions (132 total).
- `Sub-Entity` field on `Objects` records.
- `UUID` generic data type.
- Repository documentation: README, OVERVIEW, entity reference pages, data types, interactive relationship explorer, and transformation standards.
- **Installable PostgreSQL DDL** under `spec/sql/`, generated from `Objects`: 11 schemas, 500 tables, 1,781 foreign-key constraints, 1,200 indexes, and a comment on every table and column. Validated by a full install and teardown on PostgreSQL 16.
- Tooling under `scripts/`: `generate_schema.py`, `generate_erd.py`, `validate_sql.py`, `validate_postgres.py`.



### Changed

- **Renamed or replaced objects:** `OrganizationLookup` → `Organization`; `OrganizationAlternateId`/`OrganizationIdSystem` → `OrganizationIdentification`/`OrganizationIdentificationSystem`; `PersonAlternateId`/`PersonIdSystem` → `PersonIdentification`/`PersonIdentificationSystem`; `LearnerEmployment` → `PersonEmployment`; `PersonCohort`/`CohortLookup` → `CohortMembership`/`Cohort`; caseload, early-alert, and challenge referral tables → `PersonSupportReferral`; `OrganizationIndustryCode` → `OrganizationClassification`.
- **Keys simplified:** most tables now use `(TenantIdentifier, <own identifier>)` as the primary key; `PersonIdentifier` is no longer part of the primary key in about 70 tables.
- **FK references** name the referenced business identifier (e.g. `ActivityLookup.ActivityIdentifier`); the tenant column is implied.
- **Credential entity merged into Academics.**
- **Data types:** 882 identifiers changed from `Integer (bigint)` to `String (str or text)`; 441 `SourceSystem*Date` columns changed from `Datetime` to `Date`.
- **Defaults** use SQL Server syntax (`SYSUTCDATETIME`, `NEXT VALUE FOR`); the generator translates them to PostgreSQL.



### Removed

- 38 objects renamed, merged, or retired (including the renames above, `DegreePathway*`, `TransferWorkflow*`, `OrganizationProfile`, `LearnerHold`, and several `*Details` tables).



### Known issues

- 1,905 date and datetime `Example` values were exported as Excel serial numbers (e.g. `45527.41053`).
- 486 `Default` values read `SYSUTCDATETIME(` (missing the closing parenthesis); the generator still maps them to `CURRENT_TIMESTAMP`.
- `Integer (bigint)` is used by 1,024 columns but is not listed on the `DataTypes` sheet.
- 33 FK references to revisioned tables (`Assessment`, `Competency`, `AssessmentItem`, `LearningResourceLookup`, `LearnerDegreePlan`) omit the `RevisionIdentifier` their primary key requires; the generator documents and skips them.
- 78 descriptions still use the model's former name and 2 use a vendor-specific term; the generator normalizes these in the published documentation and SQL comments.
- Some `Comment` values contain internal working notes.

---



## [0.2.0] — 2026-10-09 — CRM mapping



### Added

- **Admissions entity** (17 tables): `LearnerApplication` and its checklist-item, decision, deposit, event, fee, fee-waiver, intent, program-interest, response, review, status-history, and withdrawal tables, plus lookups for application status, type, source, and decision type.
- **Core.ReferenceData:** `ReferenceCodeSet` and `ReferenceCodeValue` for small governed code lists.
- **Person:** `PersonCitizenship`, `PersonImmigrationStatus`, `PersonRelatedContact`, `PersonCommunicationConsent`, `PersonCommunicationDeliverabilityEvent`.
- **Engagement:** `PersonRecruitmentAttribution`.
- **Finances:** `LearnerThirdPartyBenefit`.
- 39 new key decisions (94 total) covering tenant scoping, lineage columns, reference data, and the admissions design.
- Totals: 317 objects, 5,961 columns, 11 entities.



### Changed

- About 1,920 identifiers changed from GUID strings to `Integer (bigint)`.
- 1,370 audit and source-system date columns changed from `Date` to `Datetime`.
- `Objects` records: `Sequence` field removed, `Comment` field added. Header renames: `Key Decisions` → `KeyDecisions`, `Version Added` → `VersionAdded`.
- `Assessment` status and type became coded identifiers; `BirthCity`/`BirthState` moved from `PersonLookup` to `PersonDemographics`.

---



## [0.1.0] — 2026-10-09 — Initial release



### Added

- The first version of the GUIDE Data Model in `.xlsx` and `.json` formats: 291 objects and 5,420 columns across 10 entities (Core, Person, Engagement, Academics, Credential, Appointment, Advising, Finances, Supports, Workforce).
- 55 key decisions documenting how the model was built, starting from an academic advising model.

