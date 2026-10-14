# Entity: Admissions

This page documents every table that belongs to the **Admissions** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 17**

## Table of contents

- [ApplicationDecisionTypeLookup](#applicationdecisiontypelookup)
- [ApplicationSourceLookup](#applicationsourcelookup)
- [ApplicationStatusLookup](#applicationstatuslookup)
- [ApplicationTypeLookup](#applicationtypelookup)
- [LearnerApplication](#learnerapplication)
- [LearnerApplicationChecklistItem](#learnerapplicationchecklistitem)
- [LearnerApplicationDecision](#learnerapplicationdecision)
- [LearnerApplicationDeposit](#learnerapplicationdeposit)
- [LearnerApplicationEvent](#learnerapplicationevent)
- [LearnerApplicationFee](#learnerapplicationfee)
- [LearnerApplicationFeeWaiver](#learnerapplicationfeewaiver)
- [LearnerApplicationIntent](#learnerapplicationintent)
- [LearnerApplicationProgramInterest](#learnerapplicationprograminterest)
- [LearnerApplicationResponse](#learnerapplicationresponse)
- [LearnerApplicationReview](#learnerapplicationreview)
- [LearnerApplicationStatusHistory](#learnerapplicationstatushistory)
- [LearnerApplicationWithdrawal](#learnerapplicationwithdrawal)

---

## ApplicationDecisionTypeLookup

**SQL identifier:** `admissions.application_decision_type_lookup`

A tenant-governed lookup defining formal admissions decision or outcome types used by application decisions. Values may reflect institution-specific admissions policy and vocabulary.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `application_decision_type_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a governed formal admissions decision type. |
| `application_decision_type_code` | `TEXT` |  | No | Stable system code for the tenant-governed formal admissions decision type |
| `application_decision_type_description` | `TEXT` |  | No | Human-readable description for the tenant-governed formal admissions decision type |
| `application_decision_type_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the tenant-governed formal admissions decision type |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the tenant-governed formal admissions decision type is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ApplicationSourceLookup

**SQL identifier:** `admissions.application_source_lookup`

A tenant-governed lookup defining business-facing application origins or channels, such as institution application, Common App, partner portal, recruiter entry, paper application, API import, or data import.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `application_source_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a governed application origin or channel. |
| `application_source_code` | `TEXT` |  | No | Stable system code for the tenant-governed application origin or channel |
| `application_source_description` | `TEXT` |  | No | Human-readable description for the tenant-governed application origin or channel |
| `application_source_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the tenant-governed application origin or channel |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the tenant-governed application origin or channel is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ApplicationStatusLookup

**SQL identifier:** `admissions.application_status_lookup`

A tenant-governed lookup defining application workflow status values used by applications and application status history. Values may reflect institution-specific admissions workflow and vocabulary.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `application_status_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a governed application workflow status. |
| `application_status_code` | `TEXT` |  | No | Stable system code for the tenant-governed application workflow status |
| `application_status_description` | `TEXT` |  | No | Human-readable description for the tenant-governed application workflow status |
| `application_status_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the tenant-governed application workflow status |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the tenant-governed application workflow status is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ApplicationTypeLookup

**SQL identifier:** `admissions.application_type_lookup`

A tenant-governed lookup defining admissions application entry paths or application processes, such as first-year, transfer, graduate, continuing education, international, visiting, or non-degree.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `application_type_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a governed admissions application entry path or process type. |
| `application_type_code` | `TEXT` |  | No | Stable system code for the tenant-governed admissions application entry path or process type |
| `application_type_name` | `TEXT` |  | No | Human-readable name or title for the tenant-governed admissions application entry path or process type |
| `application_type_description` | `TEXT` |  | Yes | Optional explanatory description for the tenant-governed admissions application entry path or process type |
| `application_type_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the tenant-governed admissions application entry path or process type |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the tenant-governed admissions application entry path or process type is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplication

**SQL identifier:** `admissions.learner_application`

A table containing the anchor or header record for a person's application to an institution for a particular admissions cycle, academic period, career or program context, or application process.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK | No | Tenant-scoped unique identifier for the learner application. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `application_number` | `TEXT` |  | Yes | User-facing or source-facing application number |
| `application_type_identifier` | `TEXT` | FK → `ApplicationTypeLookup.ApplicationTypeIdentifier` | Yes | Unique identifier for the admissions application entry path or process type |
| `application_source_identifier` | `TEXT` | FK → `ApplicationSourceLookup.ApplicationSourceIdentifier` | Yes | Unique identifier for the application origin or channel |
| `current_application_status_identifier` | `TEXT` | FK → `ApplicationStatusLookup.ApplicationStatusIdentifier` | Yes | Unique identifier for the current application workflow status |
| `current_application_status_date` | `DATE` |  | Yes | Date associated with the current application status |
| `application_date` | `DATE` |  | Yes | Date the application was created or initiated |
| `application_submitted_date` | `DATE` |  | Yes | Date the application was submitted |
| `application_completed_date` | `DATE` |  | Yes | Date the application was considered complete |
| `application_withdrawn_date` | `DATE` |  | Yes | Date the application was withdrawn |
| `application_withdrawal_reason_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application withdrawal reason |
| `entry_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for the intended entry term |
| `source_raw_application_type` | `TEXT` |  | Yes | Raw application type value from the source system |
| `source_raw_application_source` | `TEXT` |  | Yes | Raw application source value from the source system |
| `source_raw_application_status` | `TEXT` |  | Yes | Raw application status value from the source system |
| `source_raw_withdraw_reason` | `TEXT` |  | Yes | Raw withdrawal reason value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
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

## LearnerApplicationChecklistItem

**SQL identifier:** `admissions.learner_application_checklist_item`

A table recording application checklist requirements or requested materials associated with learner applications, including high-level status and completion dates.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this checklist item row within the learner application |
| `checklist_item_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Unique identifier for the application checklist item type |
| `checklist_item_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application checklist item status |
| `required_indicator` | `BOOLEAN` |  | No | Indicates whether the checklist item is required |
| `received_indicator` | `BOOLEAN` |  | No | Indicates whether the checklist item has been received |
| `waived_indicator` | `BOOLEAN` |  | No | Indicates whether the checklist item has been waived |
| `checklist_item_due_date` | `DATE` |  | Yes | Date the checklist item is due |
| `checklist_item_received_date` | `DATE` |  | Yes | Date the checklist item was received |
| `checklist_item_completed_date` | `DATE` |  | Yes | Date the checklist item was completed or satisfied |
| `checklist_item_waived_date` | `DATE` |  | Yes | Date the checklist item was waived |
| `checklist_item_description` | `TEXT` |  | Yes | Brief description or label for the checklist item |
| `source_raw_checklist_item_type` | `TEXT` |  | Yes | Raw checklist item type value from the source system |
| `source_raw_checklist_item_status` | `TEXT` |  | Yes | Raw checklist item status value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationDecision

**SQL identifier:** `admissions.learner_application_decision`

A table recording formal institutional admissions decisions or outcomes associated with a learner application.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this admissions decision row within the learner application |
| `application_decision_type_identifier` | `TEXT` | FK → `ApplicationDecisionTypeLookup.ApplicationDecisionTypeIdentifier` | No | Unique identifier for the formal admissions decision type |
| `decision_date` | `DATE` |  | No | Date the institution rendered the admissions decision |
| `decision_released_date` | `DATE` |  | Yes | Date the admissions decision was released or communicated to the applicant |
| `entry_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for the entry term associated with the decision |
| `academic_program_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for the academic program associated with the decision |
| `source_raw_application_decision_type` | `TEXT` |  | Yes | Raw application decision type value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationDeposit

**SQL identifier:** `admissions.learner_application_deposit`

A table recording admissions-facing application deposits or enrollment-deposit commitments associated with learner applications.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this application deposit row within the learner application |
| `deposit_amount` | `NUMERIC` |  | Yes | Amount expected, assessed, or paid for the application deposit |
| `application_deposit_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application deposit status |
| `deposit_due_date` | `DATE` |  | Yes | Date the application deposit was due |
| `deposit_paid_date` | `DATE` |  | Yes | Date the application deposit was paid |
| `deposit_waived_indicator` | `BOOLEAN` |  | No | Indicates whether the application deposit was waived |
| `deposit_refunded_indicator` | `BOOLEAN` |  | No | Indicates whether the application deposit was refunded |
| `deposit_refunded_date` | `DATE` |  | Yes | Date the application deposit was refunded |
| `source_raw_application_deposit_status` | `TEXT` |  | Yes | Raw application deposit status value from the source system |
| `source_raw_application_deposit_type` | `TEXT` |  | Yes | Raw application deposit type value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationEvent

**SQL identifier:** `admissions.learner_application_event`

A table recording notable dated occurrences in the lifecycle of a learner application when those occurrences are not better represented by a more specific application structure.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this application event row within the learner application |
| `application_event_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Unique identifier for the application event type |
| `application_event_date` | `DATE` |  | No | Date the application event occurred or was recognized |
| `application_event_description` | `TEXT` |  | Yes | Brief description or note for the application event |
| `source_raw_application_event_type` | `TEXT` |  | Yes | Raw application event or milestone type from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationFee

**SQL identifier:** `admissions.learner_application_fee`

A table recording admissions-facing application fee obligations, charges, requirements, and high-level fee disposition for learner applications.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this application fee row within the learner application |
| `fee_amount` | `NUMERIC` |  | Yes | Amount expected, assessed, or charged for the application fee |
| `application_fee_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application fee status |
| `fee_assessed_date` | `DATE` |  | Yes | Date the application fee was assessed or charged |
| `fee_due_date` | `DATE` |  | Yes | Date the application fee was due |
| `fee_satisfied_date` | `DATE` |  | Yes | Date the application fee requirement was satisfied |
| `fee_paid_date` | `DATE` |  | Yes | Date the application fee was paid |
| `fee_waived_indicator` | `BOOLEAN` |  | No | Indicates whether the application fee was waived |
| `fee_refunded_indicator` | `BOOLEAN` |  | No | Indicates whether the application fee was refunded |
| `source_raw_application_fee_status` | `TEXT` |  | Yes | Raw application fee status value from the source system |
| `source_raw_application_fee_type` | `TEXT` |  | Yes | Raw application fee type value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationFeeWaiver

**SQL identifier:** `admissions.learner_application_fee_waiver`

A table recording application-fee waiver requests, grants, denials, or waiver dispositions associated with learner applications and, when applicable, specific application fee rows.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplicationFee.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK, FK → `LearnerApplicationFee.SequenceNumber` | No | Sequence number for this fee waiver row within the learner application |
| `application_fee_sequence_number` | `INTEGER` |  | Yes | Sequence number of the related application fee row, when the waiver applies to a specific fee row |
| `fee_waiver_reason_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application fee waiver reason |
| `fee_waiver_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application fee waiver status |
| `fee_waiver_requested_date` | `DATE` |  | Yes | Date the application fee waiver was requested |
| `fee_waiver_approved_date` | `DATE` |  | Yes | Date the application fee waiver was approved |
| `fee_waiver_denied_date` | `DATE` |  | Yes | Date the application fee waiver was denied |
| `fee_waiver_amount` | `NUMERIC` |  | Yes | Amount of the application fee waived |
| `fee_waiver_reason_text` | `TEXT` |  | Yes | Free-text explanation of the application fee waiver reason |
| `source_raw_fee_waiver_reason` | `TEXT` |  | Yes | Raw fee waiver reason value from the source system |
| `source_raw_fee_waiver_status` | `TEXT` |  | Yes | Raw fee waiver status value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationIntent

**SQL identifier:** `admissions.learner_application_intent`

A table for application-captured applicant-stated interests, intents, and lightweight preference signals (e.g., interest in Housing, Fin Aid, etc.)

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Identifies the learner application to which the intent record applies. |
| `sequence_number` | `TEXT` | PK | No | Provides a sequential number that uniquely distinguishes multiple intent records for the same learner application. |
| `application_intent_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Identifies the standardized type of intent expressed for the learner application. |
| `application_intent_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Identifies the current standardized status of the application intent. |
| `application_intent_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Records the date and time when the application intent was expressed, received, or became effective. |
| `entry_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifies the academic entry term associated with the stated application intent, when known. |
| `application_intent_text` | `TEXT` |  | Yes | Stores a human-readable statement or note describing the applicant's expressed intent. |
| `source_raw_application_intent_type` | `TEXT` |  | Yes | Preserves the source-system value that represented the application intent type before standardization. |
| `source_raw_application_intent_status` | `TEXT` |  | Yes | Preserves the source-system value that represented the application intent status before standardization. |
| `source_raw_application_intent_value` | `TEXT` |  | Yes | Preserves the complete source-system intent value when it cannot be represented fully by the standardized type and status fields. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifies the source system from which the application intent record originated. |
| `source_system_key_value` | `TEXT` |  | Yes | Stores the source-system key or identifier for the originating application intent record. |
| `created_by` | `BIGINT` |  | Yes | Identifies the user, service, or process that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Records the date and time when the record was created in DHSS. |
| `updated_by` | `BIGINT` |  | Yes | Identifies the user, service, or process that most recently updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Records the date and time when the record was most recently updated. |
| `deleted_by` | `BIGINT` |  | Yes | Identifies the user, service, or process that logically deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Records the date and time when the record was logically deleted. |

## LearnerApplicationProgramInterest

**SQL identifier:** `admissions.learner_application_program_interest`

A table recording applicant-stated academic programs, majors, credentials, or areas of study associated with a learner application.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this program interest row within the learner application |
| `academic_program_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for the applicant-stated academic program or area of study |
| `program_interest_rank` | `INTEGER` |  | Yes | Applicant-stated rank or preference order for the program interest |
| `primary_program_interest_indicator` | `BOOLEAN` |  | No | Indicates whether this program interest is the primary applicant-stated interest |
| `entry_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for the intended entry term for this program interest |
| `source_raw_academic_program` | `TEXT` |  | Yes | Raw academic program, major, credential, or area-of-study value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationResponse

**SQL identifier:** `admissions.learner_application_response`

A table recording the applicant’s formal response to an institutional admissions decision, offer, or yield action associated with a learner application, including response type, response date, optional deadline, related decision sequence, and source raw response values.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Identifier for the learner application associated with the applicant response. |
| `sequence_number` | `TEXT` | PK | No | Sequence value that uniquely orders response rows for the learner application. |
| `application_decision_sequence_number` | `INTEGER` |  | Yes | Optional sequence number of the related learner application decision row. |
| `application_response_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Identifier for the governed type of applicant response to a decision, offer, or yield action. |
| `application_response_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Identifier for the governed status of the applicant response record. |
| `response_date` | `DATE` |  | No | Date the applicant response was submitted, recorded, or became effective. |
| `response_due_date` | `DATE` |  | Yes | Date by which the applicant response was due, when applicable. |
| `entry_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifier for the entry term to which the applicant response applies, when term-specific. |
| `academic_program_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Identifier for the academic program to which the applicant response applies, when program-specific. |
| `source_raw_application_response_type` | `TEXT` |  | Yes | Raw source-system applicant response type value where canonical mapping may be lossy. |
| `source_raw_application_response_status` | `TEXT` |  | Yes | Raw source-system applicant response status value where canonical mapping may be lossy. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the response row was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the response row. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationReview

**SQL identifier:** `admissions.learner_application_review`

A table that stores admissions review and evaluation workflow facts associated with a learner application, including review stage, review status, reviewer context, score or rating, review dates, source raw workflow values, and source lineage. This table is separate from LearnerApplicationDecision, which records the formal institutional admissions outcome.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Identifier for the learner application being reviewed. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for multiple review rows associated with the application. |
| `review_stage_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the stage of the admissions review process. |
| `review_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the status of the admissions review process. |
| `assigned_reviewer_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Tenant-scoped person/staff identifier for the reviewer or user assigned to review the application, where resolvable. |
| `last_reviewer_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Tenant-scoped person/staff identifier for the most recent reviewer, where resolvable. |
| `review_assigned_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the review or application decision workflow item was assigned. |
| `review_started_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time review activity began. |
| `review_completed_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the review activity was completed. |
| `review_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the review workflow state was last updated in the source or operational process. |
| `evaluation_score` | `NUMERIC` |  | Yes | Lightweight review or evaluation score associated with the application review. |
| `evaluation_score_maximum` | `NUMERIC` |  | Yes | Maximum possible score for the lightweight evaluation score, where available. |
| `review_comment_text` | `TEXT` |  | Yes | Limited review comment or summary text; not a full rubric or comment-history model. |
| `source_raw_review_stage` | `TEXT` |  | Yes | Source-system review stage value preserved when canonical mapping is lossy. |
| `source_raw_review_status` | `TEXT` |  | Yes | Source-system review status value preserved when canonical mapping is lossy. |
| `source_raw_assigned_reviewer` | `TEXT` |  | Yes | Source-system assigned reviewer/user value preserved when the person cannot be resolved. |
| `source_raw_last_reviewer` | `TEXT` |  | Yes | Source-system last reviewer/user value preserved when the person cannot be resolved. |
| `source_raw_evaluation_score` | `TEXT` |  | Yes | Source-system evaluation score value preserved as supplied. |
| `source_raw_decision_stage_identifier` | `INTEGER` |  | Yes | Source-system decision-stage identifier preserved as workflow lineage, not as a formal decision type. |
| `source_raw_decision_status_identifier` | `INTEGER` |  | Yes | Source-system decision-status identifier preserved as workflow lineage, not as a formal decision type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system from which the review row originated or can be reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the review row. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationStatusHistory

**SQL identifier:** `admissions.learner_application_status_history`

A table tracking status changes over the life of a learner application.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this status history row within the learner application |
| `application_status_identifier` | `TEXT` | FK → `ApplicationStatusLookup.ApplicationStatusIdentifier` | No | Unique identifier for the application workflow status |
| `application_status_date` | `DATE` |  | No | Date the application status became effective or was recorded |
| `application_status_reason_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application status reason |
| `application_status_reason_text` | `TEXT` |  | Yes | Free-text explanation of the application status reason |
| `current_status_indicator` | `BOOLEAN` |  | No | Indicates whether this row represents the current application status |
| `source_raw_application_status` | `TEXT` |  | Yes | Raw application status value from the source system |
| `source_raw_application_status_reason` | `TEXT` |  | Yes | Raw application status reason value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerApplicationWithdrawal

**SQL identifier:** `admissions.learner_application_withdrawal`

A table recording withdrawal-specific details for learner applications when withdrawal has its own business process, source-system payload, reason detail, reversal, or reporting requirements.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_application_identifier` | `TEXT` | PK, FK → `LearnerApplication.LearnerApplicationIdentifier` | No | Tenant-scoped unique identifier for the learner application. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for this withdrawal row within the learner application |
| `withdrawal_date` | `DATE` |  | No | Date the withdrawal was recorded or requested |
| `withdrawal_effective_date` | `DATE` |  | Yes | Date the withdrawal became effective |
| `application_withdrawal_reason_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Unique identifier for the application withdrawal reason |
| `withdrawal_reason_text` | `TEXT` |  | Yes | Free-text explanation of the withdrawal reason |
| `reinstated_indicator` | `BOOLEAN` |  | No | Indicates whether the withdrawn application was reinstated |
| `reinstated_date` | `DATE` |  | Yes | Date the withdrawn application was reinstated |
| `source_raw_withdraw_reason` | `TEXT` |  | Yes | Raw withdrawal reason value from the source system |
| `source_raw_withdrawal_status` | `TEXT` |  | Yes | Raw withdrawal status value from the source system |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
