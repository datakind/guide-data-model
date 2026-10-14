# Entity: Supports

This page documents every table that belongs to the **Supports** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 60**

## Table of contents

- [ChallengeLookup](#challengelookup)
- [DisabilityLookup](#disabilitylookup)
- [GoalCareerAssociation](#goalcareerassociation)
- [GoalCategoryGoalAssociation](#goalcategorygoalassociation)
- [GoalCategoryLookup](#goalcategorylookup)
- [GoalLookup](#goallookup)
- [GoalOccupationElementAssociation](#goaloccupationelementassociation)
- [HousingBuildingWing](#housingbuildingwing)
- [HousingRequest](#housingrequest)
- [HousingRequestAcademicPeriod](#housingrequestacademicperiod)
- [HousingRequestLocationPreference](#housingrequestlocationpreference)
- [HousingRequestRoomCharacteristic](#housingrequestroomcharacteristic)
- [HousingRequestRoommatePreference](#housingrequestroommatepreference)
- [HousingResidentTypeLookup](#housingresidenttypelookup)
- [HousingRoom](#housingroom)
- [HousingRoomCharacteristicAssociation](#housingroomcharacteristicassociation)
- [HousingRoomCharacteristicLookup](#housingroomcharacteristiclookup)
- [HousingRoomOccupancy](#housingroomoccupancy)
- [HousingRoomRate](#housingroomrate)
- [HousingRoomRateAmount](#housingroomrateamount)
- [HousingRoomTypeAssociation](#housingroomtypeassociation)
- [HousingRoomTypeLookup](#housingroomtypelookup)
- [HousingRoommateCharacteristicLookup](#housingroommatecharacteristiclookup)
- [LearnerEligibilityReport](#learnereligibilityreport)
- [LearnerEngagementBadge](#learnerengagementbadge)
- [LearnerResourceEligibility](#learnerresourceeligibility)
- [LearnerResourceEligibilityRequirement](#learnerresourceeligibilityrequirement)
- [LearnerResourceParticipation](#learnerresourceparticipation)
- [LearnerWellness](#learnerwellness)
- [MealPlan](#mealplan)
- [MealPlanAssignment](#mealplanassignment)
- [MealPlanAssignmentRate](#mealplanassignmentrate)
- [MealPlanComponent](#mealplancomponent)
- [MealPlanComponentRestriction](#mealplancomponentrestriction)
- [MealPlanRate](#mealplanrate)
- [MealPlanRequest](#mealplanrequest)
- [MealPlanResidentialCategory](#mealplanresidentialcategory)
- [MealTypeLookup](#mealtypelookup)
- [PersonChallenge](#personchallenge)
- [PersonDietIntake](#persondietintake)
- [PersonDisability](#persondisability)
- [PersonDisabilityAccommodation](#persondisabilityaccommodation)
- [PersonEducationGoal](#personeducationgoal)
- [PersonGoal](#persongoal)
- [PersonGoalAlignment](#persongoalalignment)
- [PersonHousing](#personhousing)
- [PersonHousingEnrollment](#personhousingenrollment)
- [PersonPriorHousing](#personpriorhousing)
- [PersonResourceGuide](#personresourceguide)
- [PersonResourceGuideResource](#personresourceguideresource)
- [PersonScheduledEventResponse](#personscheduledeventresponse)
- [ResourceCategory](#resourcecategory)
- [ResourceCategoryResourceAssociation](#resourcecategoryresourceassociation)
- [ResourceLookup](#resourcelookup)
- [ResourceRequirement](#resourcerequirement)
- [ResourceTag](#resourcetag)
- [ResourceTagResourceAssociation](#resourcetagresourceassociation)
- [ScheduledEvent](#scheduledevent)
- [StudentResidentialCategoryLookup](#studentresidentialcategorylookup)
- [ValueLookup](#valuelookup)

---

## ChallengeLookup

**SQL identifier:** `supports.challenge_lookup`

A lookup table containing common challenges learners experience during educational pursuit. The list of challenges can be associated to one or more resources, services, referrals, surveys, and intakes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `challenge_identifier` | `TEXT` | PK | No | Unique identifier for the challenge item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
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

## DisabilityLookup

**SQL identifier:** `supports.disability_lookup`

A lookup table containing descriptions of disabilities recognized by the organization and Americans with Disabilities Act (ADA).

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `disability_identifier` | `TEXT` | PK | No | Unique identifier for a disability item |
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

## GoalCareerAssociation

**SQL identifier:** `supports.goal_career_association`

A table associating goals to career pathways, career pathway components, or career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `goal_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the goal to career association |
| `goal_identifier` | `TEXT` | FK → `GoalLookup.GoalIdentifier` | No | Unique identifier for a goal item |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## GoalCategoryGoalAssociation

**SQL identifier:** `supports.goal_category_goal_association`

A table associating goal categories to goals.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `goal_category_goal_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the goal to the goal category |
| `goal_category_identifier` | `TEXT` | FK → `GoalCategoryLookup.GoalCategoryIdentifier` | No | Unique identifier for the goal category |
| `goal_identifier` | `TEXT` | FK → `GoalLookup.GoalIdentifier` | No | Unique identifier for a goal item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## GoalCategoryLookup

**SQL identifier:** `supports.goal_category_lookup`

A lookup table containing goal categories (e.g. Academic, Wellness, Career, etc.).

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `goal_category_identifier` | `TEXT` | PK | No | Unique identifier for the goal category |
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

## GoalLookup

**SQL identifier:** `supports.goal_lookup`

A lookup table containing descriptions of goals that learners may be pursuing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `goal_identifier` | `TEXT` | PK | No | Unique identifier for a goal item |
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

## GoalOccupationElementAssociation

**SQL identifier:** `supports.goal_occupation_element_association`

A table associating goals to occupation elements.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `goal_occupation_element_association_identifier` | `TEXT` | PK | No | Unique identifier for the association between a learner's goals and a skill, knowledge, or ability item as defined by ONET |
| `goal_identifier` | `TEXT` | FK → `GoalLookup.GoalIdentifier` | No | Unique identifier for a learner goal item |
| `occupation_element_identifier` | `TEXT` | FK → `OccupationElementLookup.OccupationElementIdentifier` | No | Unique identifier for the skill, knowledge, or ability as defined by ONET |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## HousingBuildingWing

**SQL identifier:** `supports.housing_building_wing`

Governed named wing or section of a building.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_building_wing_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingBuildingWing |
| `code` | `TEXT` |  | No | Wing code |
| `title` | `TEXT` |  | No | Wing title |
| `description` | `TEXT` |  | Yes | Wing description |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRequest

**SQL identifier:** `supports.housing_request`

A tenant-scoped request by a person for institutional housing, distinct from an actual housing assignment or current housing context.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_request_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRequest |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person requesting housing |
| `start_date` | `DATE` |  | Yes | Requested housing start date |
| `end_date` | `DATE` |  | Yes | Requested housing end date |
| `status` | `TEXT` |  | Yes | Source-reported request status |
| `priority_number` | `INTEGER` |  | Yes | Relative request priority |
| `floor_characteristic` | `TEXT` |  | Yes | Preferred floor characteristic |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRequestAcademicPeriod

**SQL identifier:** `supports.housing_request_academic_period`

Academic periods covered by a housing request.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_request_identifier` | `TEXT` | PK, FK → `HousingRequest.HousingRequestIdentifier` | No | Housing request |
| `term_identifier` | `TEXT` | PK, FK → `TermLookup.TermIdentifier` | No | Identifier of the academic term or period to which the housing request applies. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRequestLocationPreference

**SQL identifier:** `supports.housing_request_location_preference`

Ordered preferred housing locations for a request.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_request_identifier` | `TEXT` | PK, FK → `HousingRequest.HousingRequestIdentifier` | No | Housing request |
| `preference_sequence_number` | `TEXT` | PK | No | Deterministic source order |
| `site_identifier` | `TEXT` | FK → `SiteLookup.SiteIdentifier` | Yes | Preferred institutional site |
| `building_source_key` | `TEXT` |  | Yes | Preferred source building identifier |
| `building_wing_identifier` | `TEXT` | FK → `HousingBuildingWing.HousingBuildingWingIdentifier` | Yes | Preferred building wing |
| `floor` | `TEXT` |  | Yes | Preferred floor |
| `room_identifier` | `TEXT` | FK → `HousingRoom.HousingRoomIdentifier` | Yes | Preferred room |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRequestRoomCharacteristic

**SQL identifier:** `supports.housing_request_room_characteristic`

Required or optional room characteristics requested by a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_request_identifier` | `TEXT` | PK, FK → `HousingRequest.HousingRequestIdentifier` | No | Housing request |
| `room_characteristic_identifier` | `TEXT` | PK | No | Preferred room characteristic |
| `required_indicator` | `BOOLEAN` |  | No | Whether the characteristic is required |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRequestRoommatePreference

**SQL identifier:** `supports.housing_request_roommate_preference`

Requested roommate or roommate characteristic for a housing request.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_request_identifier` | `TEXT` | PK, FK → `HousingRequest.HousingRequestIdentifier` | No | Housing request |
| `preference_sequence_number` | `TEXT` | PK | No | Deterministic source order |
| `preferred_roommate_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Preferred identified roommate |
| `roommate_characteristic_identifier` | `TEXT` | FK → `HousingRoommateCharacteristicLookup.HousingRoommateCharacteristicIdentifier` | Yes | Preferred roommate characteristic |
| `required_indicator` | `BOOLEAN` |  | No | Whether the preference is required |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingResidentTypeLookup

**SQL identifier:** `supports.housing_resident_type_lookup`

Governed institutional housing resident category.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_resident_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingResidentType |
| `code` | `TEXT` |  | No | Institution-defined code |
| `title` | `TEXT` |  | No | Human-readable name of the housing resident type. |
| `description` | `TEXT` |  | Yes | Detailed description of the housing resident type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoom

**SQL identifier:** `supports.housing_room`

A physical institutional room used for housing or related facility purposes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRoom |
| `building_source_key` | `TEXT` |  | Yes | Source identifier for the containing building |
| `site_identifier` | `TEXT` | FK → `SiteLookup.SiteIdentifier` | Yes | Institutional site |
| `building_wing_identifier` | `TEXT` | FK → `HousingBuildingWing.HousingBuildingWingIdentifier` | Yes | Building wing |
| `room_number` | `TEXT` |  | No | Room number or code |
| `title` | `TEXT` |  | Yes | Room title |
| `description` | `TEXT` |  | Yes | Room description |
| `floor` | `TEXT` |  | Yes | Floor name or number |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomCharacteristicAssociation

**SQL identifier:** `supports.housing_room_characteristic_association`

Characteristics assigned to a room.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_identifier` | `TEXT` | PK, FK → `HousingRoom.HousingRoomIdentifier` | No | Housing room |
| `housing_room_characteristic_identifier` | `TEXT` | PK, FK → `HousingRoomCharacteristicLookup.HousingRoomCharacteristicIdentifier` | No | Room characteristic |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomCharacteristicLookup

**SQL identifier:** `supports.housing_room_characteristic_lookup`

Governed room characteristic.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_characteristic_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRoomCharacteristic |
| `code` | `TEXT` |  | No | Institution-defined code |
| `title` | `TEXT` |  | No | Human-readable name of the housing-room characteristic or amenity. |
| `description` | `TEXT` |  | Yes | Detailed description of the housing-room characteristic or amenity. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomOccupancy

**SQL identifier:** `supports.housing_room_occupancy`

Supported occupancy layout and maximum occupancy for a room.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_identifier` | `TEXT` | PK, FK → `HousingRoom.HousingRoomIdentifier` | No | Housing room |
| `occupancy_type` | `TEXT` | PK | No | Source-defined layout or occupancy type |
| `maximum_occupancy` | `INTEGER` |  | Yes | Maximum occupancy |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomRate

**SQL identifier:** `supports.housing_room_rate`

Governed room rate definition, optionally scoped to an academic period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_rate_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRoomRate |
| `code` | `TEXT` |  | No | Rate code |
| `title` | `TEXT` |  | No | Rate title |
| `description` | `TEXT` |  | Yes | Rate description |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifier of the academic term or period during which the room rate is effective. |
| `start_date` | `DATE` |  | Yes | Effective start date |
| `end_date` | `DATE` |  | Yes | Effective end date |
| `accounting_code` | `TEXT` |  | Yes | Default accounting code |
| `cancellation_accounting_code` | `TEXT` |  | Yes | Cancellation accounting code |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomRateAmount

**SQL identifier:** `supports.housing_room_rate_amount`

Monetary amount within a room rate for a defined period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_rate_identifier` | `TEXT` | PK, FK → `HousingRoomRate.HousingRoomRateIdentifier` | No | Room rate |
| `rate_sequence_number` | `TEXT` | PK | No | Deterministic source order |
| `rate_period` | `TEXT` |  | Yes | Rate interval |
| `amount` | `NUMERIC` |  | No | Rate amount |
| `currency_code` | `TEXT` |  | No | ISO 4217 currency |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomTypeAssociation

**SQL identifier:** `supports.housing_room_type_association`

Room layouts or types supported by a room.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_identifier` | `TEXT` | PK, FK → `HousingRoom.HousingRoomIdentifier` | No | Housing room |
| `housing_room_type_identifier` | `TEXT` | PK, FK → `HousingRoomTypeLookup.HousingRoomTypeIdentifier` | No | Room type |
| `detail` | `TEXT` |  | Yes | Source detail for the room type |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoomTypeLookup

**SQL identifier:** `supports.housing_room_type_lookup`

Governed room layout or room type.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_room_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRoomType |
| `code` | `TEXT` |  | No | Institution-defined code |
| `title` | `TEXT` |  | No | Human-readable name of the housing-room type or configured room layout. |
| `description` | `TEXT` |  | Yes | Detailed description of the housing-room type, configuration, or intended use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## HousingRoommateCharacteristicLookup

**SQL identifier:** `supports.housing_roommate_characteristic_lookup`

Governed roommate characteristic.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `housing_roommate_characteristic_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the HousingRoommateCharacteristic |
| `code` | `TEXT` |  | No | Institution-defined code |
| `title` | `TEXT` |  | No | Human-readable name of the housing roommate characteristic. |
| `description` | `TEXT` |  | Yes | Detailed description of the housing roommate characteristic. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## LearnerEligibilityReport

**SQL identifier:** `supports.learner_eligibility_report`

A table containing a history of learner edibility reports for academic, financial, and co-curricular programs.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_eligibility_report_identifier` | `TEXT` | PK | No | Unique identifier for eligibility report |
| `learner_degree_plan_identifier` | `TEXT` | FK → `LearnerDegreePlan.LearnerDegreePlanIdentifier` | Yes | Unique identifier for the learner's degree plan |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `eligibility_report_type` | `TEXT` |  | No | Type of eligibility report (graduation, NCAA, financial aid, scholarship) |
| `status` | `TEXT` |  | No | Eligibility status based on the report |
| `status_details` | `TEXT` |  | No | Description of the eligibility status determination |
| `eligibility_status_start_date` | `DATE` |  | Yes | Date the status became effective |
| `eligibility_status_end_date` | `DATE` |  | Yes | Date the status expired |
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
| `learner_degree_plan_revision_identifier` | `TEXT` | FK → `LearnerDegreePlan.RevisionIdentifier` | Yes | Revision of the LearnerDegreePlan referenced by this record. |

## LearnerEngagementBadge

**SQL identifier:** `supports.learner_engagement_badge`

A table containing a history of badges learners have earned for participation in platform usage encouragement endeavors (e.g. setup profile, submit 10 forum posts).

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_engagement_badge_identifier` | `TEXT` | PK | No | Unique identifier for the learner engagement badge |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `uri` | `TEXT` |  | Yes | URI to the badge earned by the person |
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

## LearnerResourceEligibility

**SQL identifier:** `supports.learner_resource_eligibility`

Represents one dated learner eligibility determination for a resource, including its effective and review lifecycle.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_resource_eligibility_identifier` | `TEXT` | PK | No | Unique identifier for a resources eligible item |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | No | Unique identifier for the support resource, service, or program |
| `eligibility_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed reference-code value describing the eligibility determination status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `source_raw_eligibility_status` | `TEXT` |  | Yes | Unmodified eligibility-status value supplied by the source system. |
| `eligibility_date` | `DATE` |  | No | Date the eligibility determination was made. |
| `effective_start_date` | `DATE` |  | Yes | Date on which the eligibility determination becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date on which the eligibility determination ceases to be effective. |
| `next_review_date` | `DATE` |  | Yes | Date on which the eligibility determination should next be reviewed. |
| `determination_reason` | `TEXT` |  | Yes | Internal operational rationale for the eligibility determination. |
| `learner_explanation` | `TEXT` |  | Yes | Plain-language explanation of the determination suitable for the learner. |
| `next_step_guidance` | `TEXT` |  | Yes | Guidance describing actions the learner may take next. |
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

## LearnerResourceEligibilityRequirement

**SQL identifier:** `supports.learner_resource_eligibility_requirement`

Records the learner-specific evaluation result for one reusable resource requirement within an eligibility determination.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_resource_eligibility_requirement_identifier` | `TEXT` | PK | No | A unique identifier for learner resource requirement details |
| `learner_resource_eligibility_identifier` | `TEXT` | FK → `LearnerResourceEligibility.LearnerResourceEligibilityIdentifier` | No | Learner Resource Eligibility Identifier for the LearnerResourceEligibilityRequirement record. [Description requires semantic review.] |
| `resource_requirement_identifier` | `TEXT` | FK → `ResourceRequirement.ResourceRequirementIdentifier` | No | Unique identifier for a resources eligible requirement item |
| `requirement_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed reference-code value describing the requirement evaluation status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | SourceSystemIdentifier for LearnerResourceEligibilityRequirement. |
| `source_raw_requirement_status` | `TEXT` |  | Yes | Unmodified requirement-status value supplied by the source system. |
| `evaluation_date` | `DATE` |  | Yes | Date the learner was evaluated against the requirement. |
| `result_value` | `TEXT` |  | Yes | Observed or derived value used in evaluating the learner against the requirement. |
| `result_comment` | `TEXT` |  | Yes | Narrative context for the requirement evaluation result. |
| `waiver_indicator` | `BOOLEAN` |  | No | Indicates that the requirement was waived for this determination. |
| `verification_method` | `TEXT` |  | Yes | Method or evidence source used to verify the requirement result. |
| `source_system_key_value` | `TEXT` |  | Yes | SourceSystemKeyValue for LearnerResourceEligibilityRequirement. |
| `source_system_created_date` | `DATE` |  | Yes | SourceSystemCreatedDate for LearnerResourceEligibilityRequirement. |
| `source_system_updated_date` | `DATE` |  | Yes | SourceSystemUpdatedDate for LearnerResourceEligibilityRequirement. |
| `source_system_deleted_date` | `DATE` |  | Yes | SourceSystemDeletedDate for LearnerResourceEligibilityRequirement. |
| `created_by` | `INTEGER` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `INTEGER` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `INTEGER` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerResourceParticipation

**SQL identifier:** `supports.learner_resource_participation`

Represents one learner participation episode in a support resource, service, or program; it may optionally be linked to the eligibility determination and/or support referral that led to participation. Attendance fields summarize the episode rather than individual sessions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner participating in the resource. |
| `learner_resource_participation_identifier` | `TEXT` | PK | No | Unique identifier for the person's resource participation |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | Yes | Resource, service, or program in which the learner participates. |
| `learner_resource_eligibility_identifier` | `TEXT` | FK → `LearnerResourceEligibility.LearnerResourceEligibilityIdentifier` | Yes | Optional reference to the learner resource eligibility determination that led to participation. |
| `person_support_referral_identifier` | `TEXT` | FK → `PersonSupportReferral.PersonSupportReferralIdentifier` | Yes | Optional support referral that led to, or is fulfilled by, this resource participation episode. The link supports closed-loop referral-to-service interoperability without requiring every participation to originate from a formal referral. |
| `resource_attendance_reporter_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier for the person reporting learner attendance |
| `resource_category_identifier` | `TEXT` | FK → `ResourceCategory.ResourceCategoryIdentifier` | Yes | Unique identifier for a resource category item |
| `participation_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed reference-code value describing the participation episode status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | A description for the record |
| `source_raw_participation_status` | `TEXT` |  | Yes | Unmodified participation-status value supplied by the source system. |
| `application_submission_date` | `DATE` |  | Yes | Date the application for this resource was submitted |
| `benefits_end_date` | `DATE` |  | Yes | Date the resource benefit expires |
| `status_comment` | `TEXT` |  | Yes | Description of additional details about the reasons for the resource status or any comments about the resource |
| `usage_start_date` | `DATE` |  | Yes | Date the resource started |
| `usage_end_date` | `DATE` |  | Yes | Date the resource ended |
| `referral_source` | `TEXT` |  | Yes | Person or application that referred the person to the resource |
| `type` | `TEXT` |  | Yes | Type of resource provided |
| `reason` | `TEXT` |  | Yes | Reason the person received the resource referral |
| `outcome` | `TEXT` |  | Yes | Outcome of the resource provided to the person |
| `attendance_status` | `TEXT` |  | Yes | Status of the resource attendance (show, no show, late) |
| `attendance_notes` | `TEXT` |  | Yes | Notes added by the care team for the resource attendance |
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

## LearnerWellness

**SQL identifier:** `supports.learner_wellness`

A table containing a history of learner wellness, including responses provided during intake.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_wellness_identifier` | `TEXT` | PK | No | Unique identifier for a wellness case item |
| `referral_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique number or alphanumeric code assigned to a person |
| `referral_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `staff_assignment_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier of the careteam member assignment to a learner |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `recorded_date` | `DATE` |  | Yes | The recorded date of the occurrence |
| `condition_status` | `TEXT` |  | Yes | The status of the client's wellness condition |
| `verification_status` | `TEXT` |  | Yes | Verification status of the client's condition by the care team, contributor, or custodian |
| `evaluation_type` | `TEXT` |  | Yes | Type of wellness evaluation |
| `category` | `TEXT` |  | Yes | The category of the wellness type |
| `criticality` | `TEXT` |  | Yes | The severity level of the condition |
| `referral_organization_name` | `TEXT` |  | Yes | Name of the organization to which the learner is being referred |
| `referral_person_name` | `TEXT` |  | Yes | Name of the person to which the learner is being referred |
| `referral_person_contact` | `TEXT` |  | Yes | Telephone or email of the person to which the learner is being referred |
| `last_occurrence` | `DATE` |  | Yes | The known date of the last occurrence this condition occurred |
| `note` | `TEXT` |  | Yes | The notes and comments on the client's condition |
| `custodian_name` | `TEXT` |  | Yes | The name of responsible party of the client |
| `supporting_information` | `TEXT` |  | Yes | Supporting documentation of the proposed plan |
| `goal` | `TEXT` |  | Yes | Description of the desired outcome |
| `status` | `TEXT` |  | Yes | The status of the person's progress towards their wellness goal |
| `basis` | `TEXT` |  | Yes | Description of evidence about the condition |
| `preferences` | `TEXT` |  | Yes | The person's preferences for this wellness category |
| `geo_location_sharing_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person has opted in to geo-location sharing to receive recommendations for nearby resources associated with this wellness item |
| `behavior_tracking_check_in_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person has opted in to receiving notifications when their behaviors indicate they need a wellness check-in |
| `ai_wellness_chat_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person has opted in to engaging in AI chat or voice discussions to find out more information about what resources might be a good fit for them |
| `need_crisis_intervention_indicator` | `BOOLEAN` |  | No | Indicator that the student has requested a referral to crisis intervention |
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

## MealPlan

**SQL identifier:** `supports.meal_plan`

Governed meal plan definition.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the MealPlan |
| `code` | `TEXT` |  | No | Meal plan code |
| `title` | `TEXT` |  | No | Meal plan title |
| `description` | `TEXT` |  | Yes | Meal plan description |
| `start_date` | `DATE` |  | Yes | Plan start date |
| `end_date` | `DATE` |  | Yes | Plan end date |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanAssignment

**SQL identifier:** `supports.meal_plan_assignment`

An effective assignment of a meal plan to a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_assignment_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the MealPlanAssignment |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Assigned person |
| `meal_plan_identifier` | `TEXT` | FK → `MealPlan.MealPlanIdentifier` | No | Assigned meal plan |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifier of the academic term or period to which the meal-plan assignment applies. |
| `start_date` | `DATE` |  | Yes | Assignment start date |
| `end_date` | `DATE` |  | Yes | Assignment end date |
| `status` | `TEXT` |  | Yes | Assignment status |
| `status_date` | `DATE` |  | Yes | Status date |
| `meal_card_identifier` | `TEXT` |  | Yes | Meal-card value |
| `number_of_periods` | `INTEGER` |  | Yes | Number of assignment periods |
| `consumption` | `NUMERIC` |  | Yes | Source-reported consumed units or percentage |
| `rate_override_amount` | `NUMERIC` |  | Yes | Override amount |
| `comment` | `TEXT` |  | Yes | Assignment comment |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanAssignmentRate

**SQL identifier:** `supports.meal_plan_assignment_rate`

Rates applied to a meal-plan assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_assignment_identifier` | `TEXT` | PK, FK → `MealPlanAssignment.MealPlanAssignmentIdentifier` | No | Meal plan assignment |
| `meal_plan_rate_identifier` | `TEXT` | PK, FK → `MealPlanRate.MealPlanRateIdentifier` | No | Applied meal-plan rate |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanComponent

**SQL identifier:** `supports.meal_plan_component`

A component of a meal plan with a unit type, quantity, and time period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_identifier` | `TEXT` | PK, FK → `MealPlan.MealPlanIdentifier` | No | Meal plan |
| `component_sequence_number` | `TEXT` | PK | No | Deterministic source order |
| `unit_type` | `TEXT` |  | No | Source-defined unit type |
| `number_of_units` | `NUMERIC` |  | No | Number of included units |
| `time_period` | `TEXT` |  | Yes | Period for the included units |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanComponentRestriction

**SQL identifier:** `supports.meal_plan_component_restriction`

Usage restriction for a meal-plan component.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_identifier` | `TEXT` | PK, FK → `MealPlan.MealPlanIdentifier` | No | Meal plan |
| `component_sequence_number` | `TEXT` | PK | No | Component sequence |
| `restriction_sequence_number` | `TEXT` | PK | No | Restriction sequence |
| `days_of_week` | `TEXT` |  | Yes | Source days-of-week expression |
| `maximum_units_per_period` | `NUMERIC` |  | Yes | Maximum units within the restriction period |
| `restriction_period` | `TEXT` |  | Yes | Period for the maximum |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanRate

**SQL identifier:** `supports.meal_plan_rate`

Meal plan pricing for an academic period and effective date range.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_rate_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the MealPlanRate |
| `meal_plan_identifier` | `TEXT` | FK → `MealPlan.MealPlanIdentifier` | No | Meal plan |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifier of the academic term or period during which the meal-plan rate is effective. |
| `code` | `TEXT` |  | No | Rate code |
| `title` | `TEXT` |  | No | Rate title |
| `description` | `TEXT` |  | Yes | Rate description |
| `start_date` | `DATE` |  | Yes | Rate start date |
| `end_date` | `DATE` |  | Yes | Rate end date |
| `rate_period` | `TEXT` |  | Yes | Rate interval |
| `amount` | `NUMERIC` |  | No | Rate amount |
| `currency_code` | `TEXT` |  | No | ISO 4217 currency |
| `accounting_code` | `TEXT` |  | Yes | Accounting code |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanRequest

**SQL identifier:** `supports.meal_plan_request`

A request by a person for a meal plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_request_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the MealPlanRequest |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person requesting a meal plan |
| `meal_plan_identifier` | `TEXT` | FK → `MealPlan.MealPlanIdentifier` | No | Requested meal plan |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Identifier of the academic term or period to which the meal-plan request applies. |
| `start_date` | `DATE` |  | Yes | Requested start date |
| `end_date` | `DATE` |  | Yes | Requested end date |
| `submitted_date` | `DATE` |  | Yes | Submission date |
| `status` | `TEXT` |  | Yes | Request status |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealPlanResidentialCategory

**SQL identifier:** `supports.meal_plan_residential_category`

Residential categories eligible for a meal plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_plan_identifier` | `TEXT` | PK, FK → `MealPlan.MealPlanIdentifier` | No | Meal plan |
| `student_residential_category_identifier` | `TEXT` | PK, FK → `StudentResidentialCategoryLookup.StudentResidentialCategoryIdentifier` | No | Residential category |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## MealTypeLookup

**SQL identifier:** `supports.meal_type_lookup`

Governed meal type used in meal-plan restrictions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `meal_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the MealType |
| `code` | `TEXT` |  | No | Meal type code |
| `title` | `TEXT` |  | No | Meal type title |
| `description` | `TEXT` |  | Yes | Meal type description |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## PersonChallenge

**SQL identifier:** `supports.person_challenge`

A table containing a history of the responses a learner provided for the challenges intake questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_challenge_identifier` | `TEXT` | PK | No | Unique identifier for a learner challenge item |
| `challenge_identifier` | `TEXT` | FK → `ChallengeLookup.ChallengeIdentifier` | No | Unique identifier for the challenge item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `identified_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Optional date and time the learner challenge, barrier, or support need was identified or reported. This is a domain timestamp and should not be inferred from canonical record creation time when the source provides the actual occurrence time. |
| `input` | `TEXT` |  | Yes | Free-form input to describe the learner challenge |
| `severity` | `TEXT` |  | Yes | Degree of severity that the challenge will impact the learner |
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

## PersonDietIntake

**SQL identifier:** `supports.person_diet_intake`

A table containing a history of the responses a learner provided for the diet intake questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_diet_intake_identifier` | `TEXT` | PK | No | Unique identifier of the diet plan intake |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | The description of the diet plan provided to the patient |
| `type` | `TEXT` |  | Yes | The type of diet |
| `height` | `TEXT` |  | Yes | The recorded client's height |
| `weight` | `TEXT` |  | Yes | The recorded client's weight |
| `body_measurement_type` | `TEXT` |  | Yes | Type of body measurement recorded for tracking progress, including units |
| `body_measurement_value` | `TEXT` |  | Yes | Client recorded body measurements for tracking progress |
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

## PersonDisability

**SQL identifier:** `supports.person_disability`

A table containing a history disabilities an organization has determined a learner to have.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_disability_identifier` | `TEXT` | PK | No | Unique identifier for the person disability item |
| `disability_identifier` | `TEXT` | FK → `DisabilityLookup.DisabilityIdentifier` | No | Unique identifier for a disability item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `disability_status_indicator` | `BOOLEAN` |  | No | An indication of whether a person is classified as disabled under the Americans with Disability Act (ADA) |
| `identifier_ea_indicator` | `BOOLEAN` |  | No | A person having intellectual disability; hearing impairment, including deafness; speech or language impairment; visual impairment, including blindness; serious emotional disturbance (hereafter referred to as emotional disturbance); orthopedic impairment; autism; traumatic brain injury; developmental delay; other health impairment; specific learning disability; deaf-blindness; or multiple disabilities and who, by reason thereof, receive special education and related services under the Individuals with Disabilities Education Act (IdentifierEA) according to an Individualized Education Program (IEP), Individual Family Service Plan (IFSP), or service plan |
| `primary_disability_type` | `TEXT` |  | Yes | The major or overriding disability condition that best describes a person's impairment |
| `disability_condition_type` | `TEXT` |  | Yes | Codes identifying the set of disability conditions |
| `disability_condition_status_type` | `TEXT` |  | Yes | Status of the disability condition type |
| `disability_determination_source_type` | `TEXT` |  | Yes | Codes identifying the set of disability determination sources |
| `section504_status_indicator` | `BOOLEAN` |  | No | Individuals with disabilities who are being provided with related aids and services under Section 504 of the Rehabilitation Act of 1973, as amended |
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

## PersonDisabilityAccommodation

**SQL identifier:** `supports.person_disability_accommodation`

A table containing accommodations needed for specific disabilities that a person has.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_disability_identifier` | `TEXT` | FK → `PersonDisability.PersonDisabilityIdentifier` | No | Unique identifier for the person disability item |
| `person_disability_accommodation_identifier` | `TEXT` | PK | No | Unique identifier for the person disability accommodation item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `accommodations_needed_type` | `TEXT` |  | No | Codes identifying the set of health accommodations |
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

## PersonEducationGoal

**SQL identifier:** `supports.person_education_goal`

An educational goal associated with a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_education_goal_identifier` | `TEXT` | PK | No | Unique identifier for an education goal |
| `goal_identifier` | `TEXT` | FK → `GoalLookup.GoalIdentifier` | No | Unique identifier for a goal item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `degree_selection_assistance_requested_indicator` | `BOOLEAN` |  | Yes | Indicator that the learner requests assistance in selecting a degree program |
| `degree_completion_goal` | `TEXT` |  | Yes | Highest degree level the learner intends to complete |
| `intended_degree_program_enrollment` | `TEXT` |  | Yes | Degree program the learner intended to pursue |
| `degree_pursuit_certainty` | `NUMERIC` |  | Yes | Learner numeric certainty to pursue the intended degree program |
| `occupation_selection_assistance_indicator` | `BOOLEAN` |  | Yes | Indicator that the learner requests assistance in selecting an occupation |
| `occupation_goal` | `TEXT` |  | Yes | Occupation the learner intends to pursue after completion |
| `occupation_certainty` | `NUMERIC` |  | Yes | Learner numeric certainty to pursue the intended occupation |
| `intended_registration_date` | `DATE` |  | Yes | Date the learner intends to register for courses |
| `anticipated_graduation_date` | `DATE` |  | Yes | The date on which the student is or was expected to graduate |
| `intended_registration_load` | `NUMERIC` |  | Yes | Number of hours for which the learner intends to register |
| `anticipated_availability` | `NUMERIC` |  | Yes | Number of hours a learner anticipated being available for class and studies each week |
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

## PersonGoal

**SQL identifier:** `supports.person_goal`

A table containing a history of the learner's goals.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_goal_identifier` | `TEXT` | PK | No | Unique identifier for a learner goal item |
| `goal_identifier` | `TEXT` | FK → `GoalLookup.GoalIdentifier` | Yes | Unique identifier for a goal item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | A statement that describes the desired outcomes |
| `labels` | `TEXT` |  | Yes | The person's labels, categories, or tags for the goal |
| `start_date` | `DATE` |  | Yes | The date on which the goal becomes active |
| `end_date` | `DATE` |  | Yes | The date on which the goal expires or has been achieved |
| `success_criteria` | `TEXT` |  | Yes | One or more statements that describes the criteria used by teachers and students to check for attainment of a goal |
| `current_performance_description` | `TEXT` |  | Yes | Current performance explanation related to the annual goal or short-term objectives |
| `attempts_count` | `INTEGER` |  | Yes | Number of attempts for the goal |
| `percentage_complete` | `NUMERIC` |  | Yes | Percentage of the goal that the person has completed |
| `measurement_type` | `TEXT` |  | Yes | Type of evidence appropriate for assessing achievement of a goal or short-term objective |
| `measurement_description` | `TEXT` |  | Yes | The procedures and/or instruments that will be used to measure achievement of a goal or short-term objective |
| `measurement_schedule` | `TEXT` |  | Yes | Frequency of evaluation of progress toward meeting the goal or short-term objective |
| `status` | `TEXT` |  | Yes | Description of status toward achievement of the annual goal or short-term objectives |
| `occ_code` | `INTEGER` |  | Yes | The 6-digit Standard Occupational Classification (SOC) code or OEWS-specific code for the occupation |
| `occ_title` | `TEXT` |  | Yes | SOC title or OEWS-specific title for the occupation |
| `naics_code` | `TEXT` |  | Yes | North American Industry Classification System (NAICS) code for the given industry |
| `naics_title` | `TEXT` |  | Yes | North American Industry Classification System (NAICS) title for the given industry |
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

## PersonGoalAlignment

**SQL identifier:** `supports.person_goal_alignment`

An alignment linking a person goal to another relevant object.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_goal_alignment_identifier` | `TEXT` | PK | No | Unique identifier for the details of a person's goal, including associations to assessments, strengths, and interests |
| `person_goal_identifier` | `TEXT` | FK → `PersonGoal.PersonGoalIdentifier` | Yes | Unique identifier for the person goal |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the assessment |
| `strength_identifier` | `TEXT` | FK → `StrengthLookup.StrengthIdentifier` | Yes | Unique identifier for strength |
| `interest_identifier` | `TEXT` | FK → `InterestLookup.InterestIdentifier` | Yes | Unique identifier of an interest item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Revision of the Assessment referenced by this record. |

## PersonHousing

**SQL identifier:** `supports.person_housing`

A table containing details about a person's housing status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `person_housing_identifier` | `TEXT` | PK | No | Unique identifier of a housing item |
| `project_provider_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | Yes | The status of the person's housing situation |
| `project_start_date` | `DATE` |  | Yes | Project start date |
| `project_exit_date` | `DATE` |  | Yes | Project exit date |
| `project_type` | `TEXT` |  | Yes | Type of project |
| `project_destination` | `TEXT` |  | Yes | Location a client will stay just after exiting a project for purposes of tracking and outcome measurement |
| `rental_subsidy_type` | `TEXT` |  | Yes | Type of rental subsidy |
| `relationship_to_head_of_household` | `TEXT` |  | Yes | Describes the relationship of the person to a head of household |
| `housing_cost` | `NUMERIC` |  | Yes | The cost in dollars of the person's housing for the given frequency |
| `housing_cost_frequency` | `TEXT` |  | Yes | The frequency with which the housing cost is billed |
| `lease_term_months` | `INTEGER` |  | Yes | The duration of the lease agreement in months |
| `lease_start_date` | `DATE` |  | Yes | Start date of the lease agreement |
| `lease_end_date` | `DATE` |  | Yes | End date of the lease agreement |
| `deposit_amount` | `NUMERIC` |  | Yes | Initial deposit amount required for housing |
| `utilities_included_indicator` | `BOOLEAN` |  | Yes | Boolean flag indicating whether utilities (water, electricity, internet) are included in rent |
| `utility_cost_estimate` | `NUMERIC` |  | Yes | Estimated monthly cost of utilities if not included in rent |
| `housing_financial_aid_support_indicator` | `BOOLEAN` |  | Yes | Boolean flag indicating whether financial aid or scholarships cover housing costs |
| `housing_subsidy_amount` | `NUMERIC` |  | Yes | Amount of financial subsidy applied toward housing costs (e.g. from government or institutional aid) |
| `housing_subsidy_period` | `TEXT` |  | Yes | Time period for which the provided housing subsidy is intended to cover |
| `rent_due_date` | `INTEGER` |  | Yes | Day of the month the rent is due |
| `late_fee_amount` | `NUMERIC` |  | Yes | Amount charged for late rent payments, if applicable |
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

## PersonHousingEnrollment

**SQL identifier:** `supports.person_housing_enrollment`

A table containing a history of learner enrollment for housing opportunities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_housing_enrollment_identifier` | `TEXT` | PK | No | Unique identifier for the person's housing enrollment |
| `person_housing_identifier` | `TEXT` | FK → `PersonHousing.PersonHousingIdentifier` | No | Unique identifier of a housing item |
| `hud_co_c_code` | `TEXT` |  | Yes | Continuum of Care (CoC) Identifier that relates to the client's household data |
| `move_in_date` | `DATE` |  | Yes | Date that a household admitted into a permanent housing project moves into housing |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonPriorHousing

**SQL identifier:** `supports.person_prior_housing`

A table containing a history of housing locations and durations for a learner.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_prior_housing_identifier` | `TEXT` | PK | No | Unique identifier for the person's prior housing |
| `person_housing_identifier` | `TEXT` | FK → `PersonHousing.PersonHousingIdentifier` | No | Unique identifier of a housing item |
| `type_of_residence` | `TEXT` |  | No | The type of residence which is used with other information to identify whether a client appears to meet the criteria for experiencing chronic homelessness at various points of enrollment |
| `length_of_stay_prior_living_situation` | `TEXT` |  | Yes | The length of time the client was residing in the living situation |
| `episode_of_homelessness_start_date` | `DATE` |  | Yes | Date an episode of homelessness began |
| `number_of_times_client_been_homeless_three_years` | `INTEGER` |  | Yes | Including today, count all the different times the client was on the streets, in an emergency shelter, or in a Safe Haven in the last 3 years where there are full breaks in between |
| `total_number_months_homelessness_three_years` | `INTEGER` |  | Yes | Count the cumulative number of months in which a person was on the streets, in an ES, or SH in the last 3 years |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonResourceGuide

**SQL identifier:** `supports.person_resource_guide`

A table containing personalized service or resource guides for users.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_resource_guide_identifier` | `TEXT` | PK | No | A unique identifier for the resource guide |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
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

## PersonResourceGuideResource

**SQL identifier:** `supports.person_resource_guide_resource`

A resource included in a person resource guide.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_resource_guide_resource_identifier` | `TEXT` | PK | No | A unique number for the resource guide details |
| `person_resource_guide_identifier` | `TEXT` | FK → `PersonResourceGuide.PersonResourceGuideIdentifier` | No | A unique identifier for the resource guide |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | No | Unique identifier for the support resource, service, or program |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonScheduledEventResponse

**SQL identifier:** `supports.person_scheduled_event_response`

A table containing a person's response to a scheduled event invitation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_scheduled_event_response_identifier` | `TEXT` | PK | No | Unique identifier for this response to the event |
| `scheduled_event_identifier` | `TEXT` | FK → `ScheduledEvent.ScheduledEventIdentifier` | No | Unique identifier for a scheduled event |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `response` | `TEXT` |  | No | Indicates whether the person is going, maybe going, or is not going to attend the event |
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

## ResourceCategory

**SQL identifier:** `supports.resource_category`

A table containing a list of categories for resources or services.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_category_identifier` | `TEXT` | PK | No | Unique identifier of the resource category |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
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

## ResourceCategoryResourceAssociation

**SQL identifier:** `supports.resource_category_resource_association`

A table associating resources to resource categories.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_category_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the resource to resource category association |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | No | Unique identifier for the support resource, service, or program |
| `resource_category_identifier` | `TEXT` | FK → `ResourceCategory.ResourceCategoryIdentifier` | No | Unique identifier of the resource category |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ResourceLookup

**SQL identifier:** `supports.resource_lookup`

A lookup table for support services and resources available to persons.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_identifier` | `TEXT` | PK | No | Unique identifier for the support resource, service, or program |
| `resource_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `email` | `TEXT` |  | Yes | Email address for the resource |
| `location` | `TEXT` |  | Yes | Location of the resource |
| `language` | `TEXT` |  | Yes | The language of the resource |
| `available_days_of_week` | `TEXT` |  | Yes | Days of the week the resource is available |
| `available_time` | `TEXT` |  | Yes | Hours during the day the resource is available |
| `url` | `TEXT` |  | Yes | URL path for the resource |
| `upvote_count` | `INTEGER` |  | Yes | The count of upvotes on the resource |
| `downvote_count` | `INTEGER` |  | Yes | The count of downvotes on the resource |
| `public_availability_indicator` | `BOOLEAN` |  | No | Indicates the resource is available for campus information |
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

## ResourceRequirement

**SQL identifier:** `supports.resource_requirement`

A table containing a list of requirements to be eligible to use a service or resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `name` | `TEXT` |  | No | Name of the reusable resource requirement. |
| `description` | `TEXT` |  | Yes | Narrative description of the reusable resource requirement. |
| `requirement_type` | `TEXT` |  | Yes | Type or category of the reusable resource requirement. |
| `required_indicator` | `BOOLEAN` |  | No | Indicates whether the requirement is mandatory for the resource. |
| `sequence_number` | `INTEGER` |  | Yes | Sequence in which the resource requirement is evaluated or presented. |
| `effective_start_date` | `DATE` |  | Yes | Date on which the resource requirement becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date on which the resource requirement ceases to be effective. |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_requirement_identifier` | `TEXT` | PK | No | Unique identifier of the resource requirement |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | No | Unique identifier for the support resource, service, or program |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ResourceTag

**SQL identifier:** `supports.resource_tag`

A table containing the tag assigned to a resource for searching and categorizing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_tag_identifier` | `TEXT` | PK | No | Unique identifier for the resource tag |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ResourceTagResourceAssociation

**SQL identifier:** `supports.resource_tag_resource_association`

A table associating resources to resource tags.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `resource_tag_resource_association_identifier` | `TEXT` | PK | No | Unique identifier of the resource to resource tag association |
| `resource_identifier` | `TEXT` | FK → `ResourceLookup.ResourceIdentifier` | No | Unique identifier for the support resource, service, or program |
| `resource_tag_identifier` | `TEXT` | FK → `ResourceTag.ResourceTagIdentifier` | No | Unique identifier for the resource tag |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ScheduledEvent

**SQL identifier:** `supports.scheduled_event`

A table containing the details of an organization's scheduled event.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `scheduled_event_identifier` | `TEXT` | PK | No | Unique identifier for the scheduled event |
| `owner_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | The person that owns this event |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `status` | `TEXT` |  | No | Status of the scheduled event (active, inactive) |
| `type` | `TEXT` |  | No | Type of event: workshop, seminar, study session, etc. |
| `date` | `DATE` |  | No | Date for the scheduled event |
| `start_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Start time for the scheduled event |
| `end_date` | `DATE` |  | No | End date for the first occurrence of this event |
| `end_time` | `TIMESTAMP WITH TIME ZONE` |  | No | End time for the first occurrence of this event |
| `repeat_indicator` | `BOOLEAN` |  | No | Does this event repeat? |
| `repeat_end_type` | `TEXT` |  | Yes | Does this repeating event never end, end after a number of occurrences, or on a date? |
| `repeat_occurrences` | `INTEGER` |  | Yes | Number of occurrences of repeating event if the end type is occurrences |
| `repeat_end_date` | `DATE` |  | Yes | End date of the repeating event if the end type is a date |
| `repeat_frequency` | `TEXT` |  | Yes | Frequency of repetition: daily, weekly, monthly or yearly |
| `repeat_frequency_gap` | `TEXT` |  | Yes | How many "skips" of frequency (e.g. every 3 days) |
| `repeat_frequency_type` | `TEXT` |  | Yes | Frequency is either Ordinal or specific days/month |
| `repeat_frequency_days_of_week` | `TEXT` |  | Yes | Encoded string that represents selected days of the week for repeating events. Format is 'SMTWTFS' where dashes in specific positions mean omission. (e.g. '-M------' means only Monday) |
| `repeat_frequency_days_of_month` | `TEXT` |  | Yes | Comma delimited list of days of the month for monthly repeating events |
| `repeat_frequency_month` | `TEXT` |  | Yes | Comma delimited list of months for yearly repeating events |
| `repeat_frequency_ordinal` | `TEXT` |  | Yes | Ordinal frequency, from list of First, Second, Third, Fourth, Fifth, Last |
| `repeat_frequency_ordinal_day` | `TEXT` |  | Yes | Day determinant from list of Day, Weekday, Weekend Day, or day of month |
| `location` | `TEXT` |  | No | Location of the scheduled event |
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

## StudentResidentialCategoryLookup

**SQL identifier:** `supports.student_residential_category_lookup`

Governed student residential category used for meal-plan eligibility.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_residential_category_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the StudentResidentialCategory |
| `code` | `TEXT` |  | No | Category code |
| `title` | `TEXT` |  | No | Category title |
| `description` | `TEXT` |  | Yes | Category description |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system identifier |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for this record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## ValueLookup

**SQL identifier:** `supports.value_lookup`

A lookup table that describes values a person or organization may hold.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `value_identifier` | `TEXT` | PK | No | Unique identifier for the value item |
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
