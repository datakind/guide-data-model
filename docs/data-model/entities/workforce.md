# Entity: Workforce

This page documents every table that belongs to the **Workforce** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 33**

## Table of contents

- [CareerPathway](#careerpathway)
- [CareerPathwayComponent](#careerpathwaycomponent)
- [CareerPathwayJob](#careerpathwayjob)
- [CareerPathwaySkillAssociation](#careerpathwayskillassociation)
- [CareerPathwayStrengthAssociation](#careerpathwaystrengthassociation)
- [CareerProjectedIncome](#careerprojectedincome)
- [CourseOccupationElementAssociation](#courseoccupationelementassociation)
- [EducationComment](#educationcomment)
- [IndustryNeed](#industryneed)
- [IndustryNeedCompetencyAssociation](#industryneedcompetencyassociation)
- [IndustryNeedInterestAssociation](#industryneedinterestassociation)
- [IndustryNeedLearningResourceAssociation](#industryneedlearningresourceassociation)
- [IndustryNeedSkillAssociation](#industryneedskillassociation)
- [IndustryNeedTag](#industryneedtag)
- [IndustryNeedTagIndustryNeedAssociation](#industryneedtagindustryneedassociation)
- [InterestCareerAssociation](#interestcareerassociation)
- [JobPosting](#jobposting)
- [JobPostingCareerAssociation](#jobpostingcareerassociation)
- [JobPostingCompetencyAssociation](#jobpostingcompetencyassociation)
- [JobPostingCredentialAssociation](#jobpostingcredentialassociation)
- [JobPostingSkillAssociation](#jobpostingskillassociation)
- [LearnerCareerPlan](#learnercareerplan)
- [LearnerCareerPlanJobPostingDetails](#learnercareerplanjobpostingdetails)
- [LearnerCareerPlanStep](#learnercareerplanstep)
- [LearnerResume](#learnerresume)
- [LearnerResumeComment](#learnerresumecomment)
- [LearnerResumeDetails](#learnerresumedetails)
- [OccupationElementLookup](#occupationelementlookup)
- [OrganizationCareerAssociation](#organizationcareerassociation)
- [PersonAlum](#personalum)
- [PersonEmployment](#personemployment)
- [ProgramOfStudyOccupationCodes](#programofstudyoccupationcodes)
- [StandardizedTestCareerAssociation](#standardizedtestcareerassociation)

---

## CareerPathway

**SQL identifier:** `workforce.career_pathway`

Tenant-scoped definition of a structured education-to-workforce route composed of pathway-specific components and leading toward one or more goals such as credentials, occupations, jobs, or other career outcomes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_pathway_identifier` | `TEXT` | PK | No | Unique identifier for the career pathway. |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `destination_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Optional pathway component that represents the principal destination or goal of this pathway. |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
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

## CareerPathwayComponent

**SQL identifier:** `workforce.career_pathway_component`

A pathway-specific node or milestone within one CareerPathway. Components provide ordering, hierarchy, pathway-specific description, and type context, and may proxy for jobs, credentials, courses, competencies, assessments, work experiences, activities, or other objectives.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_pathway_component_identifier` | `TEXT` | PK | No | Unique identifier for a pathway-specific component or node. |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | No | Career pathway to which this component belongs. |
| `preceded_by_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Optional component that immediately or logically precedes this component within the same pathway. |
| `parent_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Optional parent component when pathway components are organized hierarchically. |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `component_type` | `TEXT` |  | No | Semantic category of the pathway component, such as Job, Occupation, Credential, Course, Competency, Assessment, WorkExperience, Activity, or Other. |
| `expected_duration` | `TEXT` |  | Yes | Expected duration associated with completing or traversing this pathway component. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CareerPathwayJob

**SQL identifier:** `workforce.career_pathway_job`

Optional one-to-one job or occupation detail for a CareerPathwayComponent. Occupational and industry codes describe the job/occupation represented by the component; pathway membership, ordering, name, and description remain on CareerPathwayComponent.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_pathway_component_identifier` | `TEXT` | PK, FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | No | Pathway component for which this row provides job or occupation-specific detail. |
| `occupation_code` | `TEXT` |  | Yes | Occupation code associated with the job or occupation represented by this component. |
| `occupation_code_system` | `TEXT` |  | Yes | Code system or namespace governing OccupationCode, such as SOC, O*NET-SOC, or another occupational taxonomy. |
| `occupation_title` | `TEXT` |  | Yes | Human-readable title associated with OccupationCode. |
| `industry_code` | `TEXT` |  | Yes | Industry code associated with this job or occupation component. |
| `industry_code_system` | `TEXT` |  | Yes | Code system or namespace governing IndustryCode, such as NAICS or another industry taxonomy. |
| `industry_title` | `TEXT` |  | Yes | Human-readable title associated with IndustryCode. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CareerPathwaySkillAssociation

**SQL identifier:** `workforce.career_pathway_skill_association`

Association of a skill and proficiency expectations with a specific CareerPathwayComponent.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_pathway_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the career pathway to skill association |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | No | Unique identifier for the career pathway component |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `required_proficiency_level` | `TEXT` |  | Yes | The minimum required proficiency level of the skill for the career pathway |
| `preferred_proficiency_level` | `TEXT` |  | Yes | The preferred proficiency level of the skill for the career pathway |
| `proficiency_acquisition_difficulty` | `TEXT` |  | Yes | A rating or score representing the difficulty of acquiring the skill for the career pathway |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CareerPathwayStrengthAssociation

**SQL identifier:** `workforce.career_pathway_strength_association`

Association of a strength with a CareerPathway as a whole.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_pathway_strength_association_identifier` | `TEXT` | PK | No | Unique identifier for the association between the career pathway and the strength |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | No | Identifier for the career pathway |
| `strength_identifier` | `TEXT` | FK → `StrengthLookup.StrengthIdentifier` | No | Unique identifier for strength |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CareerProjectedIncome

**SQL identifier:** `workforce.career_projected_income`

A table containing projections of income and job demand for career pathways and jobs over time and geographic regions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `career_projected_income_identifier` | `TEXT` | PK | No | Unique identifier for the career projected income |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway to which these projections apply when they describe the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Specific pathway component, typically a job or occupation component, to which these projections apply. |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `projection_date` | `DATE` |  | Yes | Date that the income projections were made |
| `minimum_salary` | `NUMERIC` |  | Yes | Minimum salary in the range for this career pathway or job |
| `maximum_salary` | `NUMERIC` |  | Yes | Maximum salary in the range for this career pathway or job |
| `median_salary` | `NUMERIC` |  | Yes | Median annual salary for this career pathway or job |
| `entry_level_salary` | `NUMERIC` |  | Yes | Expected salary for someone just starting in the career |
| `five_years_experience_salary` | `NUMERIC` |  | Yes | Estimated yearly earnings after five years in the career |
| `ten_years_experience_salary` | `NUMERIC` |  | Yes | Estimated yearly earnings after ten years in the career |
| `fiften_years_experience_salary` | `NUMERIC` |  | Yes | Estimated yearly earnings after fifteen years in the career |
| `twenty_years_experience_salary` | `NUMERIC` |  | Yes | Estimated yearly earnings after twenty years in the career |
| `geographic_region` | `TEXT` |  | Yes | Region where the salary data applies (National, State, Metro Area) |
| `industry_growth_rate` | `NUMERIC` |  | Yes | Expected job growth rate (%) in this industry |
| `job_market_demand` | `TEXT` |  | Yes | Indicator of demand for this career (High, Medium, Low) |
| `regional_salary_variation` | `NUMERIC` |  | Yes | Adjustments based on job location (dollars) |
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

## CourseOccupationElementAssociation

**SQL identifier:** `workforce.course_occupation_element_association`

A table associating courses to occupation defined skills, abilities, and knowledge. A course may have multiple associations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_occupation_element_identifier` | `TEXT` | PK | No | Unique identifier for the association between a course and a skill, knowledge, or ability as defined by ONET |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `occupation_element_identifier` | `TEXT` | FK → `OccupationElementLookup.OccupationElementIdentifier` | No | Unique identifier for the skill, knowledge, or ability as defined by ONET |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the association between a course and a skill, knowledge, or ability as defined by ONET |
| `course_occupation_element_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## EducationComment

**SQL identifier:** `workforce.education_comment`

A table containing comments left on supported education resources such as programs of study, courses, classes, assessments, learner plans, competencies, or learning resources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `education_comment_identifier` | `TEXT` | PK | No | Unique identifier for the comment on the education resource |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `parent_education_comment_identifier` | `TEXT` | FK → `EducationComment.EducationCommentIdentifier` | Yes | Unique identifier for the parent comment on the education resource |
| `object_identifier` | `TEXT` | FK → `ObjectLookup.ObjectIdentifier` | No | Unique identifier for the object to which this comment corresponds |
| `object_row_identifier` | `TEXT` |  | Yes | Unique identifier for the object or database table row |
| `revision_identifier` | `TEXT` |  | Yes | Unique identifier for the revision to the object or database row |
| `hidden_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that hid the record |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `comment` | `TEXT` |  | No | The text of the comment |
| `hidden_indicator` | `BOOLEAN` |  | No | Indicates whether the comment is hidden from public view |
| `hidden_date` | `DATE` |  | Yes | Date record was hidden |
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

## IndustryNeed

**SQL identifier:** `workforce.industry_need`

A table containing information about workforce or industry needs.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_identifier` | `TEXT` | PK | No | Unique identifier for the industry need |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `priority` | `TEXT` |  | Yes | Relative indicator of the demand for this industry need |
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

## IndustryNeedCompetencyAssociation

**SQL identifier:** `workforce.industry_need_competency_association`

A table associating an industry need to a competency.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_competency_association_identifier` | `TEXT` | PK | No | Unique identifier for the industry need to competency association |
| `industry_need_identifier` | `TEXT` | FK → `IndustryNeed.IndustryNeedIdentifier` | No | Unique identifier for the industry need |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## IndustryNeedInterestAssociation

**SQL identifier:** `workforce.industry_need_interest_association`

A table associating an industry need to an interest.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_interest_association_identifier` | `TEXT` | PK | No | Unique identifier for the industry need to interest association |
| `industry_need_identifier` | `TEXT` | FK → `IndustryNeed.IndustryNeedIdentifier` | No | Unique identifier for the industry need |
| `interest_identifier` | `TEXT` | FK → `InterestLookup.InterestIdentifier` | No | Unique identifier of an interest item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## IndustryNeedLearningResourceAssociation

**SQL identifier:** `workforce.industry_need_learning_resource_association`

A table associating an industry need to a learning resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_learning_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the industry need to learning resource association |
| `industry_need_identifier` | `TEXT` | FK → `IndustryNeed.IndustryNeedIdentifier` | No | Unique identifier for the industry need |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## IndustryNeedSkillAssociation

**SQL identifier:** `workforce.industry_need_skill_association`

A table associating an industry need to a skill.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the industry need to skill association |
| `industry_need_identifier` | `TEXT` | FK → `IndustryNeed.IndustryNeedIdentifier` | No | Unique identifier for the industry need |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## IndustryNeedTag

**SQL identifier:** `workforce.industry_need_tag`

A table containing the tag assigned to an industry need for searching and categorizing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_tag_identifier` | `TEXT` | PK | No | Unique identifier for the industry need tag |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## IndustryNeedTagIndustryNeedAssociation

**SQL identifier:** `workforce.industry_need_tag_industry_need_association`

A table associating industry need tags to an industry need.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `industry_need_tag_industry_need_association_identifier` | `TEXT` | PK | No | Unique identifier for the industry need to industry need tag association |
| `industry_need_identifier` | `TEXT` | FK → `IndustryNeed.IndustryNeedIdentifier` | No | Unique identifier for the industry need |
| `industry_need_tag_identifier` | `TEXT` | FK → `IndustryNeedTag.IndustryNeedTagIdentifier` | No | Unique identifier for the industry need tag |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## InterestCareerAssociation

**SQL identifier:** `workforce.interest_career_association`

A table associating interests to career pathways, career pathway components, and career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `interest_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the interest to a career pathway, career pathway component, or career pathway job |
| `interest_identifier` | `TEXT` | FK → `InterestLookup.InterestIdentifier` | No | Unique identifier of an interest item |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## JobPosting

**SQL identifier:** `workforce.job_posting`

A table containing a job posting or job opening.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `job_posting_identifier` | `TEXT` | PK | No | Unique identifier of the job posting |
| `job_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Unique identifier for the organization with the job opening |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `job_title` | `TEXT` |  | Yes | The title of the job |
| `job_description` | `TEXT` |  | Yes | The description of the job posting |
| `work_hours` | `TEXT` |  | Yes | Typical working hours for this job; e.g. "1st shift", "night shift", "8am-5pm" |
| `job_qualifications` | `TEXT` |  | Yes | Summary description of the ideal candidate's qualifications for a position |
| `job_posting_language` | `TEXT` |  | Yes | The language of the content of the job posting |
| `job_location_types` | `TEXT` |  | Yes | A description of the job location (e.g. TELECOMMUTE for telecommute jobs) |
| `physical_requirements` | `TEXT` |  | Yes | The physical requirements of the job |
| `pay_minimum` | `NUMERIC` |  | Yes | The minimum pay for the job |
| `pay_maximum` | `NUMERIC` |  | Yes | The maximum pay for the job |
| `pay_average` | `NUMERIC` |  | Yes | The average pay for the job |
| `incentive_compensation` | `TEXT` |  | Yes | Description of bonus and commission compensation aspects of the job |
| `citizenship_requirements` | `TEXT` |  | Yes | Required country of the applicant's citizenship |
| `security_clearance_requirements` | `TEXT` |  | Yes | Description of any security clearance requirements |
| `travel_requirements` | `TEXT` |  | Yes | Information about any required travel, systematic or occasional |
| `work_languages` | `TEXT` |  | Yes | Information on the work languages used for the job |
| `job_terms` | `TEXT` |  | Yes | Type of employment term (e.g. "regular", "temporary", "seasonal"); select from an existing enumeration of such types. Note(s): Use a value selected from a controlled vocabulary of employment term types; select from an existing enumeration of such types. |
| `job_posted_date` | `DATE` |  | Yes | Date on which the position was created |
| `credential_requirements` | `TEXT` |  | Yes | Description of the required credential needed for the position or occupation |
| `education_requirements` | `TEXT` |  | Yes | Description of the required education or training needed for the position or occupation |
| `experience_requirements` | `TEXT` |  | Yes | Description of the required experience needed for the position or occupation |
| `responsibilities` | `TEXT` |  | Yes | Key work tasks or activities over which this position exercises some degree of authority, control or leadership |
| `risk_exposures` | `TEXT` |  | Yes | Description of any exposure to risks associated with the job including exposure to extreme noise or temperature, dust/particle matter, radiation, chemicals, airborne communicable diseases and bloodborne pathogens |
| `technologies` | `TEXT` |  | Yes | Tool, application or other form of technology that requires knowledge, skill and ability to use effectively in executing the tasks and responsibilities of the job; select from an existing enumeration of such types |
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

## JobPostingCareerAssociation

**SQL identifier:** `workforce.job_posting_career_association`

A table associating job postings to career pathways, career pathway components, and career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `job_posting_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the job posting to a career pathway, career pathway component, or career pathway job |
| `job_posting_identifier` | `TEXT` | FK → `JobPosting.JobPostingIdentifier` | No | Unique identifier of the job posting |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## JobPostingCompetencyAssociation

**SQL identifier:** `workforce.job_posting_competency_association`

A table associating job postings to competencies.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `job_posting_competency_association_identifier` | `TEXT` | PK | No | Unique identifier for the job posting to competency association |
| `job_posting_identifier` | `TEXT` | FK → `JobPosting.JobPostingIdentifier` | No | Unique identifier of the job posting |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `required_proficiency_level` | `TEXT` |  | Yes | A minimum level of proficiency for a competency associated with a position, role, course, or other item. The proficiency level is expressed as a score, a point scale, or a mark among range of values. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## JobPostingCredentialAssociation

**SQL identifier:** `workforce.job_posting_credential_association`

A table associating job postings to credentials.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `job_posting_credential_association_identifier` | `TEXT` | PK | No | Unique identifier for the job posting to credential association |
| `job_posting_identifier` | `TEXT` | FK → `JobPosting.JobPostingIdentifier` | No | Unique identifier of the job posting |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## JobPostingSkillAssociation

**SQL identifier:** `workforce.job_posting_skill_association`

A table associating job postings to skills.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `job_posting_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the job posting to skill association |
| `job_posting_identifier` | `TEXT` | FK → `JobPosting.JobPostingIdentifier` | No | Unique identifier of the job posting |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCareerPlan

**SQL identifier:** `workforce.learner_career_plan`

A table containing a learner's plan to satisfy the components and obtain skills defined in a career pathway. Learner's may have multiple plans for one or more career pathway.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_career_plan_identifier` | `TEXT` | PK | No | Unique identifier for the learner's career plan |
| `learner_degree_plan_identifier` | `TEXT` | FK → `LearnerDegreePlan.LearnerDegreePlanIdentifier` | No | Unique identifier for the learner's degree plan |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Identifier for associated career pathway |
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
| `learner_degree_plan_revision_identifier` | `TEXT` | FK → `LearnerDegreePlan.RevisionIdentifier` | No | Revision of the LearnerDegreePlan referenced by this record. |

## LearnerCareerPlanJobPostingDetails

**SQL identifier:** `workforce.learner_career_plan_job_posting_details`

A table detailing a job posting to a learner's career plan career pathway component detail.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_career_plan_job_posting_details_identifier` | `TEXT` | PK | No | Unique identifier for the association between the job posting and the career plan career pathway component detail |
| `job_posting_identifier` | `TEXT` | FK → `JobPosting.JobPostingIdentifier` | No | Unique identifier of the job posting |
| `learner_career_plan_identifier` | `TEXT` | FK → `LearnerCareerPlan.LearnerCareerPlanIdentifier` | No | Unique identifier for the learner's career plan |
| `learner_career_plan_step_identifier` | `TEXT` | FK → `LearnerCareerPlanStep.LearnerCareerPlanStepIdentifier` | Yes | Unique identifier for the learner's career plan details, including associations to relevant items such as activities, employment, credentials, etc. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCareerPlanStep

**SQL identifier:** `workforce.learner_career_plan_step`

Represents one learner-owned step within a career plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_career_plan_step_identifier` | `TEXT` | PK | No | Unique identifier for the learner's career plan details, including associations to relevant items such as activities, employment, credentials, etc. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | No | Unique identifier for the career pathway component |
| `learner_career_plan_identifier` | `TEXT` | FK → `LearnerCareerPlan.LearnerCareerPlanIdentifier` | No | Unique identifier for the learner's career plan |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | Yes | Unique identifier for the activity |
| `person_employment_identifier` | `TEXT` | FK → `PersonEmployment.PersonEmploymentIdentifier` | Yes | Unique identifier for a person employment record |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | Yes | Unique identifier for the credential or achievement |
| `target_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | School, Company, Enterprise or other target of the component |
| `duration_start` | `DATE` |  | No | When the learner estimates they will engage this career pathway component |
| `duration_end` | `DATE` |  | No | When the learner estimates they will complete this career pathway component |
| `target_location` | `TEXT` |  | Yes | Open field location as an alternative for QCEW code |
| `qcew_geographic_area_code` | `TEXT` |  | Yes | QCEW geographical area code for where this learner would engage with this component |
| `created_by` | `INTEGER` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `INTEGER` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `INTEGER` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerResume

**SQL identifier:** `workforce.learner_resume`

A table containing a list of person's resumes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_resume_identifier` | `TEXT` | PK | No | Unique identifier for the resume |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `purpose` | `TEXT` |  | Yes | Indicates the particular role, employer, or industry audience for which the resume is intended |
| `summary_statement` | `TEXT` |  | Yes | An overview of the candidate and their key skills, experience, and qualifications |
| `url` | `TEXT` |  | Yes | A URL to the resume |
| `status` | `TEXT` |  | Yes | The status of current usage of the resume (e.g. Draft, Active, Archived) |
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

## LearnerResumeComment

**SQL identifier:** `workforce.learner_resume_comment`

A table containing comments added to a learner's resume.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_resume_comment_identifier` | `TEXT` | PK | No | Unique identifier for the resume comment |
| `parent_learner_resume_comment_identifier` | `TEXT` | FK → `LearnerResumeComment.LearnerResumeCommentIdentifier` | Yes | Unique identifier for the parent resume comment |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_resume_identifier` | `TEXT` | FK → `LearnerResume.LearnerResumeIdentifier` | No | Unique identifier for the resume |
| `comment` | `TEXT` |  | No | The text of the comment |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerResumeDetails

**SQL identifier:** `workforce.learner_resume_details`

A table detailing a person's final term grades, final course grades, assessment results, standardized test results, credentials, activities, employment, skills, or strengths with their resume.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_resume_details_identifier` | `TEXT` | PK | No | Unique identifier for the resume to skill association |
| `learner_resume_identifier` | `TEXT` | FK → `LearnerResume.LearnerResumeIdentifier` | No | Unique identifier for the resume |
| `person_skill_identifier` | `TEXT` | FK → `PersonSkill.PersonSkillIdentifier` | Yes | Unique identifier of the person skills item |
| `learner_credential_identifier` | `TEXT` | FK → `LearnerCredential.LearnerCredentialIdentifier` | Yes | Unique identifier for the learner's credential history, either in-progress or completed credentials, covering certificates, diplomas, degrees, academic records, etc. |
| `person_employment_identifier` | `TEXT` | FK → `PersonEmployment.PersonEmploymentIdentifier` | Yes | Unique identifier for a person employment record |
| `person_activity_identifier` | `TEXT` | FK → `PersonActivity.PersonActivityIdentifier` | Yes | Unique identifier for learner activity details |
| `person_strength_identifier` | `TEXT` | FK → `PersonStrength.PersonStrengthIdentifier` | Yes | Unique identifier for the person's strength |
| `learner_final_grade_result_identifier` | `TEXT` | FK → `LearnerFinalGradeResult.LearnerFinalGradeResultIdentifier` | Yes | Unique identifier for the final grade result |
| `learner_assessment_result_identifier` | `TEXT` | FK → `LearnerAssessmentResult.LearnerAssessmentResultIdentifier` | Yes | Unique identifier for the assessment result |
| `standardized_test_result_identifier` | `TEXT` | FK → `LearnerStandardizedTestResult.StandardizedTestResultIdentifier` | Yes | Unique identifier for the standardized test result |
| `input` | `TEXT` |  | Yes | Free response input from the learner for the resume |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## OccupationElementLookup

**SQL identifier:** `workforce.occupation_element_lookup`

A lookup table containing occupation elements by ONET type and code.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `occupation_element_identifier` | `TEXT` | PK | No | Unique identifier for the skill, knowledge, or ability as defined by ONET |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | ONET Name of the skill, knowledge, or ability |
| `type` | `TEXT` |  | Yes | Indicates whether this record corresponds to skills, knowledge, or abilities as defined by ONET |
| `code` | `TEXT` |  | Yes | ONET Element identifier of the skill, knowledge, or ability |
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

## OrganizationCareerAssociation

**SQL identifier:** `workforce.organization_career_association`

A table associating organizations that offer certain careers or are related to certain careers to career pathways, career pathway components, and career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the activity to a career pathway, career pathway component, or career pathway job |
| `career_offered_by_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonAlum

**SQL identifier:** `workforce.person_alum`

A table containing learner contributed information as an alumnus of a secondary or post-secondary school or institution.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_alum_identifier` | `TEXT` | PK | No | Unique identifier for the alum record |
| `alum_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Alum reported institution they graduated from |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `graduation_year` | `INTEGER` |  | No | Year learner graduated |
| `program_of_study` | `TEXT` |  | Yes | Area of study |
| `current_employer` | `TEXT` |  | Yes | Alum's employer, if employed |
| `current_school` | `TEXT` |  | Yes | Alum's current school, if still enrolled |
| `note` | `TEXT` |  | Yes | Open text note to capture pertinent information |
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

## PersonEmployment

**SQL identifier:** `workforce.person_employment`

A tenant-scoped record of current or prior employment, self-employment, military service, or comparable work experience reported for a person.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_employment_identifier` | `TEXT` | PK | No | Unique identifier for a person employment record |
| `employer_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | Description of the responsibilities and accomplishments of the person in this employment |
| `start_date` | `DATE` |  | Yes | The year, month and day on which a person began self-employment or employment with an organization or institution |
| `end_date` | `DATE` |  | Yes | The year, month and day on which a person ended self-employment or employment with an organization or institution |
| `naics_code` | `TEXT` |  | Yes | The North American Industry Classification System (NAICS) code associated with an individual's employment |
| `employed_while_enrolled_indicator` | `BOOLEAN` |  | No | An individual who is a paid employee or works in his or her own business, profession, or farm, as reported through the State Unemployment Insurance Wage Report, FEDES, or WRIS, and at the same time is enrolled in secondary, postsecondary, or adult education or workforce programs |
| `employment_status_while_enrolled` | `TEXT` |  | Yes | An indication of the individual's employment status while enrolled |
| `employment_status_work_study_paid_indicator` | `BOOLEAN` |  | Yes | Indicates whether the individual is taking part in a paid work study for financial aid |
| `employment_status_work_study_unpaid_indicator` | `BOOLEAN` |  | Yes | Indicates whether the individual is taking part in an unpaid work study for financial aid |
| `employment_status_soc_code` | `TEXT` |  | Yes | SOCCode associated with the learner's employment |
| `type` | `TEXT` |  | Yes | Type of employment (e.g. Volunteer, FullTime) |
| `role` | `TEXT` |  | Yes | Role or job title during the person's employment |
| `role_specialization` | `TEXT` |  | Yes | Specialization within the role of the person during their employment |
| `employer_name` | `TEXT` |  | Yes | The name of the specific organization for which the person held positions or performed work |
| `employed_after_exit_indicator` | `BOOLEAN` |  | No | An individual who is a paid employee or works in his or her own business, profession, or farm, as reported through the State Unemployment Insurance Wage Report, FEDES, or WRIS, after exiting secondary, postsecondary, or adult education or workforce programs |
| `employed_prior_to_enrollment_indicator` | `BOOLEAN` |  | No | An individual who is a paid employee or works in his or her own business, profession, or farm, as reported through the State Unemployment Insurance Wage Report, FEDES, or WRIS, before enrolling in secondary, postsecondary, or adult education or workforce programs |
| `military_enlistment_after_exit_indicator` | `BOOLEAN` |  | No | An individual who is a member of the uniformed armed forces of the United States as reported through FEDES after exiting secondary, postsecondary, or adult education or workforce programs |
| `career_pathways_program_participation_indicator` | `BOOLEAN` |  | No | An indication of an individual who is participating in a program that is a component of or leads to a specific or recognized career pathway, as defined by the state |
| `separation_reason` | `TEXT` |  | Yes | The primary reason for the termination of the employment relationship |
| `separation_type` | `TEXT` |  | Yes | A designation of the type of separation occurring between a person and the organization |
| `location` | `TEXT` |  | Yes | Location where experience obtained |
| `contract_type` | `TEXT` |  | Yes | The type of employment contract used by an institution |
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

## ProgramOfStudyOccupationCodes

**SQL identifier:** `workforce.program_of_study_occupation_codes`

A table linking programs of study to occupations to support career and program exploration.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `program_of_study_occupation_codes_identifier` | `TEXT` | PK | No | Unique identifier for the occupation codes associated with a program of study |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the occupation codes associated with a program of study |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Unique identifier for a program of study offering |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `program_of_study_occupation_codes_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `occ_code` | `INTEGER` |  | Yes | ONET/OEWS: The 6-digit Standard Occupational Classification (SOC) code or OEWS-specific code for the occupation |
| `occ_name` | `TEXT` |  | Yes | ONET/OEWS: SOC title or OEWS-specific title or name for the occupation |
| `naics_code` | `TEXT` |  | Yes | ONET/OEWS: North American Industry Classification System (NAICS) code for the given industry |
| `naics_name` | `TEXT` |  | Yes | ONET/OEWS: North American Industry Classification System (NAICS) title or name for the given industry |
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

## StandardizedTestCareerAssociation

**SQL identifier:** `workforce.standardized_test_career_association`

A table associating standardized tests to career pathways, career pathway components, and career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `standardized_test_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of the standardized test to the career pathway, career pathway component, or career pathway job |
| `standardized_test_identifier` | `TEXT` | FK → `StandardizedTestLookup.StandardizedTestIdentifier` | No | Unique identifier for the standardized test |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `standardized_test_required_indicator` | `BOOLEAN` |  | Yes | Indicates whether the standardized test is required to pursue the career pathway |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
