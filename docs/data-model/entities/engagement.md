# Entity: Engagement

This page documents every table that belongs to the **Engagement** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 31**

## Table of contents

- [AbilityLookup](#abilitylookup)
- [ActivityCareerAssociation](#activitycareerassociation)
- [ActivityInterestAssociation](#activityinterestassociation)
- [ActivityLookup](#activitylookup)
- [ActivitySkillAssociation](#activityskillassociation)
- [ActivityStrengthAssociation](#activitystrengthassociation)
- [Answer](#answer)
- [ForumMessage](#forummessage)
- [ForumMessageSummary](#forummessagesummary)
- [ForumThread](#forumthread)
- [ForumThreadTag](#forumthreadtag)
- [ForumThreadTagForumThreadAssociation](#forumthreadtagforumthreadassociation)
- [InterestLookup](#interestlookup)
- [LearnerMatchingProfile](#learnermatchingprofile)
- [LearnerMatchingSuggestion](#learnermatchingsuggestion)
- [LearnerMatchingSummary](#learnermatchingsummary)
- [LearnerStreamedEventAggregateMeasure](#learnerstreamedeventaggregatemeasure)
- [PersonRecruitmentAttribution](#personrecruitmentattribution)
- [PersonStreamedEventSession](#personstreamedeventsession)
- [PersonSurveyResponse](#personsurveyresponse)
- [Question](#question)
- [QuestionAnswerAssociation](#questionanswerassociation)
- [StreamedEvent](#streamedevent)
- [StreamedEventAgent](#streamedeventagent)
- [StreamedEventAttempt](#streamedeventattempt)
- [StreamedEventDigitalResource](#streamedeventdigitalresource)
- [StreamedEventForumMessage](#streamedeventforummessage)
- [StreamedEventScore](#streamedeventscore)
- [Survey](#survey)
- [SurveyOffered](#surveyoffered)
- [SurveyQuestionAssociation](#surveyquestionassociation)

---

## AbilityLookup

**SQL identifier:** `engagement.ability_lookup`

A lookup table containing descriptions of abilities persons may be able to demonstrate sourced from authorities that maintain ability repositories.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `ability_identifier` | `TEXT` | PK | No | Unique identifier for an ability description |
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

## ActivityCareerAssociation

**SQL identifier:** `engagement.activity_career_association`

A table associating activities to career pathways, career pathway components, and career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `activity_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the activity to a career pathway, career pathway component, or career pathway job detail |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ActivityInterestAssociation

**SQL identifier:** `engagement.activity_interest_association`

A table associating activities to interests.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `activity_interest_association_identifier` | `TEXT` | PK | No | Unique identifier for the activity to interest association |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `interest_identifier` | `TEXT` | FK → `InterestLookup.InterestIdentifier` | No | Unique identifier of an interest item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ActivityLookup

**SQL identifier:** `engagement.activity_lookup`

A lookup table containing information about activities, including co-curricular activities, community service, professional development, athletics, recreation, and advocacy.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `activity_identifier` | `TEXT` | PK | No | Unique identifier for the activity |
| `activity_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `activity_organization_address_identifier` | `TEXT` | FK → `OrganizationAddress.OrganizationAddressIdentifier` | Yes | Unique identifier for an organization address item |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `type` | `TEXT` |  | Yes | The type of the activity such as co-curricular, community service, professional development, athletics, recreation, publication, grant, or advocacy |
| `recognition_type` | `TEXT` |  | Yes | Specifies if participation may lead to a credential, badge, or course credit |
| `eligibility_criteria` | `TEXT` |  | Yes | Describes any restrictions for eligibility to participate in the activity |
| `frequency` | `TEXT` |  | Yes | Describes how often the activity occurs |
| `location` | `TEXT` |  | Yes | Location of the activity |
| `location_type` | `TEXT` |  | Yes | Indicates if the activity is in-person, online, or hybrid |
| `url` | `TEXT` |  | Yes | A link to a web page for the activity |
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

## ActivitySkillAssociation

**SQL identifier:** `engagement.activity_skill_association`

A table associating activities to skills.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `activity_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the activity to skill association |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ActivityStrengthAssociation

**SQL identifier:** `engagement.activity_strength_association`

A table associating activities to strengths.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `activity_strength_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of activities to strengths |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `strength_identifier` | `TEXT` | FK → `StrengthLookup.StrengthIdentifier` | No | Unique identifier for strength |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## Answer

**SQL identifier:** `engagement.answer`

A table containing common answers to questions asked of learners through surveys and intakes. The list of answers can be associated to one or more questions appearing on surveys and intakes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `answer_identifier` | `TEXT` | PK | No | Unique identifier for the answer item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `answer_text` | `TEXT` |  | No | A description for the record |
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

## ForumMessage

**SQL identifier:** `engagement.forum_message`

A table containing message on a message forum used to support communication and collaboration.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `forum_message_identifier` | `TEXT` | PK | No | Unique identifier for the forum message |
| `forum_thread_identifier` | `TEXT` | FK → `ForumThread.ForumThreadIdentifier` | No | Unique identifier for the forum thread |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `reply_to_forum_message_identifier` | `TEXT` | FK → `ForumMessage.ForumMessageIdentifier` | Yes | Unique identifier for the forum message that this message is in response to |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `body` | `TEXT` |  | No | The content of the forum message |
| `upvote_count` | `INTEGER` |  | Yes | The count of upvotes on the forum message |
| `downvote_count` | `INTEGER` |  | Yes | The count of downvotes on the forum message |
| `document_name` | `TEXT` |  | Yes | Name of the file stored for the person |
| `document_description` | `TEXT` |  | Yes | Description of the file stored for a person |
| `document_size` | `NUMERIC` |  | Yes | Size of the file stored in kilobytes for the person |
| `document_url` | `TEXT` |  | Yes | URL path for the file stored for the person |
| `document_file_name` | `TEXT` |  | Yes | Name of the file stored for the person |
| `status` | `TEXT` |  | No | Status of the forum message (active, inactive) |
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

## ForumMessageSummary

**SQL identifier:** `engagement.forum_message_summary`

A table containing summaries of forum messages from selected content.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `forum_message_summary_identifier` | `TEXT` | PK | No | Unique identifier for the forum message summary |
| `name` | `TEXT` |  | Yes | A name for the record |
| `content_start_date` | `DATE` |  | No | Start date to include Learner matching content in the summary analysis |
| `content_end_date` | `DATE` |  | No | End date to include Learner matching content in the summary analysis |
| `summary_report` | `TEXT` |  | No | Summary report text for the forum messages |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ForumThread

**SQL identifier:** `engagement.forum_thread`

A table containing forum message threads in a message forum.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `forum_thread_identifier` | `TEXT` | PK | No | Unique identifier for the forum thread |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | Status of the forum thread (active, inactive) |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `forum_type` | `TEXT` |  | No | Indicates the use case, product, or feature to which this forum belongs |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_by` | `TEXT` |  | Yes | Person identifier that created the record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ForumThreadTag

**SQL identifier:** `engagement.forum_thread_tag`

A table containing forum thread tags assigned to forum message primarily for searching and categorizing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `forum_thread_tag_identifier` | `TEXT` | PK | No | Unique identifier for the forum thread tag |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ForumThreadTagForumThreadAssociation

**SQL identifier:** `engagement.forum_thread_tag_forum_thread_association`

A table associating forum thread tags to a forum thread.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `forum_thread_tag_forum_thread_association_identifier` | `TEXT` | PK | No | Unique identifier for the forum thread tag to forum thread association |
| `forum_thread_tag_identifier` | `TEXT` | FK → `ForumThreadTag.ForumThreadTagIdentifier` | No | Unique identifier for the forum thread tag |
| `forum_thread_identifier` | `TEXT` | FK → `ForumThread.ForumThreadIdentifier` | No | Unique identifier for the forum thread |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## InterestLookup

**SQL identifier:** `engagement.interest_lookup`

A lookup table containing descriptions of interests that learners may have.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `interest_identifier` | `TEXT` | PK | No | Unique identifier of an interest item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | Human-readable name of the interest classification. |
| `description` | `TEXT` |  | Yes | Detailed description of the interest classification. |
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

## LearnerMatchingProfile

**SQL identifier:** `engagement.learner_matching_profile`

A table containing information about person participation and information sharing for matching with staff, mentors, etc.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_matching_profile_identifier` | `TEXT` | PK | No | A unique identifier for a learner's matching profile record |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `learner_matching_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person has opted in to participate in Learner matching |
| `person_activity_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_demographics_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_education_goal_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_goal_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_challenge_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_experience_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_resource_participation_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_specialty_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_non_identifiable_demographics_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_recognition_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_skill_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
| `person_strength_share_opt_in_indicator` | `BOOLEAN` |  | No | Indicates whether the person opts in to share this information to their profile |
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

## LearnerMatchingSuggestion

**SQL identifier:** `engagement.learner_matching_suggestion`

A table containing the suggested matches and student disposition on the match.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_matching_suggestion_identifier` | `TEXT` | PK | No | A unique identifier for a specific match |
| `learner_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `matched_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique number or alphanumeric code assigned to a person |
| `matched_activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | Yes | Unique identifier for the activity |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `match_suggestion_status` | `TEXT` |  | No | Status of the suggested match (e.g. Open, Accepted, Rejected) |
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

## LearnerMatchingSummary

**SQL identifier:** `engagement.learner_matching_summary`

A table containing summaries of student matching results for selected content.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_matching_summary_identifier` | `TEXT` | PK | No | Unique identifier of the learner matching summary |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `content_start_date` | `DATE` |  | No | Start date to include Learner matching content in the summary analysis |
| `content_end_date` | `DATE` |  | No | End date to include Learner matching content in the summary analysis |
| `summary_report` | `TEXT` |  | No | Summary report text for the Learner matching period |
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

## LearnerStreamedEventAggregateMeasure

**SQL identifier:** `engagement.learner_streamed_event_aggregate_measure`

An aggregated learner activity or progress measure over a digital resource and measurement interval, optionally derived from a streamed event. The measure is a durable fact; protocol-level collection/envelope structures are not canonical GUIDE concepts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique number or alphanumeric code assigned to a person |
| `learner_streamed_event_aggregate_measure_identifier` | `TEXT` | PK | No | Unique identifier for the aggregate measure |
| `streamed_event_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the digital resource |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `metric_value` | `NUMERIC` |  | No | Observed aggregate value for the metric over the measurement interval. |
| `max_metric_value` | `NUMERIC` |  | Yes | Optional maximum or total possible value used to interpret the aggregate metric. |
| `metric` | `TEXT` |  | No | Metric represented by the aggregate value, such as minutes on task, units completed, skills mastered, or words read. |
| `started_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the measurement interval began. |
| `ended_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the measurement interval ended. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `source_streamed_event_identifier` | `TEXT` | FK → `StreamedEvent.StreamedEventIdentifier` | Yes | Optional streamed event from which this aggregate measure was derived or received. |

## PersonRecruitmentAttribution

**SQL identifier:** `engagement.person_recruitment_attribution`

A table that stores recruitment, source, campaign, referral, UTM, event-source, territory, or funnel-attribution facts associated with a person or prospective learner. This table captures marketing and recruitment influence context that is broader than LearnerApplication.ApplicationSourceIdentifier.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped person/prospect identifier to whom the attribution belongs. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for multiple attribution rows for the person. |
| `learner_application_identifier` | `TEXT` | FK → `LearnerApplication.LearnerApplicationIdentifier` | Yes | Optional learner application identifier when the attribution is specifically application-contextual. |
| `attribution_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the type of recruitment attribution. |
| `attribution_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time associated with the source attribution. |
| `source_name` | `TEXT` |  | Yes | Source-facing name or description of the recruitment source. |
| `source_code` | `TEXT` |  | Yes | Source code, alias, or campaign/source code assigned by the recruitment system. |
| `source_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the broad source type. |
| `source_segment` | `TEXT` |  | Yes | Source segment value associated with the attribution. |
| `source_index_weight` | `NUMERIC` |  | Yes | Source index or ranking weight supplied by the source system. |
| `first_source_indicator` | `BOOLEAN` |  | Yes | Indicates whether this row represents the first known recruitment source. |
| `calculated_indicator` | `BOOLEAN` |  | Yes | Indicates whether the attribution value was calculated or derived by the source system/process. |
| `funnel_stage_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the recruitment funnel stage. |
| `territory_name` | `TEXT` |  | Yes | Recruitment territory name or label associated with the person/prospect. |
| `campaign_name` | `TEXT` |  | Yes | Campaign name associated with the attribution where available. |
| `utm_source` | `TEXT` |  | Yes | UTM source value captured from web attribution. |
| `utm_medium` | `TEXT` |  | Yes | UTM medium value captured from web attribution. |
| `utm_campaign` | `TEXT` |  | Yes | UTM campaign value captured from web attribution. |
| `utm_content` | `TEXT` |  | Yes | UTM content value captured from web attribution. |
| `event_name` | `TEXT` |  | Yes | Event source name associated with the attribution where available. |
| `event_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Event and time source date associated with the attribution where available. |
| `source_raw_attribution_type` | `TEXT` |  | Yes | Source-system attribution type value preserved when canonical mapping is lossy. |
| `source_raw_source_type` | `TEXT` |  | Yes | Source-system source type value preserved when canonical mapping is lossy. |
| `source_raw_source_segment` | `TEXT` |  | Yes | Source-system source segment value preserved as supplied. |
| `source_raw_funnel_stage` | `TEXT` |  | Yes | Source-system funnel stage value preserved when canonical mapping is lossy. |
| `source_raw_territory` | `TEXT` |  | Yes | Source-system territory value preserved as supplied. |
| `source_raw_campaign` | `TEXT` |  | Yes | Source-system campaign value preserved as supplied. |
| `source_raw_event_source` | `TEXT` |  | Yes | Source-system event-source value preserved as supplied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system from which the attribution row originated or can be reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the attribution row. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonStreamedEventSession

**SQL identifier:** `engagement.person_streamed_event_session`

A web application user session related to a streamed event.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_streamed_event_session_identifier` | `TEXT` | PK | No | Unique identifier for the session |
| `parent_session_identifier` | `TEXT` | FK → `PersonStreamedEventSession.PersonStreamedEventSessionIdentifier` | Yes | Unique identifier for the parent session, such as the platform session in the case of an LTI tool session |
| `client_agent_identifier` | `TEXT` | FK → `StreamedEventAgent.StreamedEventAgentIdentifier` | No | Unique identifier for the client agent software application hosting the session |
| `started_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Session was commenced. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `ended_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Session was completed or terminated. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `duration` | `TEXT` |  | Yes | A time interval that represents the time taken to complete the Session. If a duration is specified the value MUST conform to the ISO 8601 duration format. |
| `lti_message_parameters` | `TEXT` |  | Yes | A map of LTI-specified message parameters that provide platform-related contextual information. LTI message parameters of whatever type (e.g. required, recommended, optional, custom and extension) MAY be referenced. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonSurveyResponse

**SQL identifier:** `engagement.person_survey_response`

A table containing a person's responses to the questions of an offered survey.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique number or alphanumeric code assigned to a person |
| `person_survey_response_identifier` | `TEXT` | PK | No | Person's response identifier |
| `survey_offered_identifier` | `TEXT` | FK → `SurveyOffered.SurveyOfferedIdentifier` | No | Identifier of survey offered they participated in |
| `question_identifier` | `TEXT` | FK → `Question.QuestionIdentifier` | No | Unique identifier for a survey question |
| `answer_identifier` | `TEXT` | FK → `Answer.AnswerIdentifier` | No | Unique identifier for the answer selection |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `response_date` | `DATE` |  | No | Date the survey response was recorded |
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

## Question

**SQL identifier:** `engagement.question`

A table containing a list of questions that may be assigned to a survey question.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `question_identifier` | `TEXT` | PK | No | Unique identifier for a survey question |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `question_text` | `TEXT` |  | No | A description for the record |
| `type` | `TEXT` |  | Yes | Type of survey question item |
| `basis` | `TEXT` |  | Yes | Source composition for the question (e.g. Learner, Template, Staff, AI, Other) |
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

## QuestionAnswerAssociation

**SQL identifier:** `engagement.question_answer_association`

A table associating answers or answer choices to questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `question_answer_association_identifier` | `TEXT` | PK | No | Unique identifier for the question to answer association |
| `question_identifier` | `TEXT` | FK → `Question.QuestionIdentifier` | No | Unique identifier for a survey question |
| `answer_identifier` | `TEXT` | FK → `Answer.AnswerIdentifier` | No | Unique identifier for the answer item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StreamedEvent

**SQL identifier:** `engagement.streamed_event`

A table to normalize streamed software usage events representing an actor, action, and object.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_identifier` | `TEXT` | PK | No | Unique identifier for the event |
| `actor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `object_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the object digital resource |
| `ed_app_agent_identifier` | `TEXT` | FK → `StreamedEventAgent.StreamedEventAgentIdentifier` | Yes | Unique identifier for the ed app agent |
| `generated_attempt_identifier` | `TEXT` | FK → `StreamedEventAttempt.StreamedEventAttemptIdentifier` | Yes | Unique identifier for the generated attempt |
| `generated_score_identifier` | `TEXT` | FK → `StreamedEventScore.StreamedEventScoreIdentifier` | Yes | Unique identifier for the generated score |
| `target_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the target digital resource |
| `referrer_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the referrer digital resource |
| `referrer_agent_identifier` | `TEXT` | FK → `StreamedEventAgent.StreamedEventAgentIdentifier` | Yes | Unique identifier for the referrer agent |
| `role_identifier` | `TEXT` | FK → `RoleLookup.RoleIdentifier` | Yes | Unique identifier for the role |
| `session_identifier` | `TEXT` | FK → `PersonStreamedEventSession.PersonStreamedEventSessionIdentifier` | Yes | Unique Identifier for the session |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `event_type` | `TEXT` |  | Yes | The type or category of event |
| `action` | `TEXT` |  | No | The action or predicate that binds the actor or subject to the object |
| `event_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that indicates when the Event occurred. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `extensions` | `TEXT` |  | Yes | A map of additional attributes not defined by the model MAY be specified for a more concise representation of the Event |
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

## StreamedEventAgent

**SQL identifier:** `engagement.streamed_event_agent`

A table representing a software application by which a streamed event action took place.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_agent_identifier` | `TEXT` | PK | No | Unique identifier for the agent, software application, technology, or tool |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `host` | `TEXT` |  | Yes | String value that identifies the host of this Software Application. This property can be used to indicate the back-end service or domain hosting a front-end web application. |
| `ip_address` | `TEXT` |  | Yes | String value that, if present, can indicate the IPv4 or IPv6 address of this Software Application. This property can be used to indicate the user agent (browser) running a front-end web application. |
| `user_agent` | `TEXT` |  | Yes | String with a value that describes the properties of the user agent hosting this Software Application. This field can be used to carry the user agent string reported by the browser running a front-end web application. |
| `version` | `TEXT` |  | Yes | An optional string value that designates the current form or version of this Software Application |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StreamedEventAttempt

**SQL identifier:** `engagement.streamed_event_attempt`

A table containing data pertaining to a learner's interaction to complete an assigned digital resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_attempt_identifier` | `TEXT` | PK | No | Unique identifier for the attempt |
| `assignee_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_assessment_attempt_identifier` | `TEXT` | FK → `LearnerAssessmentAttempt.LearnerAssessmentAttemptIdentifier` | Yes | Unique identifier for the learner's assessment attempt or submission |
| `assignable_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | No | Unique identifier for the digital resource assigned |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `attempt_count` | `INTEGER` |  | Yes | The total number of attempts inclusive of the current attempt that have been registered against the assigned digital resource |
| `started_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Attempt was commenced. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `ended_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Attempt was completed or terminated. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `duration` | `TEXT` |  | Yes | A time interval that represents the time taken to complete the Attempt. If a duration is specified the value MUST conform to the ISO 8601 duration format. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StreamedEventDigitalResource

**SQL identifier:** `engagement.streamed_event_digital_resource`

A digital learning material, such as assignments, chapters, documents, links, media, or forums, which was referred to by a streamed event.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_digital_resource_identifier` | `TEXT` | PK | No | Unique identifier for the digital resource |
| `parent_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the parent of the digital resource |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | Yes | Unique identifier of the learning resource |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier of the assessment or assignment |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `type` | `TEXT` |  | Yes | The subtype of the digital resource |
| `media_type` | `TEXT` |  | Yes | A string value drawn from the list of IANA approved media types and subtypes that identifies the file format of the resource |
| `keywords` | `TEXT` |  | Yes | An ordered collection of one or more string values that represent tags or labels used to identify the resource |
| `date_published` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that provides the publication date of the resource. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `version` | `TEXT` |  | Yes | A string value that designates the current form or version of the resource |
| `date_to_activate` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource was activated. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_show` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource should be shown or made available to learners. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_start_on` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource can be started. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_submit` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource is to be submitted for evaluation. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `max_attempts` | `INTEGER` |  | Yes | A non-negative integer that designates the number of permitted attempts |
| `max_submits` | `INTEGER` |  | Yes | A non-negative integer that designates the number of permitted submissions |
| `max_score` | `NUMERIC` |  | Yes | A number with a fractional part denoted by a decimal separator that designates the maximum score permitted |
| `frame_index` | `INTEGER` |  | Yes | A non-negative integer that represents the position of the Frame |
| `duration` | `TEXT` |  | Yes | An optional time interval that represents the total time required to view and/or listen to the MediaObject at normal speed. If a duration is specified the value MUST conform to the ISO 8601 duration format. |
| `current_time_x` | `TEXT` |  | Yes | A time interval or duration that represents the current playback position measured from the beginning of an audio object or video object. If a currentTime is specified the value MUST conform to the ISO 8601 duration format. |
| `lti_message_type` | `TEXT` |  | Yes | If present, the string value MUST be set to the term name of the LTI message type used to gain access to this LTI resource link (including but not limited to, LtiResourceLinkRequest or LtiDeepLinkingRequest, LtiDeepLinkingResponse) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | Yes | Revision of the LearningResource referenced by this record. |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Revision of the Assessment referenced by this record. |

## StreamedEventForumMessage

**SQL identifier:** `engagement.streamed_event_forum_message`

A table representing a digital written communication sent to a recipient within the thread of a forum which was referred to in a streamed event.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_forum_message_identifier` | `TEXT` | PK | No | Unique identifier for the forum message |
| `forum_message_identifier` | `TEXT` | FK → `ForumMessage.ForumMessageIdentifier` | Yes | Unique identifier for the forum message |
| `forum_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the forum digital resource |
| `thread_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the thread digital resource |
| `reply_to_forum_message_identifier` | `TEXT` | FK → `ForumMessage.ForumMessageIdentifier` | Yes | Unique identifier for the forum message in which this is a reply to |
| `attachments_parent_digital_resource_identifier` | `TEXT` | FK → `StreamedEventDigitalResource.StreamedEventDigitalResourceIdentifier` | Yes | Unique identifier for the attachments parent digital resource |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | A unique number or alphanumeric code assigned to a person |
| `name` | `TEXT` |  | Yes | A name for the record |
| `body` | `TEXT` |  | Yes | A string value comprising a plain-text rendering of the body content of the Message |
| `date_published` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that provides the publication date of the resource. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `version` | `TEXT` |  | Yes | A string value that designates the current form or version of the resource |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StreamedEventScore

**SQL identifier:** `engagement.streamed_event_score`

A table representing a numeric grade, result, or score awarded for a particular assessment or assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `streamed_event_score_identifier` | `TEXT` | PK | No | Unique identifier for the streamed event score |
| `streamed_event_attempt_identifier` | `TEXT` | FK → `StreamedEventAttempt.StreamedEventAttemptIdentifier` | Yes | Unique identifier for the streamed event attempt |
| `scored_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier for the person who scored the attempt |
| `scored_by_agent_identifier` | `TEXT` | FK → `StreamedEventAgent.StreamedEventAgentIdentifier` | Yes | Unique identifier for the agent that scored the attempt |
| `learner_assessment_result_identifier` | `TEXT` | FK → `LearnerAssessmentResult.LearnerAssessmentResultIdentifier` | Yes | Unique identifier for the assessment result |
| `score_type` | `TEXT` |  | Yes | Indicates whether the score is raw/unadjusted or adjusted/scaled |
| `max_score` | `NUMERIC` |  | Yes | A number with a fractional part denoted by a decimal separator that designates the maximum score permitted |
| `score_given` | `NUMERIC` |  | Yes | A number with a fractional part denoted by a decimal separator that designates the actual score awarded |
| `comment` | `TEXT` |  | Yes | Plain text feedback provided by the scorer |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## Survey

**SQL identifier:** `engagement.survey`

A table containing list of surveys available to send to persons.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `survey_identifier` | `TEXT` | PK | No | Unique identifier of the survey item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `category` | `TEXT` |  | Yes | Category of the survey |
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

## SurveyOffered

**SQL identifier:** `engagement.survey_offered`

A table identifying instances in which a survey was offered to persons.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `survey_offered_identifier` | `TEXT` | PK | No | Identifier of survey offered they participated in |
| `survey_identifier` | `TEXT` | FK → `Survey.SurveyIdentifier` | No | Unique identifier of the survey item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `start_date` | `DATE` |  | No | Date when survey starts (optional) |
| `end_date` | `DATE` |  | Yes | Date the survey closes |
| `min_responses` | `INTEGER` |  | Yes | The minimum number of responses accepted for the survey |
| `max_responses` | `INTEGER` |  | Yes | The maximum number of responses accepted for the survey |
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

## SurveyQuestionAssociation

**SQL identifier:** `engagement.survey_question_association`

A table associating a survey with questions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `survey_question_association_identifier` | `TEXT` | PK | No | Unique identifier for the survey to question association |
| `survey_identifier` | `TEXT` | FK → `Survey.SurveyIdentifier` | No | Unique identifier of the survey item |
| `question_identifier` | `TEXT` | FK → `Question.QuestionIdentifier` | No | Unique identifier for a survey question |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
