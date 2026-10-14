# Entity: Core

This page documents every table that belongs to the **Core** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 36**

## Table of contents

- [AdministrativePeriodLookup](#administrativeperiodlookup)
- [Cohort](#cohort)
- [MessageTemplate](#messagetemplate)
- [ObjectLookup](#objectlookup)
- [Organization](#organization)
- [OrganizationAccreditation](#organizationaccreditation)
- [OrganizationAddress](#organizationaddress)
- [OrganizationClassification](#organizationclassification)
- [OrganizationClassificationSystem](#organizationclassificationsystem)
- [OrganizationEmail](#organizationemail)
- [OrganizationIdentification](#organizationidentification)
- [OrganizationIdentificationSystem](#organizationidentificationsystem)
- [OrganizationPhone](#organizationphone)
- [OrganizationRelationship](#organizationrelationship)
- [OrganizationSocialMediaAccount](#organizationsocialmediaaccount)
- [OrganizationUnit](#organizationunit)
- [OrganizationUnitTypeLookup](#organizationunittypelookup)
- [PersonAddress](#personaddress)
- [PersonEmail](#personemail)
- [PersonIdentification](#personidentification)
- [PersonIdentificationSystem](#personidentificationsystem)
- [PersonLookup](#personlookup)
- [PersonName](#personname)
- [PersonPhone](#personphone)
- [PersonPreferredContact](#personpreferredcontact)
- [PersonRole](#personrole)
- [PersonSocialMediaAccount](#personsocialmediaaccount)
- [PersonTagLookup](#persontaglookup)
- [ReferenceCodeSet](#referencecodeset)
- [ReferenceCodeValue](#referencecodevalue)
- [RoleLookup](#rolelookup)
- [SharingPermission](#sharingpermission)
- [SourceSystemLookup](#sourcesystemlookup)
- [Template](#template)
- [Tenant](#tenant)
- [TenantOrganizationRole](#tenantorganizationrole)

---

## AdministrativePeriodLookup

**SQL identifier:** `core.administrative_period_lookup`

Tenant-scoped governed definition of an institutionally defined administrative time period used for reporting, classification, cohort, residency, student-type, or other administrative purposes. Distinct from academic terms and other domain-specific periods.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `administrative_period_identifier` | `TEXT` | PK | No | Unique GUIDE-owned identifier for the administrative period. |
| `administrative_period_code` | `TEXT` |  | No | Institutionally governed compact code identifying the administrative period. |
| `administrative_period_name` | `TEXT` |  | No | Human-readable name of the administrative period. |
| `administrative_period_description` | `TEXT` |  | Yes | Optional fuller description of the administrative period. |
| `administrative_period_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the broad type or category of administrative period. |
| `start_date` | `DATE` |  | Yes | Date on which the administrative period begins. |
| `end_date` | `DATE` |  | Yes | Date on which the administrative period ends. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the administrative period was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the administrative period. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## Cohort

**SQL identifier:** `core.cohort`

A tenant-scoped governed definition of an institution-defined cohort used for reporting, tracking, program participation, or other bounded population purposes, including optional assignment windows.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `cohort_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for an institution-defined cohort. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `cohort_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed classification of the cohort. |
| `initial_academic_period_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | First academic period in which students may be assigned to the cohort. |
| `final_academic_period_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Last academic period in which students may be assigned to the cohort. |
| `name` | `TEXT` |  | No | Institution-assigned name of the learner cohort. |
| `description` | `TEXT` |  | Yes | Description of the cohort's defining population, purpose, or membership criteria. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the cohort. |
| `assignment_start_date` | `DATE` |  | Yes | First calendar date on which students may be assigned to the cohort. |
| `assignment_end_date` | `DATE` |  | Yes | Last calendar date on which students may be assigned to the cohort. |
| `status` | `TEXT` |  | No | Operational status of the cohort (for example Active or Inactive). |
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

## MessageTemplate

**SQL identifier:** `core.message_template`

A table containing message templates that can be used to create messages by merging data (e.g. name and address into a mailing template).

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `message_template_identifier` | `TEXT` | PK | No | Unique identifier of the message template |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the message template |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `message_template_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `category` | `TEXT` |  | Yes | Message category of the resource type |
| `message_text` | `TEXT` |  | No | Template text used to create a message |
| `object_type` | `TEXT` |  | Yes | The type of resource to which this template pertains |
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

## ObjectLookup

**SQL identifier:** `core.object_lookup`

A lookup table containing a list of all objects in the data model definition.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `object_identifier` | `TEXT` | PK | No | Unique identifier for the object or database table |
| `name` | `TEXT` |  | Yes | The name of the object or database table |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## Organization

**SQL identifier:** `core.organization`

Tenant-scoped master record for a real-world organization represented within the tenant context. Holds stable organization identity and broadly reusable descriptive attributes; roles, classifications, accreditations, contacts, relationships, and time-specific measures are modeled separately.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | Official or commonly recognized name of the organization or educational institution. |
| `short_name` | `TEXT` |  | Yes | A short name for the record |
| `organization_code` | `TEXT` |  | Yes | Institutionally or externally assigned compact code identifying the organization within an applicable context. |
| `publish_indicator` | `BOOLEAN` |  | No | An indication that the record should be published to a visible directory, application, or website, etc. |
| `operational_status` | `TEXT` |  | Yes | The current status of the organization's operations, exclusive of scheduled breaks, holidays, or other temporary interruptions |
| `operational_status_start_date` | `DATE` |  | Yes | Effective date for the operational status of the organization |
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
| `organization_identifier` | `TEXT` | PK | No | Tenant-scoped unique identifier for the real-world organization represented by this record. |
| `organization_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Broad governed structural type of organization, when useful; roles such as employer or accreditor belong in relationships/domain facts rather than here. |
| `description` | `TEXT` |  | Yes | Narrative description or summary of the organization. |
| `website_url` | `TEXT` |  | Yes | Primary public website for the organization. |
| `image_url` | `TEXT` |  | Yes | URL for a representative image or logo of the organization when supplied. |

## OrganizationAccreditation

**SQL identifier:** `core.organization_accreditation`

Tenant-scoped record of accreditation granted to, sought by, or otherwise held by an organization, identifying the accrediting organization and accreditation-specific status and dates.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_accreditation_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for one organization accreditation record. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization whose accreditation is represented. |
| `accrediting_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Accrediting agency or other organization granting or evaluating the accreditation. |
| `accreditation_status` | `TEXT` |  | No | Status of the accreditation as represented by the accrediting authority or authoritative source. |
| `accreditation_award_date` | `DATE` |  | Yes | Date on which the accreditation was awarded or became effective. |
| `accreditation_expiration_date` | `DATE` |  | Yes | Date on which the accreditation expires when applicable. |
| `seeking_accreditation_date` | `DATE` |  | Yes | Date on which the organization began seeking the accreditation when known. |
| `accredited_jurisdiction` | `TEXT` |  | Yes | Region or political jurisdiction to which the accreditation applies when supplied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the accreditation record. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of the accreditation record in the source system. |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source accreditation record was created. |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source accreditation record was last modified. |

## OrganizationAddress

**SQL identifier:** `core.organization_address`

A table containing a history of physical addresses for organizations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_address_identifier` | `TEXT` | PK | No | Unique identifier for an organization address item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `address_type` | `TEXT` |  | No | The type of address listed for an organization |
| `address_line1` | `TEXT` |  | No | The street number and street name or post office box number of an address |
| `address_line2` | `TEXT` |  | Yes | The second line of the address, which may include the apartment, room, or suite number |
| `address_apartment_room_or_suite_number` | `TEXT` |  | Yes | The apartment, room, or suite number of an address |
| `address_city` | `TEXT` |  | No | The name of the city in which an address is located |
| `state_abbreviation` | `TEXT` |  | Yes | State, province, region, or analogous first-level administrative area when applicable. |
| `address_postal_code` | `TEXT` |  | Yes | Postal or ZIP code when applicable in the address country. |
| `address_county_name` | `TEXT` |  | Yes | The name of the county, parish, borough, or comparable unit (within a state) in which an address is located |
| `address_country` | `TEXT` |  | Yes | The name of the country in which the address is located |
| `building_site_number` | `TEXT` |  | Yes | The number of the building on the site, if more than one building shares the same address |
| `latitude` | `TEXT` |  | Yes | The north or south angular distance from the equator that, when combined with longitude, reflects an estimation of where the address is physically situated |
| `longitude` | `TEXT` |  | Yes | The east or west angular distance from the prime meridian that, when combined with latitude, reflects an estimation of where the address is physically situated |
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
| `effective_start_date` | `DATE` |  | Yes | Date on which this organization address becomes valid. |
| `effective_end_date` | `DATE` |  | Yes | Date after which this organization address is no longer valid. |
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates that this is the preferred organization address among addresses of the same applicable type. |
| `address_type_identifier` | `TEXT` | FK → `AddressTypeLookup.AddressTypeIdentifier` | Yes | Governed organization address type. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## OrganizationClassification

**SQL identifier:** `core.organization_classification`

Assignment of an organization to a value within a specified organization classification system, with optional effective dating.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_classification_identifier` | `TEXT` | PK | No | Unique identifier for an organization classification assignment. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization being classified. |
| `organization_classification_system_identifier` | `TEXT` | FK → `OrganizationClassificationSystem.OrganizationClassificationSystemIdentifier` | No | Classification system under which the value has meaning. |
| `classification_value` | `TEXT` |  | No | Code or value assigned to the organization in the classification system. |
| `classification_label` | `TEXT` |  | Yes | Human-readable label for the classification value, when supplied. |
| `effective_start_date` | `DATE` |  | Yes | Date on which this classification assignment becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date after which this classification assignment is no longer effective. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system for the classification assignment. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this classification assignment in the source system. |

## OrganizationClassificationSystem

**SQL identifier:** `core.organization_classification_system`

Defines a classification scheme used to categorize organizations, including externally governed schemes and institution-specific taxonomies.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_classification_system_identifier` | `TEXT` | PK | No | Unique identifier for an organization classification system. |
| `classification_system_code` | `TEXT` |  | No | Short code for the classification system. |
| `classification_system_name` | `TEXT` |  | No | Human-readable name of the classification system. |
| `authoritative_resource` | `TEXT` |  | Yes | Organization or resource governing the classification system. |
| `version` | `TEXT` |  | Yes | Version or edition of the classification system, when applicable. |

## OrganizationEmail

**SQL identifier:** `core.organization_email`

A repeatable email contact method for an organization, preserving contact type, preference, and source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_email_identifier` | `TEXT` | PK | No | Unique identifier for an organization email record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `email_address` | `TEXT` |  | No | Email address for the organization. |
| `email_address_type` | `TEXT` |  | Yes | Standardized email contact type supplied by the source. |
| `email_type_identifier` | `TEXT` | FK → `EmailTypeLookup.EmailTypeIdentifier` | Yes | Governed institution-specific email type. |
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred organization email among emails of the same applicable type. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## OrganizationIdentification

**SQL identifier:** `core.organization_identification`

A tenant-scoped identifier assigned to an organization under a defined identification system or namespace, with optional effective dates and source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_identification_identifier` | `TEXT` | PK | No | Unique identifier for this organization identification record. |
| `organization_identification_system_identifier` | `TEXT` | FK → `OrganizationIdentificationSystem.OrganizationIdentificationSystemIdentifier` | No | Identification namespace or system under which IdentifierValue has meaning. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `identifier_value` | `TEXT` |  | No | Identifier assigned to the organization within the specified identification system or namespace. |
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
| `effective_start_date` | `DATE` |  | Yes | Date on which this organization identification becomes valid. |
| `effective_end_date` | `DATE` |  | Yes | Date after which this organization identification is no longer valid. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization to which this identification value is assigned. |

## OrganizationIdentificationSystem

**SQL identifier:** `core.organization_identification_system`

Defines an identifier namespace or identification system used to assign meaningful identifiers to organizations, such as CEEB, IPEDS UNITID, OPEID, PESC GEO, state codes, or local/system namespaces.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_identification_system_identifier` | `TEXT` | PK | No | Unique identifier for this organization identification system or namespace. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `acronym` | `TEXT` |  | Yes | The short name or code for the organization identification system |
| `authoritative_resource` | `TEXT` |  | Yes | A resource of authoritative data for identifiers (e.g. State of Arizona) |
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

## OrganizationPhone

**SQL identifier:** `core.organization_phone`

A repeatable telephone contact method for an organization, preserving number components, contact type, preference, and source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_phone_identifier` | `TEXT` | PK | No | Unique identifier for an organization phone record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `telephone_number` | `TEXT` |  | No | Telephone number assigned to the organization. |
| `country_calling_code` | `TEXT` |  | Yes | International country calling code. |
| `extension` | `TEXT` |  | Yes | Telephone extension. |
| `telephone_number_type` | `TEXT` |  | Yes | Standardized phone contact type supplied by the source. |
| `phone_type_identifier` | `TEXT` | FK → `PhoneTypeLookup.PhoneTypeIdentifier` | Yes | Governed institution-specific phone type. |
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred organization phone among phones of the same applicable type. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## OrganizationRelationship

**SQL identifier:** `core.organization_relationship`

Effective-dated typed relationship between two tenant-scoped organizations. Supports parent/part-of, consortium membership, partnership, feeder, subsidiary, and other graph relationships without assuming a single hierarchy.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_relationship_identifier` | `TEXT` | PK | No | Unique identifier for an organization-to-organization relationship. |
| `subject_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization that is the subject/source of the relationship. |
| `related_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization that is the related/object organization. |
| `organization_relationship_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed type of relationship between the two organizations. |
| `effective_start_date` | `DATE` |  | Yes | Date on which the relationship becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date after which the relationship is no longer effective. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system for the relationship record. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this relationship in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |

## OrganizationSocialMediaAccount

**SQL identifier:** `core.organization_social_media_account`

A repeatable social-media account for an organization, preserving platform/type, preference, and source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_social_media_account_identifier` | `TEXT` | PK | No | Unique identifier for an organization social-media account. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `social_media_handle` | `TEXT` |  | No | Username, handle, URI, or other address of the organization social-media account. |
| `social_media_type` | `TEXT` |  | Yes | Standardized social-media account type supplied by the source. |
| `social_media_type_identifier` | `TEXT` | FK → `SocialMediaTypeLookup.SocialMediaTypeIdentifier` | Yes | Governed institution-specific social-media type. |
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred organization social-media account among accounts of the same applicable type. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## OrganizationUnit

**SQL identifier:** `core.organization_unit`

Tenant-owned internal subdivision of a specific real-world Organization, such as a department, college/school, registrar office, division, or administrative unit. OrganizationIdentifier identifies the institution to which the unit belongs; ParentOrganizationUnitIdentifier optionally expresses hierarchy among units within that tenant and organization context.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_unit_identifier` | `TEXT` | PK | No | Unique identifier for the internal organization unit. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization within which this internal organization unit exists. Required because TenantIdentifier defines the data-ownership boundary, not the institution to which the unit belongs. |
| `parent_organization_unit_identifier` | `TEXT` | FK → `OrganizationUnit.OrganizationUnitIdentifier` | Yes | Identifier for the immediate parent organization unit within the same TenantIdentifier and OrganizationIdentifier context. |
| `organization_unit_code` | `TEXT` |  | Yes | Institutionally governed short code for the organization unit. |
| `organization_unit_name` | `TEXT` |  | No | Human-readable name of the organization unit. |
| `organization_unit_type_identifier` | `TEXT` | FK → `OrganizationUnitTypeLookup.OrganizationUnitTypeIdentifier` | Yes | Identifier for the canonical type of internal organization unit. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the organization unit is active for current use. |
| `effective_start_date` | `DATE` |  | Yes | Date on which the organization unit became applicable or effective. |
| `effective_end_date` | `DATE` |  | Yes | Date on which the organization unit ceased to be applicable or effective. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the organization unit was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the organization unit. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## OrganizationUnitTypeLookup

**SQL identifier:** `core.organization_unit_type_lookup`

A tenant-governed lookup defining institutionally meaningful types of internal organization units, such as colleges, schools, faculties, divisions, departments, offices, centers, and institutes. Local terminology and structural semantics may vary by institution.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_unit_type_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a governed organization unit type. |
| `organization_unit_type_code` | `TEXT` |  | No | Institutionally governed code for the organization unit type. |
| `organization_unit_type_name` | `TEXT` |  | No | Concise display name for the institutionally governed organization unit type. |
| `organization_unit_type_description` | `TEXT` |  | Yes | Full semantic definition of the institutionally governed organization unit type. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the institutionally governed organization unit type is active for current use. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonAddress

**SQL identifier:** `core.person_address`

A table containing a history of physical addresses for the person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_address_identifier` | `TEXT` | PK | No | Unique identifier for an address |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `address_type_for_learner_or_family` | `TEXT` |  | No | The type of address listed for a learner or a parent, guardian, family member or related person |
| `formatted_address` | `TEXT` |  | Yes | Formatted address |
| `address_line1` | `TEXT` |  | No | Address street number and name |
| `address_line2` | `TEXT` |  | Yes | The second line of the address, which may include the apartment, room, or suite number |
| `address_apartment_room_or_suite_number` | `TEXT` |  | Yes | The apartment, room, or suite number of an address |
| `address_city` | `TEXT` |  | No | The name of the city in which an address is located |
| `state_abbreviation` | `TEXT` |  | No | The abbreviation for the state (within the United States) or outlying area in which an address is located |
| `address_postal_code` | `TEXT` |  | No | A number that identifies each postal delivery area in the United States used as a portion of an address |
| `address_county_name` | `TEXT` |  | Yes | The name of the county, parish, borough, or comparable unit (within a state) in which an address is located |
| `country_code` | `TEXT` |  | No | The unique two character International Organization for Standardization (ISO) code for the country in which an address is located |
| `state_of_residence` | `TEXT` |  | Yes | The state of the person's permanent address as determined by such evidence as a driver's license or voter registration. For entering freshmen, state of residence may be the legal state of residence of a parent or guardian. |
| `residence_country` | `TEXT` |  | Yes | The country (or countries) where a person currently resides |
| `latitude` | `TEXT` |  | Yes | The north or south angular distance from the equator that, when combined with longitude, reflects an estimation of where the address is physically situated |
| `longitude` | `TEXT` |  | Yes | The east or west angular distance from the prime meridian that, when combined with latitude, reflects an estimation of where the address is physically situated |
| `county_ansi_code` | `TEXT` |  | Yes | County code as defined for the identification of counties and equivalent areas of the United States, Puerto Rico, and the insular areas as established by the American National Standards Institute (ANSI) Inter-National Committee for Information Technology Standards (INCITS) in specification BSR INCITS 31-200x or more current updates. See https://www.census.gov/library/reference/code-lists/ansi.html#par_statelist |
| `publish_indicator` | `BOOLEAN` |  | No | An indication that the record should be published to a visible directory, application, or website, etc. |
| `record_start_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The start date and, optionally, time that a record is active as used to support version control |
| `record_end_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The end date and, optionally, time that a record is active as used to support version control |
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
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred address row. |
| `address_type_identifier` | `TEXT` | FK → `AddressTypeLookup.AddressTypeIdentifier` | Yes | Governed address type. |
| `source_raw_address_type` | `TEXT` |  | Yes | Raw source standard address type. |

## PersonEmail

**SQL identifier:** `core.person_email`

A table containing a list of email addresses associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_email_identifier` | `TEXT` | PK | No | Unique identifier for a person's email item |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | Status of the person's email address (active, inactive) |
| `email_address` | `TEXT` |  | No | The numbers, letters, and symbols used to identify an electronic mail (e-mail) user within the network to which the person or organization belongs |
| `email_address_type` | `TEXT` |  | No | The type of electronic mail (e-mail) address listed for a person or organization |
| `record_start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Single period between date/times |
| `record_end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Single period between date/times |
| `bounce_count` | `INTEGER` |  | Yes | The number of times this email address was unable to be reached |
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
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred email row. |
| `email_type_identifier` | `TEXT` | FK → `EmailTypeLookup.EmailTypeIdentifier` | Yes | Governed email type. |
| `source_raw_email_type` | `TEXT` |  | Yes | Raw source standard email type. |

## PersonIdentification

**SQL identifier:** `core.person_identification`

Tenant-scoped identifier assigned to a person under a defined identification system or namespace, with optional effective dates and source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person to whom this identification value is assigned. |
| `person_identification_identifier` | `TEXT` | PK | No | Unique identifier for this person identification record. |
| `person_identification_system_identifier` | `TEXT` | FK → `PersonIdentificationSystem.PersonIdentificationSystemIdentifier` | No | Identification namespace or system under which IdentifierValue has meaning. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `identifier_value` | `TEXT` |  | No | Identifier assigned to the person within the specified identification system or namespace. |
| `effective_start_date` | `DATE` |  | Yes | Date on which this person identification becomes valid. |
| `effective_end_date` | `DATE` |  | Yes | Date after which this person identification is no longer valid. |
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

## PersonIdentificationSystem

**SQL identifier:** `core.person_identification_system`

Defines an identifier namespace or identification system used to assign meaningful identifiers to persons, such as institutional person IDs, state student IDs, government identifiers, or other governed person-identifier namespaces.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identification_system_identifier` | `TEXT` | PK | No | Unique identifier for this person identification system or namespace. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `acronym` | `TEXT` |  | Yes | Short name or code for the person identification system. |
| `authoritative_resource` | `TEXT` |  | Yes | Authoritative resource or assigning authority associated with the identification system, when applicable. |
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

## PersonLookup

**SQL identifier:** `core.person_lookup`

A lookup table containing details about persons that may provide or be linked to data related to learners or organizations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | A unique number or alphanumeric code assigned to a person |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `first_name` | `TEXT` |  | No | The full legal first name given to a person at birth, baptism, or through legal change |
| `middle_name` | `TEXT` |  | Yes | A full legal middle name given to a person at birth, baptism, or through legal change |
| `last_or_surname` | `TEXT` |  | No | The full legal last name borne in common by members of a family |
| `generation_code_or_suffix` | `TEXT` |  | Yes | An appendage, if any, used to denote a person's generation in his family (e.g. Jr., Sr., III) |
| `name_prefix` | `TEXT` |  | Yes | An appellation, if any, used to denote rank, placement, or status (e.g. Mr., Ms., Reverend, Sister, Dr., Colonel) |
| `qualification_affix` | `TEXT` |  | Yes | The professional designation attached to the end of a person's name (such as M.Sc., Ph.D) |
| `title_affix` | `TEXT` |  | Yes | The title affix attached to a person's name (such as Esq., K.B.E.) |
| `name_data_quality` | `TEXT` |  | Yes | Description of the quality of the name value as reported |
| `guardian_name` | `TEXT` |  | Yes | Full name of a person's guardian (deprecated) |
| `mother_name` | `TEXT` |  | Yes | Full name of a person's mother (deprecated) |
| `father_name` | `TEXT` |  | Yes | Full name of a person's father (deprecated) |
| `ssn` | `TEXT` |  | Yes | Person social security number |
| `ssn_data_quality` | `TEXT` |  | Yes | Description of the quality of the social security number value as reported |
| `birth_date` | `DATE` |  | Yes | Person date of birth |
| `birth_date_quality` | `TEXT` |  | Yes | Description of the quality of the date of birth value as reported |
| `birth_date_verification` | `TEXT` |  | Yes | Information used to verify the DOB information |
| `death_date` | `DATE` |  | Yes | Date of death for a person |
| `record_start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The start date that this name record is effective for the person |
| `record_end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The end date that this name record is effective for the person |
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

## PersonName

**SQL identifier:** `core.person_name`

A table containing a list of names associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_name_identifier` | `TEXT` | PK | No | Unique identifier of a person name item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `first_name` | `TEXT` |  | No | The full legal first name given to a person at birth, baptism, or through legal change |
| `middle_name` | `TEXT` |  | Yes | A full legal middle name given to a person at birth, baptism, or through legal change |
| `last_or_surname` | `TEXT` |  | No | The full legal last name borne in common by members of a family |
| `generation_code_or_suffix` | `TEXT` |  | Yes | An appendage, if any, used to denote a person's generation in his family (e.g. Jr., Sr., III) |
| `name_prefix` | `TEXT` |  | Yes | An appellation, if any, used to denote rank, placement, or status (e.g., Mr. Ms., Reverend, Sister, Dr., Colonel) |
| `qualification_affix` | `TEXT` |  | Yes | The professional designation attached to the end of a person's name (such as M.Sc., Ph.D) |
| `title_affix` | `TEXT` |  | Yes | The title affix attached to a person's name (such as Esq., K.B.E.) |
| `name_data_quality` | `TEXT` |  | Yes | Description of the quality of the name value as reported |
| `name_type` | `TEXT` |  | Yes | The types of previous, alternate or other names for a person |
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
| `full_name` | `TEXT` |  | Yes | Source-provided formatted/full name. |
| `last_name_prefix` | `TEXT` |  | Yes | Article or preposition portion of surname. |
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred name row. |
| `person_name_type_identifier` | `TEXT` | FK → `PersonNameTypeLookup.PersonNameTypeIdentifier` | Yes | Governed person-name type. |
| `source_raw_name_type_category` | `TEXT` |  | Yes | Raw source name-type category. |

## PersonPhone

**SQL identifier:** `core.person_phone`

A table containing a list of phone numbers associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_phone_identifier` | `TEXT` | PK | No | Unique identifier for the telephone item |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | Status of the person's phone number (active, inactive) |
| `telephone_number` | `TEXT` |  | No | The telephone number including the area code, and extension, if applicable |
| `telephone_number_type` | `TEXT` |  | No | The type of communication number listed for a person |
| `primary_telephone_number_indicator` | `BOOLEAN` |  | No | An indication that the telephone number should be used as the principal number for a person or organization |
| `priority_sequence_number` | `INTEGER` |  | Yes | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `sms_capability_indicator` | `BOOLEAN` |  | Yes | An indication that the telephone number is technically capable of sending and receiving Short Message Resource (SMS) text messages |
| `publish_indicator` | `BOOLEAN` |  | No | An indication that the record should be published to a visible directory, application, or website, etc. |
| `telephone_number_listed_status` | `TEXT` |  | Yes | An indication of whether a telephone number is listed under a directory assistance resource |
| `record_start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Single period between date/times |
| `record_end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Single period between date/times |
| `bounce_count` | `INTEGER` |  | Yes | The number of times this phone number was unable to be reached |
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
| `extension` | `TEXT` |  | Yes | Telephone extension. |
| `country_calling_code` | `TEXT` |  | Yes | International country calling code. |
| `phone_type_identifier` | `TEXT` | FK → `PhoneTypeLookup.PhoneTypeIdentifier` | Yes | Governed phone type. |
| `source_raw_phone_type` | `TEXT` |  | Yes | Raw source standard phone type. |

## PersonPreferredContact

**SQL identifier:** `core.person_preferred_contact`

A table containing details about a learner's reported preferred contact methods.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `person_preferred_contact_identifier` | `TEXT` | PK | No | Unique identifier for a preferred contact item |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `preferred_first_name` | `TEXT` |  | Yes | Preferred first name to be used |
| `preferred_last_name` | `TEXT` |  | Yes | Preferred last name to be used |
| `preferred_telephone` | `TEXT` |  | Yes | Preferred number for telephone communication and electronic delivery |
| `preferred_email` | `TEXT` |  | Yes | Preferred email address for electronic mail delivery |
| `preferred_address_line1` | `TEXT` |  | Yes | Address street number and name |
| `preferred_address_line2` | `TEXT` |  | Yes | The second line of the address, which may include the apartment, room, or suite number |
| `address_apartment_room_or_suite_number` | `TEXT` |  | Yes | The apartment, room, or suite number of an address |
| `preferred_city` | `TEXT` |  | Yes | Preferred city |
| `preferred_state` | `TEXT` |  | Yes | Preferred state abbreviation for physical delivery of communication |
| `preferred_postal_code` | `TEXT` |  | Yes | Preferred postal code for physical delivery of communication |
| `last_contact_preferred_telephone_successful_indicator` | `BOOLEAN` |  | Yes | Indicates whether the last phone call to the preferred telephone number went through successfully |
| `last_contact_preferred_email_successful_indicator` | `BOOLEAN` |  | Yes | Indicates whether the last email to the preferred email address went through successfully |
| `last_contact_preferred_address_successful_indicator` | `BOOLEAN` |  | Yes | Indicates whether the last mail sent to the preferred address was delivered successfully |
| `preferred_language` | `TEXT` |  | Yes | Preferred language to interact in oral and written communication |
| `preferred_communication_method` | `TEXT` |  | Yes | Indicates the learner's preferred communication method (e.g. social media, email, phone, text, mail, in-person, video call) |
| `emergency_contact_name` | `TEXT` |  | Yes | Name of a person's emergency contact |
| `emergency_contact_telephone` | `TEXT` |  | Yes | Phone number of a person's emergency contact |
| `emergency_contact_email` | `TEXT` |  | Yes | Email address of a person's emergency contact |
| `start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The effective date for which the contact is valid |
| `end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The expired date for which the contact is valid |
| `person_website_url` | `TEXT` |  | Yes | The Uniform Resource Locator (URL) for the unique address of a Web page |
| `timezone` | `TEXT` |  | Yes | The timezone of the person |
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

## PersonRole

**SQL identifier:** `core.person_role`

A table containing a list of roles associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_role_identifier` | `TEXT` | PK | No | Unique identifier for a person role definition |
| `role_identifier` | `TEXT` | FK → `RoleLookup.RoleIdentifier` | No | Unique identifier for the role |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `organization_department` | `TEXT` |  | Yes | Indicates the department within the organization to which the person belongs |
| `organization_position_or_title` | `TEXT` |  | Yes | Indicates the position or title the person holds at the organization |
| `faculty_status_indicator` | `BOOLEAN` |  | No | Persons identified by the institution as such and typically those whose initial assignments are made for the purpose of conducting instruction, research or public resource as a principal activity (or activities). They may hold academic rank titles of professor, associate professor, assistant professor, instructor, lecturer or the equivalent of any of those academic ranks. Faculty may also include the chancellor/president, provost, vice provosts, deans, directors or the equivalent, as well as associate deans, assistant deans and executive officers of academic departments (chairpersons, heads or the equivalent) if their principal activity is instruction combined with research and/or public resource. The designation as "faculty" is separate from the activities to which they may be currently assigned. For example, a newly appointed president of an institution may also be appointed as a faculty member. Graduate, instruction, and research assistants are not included in this category. |
| `faculty_workload_type` | `TEXT` |  | Yes | The workload type employment status of the faculty member (PartTime, FullTime) |
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
| `role_start_date` | `DATE` |  | Yes | Effective start date of the person role. |
| `role_end_date` | `DATE` |  | Yes | Effective end date of the person role. |

## PersonSocialMediaAccount

**SQL identifier:** `core.person_social_media_account`

A social media account associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `person_social_media_account_identifier` | `TEXT` | PK | No | Person Social Media Account Identifier for the PersonSocialMediaAccount record. [Description requires semantic review.] |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `social_media_handle` | `TEXT` |  | No | A person's social media handle |
| `social_media_type` | `TEXT` |  | No | Type of social media item |
| `publish_indicator` | `BOOLEAN` |  | No | An indication that the record should be published to a visible directory, application, or website, etc. |
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
| `preferred_indicator` | `BOOLEAN` |  | Yes | Indicates the preferred social-media row. |
| `social_media_type_identifier` | `TEXT` | FK → `SocialMediaTypeLookup.SocialMediaTypeIdentifier` | Yes | Governed social-media type. |
| `source_raw_social_media_type` | `TEXT` |  | Yes | Raw source social-media type. |

## PersonTagLookup

**SQL identifier:** `core.person_tag_lookup`

A tenant-scoped governed definition of an institution-defined label or attribute that may be assigned to a person for operational tracking, segmentation, support, or reporting. Tags are not cohorts and do not by themselves define dynamic membership logic.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_tag_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for the governed person tag. |
| `code` | `TEXT` |  | No | Institution-defined code for the person tag. |
| `title` | `TEXT` |  | No | Full name of the person tag. |
| `description` | `TEXT` |  | Yes | Description of the person tag and its intended institutional use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ReferenceCodeSet

**SQL identifier:** `core.reference_code_set`

A table defining current governed sets of reference-code values used for validation, dropdown menus, reason codes, lightweight classifications, reporting taxonomies, and display ordering. Sets may be added, activated, or inactivated; the table does not maintain effective-dated or version history.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `reference_code_set_identifier` | `TEXT` | PK | No | Unique identifier for a governed reference code set |
| `reference_code_set_code` | `TEXT` |  | No | Stable system code for the reference code set |
| `reference_code_set_description` | `TEXT` |  | No | Human-readable description of the reference code set |
| `governing_authority` | `TEXT` |  | Yes | Organization or standards body governing the reference code set, such as NCES, OMB, or a state agency. |
| `jurisdiction_country_code` | `TEXT` |  | Yes | ISO 3166-1 alpha-2 country code for the jurisdiction to which the reference code set applies. |
| `reference_code_set_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the reference code set |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the reference code set is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ReferenceCodeValue

**SQL identifier:** `core.reference_code_value`

A table defining governed values within a reference code set, including stable codes, display descriptions, sort order, optional action codes, active status, and audit information.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `reference_code_value_identifier` | `TEXT` | PK | No | Unique identifier for a governed reference code value |
| `reference_code_set_identifier` | `TEXT` | FK → `ReferenceCodeSet.ReferenceCodeSetIdentifier` | No | Unique identifier for the reference code set that contains this value |
| `reference_code_value_code` | `TEXT` |  | No | Stable system code for the reference code value |
| `reference_code_value_description` | `TEXT` |  | No | Human-readable label for the reference code value |
| `reference_code_value_sort_order` | `INTEGER` |  | Yes | Display or processing sort order for the reference code value |
| `reference_code_value_action_code1` | `TEXT` |  | Yes | Optional action or rollup code for lightweight categorization of the reference code value |
| `reference_code_value_action_code2` | `TEXT` |  | Yes | Optional secondary action or rollup code for the reference code value |
| `reference_code_value_action_code3` | `TEXT` |  | Yes | Optional tertiary action or rollup code for the reference code value |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the reference code value is active for current use |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## RoleLookup

**SQL identifier:** `core.role_lookup`

A lookup table containing descriptions of roles defined by an organization that may be assigned to a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `role_identifier` | `TEXT` | PK | No | Unique identifier for the role |
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

## SharingPermission

**SQL identifier:** `core.sharing_permission`

A table describing the permissions that a grantor gives to a grantee regarding their data in the DHSS model.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `sharing_permission_identifier` | `TEXT` | PK | No | Unique identifier for the sharing permission record |
| `granted_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Unique identifier for the person giving authorization |
| `granted_to_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier for the person receiving authorization |
| `granted_to_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Unique identifier for the organization receiving authorization |
| `granted_to_role_identifier` | `TEXT` | FK → `RoleLookup.RoleIdentifier` | Yes | Unique identifier for the role receiving authorization |
| `object_identifier` | `TEXT` | FK → `ObjectLookup.ObjectIdentifier` | No | Unique identifier for the object or database table |
| `object_row_identifier` | `TEXT` |  | No | Unique identifier for the object or database table row |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `ai_granted_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not AI tools are permitted to be used with the resource |
| `scope` | `TEXT` |  | Yes | Indicates whether this permission is allowing read only or edit access to the resource type |
| `permission_type` | `TEXT` |  | Yes | Indicates whether this permission is allowing or denying access to the resource type |
| `start_date` | `DATE` |  | Yes | Date that the permission starts or becomes effective |
| `end_date` | `DATE` |  | Yes | Date that the permission ends or expires |
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

## SourceSystemLookup

**SQL identifier:** `core.source_system_lookup`

A lookup table for tracking source systems providing data to the DHSS model objects.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | PK | No | Unique identifier for the source system |
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

## Template

**SQL identifier:** `core.template`

A table containing templates to help with writing message content.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `template_identifier` | `TEXT` | PK | No | Unique identifier for the template |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `type` | `TEXT` |  | No | Indicates the type or purpose of the template |
| `text` | `TEXT` |  | No | The text of the template |
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

## Tenant

**SQL identifier:** `core.tenant`

Defines the tenant data-ownership and security boundary for a GUIDE deployment. TenantIdentifier is a UUID and is distinct from any real-world OrganizationIdentifier represented within the tenant.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `tenant_name` | `TEXT` |  | No | Human-readable name of the tenant context. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the tenant context is active. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the tenant record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the tenant record was last updated. |

## TenantOrganizationRole

**SQL identifier:** `core.tenant_organization_role`

Effective-dated tenant-relative role played by an organization, such as HomeInstitution. Prevents contextual roles from becoming intrinsic organization attributes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `tenant_organization_role_identifier` | `TEXT` | PK | No | Unique identifier for a tenant-relative organization role. |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Organization playing the role in this tenant context. |
| `tenant_organization_role_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed tenant-relative role such as HomeInstitution. |
| `effective_start_date` | `DATE` |  | Yes | Date on which the tenant-relative role becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date after which the tenant-relative role is no longer effective. |
