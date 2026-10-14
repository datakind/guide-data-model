# Entity: Person

This page documents every table that belongs to the **Person** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 61**

## Table of contents

- [AddressTypeLookup](#addresstypelookup)
- [CitizenshipStatusLookup](#citizenshipstatuslookup)
- [CohortMembership](#cohortmembership)
- [EmailTypeLookup](#emailtypelookup)
- [EthnicityLookup](#ethnicitylookup)
- [EthnicityReportingClassification](#ethnicityreportingclassification)
- [GenderIdentityLookup](#genderidentitylookup)
- [IdentityDocumentTypeLookup](#identitydocumenttypelookup)
- [LearnerReminder](#learnerreminder)
- [LearnerReminderPreferences](#learnerreminderpreferences)
- [LearnerSuccessIndicatorScore](#learnersuccessindicatorscore)
- [LearnerSuccessPlan](#learnersuccessplan)
- [LearnerSuccessPlanItem](#learnersuccessplanitem)
- [LearnerSuccessPlanItemSuccessIndicator](#learnersuccessplanitemsuccessindicator)
- [LearnerSuccessPrediction](#learnersuccessprediction)
- [LearningOutcomeActivityAssociation](#learningoutcomeactivityassociation)
- [MaritalStatusLookup](#maritalstatuslookup)
- [PersonAchievement](#personachievement)
- [PersonActivity](#personactivity)
- [PersonActivityAlignment](#personactivityalignment)
- [PersonCitizenship](#personcitizenship)
- [PersonCommunicationConsent](#personcommunicationconsent)
- [PersonCommunicationDeliverabilityEvent](#personcommunicationdeliverabilityevent)
- [PersonDemographics](#persondemographics)
- [PersonDocument](#persondocument)
- [PersonEthnicity](#personethnicity)
- [PersonGenderIdentity](#persongenderidentity)
- [PersonIdentityDocument](#personidentitydocument)
- [PersonImmigrationStatus](#personimmigrationstatus)
- [PersonInterest](#personinterest)
- [PersonNameTypeLookup](#personnametypelookup)
- [PersonNonIdentifiableDemographics](#personnonidentifiabledemographics)
- [PersonOrganizationMembership](#personorganizationmembership)
- [PersonPrivacyStatus](#personprivacystatus)
- [PersonRace](#personrace)
- [PersonRelatedContact](#personrelatedcontact)
- [PersonResidency](#personresidency)
- [PersonServiceRestriction](#personservicerestriction)
- [PersonServiceRestrictionImpact](#personservicerestrictionimpact)
- [PersonStrength](#personstrength)
- [PersonTagAssignment](#persontagassignment)
- [PersonTask](#persontask)
- [PersonTransportation](#persontransportation)
- [PersonalPronounLookup](#personalpronounlookup)
- [PersonalRelationship](#personalrelationship)
- [PersonalRelationshipStatusLookup](#personalrelationshipstatuslookup)
- [PersonalRelationshipTypeLookup](#personalrelationshiptypelookup)
- [PersonalRelationshipTypeReciprocal](#personalrelationshiptypereciprocal)
- [PhoneTypeLookup](#phonetypelookup)
- [PrivacyStatusLookup](#privacystatuslookup)
- [RaceLookup](#racelookup)
- [RaceReportingClassification](#racereportingclassification)
- [ResidencyTypeLookup](#residencytypelookup)
- [ServiceRestrictionImpactLookup](#servicerestrictionimpactlookup)
- [ServiceRestrictionReasonLookup](#servicerestrictionreasonlookup)
- [SocialMediaTypeLookup](#socialmediatypelookup)
- [StrengthCategoryLookup](#strengthcategorylookup)
- [StrengthDetailLookup](#strengthdetaillookup)
- [StrengthLookup](#strengthlookup)
- [SuccessIndicatorLookup](#successindicatorlookup)
- [SuccessPredictionModel](#successpredictionmodel)

---

## AddressTypeLookup

**SQL identifier:** `person.address_type_lookup`

Governed addresstype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `address_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the address type. |
| `title` | `TEXT` |  | No | Human-readable name of the address type. |
| `description` | `TEXT` |  | Yes | Detailed description of the purpose or intended use of the address type. |
| `standard_address_type` | `TEXT` |  | Yes | Governed/source category for AddressTypeLookup. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the address type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## CitizenshipStatusLookup

**SQL identifier:** `person.citizenship_status_lookup`

Governed citizenshipstatus definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `citizenship_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the citizenship status. |
| `title` | `TEXT` |  | No | Human-readable name of the citizenship status. |
| `description` | `TEXT` |  | Yes | Detailed description of the citizenship status. |
| `category` | `TEXT` |  | Yes | Governed/source category for CitizenshipStatusLookup. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the citizenship status value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## CohortMembership

**SQL identifier:** `person.cohort_membership`

A tenant-scoped effective membership of a person in a governed cohort, optionally qualified by academic level, administrative periods, dates, and participation status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `cohort_membership_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the cohort membership record. |
| `cohort_identifier` | `TEXT` | FK → `Cohort.CohortIdentifier` | No | Identifier of the institution-defined cohort. |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Academic level associated with this cohort membership. |
| `start_administrative_period_identifier` | `TEXT` | FK → `AdministrativePeriodLookup.AdministrativePeriodIdentifier` | Yes | Starting administrative period for the cohort membership. |
| `end_administrative_period_identifier` | `TEXT` | FK → `AdministrativePeriodLookup.AdministrativePeriodIdentifier` | Yes | Ending administrative period for the cohort membership. |
| `start_date` | `DATE` |  | Yes | Effective start date of the person’s cohort membership. |
| `end_date` | `DATE` |  | Yes | Last effective date of the person’s cohort membership. |
| `membership_status` | `TEXT` |  | No | Operational participation status of the person membership in the cohort. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## EmailTypeLookup

**SQL identifier:** `person.email_type_lookup`

Governed emailtype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `email_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the email type. |
| `title` | `TEXT` |  | No | Human-readable name of the email type. |
| `description` | `TEXT` |  | Yes | Detailed description of the email type. |
| `standard_email_type` | `TEXT` |  | Yes | Governed/source category for EmailTypeLookup. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the email type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## EthnicityLookup

**SQL identifier:** `person.ethnicity_lookup`

Governed ethnicity definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `ethnicity_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the ethnicity. |
| `title` | `TEXT` |  | No | Human-readable name of the ethnicity. |
| `description` | `TEXT` |  | Yes | Detailed description of the ethnicity classification represented by the lookup value. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the ethnicity value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## EthnicityReportingClassification

**SQL identifier:** `person.ethnicity_reporting_classification`

Tenant-scoped crosswalk from an institution/source ethnicity definition to a current governed external reporting category. Crosswalk rows may be activated or inactivated; no effective-dated or version history is maintained.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `ethnicity_reporting_classification_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the ethnicity reporting crosswalk row. |
| `ethnicity_identifier` | `TEXT` | FK → `EthnicityLookup.EthnicityIdentifier` | No | Canonical ethnicity definition being classified. |
| `reporting_category_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Current governed external reporting category assigned to this ethnicity definition. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether this ethnicity-to-reporting-category crosswalk is active for current use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system that supplied or governs this crosswalk, when applicable. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the crosswalk row, when supplied. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## GenderIdentityLookup

**SQL identifier:** `person.gender_identity_lookup`

Governed tenant-scoped gender-identity definitions with source-system lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `gender_identity_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed gender identity. |
| `code` | `TEXT` |  | No | Institution/source-defined code identifying the gender identity. |
| `title` | `TEXT` |  | No | Human-readable name of the gender identity. |
| `description` | `TEXT` |  | Yes | Detailed description of the gender identity definition. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the gender identity value is active for current use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the gender identity by the originating source system. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## IdentityDocumentTypeLookup

**SQL identifier:** `person.identity_document_type_lookup`

Governed identitydocumenttype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `identity_document_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the identity document type. |
| `title` | `TEXT` |  | No | Human-readable name of the identity document type. |
| `description` | `TEXT` |  | Yes | Detailed description of the identity document type. |
| `category` | `TEXT` |  | Yes | Governed/source category for IdentityDocumentTypeLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the identity document type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## LearnerReminder

**SQL identifier:** `person.learner_reminder`

A table containing a history of reminders previously sent or scheduled to be sent for any item with a scheduled completion or due date.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_reminder_identifier` | `TEXT` | PK | No | Unique identifier for the reminder |
| `caseload_communication_identifier` | `TEXT` | FK → `PersonCaseloadCommunication.PersonCaseloadCommunicationIdentifier` | Yes | Unique identifier for the caseload communication |
| `object_identifier` | `TEXT` | FK → `ObjectLookup.ObjectIdentifier` | Yes | Identifier associated with the item for which the reminder is created |
| `object_row_identifier` | `TEXT` |  | Yes | Unique identifier for the object or database table row |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | Text included with the reminder |
| `sent_date` | `DATE` |  | Yes | Date the item was successfully sent |
| `send_method` | `TEXT` |  | Yes | Communication method used to send the reminder |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerReminderPreferences

**SQL identifier:** `person.learner_reminder_preferences`

A table containing learner preferences for reminders of due dates and tasks.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_reminder_preferences_identifier` | `TEXT` | PK | No | Unique identifier for a learner reminder preferences item |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `learner_reminder_offset_days` | `INTEGER` |  | No | Number of days before the event, appointment, or due date to receive a reminder |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerSuccessIndicatorScore

**SQL identifier:** `person.learner_success_indicator_score`

Records an observed learner value for a success indicator, optionally in the context of a specific plan-item target.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_success_indicator_score_identifier` | `TEXT` | PK | No | Unique identifier for a success indicator score item |
| `success_indicator_identifier` | `TEXT` | FK → `SuccessIndicatorLookup.SuccessIndicatorIdentifier` | No | Success indicator whose observed value is recorded. |
| `learner_success_plan_identifier` | `TEXT` | FK → `LearnerSuccessPlan.LearnerSuccessPlanIdentifier` | Yes | Unique identifier for the success plan |
| `learner_success_plan_item_success_indicator_identifier` | `TEXT` | FK → `LearnerSuccessPlanItemSuccessIndicator.LearnerSuccessPlanItemSuccessIndicatorIdentifier` | Yes | Optional plan-item target association that gives the observed score its specific plan context. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `assigned_date` | `DATE` |  | No | Date an indicator was assigned |
| `removed_date` | `DATE` |  | Yes | Date an indicator was removed |
| `score_value` | `NUMERIC` |  | Yes | The person's score for the success indicator |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `INTEGER` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `INTEGER` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `INTEGER` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerSuccessPlan

**SQL identifier:** `person.learner_success_plan`

A table containing a list of a learner's success plans.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `description` | `TEXT` |  | Yes | Narrative description of the learner success plan. |
| `start_date` | `DATE` |  | Yes | Date on which the learner success plan begins. |
| `end_date` | `DATE` |  | Yes | Date on which the learner success plan ends. |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_success_plan_identifier` | `TEXT` | PK | No | Unique identifier for the success plan |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `status` | `TEXT` |  | No | Status of the success plan (active, inactive) |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerSuccessPlanItem

**SQL identifier:** `person.learner_success_plan_item`

Represents one actionable or assessable component of a learner success plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_success_plan_item_identifier` | `TEXT` | PK | No | Learner Success Plan Item Identifier for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `learner_success_plan_identifier` | `TEXT` | FK → `LearnerSuccessPlan.LearnerSuccessPlanIdentifier` | No | Learner Success Plan Identifier for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `learner_success_plan_item_type_identifier` | `TEXT` | FK → `LearnerSuccessPlanItemTypeLookup.LearnerSuccessPlanItemTypeIdentifier` | Yes | Governed type assigned to the plan item. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source System Identifier for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `name` | `TEXT` |  | Yes | Name for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `description` | `TEXT` |  | Yes | Description for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `source_raw_type` | `TEXT` |  | Yes | Unmodified plan-item type value supplied by the source system. |
| `status` | `TEXT` |  | Yes | Status for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `sequence_number` | `INTEGER` |  | Yes | Sequence Number for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `planned_start_date` | `DATE` |  | Yes | Planned Start Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `due_date` | `DATE` |  | Yes | Due Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `completion_date` | `DATE` |  | Yes | Completion Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `outcome_description` | `TEXT` |  | Yes | Outcome Description for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `source_system_key_value` | `TEXT` |  | Yes | Source System Key Value for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `source_system_created_date` | `DATE` |  | Yes | Source System Created Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `source_system_updated_date` | `DATE` |  | Yes | Source System Updated Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `source_system_deleted_date` | `DATE` |  | Yes | Source System Deleted Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `created_by` | `INTEGER` |  | No | Created By for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Created Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `updated_by` | `INTEGER` |  | Yes | Updated By for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Updated Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `deleted_by` | `INTEGER` |  | Yes | Deleted By for the LearnerSuccessPlanItem record. [Description requires semantic review.] |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Deleted Date for the LearnerSuccessPlanItem record. [Description requires semantic review.] |

## LearnerSuccessPlanItemSuccessIndicator

**SQL identifier:** `person.learner_success_plan_item_success_indicator`

A target or observed success indicator associated with a learner success plan item.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_success_plan_item_success_indicator_identifier` | `TEXT` | PK | No | Learner Success Plan Item Success Indicator Identifier for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `learner_success_plan_item_identifier` | `TEXT` | FK → `LearnerSuccessPlanItem.LearnerSuccessPlanItemIdentifier` | No | Learner Success Plan Item Identifier for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `success_indicator_identifier` | `TEXT` | FK → `SuccessIndicatorLookup.SuccessIndicatorIdentifier` | No | Success Indicator Identifier for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `target_score_value` | `NUMERIC` |  | Yes | Target Score Value for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `created_by` | `BIGINT` |  | No | Created By for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Created Date for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `updated_by` | `BIGINT` |  | Yes | Updated By for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Updated Date for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `deleted_by` | `BIGINT` |  | Yes | Deleted By for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Deleted Date for the LearnerSuccessPlanItemSuccessIndicator record. [Description requires semantic review.] |

## LearnerSuccessPrediction

**SQL identifier:** `person.learner_success_prediction`

One time-stamped prediction for a learner produced by a defined success prediction model, including the model-specific score and optional probability or category.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_success_prediction_identifier` | `TEXT` | PK | No | Unique identifier for one learner success prediction result. |
| `success_prediction_model_identifier` | `TEXT` | FK → `SuccessPredictionModel.SuccessPredictionModelIdentifier` | No | Prediction model used to produce this learner success prediction. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `score_value` | `NUMERIC` |  | Yes | Optional numeric score emitted by the prediction model on the model-defined scale. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `prediction_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time at which the prediction was produced or scored. |
| `predicted_probability` | `NUMERIC` |  | Yes | Optional predicted probability of the model target outcome, expressed as a decimal from 0 through 1 when the model output is probabilistic. |
| `prediction_category` | `TEXT` |  | Yes | Optional model-assigned category or bucket used to interpret the prediction, such as Very High, High, Moderate, Low, or Very Low. |

## LearningOutcomeActivityAssociation

**SQL identifier:** `person.learning_outcome_activity_association`

A table associating learning outcomes and activities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_activity_association_identifier` | `TEXT` | PK | No | Unique identifier for the learning outcome to activity association |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## MaritalStatusLookup

**SQL identifier:** `person.marital_status_lookup`

Governed maritalstatus definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `marital_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the marital status. |
| `title` | `TEXT` |  | No | Human-readable name of the marital status. |
| `description` | `TEXT` |  | Yes | Detailed description of the marital status. |
| `category` | `TEXT` |  | Yes | Governed/source category for MaritalStatusLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the marital status value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonAchievement

**SQL identifier:** `person.person_achievement`

Tenant-scoped fact that a person has earned or holds an achievement, award, certificate, or recognition, including issuer and validity dates when applicable. Distinct from reusable academic-honor definitions and from academic credentials.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_achievement_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the person achievement. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person who earned or holds the achievement. |
| `achievement_title` | `TEXT` |  | No | Human-readable title of the achievement, award, certificate, or recognition. |
| `issuer_name` | `TEXT` |  | Yes | Name of the person or organization that issued or conferred the achievement. |
| `issued_date` | `DATE` |  | Yes | Date the achievement was issued or conferred. |
| `expiration_date` | `DATE` |  | Yes | Date after which the achievement is no longer valid or current, when applicable. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the person achievement by the originating source system. |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system. |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system. |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted in the source system. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## PersonActivity

**SQL identifier:** `person.person_activity`

A table containing a history of co-curricular activities in which a learner has engaged during pursuit of education, including community service, professional development, athletics, recreation, publication, grant, advocacy, or others.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_activity_identifier` | `TEXT` | PK | No | Unique identifier for learner activity details |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifier for a term |
| `participation_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Unique identifier of the organization for the person activity |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `start_date` | `DATE` |  | Yes | Start date of participation in the activity |
| `end_date` | `DATE` |  | Yes | End date for participation in the activity or organization |
| `status` | `TEXT` |  | No | Status of the person's participation in the activity |
| `role` | `TEXT` |  | Yes | Role of the participation |
| `time_in_hours` | `NUMERIC` |  | Yes | Number of hours the person participated in the activity |
| `type` | `TEXT` |  | Yes | Type of participation |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonActivityAlignment

**SQL identifier:** `person.person_activity_alignment`

An alignment linking a person activity to another relevant object.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_activity_alignment_identifier` | `TEXT` | PK | No | Unique identifier for the competency to person activity details association |
| `person_activity_identifier` | `TEXT` | FK → `PersonActivity.PersonActivityIdentifier` | No | Unique identifier for learner activity details |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## PersonCitizenship

**SQL identifier:** `person.person_citizenship`

A table that stores one or more country-specific citizenship or citizenship-like status records for a person, including country, citizenship status, primary citizenship indication, effective dates where known, source raw citizenship values, source lineage, and audit fields. It keeps citizenship distinct from address history, residency classification, visa/immigration status, and birth location.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the person associated with the citizenship record. |
| `sequence_number` | `TEXT` | PK | No | Sequence number distinguishing multiple citizenship records for the same person. |
| `country_code` | `TEXT` |  | No | ISO 3166-1 alpha-2 country or jurisdiction code for the citizenship record. |
| `citizenship_status_identifier` | `TEXT` | FK → `CitizenshipStatusLookup.CitizenshipStatusIdentifier` | Yes | Reference-code value identifying the person's citizenship status for the country or jurisdiction. |
| `primary_citizenship_indicator` | `BOOLEAN` |  | Yes | Indicates whether this citizenship record is treated as the person's primary citizenship for reporting or operational use. |
| `citizenship_start_date` | `DATE` |  | Yes | Date on which the citizenship status or relationship began, if known. |
| `citizenship_end_date` | `DATE` |  | Yes | Date on which the citizenship status or relationship ended, if applicable and known. |
| `source_raw_country_of_citizenship` | `TEXT` |  | Yes | Raw source-system country-of-citizenship value before canonical country mapping. |
| `source_raw_citizenship_status` | `TEXT` |  | Yes | Raw source-system citizenship status value before canonical status mapping. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the citizenship record was imported, synchronized, or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the citizenship record or source person citizenship entry. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time on which the citizenship record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time on which the citizenship record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time on which the citizenship record was soft-deleted. |

## PersonCommunicationConsent

**SQL identifier:** `person.person_communication_consent`

A table that stores person-level communication consent, opt-in, opt-out, unsubscribe, and channel permission facts for channels such as email, SMS, phone, WhatsApp, or other communication media. This table supports governance of whether and how the institution may contact the person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped person identifier to whom the consent/subscription fact belongs. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for multiple communication consent rows for the person. |
| `communication_channel_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the communication channel, such as email, SMS, or WhatsApp. |
| `consent_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the consent, subscription, or opt-in/opt-out status. |
| `contact_point_value` | `TEXT` |  | Yes | Email address, phone number, WhatsApp number, or other contact point associated with the consent fact. |
| `opt_in_indicator` | `BOOLEAN` |  | Yes | Indicates whether the person is recorded as opted in for the channel/contact point. |
| `opt_in_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the opt-in was recorded or became effective. |
| `opt_out_indicator` | `BOOLEAN` |  | Yes | Indicates whether the person is recorded as opted out for the channel/contact point. |
| `opt_out_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the opt-out was recorded or became effective. |
| `unsubscribe_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the person unsubscribed from the channel/contact point. |
| `consent_source_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the source or mechanism of consent where needed. |
| `source_raw_communication_channel` | `TEXT` |  | Yes | Source-system communication channel value preserved when canonical mapping is lossy. |
| `source_raw_consent_status` | `TEXT` |  | Yes | Source-system consent/subscription status preserved when canonical mapping is lossy. |
| `source_raw_opt_in_value` | `TEXT` |  | Yes | Source-system opt-in value preserved as supplied. |
| `source_raw_opt_out_value` | `TEXT` |  | Yes | Source-system opt-out value preserved as supplied. |
| `source_raw_contact_point` | `TEXT` |  | Yes | Source-system contact point value preserved as supplied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system from which the consent row originated or can be reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the consent row. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonCommunicationDeliverabilityEvent

**SQL identifier:** `person.person_communication_deliverability_event`

A table that stores communication deliverability events associated with a person and channel, such as hard bounce, soft bounce, invalid address/number, unsubscribe event, suppression, delivery failure, or provider error. This table records what happened to communication attempts or channel reachability without becoming a full message-history table.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped person identifier to whom the deliverability event belongs. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for multiple deliverability event rows for the person. |
| `communication_channel_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the communication channel, such as email or SMS. |
| `deliverability_event_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the type of deliverability event, such as hard bounce or invalid contact point. |
| `deliverability_event_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the deliverability event occurred or was recorded. |
| `contact_point_value` | `TEXT` |  | Yes | Email address, phone number, or other contact point associated with the deliverability event. |
| `error_code` | `TEXT` |  | Yes | Source or platform error code associated with the deliverability event. |
| `error_description` | `TEXT` |  | Yes | Source or platform description of the deliverability event or error. |
| `source_raw_communication_channel` | `TEXT` |  | Yes | Source-system communication channel value preserved when canonical mapping is lossy. |
| `source_raw_deliverability_event_type` | `TEXT` |  | Yes | Source-system deliverability event type preserved when canonical mapping is lossy. |
| `source_raw_contact_point` | `TEXT` |  | Yes | Source-system contact point value preserved as supplied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system from which the deliverability event row originated or can be reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the deliverability event row. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonDemographics

**SQL identifier:** `person.person_demographics`

A tenant-scoped table containing person-specific demographic characteristics and summary/legacy demographic attributes. Governed gender identity is modeled separately through PersonGenderIdentity; the legacy Gender text remains for compatibility where needed.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_demographics_identifier` | `TEXT` | PK | No | Unique identifier for the person's demographic information |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `dependency_status` | `TEXT` |  | Yes | A person's classification as dependent or independent with regards to eligibility for Title IV Federal Student aid |
| `emancipated_minor` | `BOOLEAN` |  | Yes | A minor student under the age of 18 who has been granted by legal action to have the power and capacity of an adult |
| `birth_date` | `DATE` |  | Yes | Person date of birth |
| `person_date_entered_us` | `DATE` |  | Yes | For students born outside of the U.S., the date the student entered the U.S. |
| `birth_city` | `TEXT` |  | Yes | The city or locality in which the person was born |
| `birth_state_province` | `TEXT` |  | Yes | The state, province, territory, or comparable first-level jurisdiction in which the person was born |
| `country_of_birth_code` | `TEXT` |  | Yes | The ISO 3166-1 alpha-2 code for the country in which the person was born |
| `economic_disadvantage_status_indicator` | `BOOLEAN` |  | No | An indication that the student met the State criteria for classification as having an economic disadvantage |
| `economic_disadvantage_status_start_date` | `DATE` |  | Yes | The beginning year, month and day when the economic disadvantage status became applicable to an individual |
| `economic_disadvantage_status_end_date` | `DATE` |  | Yes | The ending year, month and day when the economic disadvantage status applied to an individual |
| `federal_race_and_ethnicity_declined_indicator` | `BOOLEAN` |  | No | A parent, guardian, or student declined to report sufficient information for identifying a student's federal race and/or ethnicity |
| `hispanic_or_latino_ethnicity_indicator` | `BOOLEAN` |  | Yes | The person's collected or resolved response to the U.S. Hispanic-or-Latino ethnicity question, maintained separately from race selections; this is not a complete representation of ethnicity. |
| `gender` | `TEXT` |  | Yes | Legacy or source-provided gender text retained for compatibility. Governed gender identity is represented through PersonGenderIdentity; legal sex remains a separate concept. |
| `sex` | `TEXT` |  | Yes | The concept describing the biological traits that distinguish the males and females of a species |
| `marital_status` | `TEXT` |  | Yes | The marital status of the person as of today |
| `military_active_student_indicator` | `TEXT` |  | Yes | An indication that the student is currently serving on Active Duty, in the National Guard, or in the Reserve components of the United States military resources (e.g. Active, NotActive, Unknown) |
| `military_branch` | `TEXT` |  | Yes | A branch of the US Military applicable for specifying more details when using Military Connected Student Indicator, Military Active Student Indicator, Military Veteran Student Indicator, and Military Enlistment After Exit elements |
| `native_language` | `TEXT` |  | Yes | Native language to interact in oral and written communication |
| `number_of_household_college_students` | `INTEGER` |  | Yes | Number of people, including the student, who will attend at least half-time in the current academic year, a program that leads to a college degree or certificate |
| `number_of_people_in_household` | `INTEGER` |  | Yes | Total number of persons residing in the same household |
| `transgender_indicator` | `BOOLEAN` |  | Yes | Indicates whether the student is transgender or not or prefers not to answer |
| `tribal_id_or_cib` | `TEXT` |  | Yes | Identification issued by tribe indicating enrollment or membership in the tribe or the identification of the Certificate of Degree of Indian Blood (CDIB/CIB) |
| `pronouns` | `TEXT` |  | Yes | Preferred pronouns of person |
| `military_veteran_student_indicator` | `TEXT` |  | Yes | An indication that the student is a veteran who served on Active Duty, in the National Guard, or in the Reserve components of the United States military resources (e.g. Veteran, NotVeteran, Unknown) |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `marital_status_identifier` | `TEXT` | FK → `MaritalStatusLookup.MaritalStatusIdentifier` | Yes | Governed current marital status. |
| `source_raw_marital_category` | `TEXT` |  | Yes | Raw source marital category. |
| `personal_pronoun_identifier` | `TEXT` | FK → `PersonalPronounLookup.PersonalPronounIdentifier` | Yes | Governed preferred personal pronoun. |

## PersonDocument

**SQL identifier:** `person.person_document`

A table containing details about documents that have been saved for a person, including links to the authoritative document.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_document_identifier` | `TEXT` | PK | No | Unique identifier for a person's document |
| `person_document_author_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person identifier of the person who authored document |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | Yes | Unique identifier for the FAFSA or other financial aid application |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | Description of the file stored for a person |
| `status` | `TEXT` |  | No | Indicates whether the document is active, inactive, archived, etc. |
| `type` | `TEXT` |  | Yes | Specifies a short description of the data in the document |
| `document_name` | `TEXT` |  | No | Name of the file stored for the person |
| `size` | `NUMERIC` |  | Yes | Size of the file stored in kilobytes for the person |
| `url` | `TEXT` |  | Yes | URL path for the file stored for the person |
| `record_name` | `TEXT` |  | No | A name for the record |
| `visible_indicator` | `BOOLEAN` |  | No | Indicator that a document should be visible to others besides the author and learner |
| `mime_type` | `TEXT` |  | Yes | Indicates the nature and format of the document or file as defined and standardized in IETF's RFC 6838 |
| `waive_right_to_access_indicator` | `BOOLEAN` |  | Yes | Indicator that a student waived the right to access a letter of recommendation |
| `exclude_from_learner_financial_aid_indicator` | `BOOLEAN` |  | Yes | Indicator that the students wants to exclude the letter of recommendation in their scholarship application |
| `financial_aid_document_status` | `TEXT` |  | Yes | Status of a document submitted with the financial aid application |
| `completion_status` | `TEXT` |  | Yes | Indicates how far along a document is in the process of being authored |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonEthnicity

**SQL identifier:** `person.person_ethnicity`

Associates a person with a governed ethnicity definition without collapsing ethnicity into race.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonLookup.PersonIdentifier` | No | Person. |
| `ethnicity_identifier` | `TEXT` | PK, FK → `EthnicityLookup.EthnicityIdentifier` | No | Governed ethnicity. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonGenderIdentity

**SQL identifier:** `person.person_gender_identity`

Tenant-scoped association between a person and a governed gender-identity definition, preserving source lineage independently from legal sex and transgender indicator.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_gender_identity_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the person gender-identity association. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person associated with the governed gender identity. |
| `gender_identity_identifier` | `TEXT` | FK → `GenderIdentityLookup.GenderIdentityIdentifier` | No | Governed gender identity associated with the person. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the person gender-identity association by the originating source system, when supplied. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonIdentityDocument

**SQL identifier:** `person.person_identity_document`

Identity document held or reported for a person, with governed type and issuing jurisdiction.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person. |
| `person_identity_document_identifier` | `TEXT` | PK | No | GUIDE-owned identity-document identifier. |
| `identity_document_type_identifier` | `TEXT` | FK → `IdentityDocumentTypeLookup.IdentityDocumentTypeIdentifier` | No | Governed document type. |
| `document_number` | `TEXT` |  | No | Document identifier/number. |
| `issuing_country_code` | `TEXT` |  | Yes | Issuing country code. |
| `issuing_region_code` | `TEXT` |  | Yes | Issuing region code. |
| `expiration_date` | `DATE` |  | Yes | Document expiration date. |
| `source_raw_document_category` | `TEXT` |  | Yes | Raw source document category. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonImmigrationStatus

**SQL identifier:** `person.person_immigration_status`

A table that stores visa, immigration, permit, and study/work authorization facts for a person, including broad immigration status type, visa type, visa status, visa-required and visa-holder indicators, issuing country, issue and expiration dates, effective dates, source raw immigration/visa values, source lineage, and audit fields. It keeps immigration and visa facts distinct from citizenship, address history, residency classification, and birth location.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the person associated with the immigration-status record. |
| `sequence_number` | `TEXT` | PK | No | Sequence number distinguishing multiple immigration-status records for the same person. |
| `immigration_status_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Reference-code value identifying the broad immigration, permit, or authorization classification being recorded. |
| `visa_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the visa type where a visa-specific fact is recorded. |
| `visa_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the high-level status of the visa or visa-related record. |
| `visa_required_indicator` | `BOOLEAN` |  | Yes | Indicates whether the person is recorded as requiring a visa for the relevant study, work, enrollment, or institutional context. |
| `visa_holder_indicator` | `BOOLEAN` |  | Yes | Indicates whether the person is recorded as holding a visa in the relevant source or institutional context. |
| `visa_issuing_country_code` | `TEXT` |  | Yes | ISO 3166-1 alpha-2 code for the country or jurisdiction that issued the visa, where known. |
| `visa_issued_date` | `DATE` |  | Yes | Date on which the visa was issued, where known. |
| `visa_expiration_date` | `DATE` |  | Yes | Date on which the visa expires, where applicable and known. |
| `immigration_status_start_date` | `DATE` |  | Yes | Date on which the immigration-status or authorization classification began, where known. |
| `immigration_status_end_date` | `DATE` |  | Yes | Date on which the immigration-status or authorization classification ended, where applicable and known. |
| `source_raw_immigration_status_type` | `TEXT` |  | Yes | Raw source-system immigration-status or authorization type before canonical mapping. |
| `source_raw_visa_type` | `TEXT` |  | Yes | Raw source-system visa type before canonical mapping. |
| `source_raw_visa_status` | `TEXT` |  | Yes | Raw source-system visa status before canonical mapping. |
| `source_raw_visa_required` | `TEXT` |  | Yes | Raw source-system visa-required value before canonical interpretation. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the immigration-status record was imported, synchronized, or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the immigration-status record or source person immigration entry. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time on which the immigration-status record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time on which the immigration-status record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time on which the immigration-status record was soft-deleted. |

## PersonInterest

**SQL identifier:** `person.person_interest`

A table containing a history of the learner's reported interests.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_interest_identifier` | `TEXT` | PK | No | Unique identifier for a learner interest item |
| `interest_identifier` | `TEXT` | FK → `InterestLookup.InterestIdentifier` | Yes | Unique identifier of an interest item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `input` | `TEXT` |  | Yes | Free-form input to describe the learner interest |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonNameTypeLookup

**SQL identifier:** `person.person_name_type_lookup`

Governed personnametype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_name_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the person name type. |
| `title` | `TEXT` |  | No | Human-readable name of the person name type. |
| `description` | `TEXT` |  | Yes | Detailed description of the person name type. |
| `category` | `TEXT` |  | Yes | Governed/source category for PersonNameTypeLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the person name type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonNonIdentifiableDemographics

**SQL identifier:** `person.person_non_identifiable_demographics`

A table containing details about a the non-identifiable demographics as reported by the learner.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_non_identifiable_demographics_identifier` | `TEXT` | PK | No | Unique identifier for the person's non-identifiable demographic information |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `number_of_dependents` | `INTEGER` |  | Yes | The number of dependents who live with the student and receive more than half their support from them |
| `number_of_dependents_type` | `TEXT` |  | Yes | The student's relationship to the dependents who live with the student or receive more than half of the student's support |
| `paternal_guardian_education` | `TEXT` |  | Yes | The highest level of education attained by a person's father or paternal guardian |
| `single_parent_or_single_pregnant_woman_status_indicator` | `BOOLEAN` |  | No | A student who, at some time during the school year, is either a pregnant female student who is unmarried; or a male or female student who is unmarried or legally separated from a spouse and has a minor child or children |
| `children_of_fallen_heroes_indicator` | `BOOLEAN` |  | No | Pell-eligible students whose parent or guardian was a member of the US armed forces and died as a result of military resource performed in Iraq or Afghanistan after the events of 9/11 or a public safety officer and died as a result of active resource in the line of duty At the time of the parent's or guardian's death, the student must be less than 24 years of age or enrolled in college or career school at least part-time |
| `first_generation_college_student` | `BOOLEAN` |  | Yes | The term First Generation College Student means an individual both of whose parents did not complete a baccalaureate degree or in the case of any individual who regularly resided with and received support from only one parent, an individual whose only such parent did not complete a baccalaureate degree |
| `homelessness_status_indicator` | `BOOLEAN` |  | No | Children and youth who lack a fixed, regular, and adequate nighttime residence Homeless children and youth include: 1) children and youth who are sharing the housing of other persons due to loss of housing, economic hardship, or a similar reason; are living in motels, hotels, trailer parks, or camping grounds due to the lack of alternative adequate accommodations; are living in emergency or transitional shelters; are abandoned in hospitals; or are awaiting foster care placement; 2) children and youth who have a primary nighttime residence that is a public or private place not designed for or originally used as a regular sleeping accommodation for human beings; or 3) children and youths who are living in cars, parks, public spaces, abandoned buildings, substandard housing, bus or train stations, or similar settings 4) migratory children who qualify as homeless because the children are living in circumstances described in the above (See Section 103 of the McKinney Act for a more detailed description of this data element) |
| `homelessness_status_start_date` | `DATE` |  | Yes | Indicates the month, day, and year upon which the student began being homeless |
| `homelessness_status_end_date` | `DATE` |  | Yes | Indicates the month, day, and year upon which the student stopped being homeless |
| `agriculture_migrant_status_indicator` | `BOOLEAN` |  | No | Persons who are, or whose parents or spouses are, migratory agricultural workers, including migratory dairy workers, or migratory fishers, and who, in the preceding 36 months, in order to obtain, or accompany such parents or spouses, in order to obtain, temporary or seasonal employment in agricultural or fishing work (A) have moved from one LEA to another; (B) in a state that comprises a single LEA, have moved from one administrative area to another within such LEA; or (C) reside in an LEA of more than 15,000 square miles, and migrate a distance of 20 miles or more to a temporary residence to engage in a fishing activity |
| `public_assistance_status_indicator` | `BOOLEAN` |  | No | A person who receives financial assistance from Federal, State, or local government agencies, including Temporary Assistance for Needy Families or equivalent |
| `maternal_guardian_education` | `TEXT` |  | Yes | The highest level of education attained by a person's mother or maternal guardian |
| `naspa_first_generation_college_student` | `TEXT` |  | Yes | Indicates NASPA's coding for first generation status of the student |
| `incarcerated_status` | `TEXT` |  | Yes | Indicates person's incarceration status |
| `orphan_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the person is or was an orphan (no living or biological parent) |
| `orphan_status_start_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person became an orphan (no living or biological parent) |
| `orphan_status_end_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person was no longer an orphan (no living or biological parent) |
| `ward_of_the_court_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the person is or was a ward of the court |
| `ward_of_the_court_start_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person became a ward of the court |
| `ward_of_the_court_end_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person was no longer a ward of the court |
| `foster_care_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the person is or was in foster care |
| `foster_care_status_start_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person began foster care |
| `foster_care_status_end_date` | `DATE` |  | Yes | Indicates the month, day, and year that the person was no longer in foster care |
| `guardianship_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether the student is or was in a legal guardianship with someone other than their parent or stepparent, as determined by a court in their state of residence |
| `self_supporting_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time on or after July 1, the student was unaccompanied and either (1) homeless or (2) self-supporting and at risk of being homeless |
| `unusual_circumstances_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether unusual circumstances prevent the student from contacting their parents or whether contacting their parents pose a risk to the student. A student may be experiencing unusual circumstances if they: left home due to an abusive or threatening environment; are abandoned by or estranged from their parents and have not been adopted; have refugee or asylee status and are separated from their parents, or their parents are displaced in a foreign country; are a victim of human trafficking; are incarcerated, or their parents are incarcerated and contact with the parents would pose a risk to the student; or are otherwise unable to contact or locate their parents and have not been adopted. |
| `parent_marital_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the student's parents are married to each other |
| `parent_unwilling_to_provide_fafsa_information_indicator` | `BOOLEAN` |  | Yes | Indicates whether the student's parents unwilling to provide their information, but the student doesn't have an unusual circumstance that prevents them from contacting or obtaining their parents' information, meaning that the student wants a financial aid administrator at their school to use their FAFSA information to determine their eligibility for a Direct Unsubsidized Loan only |
| `education_verification_method` | `TEXT` |  | Yes | The method by which the formal education is verified |
| `homeless_primary_residence` | `TEXT` |  | Yes | The primary nighttime residence of the students at the time the students are identified as homeless |
| `education_highest_level` | `TEXT` |  | Yes | The extent of formal instruction a person has received. The highest grade in school completed or its equivalent or the highest degree received. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonOrganizationMembership

**SQL identifier:** `person.person_organization_membership`

Tenant-scoped fact representing a person's membership, participation, or role in an organization, optionally bounded by an academic term and start/end dates. Distinct from a general activity definition and from employment or academic enrollment relationships.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_organization_membership_identifier` | `TEXT` | PK | No | Unique identifier for the person-to-organization membership or involvement fact. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Identifier of the person participating in or belonging to the organization. |
| `membership_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Identifier of the organization in which the person participates or holds membership. |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Academic term or period associated with the membership or involvement when applicable. |
| `start_date` | `DATE` |  | Yes | Date on which the person's membership or involvement began. |
| `end_date` | `DATE` |  | Yes | Date on which the person's membership or involvement ended. |
| `role` | `TEXT` |  | Yes | Role held by the person in the organization during the membership or involvement. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this membership/involvement record in the source system. |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system. |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system. |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## PersonPrivacyStatus

**SQL identifier:** `person.person_privacy_status`

Current or effective person-level privacy status supplied by a governed privacy-status definition.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person. |
| `person_privacy_status_identifier` | `TEXT` | PK | No | GUIDE-owned privacy-status assignment identifier. |
| `privacy_status_identifier` | `TEXT` | FK → `PrivacyStatusLookup.PrivacyStatusIdentifier` | No | Governed privacy status. |
| `source_raw_privacy_category` | `TEXT` |  | Yes | Raw source privacy category. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonRace

**SQL identifier:** `person.person_race`

A tenant-scoped association table linking a person to one or more canonical race values while preserving source lineage where needed.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_race_identifier` | `TEXT` | PK | No | Unique identifier for the person race association. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Tenant-scoped identifier for the person associated with the race value. |
| `race_identifier` | `TEXT` | FK → `RaceLookup.RaceIdentifier` | No | Identifier for the canonical race value selected for the person. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the person race association was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the person race association or source array member. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonRelatedContact

**SQL identifier:** `person.person_related_contact`

Stores limited information about a related or supporting contact who is not necessarily modeled as a GUIDE Person, including relationship/role, priority, one selected phone/contact method, one selected contact type, limited family-background facts, and source-group lineage. When multiple source phones or contact types are supplied, GUIDE intentionally retains only the first applicable value rather than creating repeated child rows.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the learner or person to whom the related contact belongs. |
| `sequence_number` | `TEXT` | PK | No | Tenant-local sequence distinguishing related-contact rows for the same person. For grouped source resources, assign deterministically within the person/source contact set; it is not a source-issued durable identifier. |
| `contact_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the broad category of related contact. |
| `relationship_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying who the contact is in relation to the person. |
| `contact_role_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the functional role the contact plays for the person. |
| `contact_priority_number` | `INTEGER` |  | Yes | Source or institutional priority/order for the contact, such as Guardian 1 or Guardian 2. |
| `contact_name` | `TEXT` |  | Yes | Source-supplied or displayable full name of the related contact. |
| `first_name` | `TEXT` |  | Yes | Structured given name of the related contact when supplied or reliably parsed. |
| `last_name` | `TEXT` |  | Yes | Structured family name of the related contact when supplied or reliably parsed. |
| `primary_contact_indicator` | `BOOLEAN` |  | Yes | Indicates whether this contact is treated as the primary contact for the person. |
| `primary_guardian_indicator` | `BOOLEAN` |  | Yes | Indicates whether this contact is treated as the primary guardian for the person. |
| `emergency_contact_indicator` | `BOOLEAN` |  | Yes | Indicates whether this contact may be used as an emergency contact. |
| `authorized_contact_indicator` | `BOOLEAN` |  | Yes | Indicates whether this contact is authorized for appropriate institutional contact under local policy. |
| `lives_with_indicator` | `BOOLEAN` |  | Yes | Indicates whether the person is recorded as living with this related contact. |
| `same_address_indicator` | `BOOLEAN` |  | Yes | Indicates whether this related contact shares the same address as the person. |
| `deceased_indicator` | `BOOLEAN` |  | Yes | Indicates whether the related contact is recorded as deceased. |
| `can_contact_indicator` | `BOOLEAN` |  | Yes | Indicates whether the institution may contact this related contact for the recorded purpose. |
| `email_address` | `TEXT` |  | Yes | Email address for the related contact when supplied. |
| `phone_number` | `TEXT` |  | Yes | Phone number retained for the related contact. If multiple source phones are supplied, retain only the first phone occurrence in deterministic source order. |
| `address_line1` | `TEXT` |  | Yes | First address line for the related contact when supplied. |
| `address_line2` | `TEXT` |  | Yes | Second address line for the related contact when supplied. |
| `city` | `TEXT` |  | Yes | City for the related contact address. |
| `state_province` | `TEXT` |  | Yes | State, province, or region for the related contact address. |
| `postal_code` | `TEXT` |  | Yes | Postal or ZIP code for the related contact address. |
| `country_code` | `TEXT` |  | Yes | ISO 3166-1 alpha-2 country or jurisdiction code associated with the related-contact address. |
| `highest_education_level_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the highest known education level for the related contact. |
| `college_attended_indicator` | `BOOLEAN` |  | Yes | Indicates whether the related contact is recorded as having attended college. |
| `college_name` | `TEXT` |  | Yes | Name of the college or institution attended by the related contact, when supplied. |
| `degree_earned_indicator` | `BOOLEAN` |  | Yes | Indicates whether the related contact is recorded as having earned a degree. |
| `highest_degree_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the highest known degree earned by the related contact. |
| `employer_name` | `TEXT` |  | Yes | Name of the related contact employer when supplied. |
| `occupation_text` | `TEXT` |  | Yes | Free-text occupation, job title, or employment description for the related contact. |
| `institution_employee_indicator` | `BOOLEAN` |  | Yes | Indicates whether the related contact is recorded as an employee of the institution. |
| `source_raw_contact_type` | `TEXT` |  | Yes | Selected original source-system contact-type value. If multiple source contact types are supplied, retain only the first available type for the related contact. |
| `source_raw_relationship_type` | `TEXT` |  | Yes | Original source-system value for the relationship type, before DHSS reference-code interpretation. |
| `source_raw_contact_role` | `TEXT` |  | Yes | Original source-system value for the contact role, before DHSS reference-code interpretation. |
| `source_raw_education_level` | `TEXT` |  | Yes | Original source-system value for the related contact education level. |
| `source_raw_college_name` | `TEXT` |  | Yes | Original source-system value for the related contact college name. |
| `source_raw_degree` | `TEXT` |  | Yes | Original source-system value for the related contact degree. |
| `source_raw_employer` | `TEXT` |  | Yes | Original source-system value for the related contact employer. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the related-contact row was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the source resource or source grouping from which the related-contact row was derived. It may repeat across multiple related-contact rows and is not the canonical row identity. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the related-contact row was created in DHSS. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the related-contact row was last updated in DHSS. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the related-contact row was soft-deleted, if applicable. |
| `middle_name` | `TEXT` |  | Yes | Structured middle name of the related contact when supplied. |
| `phone_country_calling_code` | `TEXT` |  | Yes | Country calling code associated with the retained first related-contact phone occurrence. |
| `phone_extension` | `TEXT` |  | Yes | Extension associated with the retained first related-contact phone occurrence. |
| `contact_availability_text` | `TEXT` |  | Yes | Source-supplied best-time or availability note associated with the retained first related-contact phone occurrence. |
| `contact_address_text` | `TEXT` |  | Yes | Source-formatted full address for the related contact when reliable structured parsing is unavailable. |

## PersonResidency

**SQL identifier:** `person.person_residency`

A table containing details of the person's residency declarations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_residency_identifier` | `TEXT` | PK | No | Unique identifier for a learner residency item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `united_states_citizenship_status` | `TEXT` |  | Yes | An indicator of whether or not the person is a US citizen (e.g. USCitizen, PermanentResident, ResidentAlien, NonResidentAlien, Refugee) |
| `visa_type` | `TEXT` |  | Yes | An indicator of a non-US citizen's Visa type |
| `tuition_residency_type` | `TEXT` |  | Yes | A person's residency status for tuition purposes |
| `campus_residency_type` | `TEXT` |  | Yes | A person's residency arrangement as defined in the Free Application for Federal Student Aid (FAFSA) |
| `legal_resident_of_state_start_date` | `DATE` |  | Yes | The month and year in which legal residency of the state began for the person |
| `united_states_residency_start_date` | `DATE` |  | Yes | US residency start date |
| `deferred_action_for_childhood_arrivals_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether the individual has Deferred Action for Childhood Arrivals (DACA) status in the United States |
| `temporary_protected_status_indicator` | `BOOLEAN` |  | Yes | Indicates whether the individual has Temporary Protected Status (TPS) as designated by the Secretary of Homeland Security or United States Citizenship and Immigration Resources (USCIS) |
| `congressional_district` | `TEXT` |  | Yes | The congressional district in which an address is located |
| `county_fips_code` | `TEXT` |  | Yes | The Federal Information Processing Standards (FIPS) numeric code for the county issued by the National Institute of Standards and Technology (NIST). Counties are considered to be the "first-order subdivisions" of each State and statistically equivalent entity, regardless of their local designations (county, parish, borough, etc.) Counties in different States will have the same code. A unique county number is created when combined with the 2-digit FIPS State Code. |
| `publish_indicator` | `BOOLEAN` |  | No | An indication that the address should be published to a visible directory, application, or website, etc. |
| `residence_setting` | `TEXT` |  | Yes | A general geographic indicator that categorizes U.S. territory (e.g. City, Suburban) |
| `residence_verification` | `TEXT` |  | Yes | An accepted form of proof of residency in the district/county/other locality |
| `record_start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The effective date for which the address is valid. For physical addresses, the periods in which the person lived at that address. |
| `record_end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The expired date for which the address is valid. For physical addresses, the periods in which the person lived at that address. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `residency_type_identifier` | `TEXT` | FK → `ResidencyTypeLookup.ResidencyTypeIdentifier` | Yes | Governed residency type. |
| `administrative_period_identifier` | `TEXT` | FK → `AdministrativePeriodLookup.AdministrativePeriodIdentifier` | Yes | Starting administrative period for the residency determination. |

## PersonServiceRestriction

**SQL identifier:** `person.person_service_restriction`

An institutionally imposed restriction assigned to a person for a governed reason. The restriction may be date- or term-scoped and may be affirmatively released. Current effectiveness is derived from its effective period and release rather than stored as a generic status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_service_restriction_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the restriction assigned to the person. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person to whom the institutional service restriction applies. |
| `service_restriction_reason_identifier` | `TEXT` | FK → `ServiceRestrictionReasonLookup.ServiceRestrictionReasonIdentifier` | No | Governed reason explaining why the restriction was imposed. |
| `start_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional first academic or administrative term to which the restriction applies. |
| `end_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional last academic or administrative term to which the restriction applies. |
| `effective_start_date` | `DATE` |  | Yes | Optional date on which the restriction begins to have institutional effect. |
| `effective_end_date` | `DATE` |  | Yes | Optional date after which the restriction is no longer intended to have institutional effect. |
| `release_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the institution affirmatively released or removed the restriction. Null when no explicit release has occurred. |
| `responsible_organization_unit_identifier` | `TEXT` | FK → `OrganizationUnit.OrganizationUnitIdentifier` | Yes | Optional organizational unit responsible for administering or resolving the restriction. |
| `comments` | `TEXT` |  | Yes | Optional contextual comments about the assigned restriction. Do not use this field as a substitute for governed reason or impact semantics. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the canonical record was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the record in the source system. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the canonical record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that soft-deleted the canonical record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was soft-deleted, if applicable. |

## PersonServiceRestrictionImpact

**SQL identifier:** `person.person_service_restriction_impact`

One concrete institutional service, action, or process affected by a PersonServiceRestriction. A restriction may have multiple impacts, and each impact may optionally have its own date or term scope.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_service_restriction_identifier` | `TEXT` | PK, FK → `PersonServiceRestriction.PersonServiceRestrictionIdentifier` | No | Restriction whose concrete institutional effect is being recorded. |
| `impact_sequence_number` | `TEXT` | PK | No | Tenant-local sequence distinguishing multiple impacts for the same restriction. |
| `service_restriction_impact_identifier` | `TEXT` | FK → `ServiceRestrictionImpactLookup.ServiceRestrictionImpactIdentifier` | No | Governed service, action, or process prevented or limited by this restriction. |
| `start_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional first term during which this specific impact applies. |
| `end_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional last term during which this specific impact applies. |
| `effective_start_date` | `DATE` |  | Yes | Optional date on which this specific impact begins to apply. |
| `effective_end_date` | `DATE` |  | Yes | Optional date after which this specific impact no longer applies. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the canonical impact row. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical impact row was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical impact row. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical impact row was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that soft-deleted the canonical impact row. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical impact row was soft-deleted, if applicable. |

## PersonStrength

**SQL identifier:** `person.person_strength`

A table containing the strengths assigned to a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_strength_identifier` | `TEXT` | PK | No | Unique identifier for the person's strength |
| `strength_identifier` | `TEXT` | FK → `StrengthLookup.StrengthIdentifier` | No | Unique identifier for strength |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `score` | `TEXT` |  | Yes | An alphanumeric value indicating the degree to which the strength is associated with the person |
| `score_scheme_description` | `TEXT` |  | Yes | Description of the scheme used to determine the strength score |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonTagAssignment

**SQL identifier:** `person.person_tag_assignment`

A tenant-scoped effective-dated assignment of a governed person tag to a person, optionally bounded by administrative periods and calendar dates.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_tag_assignment_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the person tag assignment. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Identifier of the person receiving the tag assignment. |
| `person_tag_identifier` | `TEXT` | FK → `PersonTagLookup.PersonTagIdentifier` | No | Identifier of the governed person tag. |
| `start_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional starting administrative period for the tag assignment. |
| `end_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional ending administrative period for the tag assignment. |
| `start_date` | `DATE` |  | Yes | Effective start date of the tag assignment. |
| `end_date` | `DATE` |  | Yes | Effective end date of the tag assignment. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonTask

**SQL identifier:** `person.person_task`

A table containing a history of incomplete and complete tasks assigned to a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_task_author_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Unique identifier for the person authoring the task |
| `person_task_identifier` | `TEXT` | PK | No | A unique identifier for the task |
| `person_goal_identifier` | `TEXT` | FK → `PersonGoal.PersonGoalIdentifier` | Yes | Unique identifier for the person goal |
| `caseload_communication_identifier` | `TEXT` | FK → `PersonCaseloadCommunication.PersonCaseloadCommunicationIdentifier` | Yes | Unique identifier for the caseload communication |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the assessment |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | Yes | Unique identifier for the FAFSA or other financial aid application |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `due_date` | `DATE` |  | No | Deadline for the task to be completed |
| `status` | `TEXT` |  | No | Status of the task (open, closed) |
| `priority` | `TEXT` |  | Yes | Priority of the task (e.g. high, medium, low) |
| `sequence_number` | `INTEGER` |  | Yes | Number indicating when in a sequence of categorized tasks this one should be completed |
| `category` | `TEXT` |  | Yes | Category or type of task assigned to the person |
| `details` | `TEXT` |  | Yes | Complete details of the task assigned to a person |
| `outcome_description` | `TEXT` |  | Yes | A description of the intended outcome of the task |
| `visible_indicator` | `BOOLEAN` |  | No | Indicates the task should be visible to others besides the author and assignee |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Revision of the Assessment referenced by this record. |

## PersonTransportation

**SQL identifier:** `person.person_transportation`

A table containing details about a person's transportation status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_transportation_identifier` | `TEXT` | PK | No | Unique identifier for the person's transportation |
| `learner_resource_participation_identifier` | `TEXT` | FK → `LearnerResourceParticipation.LearnerResourceParticipationIdentifier` | Yes | Unique identifier for the person's resource record |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `transportation_type` | `TEXT` |  | Yes | Indicates the type of transportation (e.g. Bus, RideShare, Automobile, Bicycle, ElectricScooter, Scooter, Skateboard, Walking, etc.) |
| `transit_provider` | `TEXT` |  | Yes | Name of the transportation provider (e.g. City Bus, Uber, Lyft, MetroRail) |
| `vehicle_ownership_status` | `TEXT` |  | Yes | Indicates the ownership relationship the person has to the vehicle (e.g. Owned, Lease, Loan, FamilySharedCar, Borrowed, NoCar) |
| `vehicle_condition` | `TEXT` |  | Yes | Indicates the status of the vehicle's operational condition (e.g. Reliable, NeedsRepairs, NonOperational) |
| `loan_or_lease_monthly_cost` | `NUMERIC` |  | Yes | Monthly loan/lease payment amount |
| `maintenance_repairs_monthly_cost` | `NUMERIC` |  | Yes | Approximate monthly repairs or maintenance cost for the vehicle |
| `car_insurance_status` | `TEXT` |  | Yes | Indicates whether or not the vehicle is insured |
| `car_insurance_monthly_cost` | `NUMERIC` |  | Yes | Monthly car insurance payment amount |
| `car_fuel_monthly_cost` | `NUMERIC` |  | Yes | Estimated monthly cost of fuel |
| `total_monthly_cost` | `NUMERIC` |  | Yes | Total monthly transportation cost |
| `transportation_subsidy_amount` | `NUMERIC` |  | Yes | Amount of financial support for transportation |
| `transportation_subsidy_end_date` | `DATE` |  | Yes | Date the subsidy or discount expires |
| `usage_frequency` | `TEXT` |  | Yes | The frequency with which the transportation is utilized |
| `critical_for_school` | `TEXT` |  | Yes | Indicates how critical the transportation is for the person to attend school (e.g. Essential, Helpful, NotNeeded) |
| `critical_for_work` | `TEXT` |  | Yes | Indicates how critical the transportation is for the person to attend work (e.g. Essential, Helpful, NotNeeded) |
| `last_used_date` | `DATE` |  | Yes | Last recorded usage of the transportation |
| `transportation_notes` | `TEXT` |  | Yes | Comments or notes about the transportation |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonalPronounLookup

**SQL identifier:** `person.personal_pronoun_lookup`

Governed personalpronoun definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `personal_pronoun_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the personal pronoun. |
| `title` | `TEXT` |  | No | Human-readable name of the personal pronoun. |
| `description` | `TEXT` |  | Yes | Detailed description of the personal pronoun. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the personal pronoun value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonalRelationship

**SQL identifier:** `person.personal_relationship`

Tenant-scoped effective relationship between two identified canonical Persons.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `personal_relationship_identifier` | `TEXT` | PK | No | GUIDE-owned relationship identifier. |
| `subject_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Subject person. |
| `related_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Related person. |
| `direct_relationship_type_identifier` | `TEXT` | FK → `PersonalRelationshipTypeLookup.PersonalRelationshipTypeIdentifier` | No | Subject-to-related relationship type. |
| `reciprocal_relationship_type_identifier` | `TEXT` | FK → `PersonalRelationshipTypeLookup.PersonalRelationshipTypeIdentifier` | Yes | Related-to-subject reciprocal relationship type. |
| `personal_relationship_status_identifier` | `TEXT` | FK → `PersonalRelationshipStatusLookup.PersonalRelationshipStatusIdentifier` | Yes | Governed relationship status. |
| `start_date` | `DATE` |  | Yes | Relationship effective start date. |
| `end_date` | `DATE` |  | Yes | Relationship effective end date. |
| `comment_text` | `TEXT` |  | Yes | Source or institutional comment about the relationship. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Source relationship identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonalRelationshipStatusLookup

**SQL identifier:** `person.personal_relationship_status_lookup`

Tenant-scoped governed lifecycle statuses for person-to-person relationships.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `personal_relationship_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for governed lifecycle statuses for person-to-person relationships. |
| `code` | `TEXT` |  | No | Institutional/source code. |
| `title` | `TEXT` |  | No | Human-readable name of the personal relationship status. |
| `description` | `TEXT` |  | Yes | Detailed description of the personal relationship status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the personal relationship status value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonalRelationshipTypeLookup

**SQL identifier:** `person.personal_relationship_type_lookup`

Tenant-scoped governed person-to-person relationship types.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `personal_relationship_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for governed person-to-person relationship types. |
| `code` | `TEXT` |  | No | Institutional/source code. |
| `title` | `TEXT` |  | No | Human-readable name of the personal relationship type. |
| `description` | `TEXT` |  | Yes | Detailed description of the personal relationship type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the personal relationship type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |
| `relationship_category` | `TEXT` |  | Yes | Source-defined broad relationship category retained separately from the governed relationship code. |

## PersonalRelationshipTypeReciprocal

**SQL identifier:** `person.personal_relationship_type_reciprocal`

Valid governed reciprocal relationship-type pairing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `direct_relationship_type_identifier` | `TEXT` | PK, FK → `PersonalRelationshipTypeLookup.PersonalRelationshipTypeIdentifier` | No | Direct relationship type. |
| `reciprocal_relationship_type_identifier` | `TEXT` | PK, FK → `PersonalRelationshipTypeLookup.PersonalRelationshipTypeIdentifier` | No | Valid reciprocal relationship type. |
| `reciprocal_relationship_detail` | `TEXT` |  | Yes | Optional source-defined extension or detail for the reciprocal pairing. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PhoneTypeLookup

**SQL identifier:** `person.phone_type_lookup`

Governed phonetype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `phone_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the phone type. |
| `title` | `TEXT` |  | No | Human-readable name of the phone type. |
| `description` | `TEXT` |  | Yes | Detailed description of the phone type. |
| `standard_phone_type` | `TEXT` |  | Yes | Governed/source category for PhoneTypeLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the phone type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PrivacyStatusLookup

**SQL identifier:** `person.privacy_status_lookup`

Governed privacystatus definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `privacy_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the privacy status. |
| `title` | `TEXT` |  | No | Human-readable name of the privacy status. |
| `description` | `TEXT` |  | Yes | Detailed description of the privacy status. |
| `category` | `TEXT` |  | Yes | Governed/source category for PrivacyStatusLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the privacy status value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## RaceLookup

**SQL identifier:** `person.race_lookup`

A governed lookup table defining canonical race values used by PersonRace.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `race_identifier` | `TEXT` | PK | No | Unique identifier for a canonical race value. |
| `race_code` | `TEXT` |  | No | Stable code for the canonical race value. |
| `race_name` | `TEXT` |  | No | Concise display name for the canonical race value. |
| `race_description` | `TEXT` |  | Yes | Full semantic definition of the canonical race value. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the canonical race value is active for current use. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the race value by the originating source system. |

## RaceReportingClassification

**SQL identifier:** `person.race_reporting_classification`

Tenant-scoped crosswalk from an institution/source race definition to a current governed external reporting category. Crosswalk rows may be activated or inactivated; no effective-dated or version history is maintained.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `race_reporting_classification_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the race reporting crosswalk row. |
| `race_identifier` | `TEXT` | FK → `RaceLookup.RaceIdentifier` | No | Canonical race definition being classified. |
| `reporting_category_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Current governed external reporting category assigned to this race definition. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether this race-to-reporting-category crosswalk is active for current use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system that supplied or governs this crosswalk, when applicable. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the crosswalk row, when supplied. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ResidencyTypeLookup

**SQL identifier:** `person.residency_type_lookup`

Governed residencytype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `residency_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the residency type. |
| `title` | `TEXT` |  | No | Human-readable name of the residency type. |
| `description` | `TEXT` |  | Yes | Detailed description of the residency type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the residency type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## ServiceRestrictionImpactLookup

**SQL identifier:** `person.service_restriction_impact_lookup`

Tenant-governed definition of an institutional service, action, or process that may be prevented or limited by a person service restriction, such as registration, transcript release, diploma release, or financial-aid processing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `service_restriction_impact_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the governed service-restriction impact. |
| `code` | `TEXT` |  | No | Institution-defined code for the affected service, action, or process. |
| `title` | `TEXT` |  | No | Human-readable name of the affected service, action, or process. |
| `description` | `TEXT` |  | Yes | Description of the institutional service, action, or process that may be prevented or limited by a restriction. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the canonical record was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the record in the source system. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the canonical record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that soft-deleted the canonical record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was soft-deleted, if applicable. |

## ServiceRestrictionReasonLookup

**SQL identifier:** `person.service_restriction_reason_lookup`

Tenant-governed definition of why an institutional service restriction may be imposed on a person. Separates the cause of a restriction from the services or actions it affects and may provide institution-facing or person-facing resolution guidance.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `service_restriction_reason_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the governed service-restriction reason. |
| `code` | `TEXT` |  | No | Institution-defined code for the restriction reason. |
| `title` | `TEXT` |  | No | Human-readable name of the restriction reason. |
| `description` | `TEXT` |  | Yes | Description of the condition or institutional reason that may cause the restriction. |
| `resolution_instructions` | `TEXT` |  | Yes | Optional guidance describing how the person may satisfy or resolve the underlying condition. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the canonical record was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the record in the source system. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the canonical record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that soft-deleted the canonical record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was soft-deleted, if applicable. |

## SocialMediaTypeLookup

**SQL identifier:** `person.social_media_type_lookup`

Governed socialmediatype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `social_media_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the social media type. |
| `title` | `TEXT` |  | No | Human-readable name of the social media type. |
| `description` | `TEXT` |  | Yes | Detailed description of the social media type. |
| `standard_social_media_type` | `TEXT` |  | Yes | Governed/source category for SocialMediaTypeLookup. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the social media type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## StrengthCategoryLookup

**SQL identifier:** `person.strength_category_lookup`

A lookup table containing categories that can be applied to strengths.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `strength_category_identifier` | `TEXT` | PK | No | Unique identifier for strength category |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StrengthDetailLookup

**SQL identifier:** `person.strength_detail_lookup`

A lookup table containing details describing a strength.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `strength_detail_identifier` | `TEXT` | PK | No | Unique identifier for strength detail |
| `strength_identifier` | `TEXT` | FK → `StrengthLookup.StrengthIdentifier` | No | Unique identifier for strength |
| `detail` | `TEXT` |  | No | User readable strength detail description |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StrengthLookup

**SQL identifier:** `person.strength_lookup`

A lookup table containing strengths that can be assigned to a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `strength_identifier` | `TEXT` | PK | No | Unique identifier for strength |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `category_identifier` | `TEXT` | FK → `StrengthCategoryLookup.StrengthCategoryIdentifier` | No | Unique identifier for strength category |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## SuccessIndicatorLookup

**SQL identifier:** `person.success_indicator_lookup`

A lookup table containing a list of success indicators that may be used in a success plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `success_indicator_identifier` | `TEXT` | PK | No | Unique identifier for the success indicator |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `type` | `TEXT` |  | No | Type of an indicator item |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## SuccessPredictionModel

**SQL identifier:** `person.success_prediction_model`

Tenant-scoped definition of a predictive model used to estimate a learner outcome such as persistence, retention, completion, or graduation. Model identity and interpretation are separated from individual learner prediction results.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `success_prediction_model_identifier` | `TEXT` | PK | No | Unique identifier for the learner success prediction model. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Optional source system from which the model definition was obtained. |
| `name` | `TEXT` |  | No | Human-readable name of the prediction model. |
| `target_outcome` | `TEXT` |  | No | Higher-education outcome the model is intended to predict, such as persistence, retention, completion, or graduation. |
| `model_version` | `TEXT` |  | Yes | Optional source- or institution-defined model version. |
| `time_horizon_description` | `TEXT` |  | Yes | Optional description of the outcome horizon used by the model, such as next academic term or completion within six years. |
| `description` | `TEXT` |  | Yes | Narrative description of the model and the interpretation of its outputs. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the model definition in the source system. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
