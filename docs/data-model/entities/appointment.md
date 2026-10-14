# Entity: Appointment

This page documents every table that belongs to the **Appointment** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 8**

## Table of contents

- [AppointmentAgenda](#appointmentagenda)
- [AppointmentAgendaTopic](#appointmentagendatopic)
- [AppointmentAgendaTopicAppointmentAgendaAssociation](#appointmentagendatopicappointmentagendaassociation)
- [AppointmentSchedule](#appointmentschedule)
- [AppointmentScheduleAppointmentTemplateAssociation](#appointmentscheduleappointmenttemplateassociation)
- [AppointmentTemplate](#appointmenttemplate)
- [PersonAppointment](#personappointment)
- [PersonAppointmentAvailability](#personappointmentavailability)

---

## AppointmentAgenda

**SQL identifier:** `appointment.appointment_agenda`

A table containing an agenda definition for an appointment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_agenda_identifier` | `TEXT` | PK | No | Unique identifier for the agenda associated with the appointment |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | A description for the record |
| `category` | `TEXT` |  | Yes | Category assigned to the appointment agenda |
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

## AppointmentAgendaTopic

**SQL identifier:** `appointment.appointment_agenda_topic`

A table containing a list of discussion topics that are available to be associated with appointment agendas.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_agenda_topic_identifier` | `TEXT` | PK | No | Unique identifier for the agenda topic |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `defined_note` | `TEXT` |  | Yes | Optional defined note to be added to case notes based on the agenda topic |
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

## AppointmentAgendaTopicAppointmentAgendaAssociation

**SQL identifier:** `appointment.appointment_agenda_topic_appointment_agenda_association`

A table associating agenda topics with appointment agendas.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_agenda_topic_appointment_agenda_associatio_986e4a7d` | `TEXT` | PK | No | Unique identifier for the appointment agenda to topic association |
| `appointment_agenda_identifier` | `TEXT` | FK → `AppointmentAgenda.AppointmentAgendaIdentifier` | No | Unique identifier for the agenda associated with the appointment |
| `appointment_agenda_topic_identifier` | `TEXT` | FK → `AppointmentAgendaTopic.AppointmentAgendaTopicIdentifier` | No | Unique identifier for the agenda topic |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AppointmentSchedule

**SQL identifier:** `appointment.appointment_schedule`

A table containing meeting scheduling parameters to be scheduled as appointments.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_schedule_identifier` | `TEXT` | PK | No | Unique identifier for the appointment schedule |
| `appointment_agenda_identifier` | `TEXT` | FK → `AppointmentAgenda.AppointmentAgendaIdentifier` | Yes | Unique identifier for the agenda associated with the appointment |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `appointment_meeting_duration` | `INTEGER` |  | No | Recommended duration for the meeting activity in minutes |
| `appointment_meeting_term_applicable` | `TEXT` |  | Yes | Term for which the meeting activity is recommended |
| `appointment_meeting_numberof_days_to_complete` | `INTEGER` |  | No | The maximum number of days into the term before which the meeting should be completed |
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

## AppointmentScheduleAppointmentTemplateAssociation

**SQL identifier:** `appointment.appointment_schedule_appointment_template_association`

A table associating appointment templates with schedules.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_schedule_appointment_template_association__418349cc` | `TEXT` | PK | No | Unique identifier for the appointment schedule to appointment schedule template association |
| `appointment_template_identifier` | `TEXT` | FK → `AppointmentTemplate.AppointmentTemplateIdentifier` | No | Unique identifier for the appointment schedule template |
| `appointment_schedule_identifier` | `TEXT` | FK → `AppointmentSchedule.AppointmentScheduleIdentifier` | No | Unique identifier for the appointment schedule |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AppointmentTemplate

**SQL identifier:** `appointment.appointment_template`

A table containing meeting templates that can be used to schedule all appointments with persons for a term.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `appointment_template_identifier` | `TEXT` | PK | No | Unique identifier for the schedule template associated with the appointment |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `category` | `TEXT` |  | Yes | Category assigned to the appointment schedule |
| `sub_category` | `TEXT` |  | Yes | Subcategory assigned to the appointment schedule |
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

## PersonAppointment

**SQL identifier:** `appointment.person_appointment`

A table containing a history of learner appointments with care team members and organization staff. The appointment entries describe future and past appointments.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_appointment_identifier` | `TEXT` | PK | No | Unique identifier for the person's appointment |
| `appointment_agenda_identifier` | `TEXT` | FK → `AppointmentAgenda.AppointmentAgendaIdentifier` | Yes | Unique identifier for the agenda associated with the appointment |
| `appointment_template_identifier` | `TEXT` | FK → `AppointmentTemplate.AppointmentTemplateIdentifier` | Yes | Unique identifier for the schedule template associated with the appointment |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `start_date` | `DATE` |  | No | Appointment scheduled start date |
| `start_time` | `TIMESTAMP WITH TIME ZONE` |  | No | RFC 3339 Start time for this appointment |
| `duration` | `INTEGER` |  | No | Duration of the scheduled appointment in minutes |
| `location` | `TEXT` |  | No | Location of the appointment |
| `status` | `TEXT` |  | No | Appointment status, such as Canceled, Declined, Completed |
| `repeat_flag_indicator` | `BOOLEAN` |  | Yes | Indicator that the meeting repeats on a regular schedule |
| `cadence` | `TEXT` |  | Yes | Cadence of a repeating appointment |
| `repeat_end_date` | `DATE` |  | Yes | Last day of a repeating appointment |
| `repeat_count` | `INTEGER` |  | Yes | Alternative to End Date, number of appointments for this record |
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

## PersonAppointmentAvailability

**SQL identifier:** `appointment.person_appointment_availability`

A table containing details about the availability of a person for appointments.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_appointment_availability_identifier` | `TEXT` | PK | No | Unique identifier of the person's appointment availability |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `person_available_date` | `DATE` |  | No | The available date for scheduling |
| `person_available_start_time` | `TIMESTAMP WITH TIME ZONE` |  | No | The available start time for the available date |
| `person_available_end_time` | `TIMESTAMP WITH TIME ZONE` |  | No | The end time for the available date and start time |
| `person_available_duration` | `INTEGER` |  | No | The person's preferred appointment duration in minutes |
| `person_available_status` | `TEXT` |  | Yes | Availability status for the designated date and time |
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
