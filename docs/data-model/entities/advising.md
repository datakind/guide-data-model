# Entity: Advising

This page documents every table that belongs to the **Advising** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 17**

## Table of contents

- [CaseNotesPredefinedEntry](#casenotespredefinedentry)
- [LearnerCaseDocument](#learnercasedocument)
- [LearnerCaseNote](#learnercasenote)
- [LearnerCaseNotesSummary](#learnercasenotessummary)
- [LearnerEarlyAlert](#learnerearlyalert)
- [LearnerEarlyAlertActivity](#learnerearlyalertactivity)
- [PersonCaseloadCommunication](#personcaseloadcommunication)
- [PersonCommunicationCampaign](#personcommunicationcampaign)
- [PersonIntakeParticipation](#personintakeparticipation)
- [PersonIntakeSummary](#personintakesummary)
- [PersonResourceExpectation](#personresourceexpectation)
- [PersonResourceValue](#personresourcevalue)
- [PersonSpecialty](#personspecialty)
- [PersonSupportAssignment](#personsupportassignment)
- [PersonSupportReferral](#personsupportreferral)
- [SpecialtyLookup](#specialtylookup)
- [SupportAssignmentRoleLookup](#supportassignmentrolelookup)

---

## CaseNotesPredefinedEntry

**SQL identifier:** `advising.case_notes_predefined_entry`

A table containing defined notes entries and details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `case_notes_predefined_entry_identifier` | `TEXT` | PK | No | Unique identifier for the case notes predefined entry |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `category` | `TEXT` |  | Yes | Category assigned to the notes entry |
| `entry` | `TEXT` |  | No | Entry text for the case note |
| `related_task` | `TEXT` |  | Yes | Text for a task created when the notes entry is added to case notes |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCaseDocument

**SQL identifier:** `advising.learner_case_document`

A table containing a history of documents saved to organizational support systems by the care team in support of the learner's education pursuit. A description of the document and link to the artifacts are included.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `case_document_identifier` | `TEXT` | PK | No | Unique identifier for the case document |
| `person_document_author_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person identifier of the person who authored document |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | Name of the file stored for the person |
| `description` | `TEXT` |  | Yes | Description of the file stored for a person |
| `status` | `TEXT` |  | No | Indicates whether the document is active, inactive, archived, etc. |
| `type` | `TEXT` |  | No | Specifies a short description of the data in the document |
| `size` | `NUMERIC` |  | Yes | Size of the file stored in kilobytes for the person |
| `url` | `TEXT` |  | Yes | URL path for the file stored for the person |
| `file_name` | `TEXT` |  | No | Name of the file stored for the person |
| `privacy_indicator` | `BOOLEAN` |  | No | Indicator that a document should only be visible to the author and learner |
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

## LearnerCaseNote

**SQL identifier:** `advising.learner_case_note`

A table containing notes about care team members' interactions with learners.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `case_note_identifier` | `TEXT` | PK | No | Unique identifier of a note item |
| `person_case_note_author_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Unique identifier for the person authoring the notes |
| `case_notes_predefined_entry_identifier` | `TEXT` | FK → `CaseNotesPredefinedEntry.CaseNotesPredefinedEntryIdentifier` | Yes | Unique identifier for the case notes predefined entry |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | Status of the note (active, inactive) |
| `case_note_type` | `TEXT` |  | No | Type of the note |
| `source` | `TEXT` |  | No | Source activity in which the note was authored (caseload, degree plan, service) |
| `case_note_name` | `TEXT` |  | No | Name of the note |
| `case_note_details` | `TEXT` |  | No | Details of a note added to an item |
| `case_note_privacy_indicator` | `BOOLEAN` |  | No | Privacy indicator for the note to only be visible by the author and learner |
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

## LearnerCaseNotesSummary

**SQL identifier:** `advising.learner_case_notes_summary`

A table containing summary reports produced by analysis of case notes data.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `case_notes_summary_identifier` | `TEXT` | PK | No | Unique identifier of the case notes summary |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `case_notes_content_start_date` | `DATE` |  | No | Start date to include case notes content in the summary analysis |
| `case_notes_content_end_date` | `DATE` |  | No | End date to include case notes content in the summary analysis |
| `case_notes_summary_name` | `TEXT` |  | Yes | Name of the case notes summary |
| `summary_report` | `TEXT` |  | No | Summary report text for the case notes period |
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

## LearnerEarlyAlert

**SQL identifier:** `advising.learner_early_alert`

A table containing a history of early alerts created by faculty, staff, and care team members to recognize student successes and challenges related to learners progress towards activity, course, and program of study completion.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_early_alert_identifier` | `TEXT` | PK | No | Unique identifier of the early alert |
| `alert_reporter_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Identifier of the person reporting the alert |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `alert_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the early alert was raised or became known as a student-success signal. This is the business-event time and is distinct from source-system or canonical record creation timestamps. |
| `alert_type` | `TEXT` |  | No | Type of alert that was created for the learner |
| `alert_reason` | `TEXT` |  | No | Reason that the alert was created |
| `alert_origin_activity` | `TEXT` |  | Yes | Activity from which the alert originated |
| `alert_source` | `TEXT` |  | Yes | Source person or system the created the alert |
| `alert_recommendations` | `TEXT` |  | Yes | Recommendations for the alert intervention |
| `alert_status` | `TEXT` |  | Yes | Status of the alert (open, closed, etc) |
| `alert_resolution_description` | `TEXT` |  | Yes | A description of the resolution for the alert |
| `alert_notes` | `TEXT` |  | Yes | Care team notes related to the alert |
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

## LearnerEarlyAlertActivity

**SQL identifier:** `advising.learner_early_alert_activity`

A table containing the history of activity that care team members recorded in response to an early alert created for a learner.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_early_alert_activity_identifier` | `TEXT` | PK | No | Unique identifier of the early alert activity |
| `learner_early_alert_identifier` | `TEXT` | FK → `LearnerEarlyAlert.LearnerEarlyAlertIdentifier` | No | Unique identifier of the early alert |
| `contributor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Unique identifier of the person contributing information |
| `activity_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the early-alert response or follow-up activity occurred. This is the business-event time and is distinct from the canonical CreatedDate audit timestamp. |
| `description` | `TEXT` |  | Yes | A description for the record |
| `message_to_student` | `TEXT` |  | Yes | Contributor's message to a student related to the activity |
| `message_to_care_team` | `TEXT` |  | Yes | Contributor's message to the care team related to the activity |
| `contributor_comment` | `TEXT` |  | Yes | A comment added to the early alert by an author, student, faculty, or care team member |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonCaseloadCommunication

**SQL identifier:** `advising.person_caseload_communication`

A table containing a history of communication from the care team to the learner. Communications could include individual and private communications as well as broad campaigns via email, SMS, and other communication mediums.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_caseload_communication_identifier` | `TEXT` | PK | No | Unique identifier for the caseload communication |
| `sender_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Unique identifier of the person sending the communication |
| `person_communication_campaign_identifier` | `TEXT` | FK → `PersonCommunicationCampaign.PersonCommunicationCampaignIdentifier` | Yes | Unique identifier for the communication campaign |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_activity_type` | `TEXT` |  | No | Type of activity that triggered a notification to the care team (Early Alert, Caseload Assignment, etc) |
| `recipient_contact_type` | `TEXT` |  | No | Type of communication sent (SMS, email, etc) |
| `recipient_contact` | `TEXT` |  | No | Communication destination address (email, phone number) |
| `message` | `TEXT` |  | No | Details of the notification included in the communication |
| `sent_date` | `DATE` |  | Yes | Date the item was successfully sent |
| `topic_tag` | `TEXT` |  | Yes | Comma delimited list to tag topics discussed (e.g. applications, FAFSA, parent communication, transcripts, scholarships, due dates) |
| `metadata` | `TEXT` |  | Yes | Any additional information about the communication such as the location of an in-person meeting |
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

## PersonCommunicationCampaign

**SQL identifier:** `advising.person_communication_campaign`

A table containing details about communication plans and campaigns for learners and institution-defined cohorts, including the messages, methods, cadence, and outcomes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `person_communication_campaign_identifier` | `TEXT` | PK | No | Unique identifier for the communication campaign |
| `recipient_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique identifier of the recipient of the campaign communication |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier of the care team member who authored the campaign |
| `cohort_identifier` | `TEXT` | FK → `Cohort.CohortIdentifier` | Yes | Unique identifier of the cohort group |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `goal` | `TEXT` |  | Yes | A description of the campaign's goal |
| `start_date` | `DATE` |  | Yes | The start date of the campaign |
| `end_date` | `DATE` |  | Yes | The end date of the campaign |
| `status` | `TEXT` |  | No | Status of a communication campaign item (active, inactive) |
| `type` | `TEXT` |  | Yes | Type of the communication campaign |
| `message_content` | `TEXT` |  | Yes | Text to include with the message |
| `frequency` | `TEXT` |  | Yes | Frequency of communication to associated recipients |
| `objectives` | `TEXT` |  | Yes | Description of objectives the communication campaign should satisfy |
| `preferred_contact_type` | `TEXT` |  | Yes | Recipient preferred contact type for messages included in the communication campaign |
| `messages_sent_count` | `INTEGER` |  | Yes | The number of recipients of the message to the target cohort of the campaign |
| `messages_read_count` | `INTEGER` |  | Yes | The number of messages opened by the target cohort of the campaign |
| `success_rate` | `NUMERIC` |  | Yes | The percentage of people targeted in the campaign who achieved the goal of the campaign |
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

## PersonIntakeParticipation

**SQL identifier:** `advising.person_intake_participation`

A table containing the status of a person's participation in providing and updating intake data.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_intake_participation_identifier` | `TEXT` | PK | No | Unique identifier for the person intake participation record |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | The current status of the person participating in intake reminders and updates |
| `status_date` | `DATE` |  | Yes | The date the status has most recently changed |
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

## PersonIntakeSummary

**SQL identifier:** `advising.person_intake_summary`

A table containing summary reports produced by analysis of intake data for select content.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_intake_summary_identifier` | `TEXT` | PK | No | Unique identifier of the person intake summary |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `intake_content_start_date` | `DATE` |  | No | Start date to include intake content in the summary analysis |
| `intake_content_end_date` | `DATE` |  | No | End date to include intake content in the summary analysis |
| `summary_report` | `TEXT` |  | No | Summary report text for the intake period |
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

## PersonResourceExpectation

**SQL identifier:** `advising.person_resource_expectation`

A table containing a history of the responses a learner provided for the service or resource expectations intake questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_resource_expectation_identifier` | `TEXT` | PK | No | Unique identifier for a learner resource expectation item |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | Yes | Unique identifier for the support resource, service, or program |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `input` | `TEXT` |  | Yes | Free-form input to describe the learner resource expectation |
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

## PersonResourceValue

**SQL identifier:** `advising.person_resource_value`

A table containing a history of the responses a learner provided for the service or resource value intake questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_resource_value_identifier` | `TEXT` | PK | No | Unique identifier for a learner's association of values to a resource |
| `value_identifier` | `TEXT` | FK → `ValueLookup.ValueIdentifier` | Yes | Unique identifier for the value item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `input` | `TEXT` |  | Yes | Free-form input to describe the learner resource value |
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

## PersonSpecialty

**SQL identifier:** `advising.person_specialty`

A table containing details of the responses a person provided for the specialty intake questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_specialty_identifier` | `TEXT` | PK | No | Unique identifier for a person specialty item |
| `specialty_identifier` | `TEXT` | FK → `SpecialtyLookup.SpecialtyIdentifier` | Yes | Unique identifier for a specialty item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `input` | `TEXT` |  | Yes | Free-form input to describe the person specialty |
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

## PersonSupportAssignment

**SQL identifier:** `advising.person_support_assignment`

Records an institutionally assigned person-to-person support relationship, identifying the person receiving support, the person providing support, the governed role being performed, whether the assignment is primary within the applicable support role or context, and the effective period. The assignment is not defined by a particular caseload, advising program, academic program, or source-system implementation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `support_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Identifier of the person providing support under this institutional assignment. |
| `person_support_assignment_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the person support assignment. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `primary_assignment_indicator` | `BOOLEAN` |  | No | Indicates that this assignment is primary for the supported person within the applicable support role or context. It does not mean the support provider has one globally primary assignment. |
| `support_assignment_role_identifier` | `TEXT` | FK → `SupportAssignmentRoleLookup.SupportAssignmentRoleIdentifier` | No | Identifier of the governed institutional support role performed in this assignment. |
| `effective_start_date` | `DATE` |  | No | Date on which the person support assignment begins to apply. |
| `effective_end_date` | `DATE` |  | Yes | Optional date after which the person support assignment no longer applies. |
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

## PersonSupportReferral

**SQL identifier:** `advising.person_support_referral`

A tenant-scoped referral of a person to one or more support destinations such as a resource, service provider, person, or organization. The referral may originate from an early-alert response, an identified person challenge, or another support workflow. At least one destination reference must be populated. Referral lifecycle and outcome fields support closed-loop student-support interoperability without making the referral dependent on any one vendor workflow.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_support_referral_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for one support referral. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person receiving or intended to receive support through the referral. |
| `referring_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person who initiated the referral, when the referral was initiated by a person rather than an automated process. |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | Yes | Support resource, service, or program to which the person was referred, when applicable. |
| `referred_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Specific person to whom the person was referred, when applicable. |
| `referred_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization to which the person was referred, when applicable. |
| `learner_early_alert_activity_identifier` | `TEXT` | FK → `LearnerEarlyAlertActivity.LearnerEarlyAlertActivityIdentifier` | Yes | Optional early-alert response activity that gave rise to the referral. |
| `person_challenge_identifier` | `TEXT` | FK → `PersonChallenge.PersonChallengeIdentifier` | Yes | Optional person challenge that gave rise to the referral. |
| `referral_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the referral was initiated. |
| `referral_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed reference-code value describing the referral lifecycle status. |
| `referral_reason` | `TEXT` |  | Yes | Reason or support need motivating the referral. |
| `outcome_description` | `TEXT` |  | Yes | Narrative outcome or resolution of the referral, when known. |
| `closed_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the referral was closed or otherwise completed. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system. |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system. |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted in the source system. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## SpecialtyLookup

**SQL identifier:** `advising.specialty_lookup`

A lookup table containing descriptions of specialties of academic advisors or members of the care team.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `specialty_identifier` | `TEXT` | PK | No | Unique identifier for a specialty item |
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

## SupportAssignmentRoleLookup

**SQL identifier:** `advising.support_assignment_role_lookup`

Tenant-governed vocabulary of institutional support roles used when one person is assigned to support another person, such as academic advisor, success coach, career advisor, or peer advisor. Roles describe the function performed in the relationship and remain distinct from staff specialties.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `support_assignment_role_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the governed support role. |
| `code` | `TEXT` |  | No | Institution-defined code for the support role. |
| `title` | `TEXT` |  | No | Human-readable name of the support role. |
| `description` | `TEXT` |  | Yes | Description of the function performed by a support person in this role. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the canonical role definition was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier of the support-role definition in the source system. |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the canonical role row. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical role row was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical role row. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical role row was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that soft-deleted the canonical role row. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical role row was soft-deleted, if applicable. |
