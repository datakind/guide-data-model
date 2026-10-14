# Entity: Academics

This page documents every table that belongs to the **Academics** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 199**

## Table of contents

- [AcademicCatalog](#academiccatalog)
- [AcademicCatalogProgram](#academiccatalogprogram)
- [AcademicDiscipline](#academicdiscipline)
- [AcademicHonor](#academichonor)
- [AcademicLevelLookup](#academiclevellookup)
- [AcademicPeriodCensusDate](#academicperiodcensusdate)
- [AcademicPeriodEnrollmentStatusLookup](#academicperiodenrollmentstatuslookup)
- [AcademicSubject](#academicsubject)
- [AdministrativeInstructionalMethodLookup](#administrativeinstructionalmethodlookup)
- [Assessment](#assessment)
- [AssessmentCompetencyAssociation](#assessmentcompetencyassociation)
- [AssessmentItem](#assessmentitem)
- [AssessmentItemAssessmentAssociation](#assessmentitemassessmentassociation)
- [AssessmentItemOption](#assessmentitemoption)
- [AssessmentItemTag](#assessmentitemtag)
- [AssessmentItemTagAssessmentItemAssociation](#assessmentitemtagassessmentitemassociation)
- [AssessmentLearningResourceAssociation](#assessmentlearningresourceassociation)
- [CIPCodeLookup](#cipcodelookup)
- [ChargeAssessmentMethodLookup](#chargeassessmentmethodlookup)
- [ClassAcademicLevelAssociation](#classacademiclevelassociation)
- [ClassAlternateIdentifier](#classalternateidentifier)
- [ClassCategoryAssociation](#classcategoryassociation)
- [ClassCensusDate](#classcensusdate)
- [ClassCourseLevelAssociation](#classcourselevelassociation)
- [ClassCredit](#classcredit)
- [ClassCrossList](#classcrosslist)
- [ClassCrossListMember](#classcrosslistmember)
- [ClassDescription](#classdescription)
- [ClassGradeSchemeAssociation](#classgradeschemeassociation)
- [ClassInstructionalHours](#classinstructionalhours)
- [ClassInstructionalMethodAssociation](#classinstructionalmethodassociation)
- [ClassInstructorAssignment](#classinstructorassignment)
- [ClassLearningResourceAssociation](#classlearningresourceassociation)
- [ClassLookup](#classlookup)
- [ClassOrganizationUnitOwnership](#classorganizationunitownership)
- [ClassRequisiteRuleApplication](#classrequisiteruleapplication)
- [ClassTitle](#classtitle)
- [Competency](#competency)
- [CompetencyCareerAssociation](#competencycareerassociation)
- [CompetencyCourseAssociation](#competencycourseassociation)
- [CompetencyFramework](#competencyframework)
- [CompetencySkillAssociation](#competencyskillassociation)
- [CourseAcademicLevelAssociation](#courseacademiclevelassociation)
- [CourseAlternateIdentifier](#coursealternateidentifier)
- [CourseBillingRange](#coursebillingrange)
- [CourseCategoryAssociation](#coursecategoryassociation)
- [CourseCategoryLookup](#coursecategorylookup)
- [CourseCourseLevelAssociation](#coursecourselevelassociation)
- [CourseCredit](#coursecredit)
- [CourseGeneralEducationAssociation](#coursegeneraleducationassociation)
- [CourseGradeSchemeAssociation](#coursegradeschemeassociation)
- [CourseInstructionalHours](#courseinstructionalhours)
- [CourseInstructionalMethodAssociation](#courseinstructionalmethodassociation)
- [CourseLevelLookup](#courselevellookup)
- [CourseLookup](#courselookup)
- [CourseOrganizationUnitOwnership](#courseorganizationunitownership)
- [CourseReportingDetail](#coursereportingdetail)
- [CourseRequisiteCondition](#courserequisitecondition)
- [CourseRequisiteRule](#courserequisiterule)
- [CourseRequisiteRuleApplication](#courserequisiteruleapplication)
- [CourseStatusLookup](#coursestatuslookup)
- [CourseTermAssociation](#coursetermassociation)
- [CourseTitle](#coursetitle)
- [CourseTitleTypeLookup](#coursetitletypelookup)
- [CourseTopicAssociation](#coursetopicassociation)
- [CourseTopicLookup](#coursetopiclookup)
- [CredentialActivityAssociation](#credentialactivityassociation)
- [CredentialAssessmentAssociation](#credentialassessmentassociation)
- [CredentialCareerAssociation](#credentialcareerassociation)
- [CredentialCompetencyAssociation](#credentialcompetencyassociation)
- [CredentialCourseAssociation](#credentialcourseassociation)
- [CredentialIssuingOrganizationAssociation](#credentialissuingorganizationassociation)
- [CredentialLearningOutcomeAssociation](#credentiallearningoutcomeassociation)
- [CredentialLookup](#credentiallookup)
- [CredentialSkillAssociation](#credentialskillassociation)
- [CreditCategoryLookup](#creditcategorylookup)
- [Enrollment](#enrollment)
- [EnrollmentAcademicOutcome](#enrollmentacademicoutcome)
- [EnrollmentAcademicOutcomeChange](#enrollmentacademicoutcomechange)
- [EnrollmentApproval](#enrollmentapproval)
- [EquivalencyRule](#equivalencyrule)
- [EquivalencyRuleFromCourse](#equivalencyrulefromcourse)
- [EquivalencyRuleFromExam](#equivalencyrulefromexam)
- [EquivalencyRuleToCourse](#equivalencyruletocourse)
- [FlashCard](#flashcard)
- [FlashCardSet](#flashcardset)
- [GeneralEducationCategory](#generaleducationcategory)
- [GradeChangeReasonLookup](#gradechangereasonlookup)
- [GradeDefinitionEquivalent](#gradedefinitionequivalent)
- [GradeDefinitionLookup](#gradedefinitionlookup)
- [GradeModeLookup](#grademodelookup)
- [GradeSchemeLookup](#gradeschemelookup)
- [InstructionalDeliveryMethodLookup](#instructionaldeliverymethodlookup)
- [InstructionalMethodLookup](#instructionalmethodlookup)
- [InstructionalPlatformLookup](#instructionalplatformlookup)
- [LearnerAcademicCredit](#learneracademiccredit)
- [LearnerAcademicCreditLocalCourseOutcome](#learneracademiccreditlocalcourseoutcome)
- [LearnerAcademicCreditPriorLearningEvaluation](#learneracademiccreditpriorlearningevaluation)
- [LearnerAcademicCreditTestEvaluation](#learneracademiccredittestevaluation)
- [LearnerAcademicCreditTransferEvaluation](#learneracademiccredittransferevaluation)
- [LearnerAcademicStandingAndStatus](#learneracademicstandingandstatus)
- [LearnerAssessmentAlignment](#learnerassessmentalignment)
- [LearnerAssessmentAttempt](#learnerassessmentattempt)
- [LearnerAssessmentResult](#learnerassessmentresult)
- [LearnerAssessmentRubricCriterionResult](#learnerassessmentrubriccriterionresult)
- [LearnerClassAttendance](#learnerclassattendance)
- [LearnerCredential](#learnercredential)
- [LearnerCredentialDetails](#learnercredentialdetails)
- [LearnerCredentialDiscipline](#learnercredentialdiscipline)
- [LearnerCredentialEvidence](#learnercredentialevidence)
- [LearnerCredentialHonor](#learnercredentialhonor)
- [LearnerCredentialSharingLog](#learnercredentialsharinglog)
- [LearnerDegreePlan](#learnerdegreeplan)
- [LearnerDegreePlanAvailability](#learnerdegreeplanavailability)
- [LearnerDegreePlanItem](#learnerdegreeplanitem)
- [LearnerDegreePlanPreferences](#learnerdegreeplanpreferences)
- [LearnerExternalCourse](#learnerexternalcourse)
- [LearnerFinalGradeResult](#learnerfinalgraderesult)
- [LearnerFlashCardProgress](#learnerflashcardprogress)
- [LearnerInstructorClassRating](#learnerinstructorclassrating)
- [LearnerInstructorClassRatingComment](#learnerinstructorclassratingcomment)
- [LearnerPriorLearningEvaluation](#learnerpriorlearningevaluation)
- [LearnerPriorLearningEvaluationEvidence](#learnerpriorlearningevaluationevidence)
- [LearnerPriorLearningEvidence](#learnerpriorlearningevidence)
- [LearnerStandardizedTestResult](#learnerstandardizedtestresult)
- [LearnerStudyPlan](#learnerstudyplan)
- [LearnerStudySession](#learnerstudysession)
- [LearnerTestCreditEvaluation](#learnertestcreditevaluation)
- [LearnerTransferCreditEvaluation](#learnertransfercreditevaluation)
- [LearnerTransferCreditEvaluationEquivalentCourse](#learnertransfercreditevaluationequivalentcourse)
- [LearnerTransferCreditEvaluationSourceCourse](#learnertransfercreditevaluationsourcecourse)
- [LearningOutcome](#learningoutcome)
- [LearningOutcomeAssessmentAssociation](#learningoutcomeassessmentassociation)
- [LearningOutcomeCourseAssociation](#learningoutcomecourseassociation)
- [LearningOutcomeProgramOfStudyAssociation](#learningoutcomeprogramofstudyassociation)
- [LearningOutcomeSkillAssociation](#learningoutcomeskillassociation)
- [LearningResourceLookup](#learningresourcelookup)
- [OrganizationLearningResourceAssociation](#organizationlearningresourceassociation)
- [PersonAcademicLevelClassification](#personacademiclevelclassification)
- [PersonAcademicPeriod](#personacademicperiod)
- [PersonAcademicPeriodAcademicLevel](#personacademicperiodacademiclevel)
- [PersonAcademicPeriodAcademicLoad](#personacademicperiodacademicload)
- [PersonAcademicPeriodAcademicStatus](#personacademicperiodacademicstatus)
- [PersonExternalEducation](#personexternaleducation)
- [PersonExternalEducationDiscipline](#personexternaleducationdiscipline)
- [PersonExternalEducationHonor](#personexternaleducationhonor)
- [PersonOfficeHours](#personofficehours)
- [PersonPriorityRegistrationTimeSlot](#personpriorityregistrationtimeslot)
- [PersonProgram](#personprogram)
- [PersonProgramCredential](#personprogramcredential)
- [PersonProgramDiscipline](#personprogramdiscipline)
- [PersonProgramProgressEvaluation](#personprogramprogressevaluation)
- [PersonProgramRequirementEvaluation](#personprogramrequirementevaluation)
- [PersonProgramRequirementEvidence](#personprogramrequirementevidence)
- [PersonRegistrationEligibility](#personregistrationeligibility)
- [PersonRegistrationIneligibilityReason](#personregistrationineligibilityreason)
- [PersonSkill](#personskill)
- [PersonSkillEndorser](#personskillendorser)
- [PersonStudentType](#personstudenttype)
- [ProgramCredential](#programcredential)
- [ProgramCurriculum](#programcurriculum)
- [ProgramEnrollmentStatusLookup](#programenrollmentstatuslookup)
- [ProgramOfStudyLookup](#programofstudylookup)
- [ProgramRequirement](#programrequirement)
- [ProgramRequirementCourse](#programrequirementcourse)
- [ResultCategory](#resultcategory)
- [Rubric](#rubric)
- [RubricCriterion](#rubriccriterion)
- [RubricCriterionLevel](#rubriccriterionlevel)
- [ScoreScale](#scorescale)
- [ScoreScaleValue](#scorescalevalue)
- [SectionDescriptionTypeLookup](#sectiondescriptiontypelookup)
- [SectionRegistrationStatusLookup](#sectionregistrationstatuslookup)
- [SectionStatusLookup](#sectionstatuslookup)
- [SectionTitleTypeLookup](#sectiontitletypelookup)
- [SiteLookup](#sitelookup)
- [SkillAssociation](#skillassociation)
- [SkillLookup](#skilllookup)
- [SkillTag](#skilltag)
- [SkillTagSkillAssociation](#skilltagskillassociation)
- [StandardizedTestLearningResourceAssociation](#standardizedtestlearningresourceassociation)
- [StandardizedTestLookup](#standardizedtestlookup)
- [StudentAcademicPeriodStatusLookup](#studentacademicperiodstatuslookup)
- [StudentAcademicPeriodStatusUsage](#studentacademicperiodstatususage)
- [StudentClassificationLookup](#studentclassificationlookup)
- [StudentStatusLookup](#studentstatuslookup)
- [StudentTypeLookup](#studenttypelookup)
- [StudyTopic](#studytopic)
- [StudyTopicLearningResourceAssociation](#studytopiclearningresourceassociation)
- [Syllabus](#syllabus)
- [SyllabusAcademicField](#syllabusacademicfield)
- [SyllabusCompetencyAssociation](#syllabuscompetencyassociation)
- [SyllabusLearningResourceAssociation](#syllabuslearningresourceassociation)
- [SyllabusPolicy](#syllabuspolicy)
- [SyllabusPolicySyllabusAssociation](#syllabuspolicysyllabusassociation)
- [SyllabusScheduleItem](#syllabusscheduleitem)
- [SyllabusScheduleItemAssessmentAssociation](#syllabusscheduleitemassessmentassociation)
- [SyllabusScheduleItemLearningResourceAssociation](#syllabusscheduleitemlearningresourceassociation)
- [TermLookup](#termlookup)

---

## AcademicCatalog

**SQL identifier:** `academics.academic_catalog`

Tenant-scoped academic catalog edition used to identify the governing curriculum and program requirements applicable to person-program and reusable program contexts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_catalog_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an academic catalog edition |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record |
| `catalog_code` | `TEXT` |  | No | Institutionally governed code identifying the academic catalog edition |
| `catalog_title` | `TEXT` |  | No | Display title of the academic catalog edition |
| `description` | `TEXT` |  | Yes | Narrative description of the academic catalog edition |
| `status` | `TEXT` |  | No | Governed lifecycle status of the academic catalog edition |
| `effective_start_date` | `DATE` |  | Yes | Date on which the academic catalog edition becomes effective |
| `effective_end_date` | `DATE` |  | Yes | Date on which the academic catalog edition ceases to be effective |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the academic catalog edition |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AcademicCatalogProgram

**SQL identifier:** `academics.academic_catalog_program`

Associates an academic catalog edition with a program of study included in that catalog.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_catalog_program_identifier` | `TEXT` | PK | No | AcademicCatalogProgramIdentifier for AcademicCatalogProgram. |
| `academic_catalog_identifier` | `TEXT` | FK → `AcademicCatalog.AcademicCatalogIdentifier` | No | AcademicCatalogIdentifier for AcademicCatalogProgram. |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | ProgramOfStudyIdentifier for AcademicCatalogProgram. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | SourceSystemIdentifier for AcademicCatalogProgram. |
| `source_system_key_value` | `TEXT` |  | Yes | SourceSystemKeyValue for AcademicCatalogProgram. |
| `source_system_created_date` | `DATE` |  | Yes | SourceSystemCreatedDate for AcademicCatalogProgram. |
| `source_system_updated_date` | `DATE` |  | Yes | SourceSystemUpdatedDate for AcademicCatalogProgram. |
| `source_system_deleted_date` | `DATE` |  | Yes | SourceSystemDeletedDate for AcademicCatalogProgram. |
| `created_by` | `INTEGER` |  | No | CreatedBy for AcademicCatalogProgram. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | CreatedDate for AcademicCatalogProgram. |
| `updated_by` | `INTEGER` |  | Yes | UpdatedBy for AcademicCatalogProgram. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | UpdatedDate for AcademicCatalogProgram. |
| `deleted_by` | `INTEGER` |  | Yes | DeletedBy for AcademicCatalogProgram. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | DeletedDate for AcademicCatalogProgram. |

## AcademicDiscipline

**SQL identifier:** `academics.academic_discipline`

A tenant-scoped institutionally governed academic field-of-study designation, such as a major, minor, concentration, or comparable source-defined type. Distinct from course subject and from learner- or program-specific associations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_discipline_identifier` | `TEXT` | PK | No | Unique GUIDE-owned identifier for the academic discipline designation. |
| `academic_discipline_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Reference-code value identifying the designation type, such as major, minor, or concentration. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the academic discipline was imported or reconciled. |
| `academic_discipline_code` | `TEXT` |  | No | Institutionally governed compact code or abbreviation for the academic discipline designation. |
| `academic_discipline_name` | `TEXT` |  | No | Human-readable name of the academic discipline designation. |
| `reporting_country_code` | `TEXT` |  | Yes | Optional country or jurisdiction code qualifying the discipline reporting classification. |
| `classification_of_instructional_program_code` | `TEXT` |  | Yes | Optional country-qualified instructional-program classification code associated with the discipline. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the academic discipline designation. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AcademicHonor

**SQL identifier:** `academics.academic_honor`

Tenant-scoped governed definition of an academic honor or award designation that may be assigned to a person, credential, academic period, or other academic context. The definition is separate from any learner-specific receipt of the honor.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_honor_identifier` | `TEXT` | PK | No | Unique GUIDE-owned identifier for the academic honor definition. |
| `academic_honor_code` | `TEXT` |  | No | Institutionally governed compact code identifying the academic honor. |
| `academic_honor_name` | `TEXT` |  | No | Human-readable name of the academic honor. |
| `academic_honor_description` | `TEXT` |  | Yes | Optional fuller description of the academic honor. |
| `academic_honor_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the broad type or category of academic honor. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the academic honor definition was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the academic honor definition. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AcademicLevelLookup

**SQL identifier:** `academics.academic_level_lookup`

Reusable institutionally governed academic-level definitions referenced across program, period, registration, and reporting contexts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_level_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an academic level |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record |
| `code` | `TEXT` |  | No | Institutionally governed code for the academic level |
| `name` | `TEXT` |  | No | Display name of the academic level |
| `description` | `TEXT` |  | Yes | Description of the academic level |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the academic level remains available for use |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the academic level |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## AcademicPeriodCensusDate

**SQL identifier:** `academics.academic_period_census_date`

One official or default enrollment/headcount census date associated with an academic period; multiple dated rows may exist per period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `term_identifier` | `TEXT` | PK, FK → `TermLookup.TermIdentifier` | No | Academic period to which the census date applies. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for multiple census dates in one academic period. |
| `census_date` | `DATE` |  | No | Official or default enrollment/headcount census date for the academic period. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was last updated. |

## AcademicPeriodEnrollmentStatusLookup

**SQL identifier:** `academics.academic_period_enrollment_status_lookup`

Tenant-scoped governed definition of an enrollment status applicable to an academic period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_period_enrollment_status_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an academic-period enrollment status |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | No | Identifier of the source system that supplied the record |
| `code` | `TEXT` |  | No | Institutionally governed code for the academic-period enrollment status |
| `title` | `TEXT` |  | No | Display title of the academic-period enrollment status |
| `description` | `TEXT` |  | Yes | Description of the academic-period enrollment status |
| `source_system_key_value` | `TEXT` |  | No | Source-system identifier for the enrollment-status definition |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## AcademicSubject

**SQL identifier:** `academics.academic_subject`

Tenant-scoped institutionally governed academic subject or course-prefix area used to identify and group courses. Referenced singularly from CourseLookup; sections inherit subject through their course. Distinct from academic discipline, organization unit, category, topic, and program of study.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_subject_identifier` | `TEXT` | PK | No | Unique GUIDE identifier for the academic subject. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the subject was imported or reconciled. |
| `academic_subject_code` | `TEXT` |  | No | Institutionally governed code for the academic subject. |
| `academic_subject_abbreviation` | `TEXT` |  | Yes | Short display abbreviation for the academic subject when distinct from its governed code. |
| `academic_subject_name` | `TEXT` |  | No | Human-readable name of the academic subject. |
| `academic_subject_description` | `TEXT` |  | Yes | Optional fuller description of the academic subject. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the academic subject is active for current use. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the academic subject. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AdministrativeInstructionalMethodLookup

**SQL identifier:** `academics.administrative_instructional_method_lookup`

Administrative instructional methods used to classify section contact or workload hours.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `administrative_instructional_method_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `instructional_method_identifier` | `TEXT` | FK → `InstructionalMethodLookup.InstructionalMethodIdentifier` | Yes | Related instructional method. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `code` | `TEXT` |  | No | Governed administrative instructional-method code. |
| `title` | `TEXT` |  | No | Human-readable name of the administrative instructional method. |
| `description` | `TEXT` |  | Yes | Description of the administrative method. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## Assessment

**SQL identifier:** `academics.assessment`

An assignment or assessment used to gauge student learning and performance.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the assessment |
| `assessment_identifier` | `TEXT` | PK | No | Unique identifier for the assessment |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `parent_assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the parent assessment; when populated, ParentAssessmentRevisionIdentifier identifies the specific parent revision. |
| `parent_assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Unique identifier for the specific revision of the parent assessment. |
| `rubric_identifier` | `TEXT` | FK → `Rubric.RubricIdentifier` | Yes | Unique identifier for the rubric |
| `result_category_identifier` | `TEXT` | FK → `ResultCategory.ResultCategoryIdentifier` | Yes | Unique identifier for the result category |
| `locked_for_editing_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that locked the record for editing |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `assessment_revision_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the workflow status of this assessment revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `assessment_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the assessment type or category. |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `short_name` | `TEXT` |  | Yes | A short name for the record |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the assessment is active. |
| `date_published` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that provides the publication date of the resource. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_activate` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource was activated. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_show` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource should be shown or made available to learners. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_start_on` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource can be started. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `date_to_submit` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the resource is to be submitted for evaluation. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `max_attempts` | `INTEGER` |  | Yes | A non-negative integer that designates the number of permitted attempts |
| `max_score` | `NUMERIC` |  | Yes | A number with a fractional part denoted by a decimal separator that designates the maximum score permitted |
| `max_submits` | `INTEGER` |  | Yes | A non-negative integer that designates the number of permitted submissions |
| `submission_type` | `TEXT` |  | Yes | The type of submission for the assessment or assignment (e.g. on paper, online, external tool) |
| `version` | `TEXT` |  | Yes | The version of the assessment |
| `current_version_indicator` | `BOOLEAN` |  | Yes | Indicates that this is the most current version of the assessment |
| `locked_for_editing_indicator` | `BOOLEAN` |  | No | Indicates whether the assessment is locked for editing |
| `workforce_endorsed_indicator` | `BOOLEAN` |  | Yes | Indicates whether this competency is endorsed and approved by a workforce partner of the organization |
| `date_to_hide` | `DATE` |  | Yes | Date after which the assessment will no longer be accessible by learners. |
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

## AssessmentCompetencyAssociation

**SQL identifier:** `academics.assessment_competency_association`

A table associating assessments with competencies.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_competency_association_identifier` | `TEXT` | PK | No | Unique identifier for the assessment competency association |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## AssessmentItem

**SQL identifier:** `academics.assessment_item`

A table containing individual assessment items or questions that belong in an assessment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_item_identifier` | `TEXT` | PK | No | Unique identifier for the assessment item |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the assessment item |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | Yes | Unique identifier for the competency or learning objective |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `stimulus_learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | Yes | Unique identifier for the learning resource that is the stimulus in this assessment item |
| `name` | `TEXT` |  | Yes | A name for the record |
| `assessment_item_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `status` | `TEXT` |  | No | Status of the assessment item (active, inactive) |
| `max_score` | `NUMERIC` |  | Yes | A number with a fractional part denoted by a decimal separator that designates the maximum score permitted |
| `sequence_number` | `INTEGER` |  | Yes | Number indicating where in a sequence of questions or items on this assessment this one exists |
| `interaction_type` | `TEXT` |  | Yes | The type of question or interaction of the assessment item |
| `prompt` | `TEXT` |  | Yes | The question, prompt, or label of the assessment item |
| `stimulus` | `TEXT` |  | Yes | Additional reading material or media for the question |
| `url` | `TEXT` |  | Yes | A URL to the question or assessment item |
| `scoring_method` | `TEXT` |  | Yes | Indicates the method of scoring the item |
| `tolerance` | `NUMERIC` |  | Yes | Allowed margin of error for numeric or range-based responses |
| `formula` | `TEXT` |  | Yes | Scoring formula for math-based questions |
| `correct_response` | `TEXT` |  | Yes | Expected answer(s) for free-text, numeric, or other non-option-based questions |
| `general_feedback` | `TEXT` |  | Yes | General feedback displayed after answering |
| `correct_feedback` | `TEXT` |  | Yes | Feedback displayed when the correct answer is selected |
| `incorrect_feedback` | `TEXT` |  | Yes | Feedback displayed when the incorrect answer is selected |
| `difficulty` | `TEXT` |  | Yes | Indicates the difficulty level of the question (easy, medium, hard) |
| `time_limit` | `INTEGER` |  | Yes | Suggested time limit in seconds for completing the question |
| `accessibility` | `TEXT` |  | Yes | Accessibility features (e.g. alt text, screen reader compatibility) for compliance |
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
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | Yes | Revision of the Competency referenced by this record. |
| `stimulus_learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | Yes | Revision of the LearningResource referenced by this record. |

## AssessmentItemAssessmentAssociation

**SQL identifier:** `academics.assessment_item_assessment_association`

A table associating an assessment item to an assessment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_item_assessment_association_identifier` | `TEXT` | PK | No | Unique identifier for the assessment to assessment item association |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the assessment to assessment item association |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `assessment_item_identifier` | `TEXT` | FK → `AssessmentItem.AssessmentItemIdentifier` | No | Unique identifier for the assessment item |
| `assessment_item_assessment_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |
| `assessment_item_revision_identifier` | `TEXT` | FK → `AssessmentItem.RevisionIdentifier` | No | Revision of the AssessmentItem referenced by this record. |

## AssessmentItemOption

**SQL identifier:** `academics.assessment_item_option`

A table containing individual options for assessment items or questions that are multiple choice, matching, ordering, or other similar types.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_item_option_identifier` | `TEXT` | PK | No | Unique identifier for the assessment item option or choice |
| `assessment_item_identifier` | `TEXT` | FK → `AssessmentItem.AssessmentItemIdentifier` | No | Unique identifier for the assessment item |
| `assessment_item_option_type` | `TEXT` |  | No | Indicates whether the type of question option is for multiple choice, matching, ordering, or other |
| `display_text` | `TEXT` |  | Yes | Text displayed for the answer choice |
| `correct_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the option is correct |
| `weighting` | `NUMERIC` |  | Yes | Partial credit weight assigned to the option |
| `match_group` | `TEXT` |  | Yes | Indicates the group of options to which this match corresponds for matching type questions |
| `sequence_number` | `TEXT` |  | Yes | Indicates the correct numeric ordering of this option for ordering type questions |
| `media_url` | `TEXT` |  | Yes | URL linking to media (image, video, audio) associated with the answer choice |
| `feedback` | `TEXT` |  | Yes | Feedback displayed when this option is selected |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_item_revision_identifier` | `TEXT` | FK → `AssessmentItem.RevisionIdentifier` | No | Revision of the AssessmentItem referenced by this record. |

## AssessmentItemTag

**SQL identifier:** `academics.assessment_item_tag`

A table containing the tag assigned to an assessment primarily for searching and categorizing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_item_tag_identifier` | `TEXT` | PK | No | Unique identifier for the assessment item tag |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## AssessmentItemTagAssessmentItemAssociation

**SQL identifier:** `academics.assessment_item_tag_assessment_item_association`

A table associating an assessment item tag to an assessment item.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_item_tag_assessment_item_association_identifier` | `TEXT` | PK | No | Unique identifier for the assessment item tag to assessment item association |
| `assessment_item_identifier` | `TEXT` | FK → `AssessmentItem.AssessmentItemIdentifier` | No | Unique identifier for the assessment item |
| `assessment_item_tag_identifier` | `TEXT` | FK → `AssessmentItemTag.AssessmentItemTagIdentifier` | No | Unique identifier for the assessment item tag |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_item_revision_identifier` | `TEXT` | FK → `AssessmentItem.RevisionIdentifier` | No | Revision of the AssessmentItem referenced by this record. |

## AssessmentLearningResourceAssociation

**SQL identifier:** `academics.assessment_learning_resource_association`

A table associating assessments with learning resources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `assessment_learning_resource_identifier` | `TEXT` | PK | No | Unique identifier for the assessment to learning resource association |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment or assignment |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## CIPCodeLookup

**SQL identifier:** `academics.cip_code_lookup`

Tenant-scoped representation of a Classification of Instructional Programs (CIP) code definition for a specific NCES revision, including code, title, description, and source lineage. Separate from institutional academic disciplines and from the association of a CIP classification to a course, program, discipline, or credential.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `cip_code_identifier` | `TEXT` | PK | No | Unique GUIDE-owned identifier for the CIP code definition. |
| `cip_code` | `TEXT` |  | No | Classification of Instructional Programs code as published for the specified revision year. |
| `cip_title` | `TEXT` |  | No | Official or source-supplied human-readable title of the CIP code. |
| `cip_description` | `TEXT` |  | Yes | Official or source-supplied description of the CIP code. |
| `cip_revision_year` | `INTEGER` |  | No | Revision year of the CIP taxonomy to which this code definition belongs. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier for the source system from which the CIP code definition was imported or reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the CIP code definition. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ChargeAssessmentMethodLookup

**SQL identifier:** `academics.charge_assessment_method_lookup`

Governed methods used to assess charges for sections.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `charge_assessment_method_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `code` | `TEXT` |  | No | Governed charge-assessment-method code. |
| `title` | `TEXT` |  | No | Human-readable name of the charge assessment method. |
| `description` | `TEXT` |  | Yes | Description of the charge-assessment method. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## ClassAcademicLevelAssociation

**SQL identifier:** `academics.class_academic_level_association`

Associates a section with each governed academic level applicable to the offering.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `academic_level_identifier` | `TEXT` | PK, FK → `AcademicLevelLookup.AcademicLevelIdentifier` | No | Governed academic level associated with the section. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassAlternateIdentifier

**SQL identifier:** `academics.class_alternate_identifier`

Preserves repeating source-system alternate identifiers assigned to a section.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for repeating members without a durable source identifier. |
| `identifier_type` | `TEXT` |  | Yes | Source-defined title or type of the alternate identifier. |
| `identifier_value` | `TEXT` |  | No | Alternate identifier value assigned to the section. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassCategoryAssociation

**SQL identifier:** `academics.class_category_association`

A tenant-scoped association linking a stable class offering (SIS section) to one governed institution-defined course category. Kept distinct from course-level category assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Class offering associated with the governed category value. |
| `course_category_identifier` | `TEXT` | PK, FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed reference-code value identifying the institution-defined course category. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association row was last updated. |

## ClassCensusDate

**SQL identifier:** `academics.class_census_date`

Preserves one section-specific census date overriding or supplementing academic-period defaults.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for repeating members without a durable source identifier. |
| `census_date` | `DATE` |  | No | Official section-specific enrollment or headcount census date. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassCourseLevelAssociation

**SQL identifier:** `academics.class_course_level_association`

Associates a section with each governed course level applicable to the offering.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `course_level_identifier` | `TEXT` | PK, FK → `CourseLevelLookup.CourseLevelIdentifier` | No | Governed course level associated with the section. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassCredit

**SQL identifier:** `academics.class_credit`

One section-level credit specification, including category, measure, range, and increment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `credit_category_identifier` | `TEXT` | FK → `CreditCategoryLookup.CreditCategoryIdentifier` | Yes | Governed credit category for the specification. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for repeating members without a durable source identifier. |
| `credit_type` | `TEXT` |  | Yes | Higher-level source credit type retained for traceability. |
| `measure` | `TEXT` |  | No | Unit or standard of credit measurement. |
| `minimum_value` | `NUMERIC` |  | Yes | Minimum credit value. |
| `maximum_value` | `NUMERIC` |  | Yes | Maximum credit value. |
| `increment` | `NUMERIC` |  | Yes | Permitted increment within the credit range. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassCrossList

**SQL identifier:** `academics.class_cross_list`

Tenant-scoped group of sections offered as a coordinated cross-list with combined enrollment and waitlist controls.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_cross_list_identifier` | `TEXT` | PK | No | GUIDE-owned cross-list identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | Yes | Institutionally meaningful cross-list code. |
| `enrollment_capacity` | `INTEGER` |  | Yes | Maximum combined enrollment. |
| `waitlist_capacity` | `INTEGER` |  | Yes | Maximum combined waitlist. |
| `waitlist_capacity_scope` | `TEXT` |  | Yes | Whether waitlisting is triggered by individual-section or combined capacity. |
| `source_system_key_value` | `TEXT` |  | Yes | Source cross-list identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Created timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Updated timestamp. |

## ClassCrossListMember

**SQL identifier:** `academics.class_cross_list_member`

Membership of a section in a cross-list group, including primary or secondary designation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_cross_list_identifier` | `TEXT` | PK, FK → `ClassCrossList.ClassCrossListIdentifier` | No | Cross-list group. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Member section. |
| `membership_type` | `TEXT` |  | Yes | Primary or secondary role within the group. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Created timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Updated timestamp. |

## ClassDescription

**SQL identifier:** `academics.class_description`

One typed description assigned to a section.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `section_description_type_identifier` | `TEXT` | PK, FK → `SectionDescriptionTypeLookup.SectionDescriptionTypeIdentifier` | No | Governed type of section description. |
| `description_text` | `TEXT` |  | No | Text of the typed section description. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassGradeSchemeAssociation

**SQL identifier:** `academics.class_grade_scheme_association`

Associates a section with a governed grade scheme available for the offering.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `grade_scheme_identifier` | `TEXT` | PK, FK → `GradeSchemeLookup.GradeSchemeIdentifier` | No | Governed grade scheme associated with the section. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassInstructionalHours

**SQL identifier:** `academics.class_instructional_hours`

One administrative instructional-method hour specification for a section.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `administrative_instructional_method_identifier` | `TEXT` | FK → `AdministrativeInstructionalMethodLookup.AdministrativeInstructionalMethodIdentifier` | Yes | Governed administrative instructional method for the hour specification. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for repeating members without a durable source identifier. |
| `minimum_hours` | `NUMERIC` |  | Yes | Minimum hours. |
| `maximum_hours` | `NUMERIC` |  | Yes | Maximum hours. |
| `increment` | `NUMERIC` |  | Yes | Permitted increment within the hour range. |
| `interval` | `TEXT` |  | Yes | Source-defined interval for the hour specification. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassInstructionalMethodAssociation

**SQL identifier:** `academics.class_instructional_method_association`

Associates a section with a governed instructional method.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `instructional_method_identifier` | `TEXT` | PK, FK → `InstructionalMethodLookup.InstructionalMethodIdentifier` | No | Governed instructional method associated with the section. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## ClassInstructorAssignment

**SQL identifier:** `academics.class_instructor_assignment`

Tenant-scoped assignment of an instructor to a section, including role, instructional method, responsibility, workload, and effective dates.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_instructor_assignment_identifier` | `TEXT` | PK | No | GUIDE-owned assignment identifier. |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Assigned section. |
| `instructor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person serving as instructor. |
| `instructional_method_identifier` | `TEXT` | FK → `InstructionalMethodLookup.InstructionalMethodIdentifier` | Yes | Instructional method for this assignment. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `instructor_role` | `TEXT` |  | Yes | Role of the instructor in the section. |
| `responsibility_percentage` | `NUMERIC` |  | Yes | Percentage of responsibility assigned. |
| `work_load` | `NUMERIC` |  | Yes | Source-reported workload amount. |
| `work_start_date` | `DATE` |  | Yes | Assignment start date. |
| `work_end_date` | `DATE` |  | Yes | Assignment end date. |
| `source_system_key_value` | `TEXT` |  | Yes | Source assignment identifier. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Created timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Updated timestamp. |

## ClassLearningResourceAssociation

**SQL identifier:** `academics.class_learning_resource_association`

A table associating classes to learning resources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_learning_resource_identifier` | `TEXT` | PK | No | Unique identifier for the class to learning resource association |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Unique identifier for the class |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `type` | `TEXT` |  | Yes | Indicates the type of association between the class and the learning resource, such as placement. |
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
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## ClassLookup

**SQL identifier:** `academics.class_lookup`

A lookup table containing a history of courses offered as classes during a term (often called sections and components). Each instance of a course offered as a class is uniquely identified and contains information to support learner enrollment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK | No | Unique identifier for the class |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Unique identifier for the score scale |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifier for a term |
| `department_organization_unit_identifier` | `TEXT` | FK → `OrganizationUnit.OrganizationUnitIdentifier` | Yes | Internal academic organization unit responsible for the class or course offering. |
| `instructor_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier for the instructor |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `reporting_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Reporting academic period associated with the section. |
| `site_identifier` | `TEXT` | FK → `SiteLookup.SiteIdentifier` | Yes | Primary institutional site or campus associated with the section. |
| `section_status_identifier` | `TEXT` | FK → `SectionStatusLookup.SectionStatusIdentifier` | Yes | Governed status of the section. |
| `instructional_delivery_method_identifier` | `TEXT` | FK → `InstructionalDeliveryMethodLookup.InstructionalDeliveryMethodIdentifier` | Yes | Governed delivery mode for the section. |
| `instructional_platform_identifier` | `TEXT` | FK → `InstructionalPlatformLookup.InstructionalPlatformIdentifier` | Yes | Technology platform used to administer or deliver the section. |
| `charge_assessment_method_identifier` | `TEXT` | FK → `ChargeAssessmentMethodLookup.ChargeAssessmentMethodIdentifier` | Yes | Governed method used to assess charges for the section. |
| `name` | `TEXT` |  | No | A name for the record |
| `section_number` | `TEXT` |  | Yes | The number assigned to differentiate among distinct occurrences of courses that have the same course abbreviation and number but are considered to be different courses |
| `code` | `TEXT` |  | Yes | Institutionally meaningful section code, generally unique within an academic period. |
| `overview` | `TEXT` |  | Yes | Overview of the class content and instruction |
| `start_date` | `DATE` |  | Yes | Start date for the class |
| `start_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Start time for the class |
| `end_date` | `DATE` |  | Yes | End date for the class |
| `end_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | End time for the class |
| `duration` | `TEXT` |  | Yes | Source-defined scheme or duration used for the section. |
| `cross_listed_indicator` | `BOOLEAN` |  | Yes | Indicates that the section participates in a cross-list arrangement; it does not identify the related sections. |
| `reserved_seat_capacity` | `INTEGER` |  | Yes | Maximum number of seats reserved within the section. |
| `meet_monday_indicator` | `BOOLEAN` |  | Yes | Monday meeting indicator |
| `meet_tuesday_indicator` | `BOOLEAN` |  | Yes | Tuesday meeting indicator |
| `meet_wednesday_indicator` | `BOOLEAN` |  | Yes | Wednesday meeting indicator |
| `meet_thursday_indicator` | `BOOLEAN` |  | Yes | Thursday meeting indicator |
| `meet_friday_indicator` | `BOOLEAN` |  | Yes | Friday meeting indicator |
| `meet_saturday_indicator` | `BOOLEAN` |  | Yes | Saturday meeting indicator |
| `meet_sunday_indicator` | `BOOLEAN` |  | Yes | Sunday meeting indicator |
| `building_key` | `TEXT` |  | Yes | Unique identifier for the building |
| `building_name` | `TEXT` |  | Yes | Common name of the building |
| `building_address` | `TEXT` |  | Yes | Address of the classroom building |
| `building_room_number` | `TEXT` |  | Yes | Room number of the building |
| `enrollment_total` | `INTEGER` |  | Yes | Total number of actual enrolled seats for the class |
| `enrollment_capacity` | `INTEGER` |  | Yes | Total number of seats for the class |
| `enrollment_wait_total` | `INTEGER` |  | Yes | Total number of actual waited seats for the class |
| `enrollment_wait_cap` | `INTEGER` |  | Yes | Total number of waited seats for the class |
| `consent_required_indicator` | `BOOLEAN` |  | Yes | Indicator that requires consent for enrollment |
| `enrollment_deadline` | `DATE` |  | Yes | Enrollment deadline date |
| `accepting_enrollments` | `BOOLEAN` |  | Yes | Indicator of whether or not this course is accepting enrollments at this time |
| `withdrawal_deadline` | `DATE` |  | Yes | Withdrawal deadline date |
| `syllabus_url` | `TEXT` |  | Yes | URL for class syllabus |
| `learning_outcomes` | `TEXT` |  | Yes | Text description of the learning outcomes designed for the class |
| `learning_objectives` | `TEXT` |  | Yes | Text description of the learning objectives designed for the class |
| `grading_requirements` | `TEXT` |  | Yes | Grading requirements or rubric for class assignments and exams |
| `resources` | `TEXT` |  | Yes | Text, media and resources utilized during the class |
| `outline` | `TEXT` |  | Yes | Outline that describes instruction during the class |
| `fee_per_credit_hour` | `NUMERIC` |  | Yes | Fee assessed per credit hour of enrollment in addition to tuition |
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

## ClassOrganizationUnitOwnership

**SQL identifier:** `academics.class_organization_unit_ownership`

A tenant-scoped association linking a stable class offering (SIS section) to one owning or administering internal organization unit. Preserves source ownership percentage without inferring a primary owner or requiring all percentages to total 100.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Class offering associated with the owning organization unit. |
| `organization_unit_identifier` | `TEXT` | PK, FK → `OrganizationUnit.OrganizationUnitIdentifier` | No | Internal organization unit that owns or administers the class. |
| `ownership_percentage` | `NUMERIC` |  | Yes | Source-reported percentage associated with the organization-unit ownership relationship. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association row was last updated. |

## ClassRequisiteRuleApplication

**SQL identifier:** `academics.class_requisite_rule_application`

Tenant-safe assignment of a reusable requisite rule to a stable Class, including catalog-rule inheritance or override handling.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Stable Class identity to which the rule applies. |
| `course_requisite_rule_identifier` | `TEXT` | PK, FK → `CourseRequisiteRule.CourseRequisiteRuleIdentifier` | No | Reusable requisite rule applied to the Class. |
| `catalog_requisite_handling` | `TEXT` |  | No | How class-level rules interact with catalog Course rules. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date the rule assignment was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the rule assignment was last updated. |

## ClassTitle

**SQL identifier:** `academics.class_title`

One typed title assigned to a section.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `class_identifier` | `TEXT` | PK, FK → `ClassLookup.ClassIdentifier` | No | Section offering associated with the child row. |
| `section_title_type_identifier` | `TEXT` | PK, FK → `SectionTitleTypeLookup.SectionTitleTypeIdentifier` | No | Governed type of section title. |
| `title_text` | `TEXT` |  | No | Text of the typed section title. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## Competency

**SQL identifier:** `academics.competency`

A table of measurable learning objectives for learners to demonstrate.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `competency_identifier` | `TEXT` | PK | No | Unique identifier for the competency |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the competency. |
| `parent_competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | Yes | Unique identifier for the parent competency; when populated, ParentCompetencyRevisionIdentifier identifies the specific parent revision. |
| `parent_competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | Yes | Unique identifier for the specific revision of the parent competency in the hierarchy. |
| `competency_framework_identifier` | `TEXT` | FK → `CompetencyFramework.CompetencyFrameworkIdentifier` | Yes | Unique identifier for the competency framework |
| `locked_for_editing_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that locked the record for editing |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `short_name` | `TEXT` |  | Yes | A short name for the record |
| `competency_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `statement` | `TEXT` |  | No | The text of the statement. The textual content that either describes a specific competency or describes a less granular group of competencies within the taxonomy of the competency framework. |
| `url` | `TEXT` |  | Yes | A network-resolvable Uniform Resource Locator (URL) pointing to the authoritative reference for the competency definition |
| `code` | `TEXT` |  | Yes | A human-referenceable code designated by the publisher to identify the item in the hierarchy of competency definitions |
| `current_version_indicator` | `BOOLEAN` |  | No | Indicates that this is the most current version of the Competency Definition |
| `version` | `TEXT` |  | Yes | A label assigned by the publisher indicating the version of the competency framework statement |
| `blooms_taxonomy_domain` | `TEXT` |  | Yes | Classification of the Competency Definition using Bloom's Taxonomy Domains |
| `language` | `TEXT` |  | Yes | The default language of the text used for the content in the competency definition statement |
| `multiple_intelligence` | `TEXT` |  | Yes | Classification of the Competency Definition using intelligences defined for Howard Earl Gardner's Theory of Multiple Intelligences |
| `locked_for_editing_indicator` | `BOOLEAN` |  | No | Indicates whether the competency is locked for editing |
| `workforce_endorsed_indicator` | `BOOLEAN` |  | Yes | Indicates whether this competency is endorsed and approved by a workforce partner of the organization |
| `competency_context` | `TEXT` |  | Yes | Indicates context in which comptetency hierarchy applies (unspecified, account, course, college, department) |
| `status` | `TEXT` |  | No | Status of the competency (active, inactive) |
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
| `competency_framework_revision_identifier` | `TEXT` | FK → `CompetencyFramework.RevisionIdentifier` | Yes | Revision of the CompetencyFramework referenced by this record. |

## CompetencyCareerAssociation

**SQL identifier:** `academics.competency_career_association`

A table associating competencies to career pathways, career pathway components, or career pathway job details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `competency_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the competency to career association |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## CompetencyCourseAssociation

**SQL identifier:** `academics.competency_course_association`

A table associating competencies to courses.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `competency_course_association_identifier` | `TEXT` | PK | No | Unique identifier for the career pathway to course association |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## CompetencyFramework

**SQL identifier:** `academics.competency_framework`

A table representing a framework to which competencies belong.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `competency_framework_identifier` | `TEXT` | PK | No | Unique identifier for the competency framework |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the competency framework |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `competency_framework_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `subject` | `TEXT` |  | Yes | The topic or academic subject of the competency framework |
| `version` | `TEXT` |  | Yes | Defines the revision of the competency framework as a version number or date |
| `language` | `TEXT` |  | Yes | The default language of the text used for the content in the competency framework |
| `source_url` | `TEXT` |  | Yes | A URL that resolves to the original or authoritative competency framework document |
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

## CompetencySkillAssociation

**SQL identifier:** `academics.competency_skill_association`

A table associating a competency to a skill.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `competency_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the competency to skill association |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the competency to skill association |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `competency_skill_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## CourseAcademicLevelAssociation

**SQL identifier:** `academics.course_academic_level_association`

Associates a stable course definition with each governed academic level for which it is intended.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `academic_level_identifier` | `TEXT` | PK, FK → `AcademicLevelLookup.AcademicLevelIdentifier` | No | Governed academic level. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseAlternateIdentifier

**SQL identifier:** `academics.course_alternate_identifier`

Preserves repeating alternate course identifiers and their source-defined types without replacing canonical course identity.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence. |
| `identifier_type` | `TEXT` |  | Yes | Source-defined alternate identifier type. |
| `identifier_value` | `TEXT` |  | No | Alternate course identifier value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseBillingRange

**SQL identifier:** `academics.course_billing_range`

Preserves the course-level range and increment of billing units used as defaults for sections or student charges.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `minimum_value` | `NUMERIC` |  | Yes | Minimum billing units. |
| `maximum_value` | `NUMERIC` |  | Yes | Maximum billing units. |
| `increment` | `NUMERIC` |  | Yes | Permitted billing-unit increment. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseCategoryAssociation

**SQL identifier:** `academics.course_category_association`

A tenant-scoped association linking a stable course to one governed institution-defined course category.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Course associated with the governed category value. |
| `course_category_identifier` | `TEXT` | PK, FK → `CourseCategoryLookup.CourseCategoryIdentifier` | No | Governed reference-code value identifying the institution-defined course category. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association row was last updated. |

## CourseCategoryLookup

**SQL identifier:** `academics.course_category_lookup`

Governed course-category definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_category_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed lookup value. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institutionally meaningful code. |
| `title` | `TEXT` |  | No | Human-readable name of the course category. |
| `description` | `TEXT` |  | Yes | Detailed description of the course category. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for crosswalk resolution. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseCourseLevelAssociation

**SQL identifier:** `academics.course_course_level_association`

Associates a stable course definition with each governed course level.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `course_level_identifier` | `TEXT` | PK, FK → `CourseLevelLookup.CourseLevelIdentifier` | No | Governed course level. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseCredit

**SQL identifier:** `academics.course_credit`

Preserves one course-level academic-credit specification, including category, measure, range, and increment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `credit_category_identifier` | `TEXT` | FK → `CreditCategoryLookup.CreditCategoryIdentifier` | Yes | Governed credit category. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence. |
| `credit_type` | `TEXT` |  | Yes | Higher-level source credit type. |
| `measure` | `TEXT` |  | No | Credit measurement unit. |
| `minimum_value` | `NUMERIC` |  | Yes | Minimum credit value. |
| `maximum_value` | `NUMERIC` |  | Yes | Maximum credit value. |
| `increment` | `NUMERIC` |  | Yes | Permitted credit increment. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseGeneralEducationAssociation

**SQL identifier:** `academics.course_general_education_association`

A table associating a general education category to a course. A course may have multiple general education category associations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_general_education_association_identifier` | `TEXT` | PK | No | Unique identifier of a general education course association |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the general education course association |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `general_education_category_identifier` | `TEXT` | FK → `GeneralEducationCategory.GeneralEducationCategoryIdentifier` | No | Unique identifier for the general education category |
| `course_general_education_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `status` | `TEXT` |  | No | Status of the general education association |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CourseGradeSchemeAssociation

**SQL identifier:** `academics.course_grade_scheme_association`

Associates a course with available grade schemes and identifies the registration default where supplied.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `grade_scheme_identifier` | `TEXT` | PK, FK → `GradeSchemeLookup.GradeSchemeIdentifier` | No | Governed grade scheme. |
| `registration_default_indicator` | `BOOLEAN` |  | Yes | Whether this scheme is the default for registration. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseInstructionalHours

**SQL identifier:** `academics.course_instructional_hours`

Preserves course-level instructional-hour ranges by administrative instructional method.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `administrative_instructional_method_identifier` | `TEXT` | FK → `AdministrativeInstructionalMethodLookup.AdministrativeInstructionalMethodIdentifier` | Yes | Governed administrative instructional method. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence. |
| `minimum_hours` | `NUMERIC` |  | Yes | Minimum instructional hours. |
| `maximum_hours` | `NUMERIC` |  | Yes | Maximum instructional hours. |
| `increment` | `NUMERIC` |  | Yes | Permitted hours increment. |
| `interval` | `TEXT` |  | Yes | Source-defined hours interval. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseInstructionalMethodAssociation

**SQL identifier:** `academics.course_instructional_method_association`

Associates a course with instructional methods and delivery methods used as scheduling defaults.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `instructional_method_identifier` | `TEXT` | FK → `InstructionalMethodLookup.InstructionalMethodIdentifier` | Yes | Governed instructional method. |
| `instructional_delivery_method_identifier` | `TEXT` | FK → `InstructionalDeliveryMethodLookup.InstructionalDeliveryMethodIdentifier` | Yes | Governed delivery method. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseLevelLookup

**SQL identifier:** `academics.course_level_lookup`

Governed course-level definitions referenced by courses and sections.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_level_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `code` | `TEXT` |  | No | Institutionally governed course-level code. |
| `title` | `TEXT` |  | No | Human-readable name of the course level. |
| `description` | `TEXT` |  | Yes | Description of the course level. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## CourseLookup

**SQL identifier:** `academics.course_lookup`

A lookup table containing a list of courses that may be offered by a school or institution. The details include title, description, units, and other descriptive information.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `course_recognized_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Agent that acknowledges the validity of the course |
| `course_regulated_by_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Quality assurance organization that enforces the legal requirements of the course |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `course_offered_by_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Unique identifier for the score scale |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `academic_subject_identifier` | `TEXT` | FK → `AcademicSubject.AcademicSubjectIdentifier` | Yes | Identifier for the canonical academic subject assigned to the course. |
| `cip_code_identifier` | `TEXT` | FK → `CIPCodeLookup.CIPCodeIdentifier` | Yes | Identifier of the canonical Classification of Instructional Programs (CIP) code associated with this record. |
| `display_identifier` | `TEXT` |  | Yes | System-managed course identifier selected for display, independent of canonical identity and alternate identifiers. |
| `course_status_identifier` | `TEXT` | FK → `CourseStatusLookup.CourseStatusIdentifier` | Yes | Governed lifecycle status of the course definition. |
| `original_course_code` | `TEXT` |  | Yes | Legacy or historical course code under which the course was previously listed, such as before a catalog renumbering or system conversion. This is a source-facing code, not a foreign key to another GUIDE course row. |
| `offering_start_date` | `DATE` |  | Yes | The date on which the course first becomes available for institutional offering or catalog use. This is a course lifecycle attribute, not a revision identifier. |
| `offering_end_date` | `DATE` |  | Yes | The date after which the course is no longer available for institutional offering or catalog use. This is a course lifecycle attribute, not a revision identifier. |
| `subject_abbreviation` | `TEXT` |  | Yes | The alphabetic abbreviation of the academic department or discipline offering the course. |
| `number` | `TEXT` |  | No | The official reference number portion of a course identifier. This number normally designates the level of the course as well as the level of the individual expected to enroll in the course. |
| `title` | `TEXT` |  | No | The descriptive name given to a course of study offered in a school or other institution or organization. In departmentalized classes at the elementary, secondary, and postsecondary levels (and for staff development activities), this refers to the name by which a course is identified (e.g., American History, English III). For elementary and other non-departmentalized classes, it refers to any portion of the instruction for which a grade or report is assigned (e.g. reading, composition, spelling, and language arts). |
| `description` | `TEXT` |  | Yes | Catalog description of the course's subject matter, scope, and instructional content. |
| `repeatability_indicator` | `BOOLEAN` |  | No | Indicates whether or not the course can be repeated for credit |
| `repeatability_maximum_credit` | `NUMERIC` |  | Yes | The maximum hours for which the course may be taken for credit |
| `repeatability_maximum_number` | `INTEGER` |  | Yes | The maximum number of times the course may be taken or completed for credit |
| `syllabus_url` | `TEXT` |  | Yes | URL for course syllabus |
| `learning_outcomes` | `TEXT` |  | Yes | Text description of the learning outcomes designed for the course |
| `resources` | `TEXT` |  | Yes | Text, media and resources utilized during the course |
| `credit_unit_type` | `TEXT` |  | Yes | The type of credit (unit, semester, or quarter) associated with the credit hours earned for the course |
| `credit_value` | `NUMERIC` |  | Yes | The amount of credit available to the student who successfully meets the objectives of the course or learning opportunity based on the units defined by Credit Unit Type |
| `instruction_site_name` | `TEXT` |  | Yes | The name of the location at which the course is taught |
| `instruction_site_type` | `TEXT` |  | Yes | An indication of the type of location at which the course is taught |
| `level_type` | `TEXT` |  | Yes | The level of work which is reflected in the credits associated with the academic course being described or the level of the typical individual taking the academic course |
| `honors_type` | `TEXT` |  | Yes | An indication that the course is or can be counted as an honors course |
| `credit_basis_type` | `TEXT` |  | Yes | The type of enrollment associated with the credit hours for the course |
| `credit_level_type` | `TEXT` |  | Yes | The level of credit associated with the credit hours earned for the course |
| `instruction_method` | `TEXT` |  | Yes | The primary method of instruction used for the course |
| `narrative_explanation_grade` | `TEXT` |  | Yes | The narrative of the grade awarded to an individual in an academic course in those cases where a course does not receive a letter or numeric grade included in the grading scale of the Course Academic Grade Qualifier |
| `repeat_code` | `TEXT` |  | Yes | Indicates how the course repeat should be computed in the student's academic grade average |
| `academic_grade_scale_code` | `TEXT` |  | Yes | The grading scale used by an academic educational institution for an academic course |
| `certification_name_association` | `TEXT` |  | Yes | A description of the certification or recognition associated with this course (ex. Networking, CAD, etc.) |
| `code_system` | `TEXT` |  | Yes | A system that is used to identify the organization of subject matter and related learning experiences provided for the instruction of persons |
| `contact_minutes` | `NUMERIC` |  | Yes | The actual or estimated number of clock minutes required for course completion. This number is especially important for career and technical education course and may represent (in minutes) the clock hour requirement of the course, the number of minutes (or clock hours) of class time per week, times the number of equivalent weeks the class typically meets. |
| `duration` | `TEXT` |  | Yes | Estimated time it will take to complete a course |
| `estimated_cost` | `TEXT` |  | Yes | Estimated cost of a course |
| `language_of_instruction` | `TEXT` |  | Yes | The primary language or languages of the entity, even if it makes use of other languages (e.g. a course offered in English to teach Spanish would have an inLanguage of English, while a credential in Quebec could have an inLanguage of both French and English) |
| `learning_standard` | `TEXT` |  | Yes | Learning standard(s) to be taught by the course |
| `online_availability` | `TEXT` |  | Yes | Online location where the course can be pursued |
| `standard_association_indicator` | `BOOLEAN` |  | Yes | An indication whether a course is aligned with the established standards of a curriculum framework |
| `subject_url` | `TEXT` |  | Yes | The webpage that describes this entity |
| `instructional_delivery_mode` | `TEXT` |  | Yes | The primary setting or medium of delivery for the course |
| `level_characteristic` | `TEXT` |  | Yes | An indication of the general nature and difficulty of instruction provided throughout a course |
| `applicable_education_level` | `TEXT` |  | Yes | The education level, grade level or primary instructional level at which a course is intended |
| `interaction_mode` | `TEXT` |  | Yes | The primary type of interaction, synchronous or asynchronous, defined for the course |
| `nces_college_course_map_code` | `TEXT` |  | Yes | The code from the taxonomy system for coding postsecondary courses in NCES research studies |
| `corequisite_site_restriction_indicator` | `BOOLEAN` |  | Yes | Indicates that applicable corequisite components must be co-located at the same site. |
| `allow_multiple_section_waitlist_indicator` | `BOOLEAN` |  | Yes | Indicates whether a learner may simultaneously waitlist multiple sections of the same course. |
| `advanced_placement_course_code` | `TEXT` |  | Yes | Course areas for advanced placement or credit For a list of codes see http://apcentralcollegeboardcom/apc/public/courses/teachers_corner/indexhtml |
| `developmental_education_type` | `TEXT` |  | Yes | The category of developmental education |
| `work_based_learning_type` | `TEXT` |  | Yes | The category of work based learning |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `syllabus_body` | `TEXT` |  | Yes | The text of the syllabus for this course |
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

## CourseOrganizationUnitOwnership

**SQL identifier:** `academics.course_organization_unit_ownership`

A tenant-scoped association linking a stable course to one owning or administering internal organization unit. Preserves source ownership percentage without inferring a primary owner or requiring all percentages to total 100.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Course associated with the owning organization unit. |
| `organization_unit_identifier` | `TEXT` | PK, FK → `OrganizationUnit.OrganizationUnitIdentifier` | No | Internal organization unit that owns or administers the course. |
| `ownership_percentage` | `NUMERIC` |  | Yes | Source-reported percentage associated with this organization-unit ownership relationship. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association row was last updated. |

## CourseReportingDetail

**SQL identifier:** `academics.course_reporting_detail`

Preserves source-specific course reporting type and weight without assuming universal semantics.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `reporting_type` | `TEXT` |  | Yes | Source-defined reporting locality or type. |
| `course_weight` | `NUMERIC` |  | Yes | Source-reported course weight. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseRequisiteCondition

**SQL identifier:** `academics.course_requisite_condition`

Ordered evaluable condition within a course requisite rule, including course, score, level, program, credit, permission, or other conditions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_requisite_condition_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for one evaluable condition within a requisite rule. |
| `course_requisite_rule_identifier` | `TEXT` | FK → `CourseRequisiteRule.CourseRequisiteRuleIdentifier` | No | Rule to which this condition belongs. |
| `related_course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | Stable Course identity used when ConditionType is Course. |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Score scale used for a grade or test-score threshold when applicable. |
| `condition_sequence` | `INTEGER` |  | No | Order in which the condition is presented or evaluated. |
| `condition_group_number` | `INTEGER` |  | Yes | Optional grouping number for simple nested or grouped condition logic. |
| `logical_connector` | `TEXT` |  | Yes | Connector to the preceding condition within the rule or condition group. |
| `condition_type` | `TEXT` |  | No | Type of evaluable condition. |
| `requisite_timing` | `TEXT` |  | Yes | Timing relationship for a requisite condition. |
| `minimum_grade` | `TEXT` |  | Yes | Minimum grade required when applicable. |
| `numeric_threshold` | `NUMERIC` |  | Yes | Numeric threshold required by the condition when applicable. |
| `condition_value` | `TEXT` |  | Yes | Institution- or source-defined value used by non-course condition types. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was last updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CourseRequisiteRule

**SQL identifier:** `academics.course_requisite_rule`

Reusable governed rule defining registration requirements, denials, or warnings.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_requisite_rule_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for a reusable governed course requisite rule. |
| `code` | `TEXT` |  | Yes | Optional institution-defined code for the requisite rule. |
| `description` | `TEXT` |  | No | Human-readable description of the requisite rule. |
| `registration_effect` | `TEXT` |  | No | Registration behavior when the rule is evaluated. |
| `effective_start_date` | `DATE` |  | Yes | Date the rule becomes effective. |
| `effective_end_date` | `DATE` |  | Yes | Date the rule ceases to be effective. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was last updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CourseRequisiteRuleApplication

**SQL identifier:** `academics.course_requisite_rule_application`

Tenant-safe assignment of a reusable requisite rule to a stable Course.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable Course identity to which the rule applies. |
| `course_requisite_rule_identifier` | `TEXT` | PK, FK → `CourseRequisiteRule.CourseRequisiteRuleIdentifier` | No | Reusable requisite rule applied to the Course. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date the rule assignment was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the rule assignment was last updated. |

## CourseStatusLookup

**SQL identifier:** `academics.course_status_lookup`

Governed course lifecycle statuses with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed lookup value. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institutionally meaningful code. |
| `title` | `TEXT` |  | No | Human-readable title. |
| `description` | `TEXT` |  | Yes | Detailed description of the status governing a course's institutional availability or use. |
| `status_category` | `TEXT` |  | Yes | Normalized lifecycle category such as Active or Ended. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for crosswalk resolution. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseTermAssociation

**SQL identifier:** `academics.course_term_association`

A table associating courses to terms to indicate in which terms courses are offered as classes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_term_association_identifier` | `TEXT` | PK | No | Unique identifier for a course to term association item |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the course to term association item |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifier for a term |
| `course_term_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CourseTitle

**SQL identifier:** `academics.course_title`

Preserves repeating typed course titles.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `course_title_type_identifier` | `TEXT` | PK, FK → `CourseTitleTypeLookup.CourseTitleTypeIdentifier` | No | Governed course title type. |
| `title_text` | `TEXT` |  | No | Typed course title. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseTitleTypeLookup

**SQL identifier:** `academics.course_title_type_lookup`

Governed types used to classify course titles.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_title_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed lookup value. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institutionally meaningful code. |
| `title` | `TEXT` |  | No | Human-readable title. |
| `description` | `TEXT` |  | Yes | Detailed description of the course title type. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for crosswalk resolution. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseTopicAssociation

**SQL identifier:** `academics.course_topic_association`

Associates a stable course definition with governed topics.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Stable course definition. |
| `course_topic_identifier` | `TEXT` | PK, FK → `CourseTopicLookup.CourseTopicIdentifier` | No | Governed course topic. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CourseTopicLookup

**SQL identifier:** `academics.course_topic_lookup`

Governed course-topic definitions referenced by course associations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `course_topic_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed lookup value. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `code` | `TEXT` |  | No | Institutionally meaningful code. |
| `title` | `TEXT` |  | No | Human-readable name of the course topic. |
| `description` | `TEXT` |  | Yes | Detailed description of the course topic. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for crosswalk resolution. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Canonical creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Canonical update timestamp. |

## CredentialActivityAssociation

**SQL identifier:** `academics.credential_activity_association`

A table associating credentials to activities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_activity_association_identifier` | `TEXT` | PK | No | Unique identifier for the credential to activity association |
| `activity_identifier` | `TEXT` | FK → `ActivityLookup.ActivityIdentifier` | No | Unique identifier for the activity |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for credential |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CredentialAssessmentAssociation

**SQL identifier:** `academics.credential_assessment_association`

A table associating a credential to one or more assessment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_assessment_association_identifier` | `TEXT` | PK | No | Unique identifier for the credential to assessment association |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment or assignment |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |

## CredentialCareerAssociation

**SQL identifier:** `academics.credential_career_association`

A table associating a credential to one or more career lookup, including career pathway and career pathway component.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_career_association_identifier` | `TEXT` | PK | No | Unique identifier for the credential to career association |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Career pathway targeted by this record when the fact applies to the pathway as a whole. |
| `career_pathway_component_identifier` | `TEXT` | FK → `CareerPathwayComponent.CareerPathwayComponentIdentifier` | Yes | Career pathway component targeted by this record when the fact applies to a specific pathway node. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CredentialCompetencyAssociation

**SQL identifier:** `academics.credential_competency_association`

A table associating a credential to a competency.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_competency_association_identifier` | `TEXT` | PK | No | Unique identifier for the association between the credential and the competency |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## CredentialCourseAssociation

**SQL identifier:** `academics.credential_course_association`

A table associating a credential to one or more course.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_course_association_identifier` | `TEXT` | PK | No | Unique identifier for the credential to course association |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CredentialIssuingOrganizationAssociation

**SQL identifier:** `academics.credential_issuing_organization_association`

A table associating a credential to an issuing organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_issuing_organization_association_identifier` | `TEXT` | PK | No | Unique identifier for the association between the credential and the issuing organization |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential |
| `issuing_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CredentialLearningOutcomeAssociation

**SQL identifier:** `academics.credential_learning_outcome_association`

A table associating a credential to a learning outcome.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_learning_outcome_association_identifier` | `TEXT` | PK | No | Unique identifier for the association between the credential and the learning outcome |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CredentialLookup

**SQL identifier:** `academics.credential_lookup`

A lookup table that contains all existing approved and proposed credentials for issuance to learners.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_identifier` | `TEXT` | PK | No | Unique identifier for the credential or achievement |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `credential_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the type of academic credential, such as degree, certificate, diploma, or microcredential. |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `endorsed_by_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `name` | `TEXT` |  | No | Official name of the academic credential, degree, certificate, or other recognized achievement. |
| `abbreviation` | `TEXT` |  | Yes | The abbreviation or short name used to identify the credential or academic award |
| `description` | `TEXT` |  | Yes | Detailed description of the academic credential, degree, certificate, or other recognized achievement. |
| `narrative` | `TEXT` |  | Yes | A narrative of what is needed to earn the achievement |
| `field_of_study` | `TEXT` |  | Yes | Category, subject, area of study, discipline, or general branch of knowledge |
| `uri` | `TEXT` |  | Yes | A Uniform Resource Identifier for the credential |
| `credits_available` | `NUMERIC` |  | Yes | Credit hours associated with this entity, or credit hours possible |
| `image_url` | `TEXT` |  | Yes | A URL to the image representing the credential |
| `image_caption` | `TEXT` |  | Yes | The caption for the image representing the credential |
| `approval_status` | `TEXT` |  | No | Indicates the status of the credential between initial proposal and final approval for issuance |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `endorsed_indicator` | `BOOLEAN` |  | Yes | Indicates whether the curruclum for this credential's program has been provided by or endorsed by an industry-recognized credentialing body |
| `credential_engine_id` | `TEXT` |  | Yes | Credential registry number or CTID serving as the primary unique identifier in the Credential Engine Credential Registry. |
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

## CredentialSkillAssociation

**SQL identifier:** `academics.credential_skill_association`

A table associating a credential to one or more skill.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credential_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the credential to skill association |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Unique identifier for the credential or achievement |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## CreditCategoryLookup

**SQL identifier:** `academics.credit_category_lookup`

Governed academic-credit categories used for course and section credit specifications.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `credit_category_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `code` | `TEXT` |  | No | Governed credit-category code. |
| `title` | `TEXT` |  | No | Human-readable name of the credit category. |
| `description` | `TEXT` |  | Yes | Description of the credit category. |
| `credit_type` | `TEXT` |  | Yes | Higher-level source category of academic credit. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## Enrollment

**SQL identifier:** `academics.enrollment`

A tenant-scoped person-to-learning-offering enrollment record. For section registrations it preserves registration status, credit, grading choices, involvement dates, overrides, and waitlist position.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `enrollment_identifier` | `TEXT` | PK | No | Unique identifier for the enrollment |
| `role_identifier` | `TEXT` | FK → `RoleLookup.RoleIdentifier` | No | Unique identifier for the role |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Academic level at which the learner registered for the section. |
| `section_registration_status_identifier` | `TEXT` | FK → `SectionRegistrationStatusLookup.SectionRegistrationStatusIdentifier` | No | Governed current status of the person-section registration. |
| `grade_scheme_identifier` | `TEXT` | FK → `GradeSchemeLookup.GradeSchemeIdentifier` | Yes | Governed grade scheme elected or assigned for the registration. |
| `grade_mode_identifier` | `TEXT` | FK → `GradeModeLookup.GradeModeIdentifier` | Yes | Governed grade-reporting mode elected or assigned for the registration. |
| `override_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Academic period applied as a registration-specific override. |
| `override_site_identifier` | `TEXT` | FK → `SiteLookup.SiteIdentifier` | Yes | Institutional site applied as a registration-specific override. |
| `active_indicator` | `BOOLEAN` |  | No | Used to identify if the enrollment described in this entity is currently active or inactive |
| `status` | `TEXT` |  | No | The status of this enrollment (e.g. Pre-registered, Pending, Registered, Enrolled, Withdrawn, OnHold, WaitListed, etc.) |
| `exit_reason` | `TEXT` |  | Yes | The circumstances under which the person exited from membership in the learning experience |
| `start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The start date of the associated event |
| `end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The end date of the associated event |
| `offering_type` | `TEXT` |  | Yes | The type of education being offered (e.g. Collection, Course, Component) |
| `last_active_online_date` | `DATE` |  | Yes | The date on which the learner was last active in their online learning portal for this enrollment |
| `total_active_online_time` | `INTEGER` |  | Yes | The total time in seconds for which the learner was active in their online learning portal for this enrollment |
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
| `registration_status_date` | `DATE` |  | Yes | Date on which the current registration status was set. |
| `registration_credit_measure` | `TEXT` |  | Yes | Unit or standard used for the learner registration credit. |
| `registration_credit_value` | `NUMERIC` |  | Yes | Credit value for which the learner registered. |
| `originally_registered_date` | `DATE` |  | Yes | Date on which the person originally registered for the section. |
| `involvement_start_date` | `DATE` |  | Yes | Date the learner first attended or accessed the section. |
| `involvement_end_date` | `DATE` |  | Yes | Date the learner last attended or accessed the section. |
| `waitlist_priority_number` | `INTEGER` |  | Yes | Current queue position when the registration is waitlisted. |

## EnrollmentAcademicOutcome

**SQL identifier:** `academics.enrollment_academic_outcome`

Current transcriptable academic outcome for a person and course/enrollment, including awarded grade, credits, quality points, repeat treatment, and incomplete-lapse facts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `enrollment_academic_outcome_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier for the academic outcome. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person to whom the academic outcome belongs. |
| `enrollment_identifier` | `TEXT` | FK → `Enrollment.EnrollmentIdentifier` | Yes | Person-to-offering enrollment that produced the outcome when directly resolvable. |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Academic period in which the outcome was recorded. |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | Course associated with the transcriptable outcome when supplied independently of an enrollment identifier. |
| `grade_scheme_identifier` | `TEXT` | FK → `GradeSchemeLookup.GradeSchemeIdentifier` | Yes | Grade scheme governing the awarded grade. |
| `grade_definition_identifier` | `TEXT` | FK → `GradeDefinitionLookup.GradeDefinitionIdentifier` | Yes | Governed grade definition currently awarded for the outcome. |
| `credit_category_identifier` | `TEXT` | FK → `CreditCategoryLookup.CreditCategoryIdentifier` | Yes | Governed credit category associated with the outcome. |
| `current_grade_change_reason_identifier` | `TEXT` | FK → `GradeChangeReasonLookup.GradeChangeReasonIdentifier` | Yes | Reason associated with the most recently applied grade change when supplied by the source. |
| `recorded_date` | `DATE` |  | Yes | Date the current transcript grade/outcome was recorded. |
| `attempted_credit` | `NUMERIC` |  | Yes | Credit attempted for the course or enrollment represented by this outcome. |
| `earned_credit` | `NUMERIC` |  | Yes | Credit earned from the course or enrollment represented by this outcome. |
| `gpa_quality_points` | `NUMERIC` |  | Yes | Weighted quality points used in grade-point-average calculation. |
| `base_quality_points` | `NUMERIC` |  | Yes | Non-weighted or base quality points associated with the outcome. |
| `repeat_grade_treatment_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed treatment specifying how this repeated-course outcome participates in GPA calculation. |
| `incomplete_extension_date` | `DATE` |  | Yes | Date after which an incomplete grade may lapse or a default final grade may be applied. |
| `incomplete_default_grade_value` | `TEXT` |  | Yes | Default final grade value to apply if incomplete work is not resolved by the applicable deadline. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the academic outcome. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the transcript-grade/outcome record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was last updated. |

## EnrollmentAcademicOutcomeChange

**SQL identifier:** `academics.enrollment_academic_outcome_change`

Ordered historical grade-state changes for an EnrollmentAcademicOutcome, preserving prior grade, reason, recorded date, and incomplete-lapse values.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `enrollment_academic_outcome_change_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for one historical change to an enrollment academic outcome. |
| `enrollment_academic_outcome_identifier` | `TEXT` | FK → `EnrollmentAcademicOutcome.EnrollmentAcademicOutcomeIdentifier` | No | Academic outcome whose grade state changed. |
| `sequence_number` | `INTEGER` |  | Yes | Source-reported ordinal sequence of the grade change when available. |
| `grade_scheme_identifier` | `TEXT` | FK → `GradeSchemeLookup.GradeSchemeIdentifier` | Yes | Grade scheme applicable to this historical grade state. |
| `grade_definition_identifier` | `TEXT` | FK → `GradeDefinitionLookup.GradeDefinitionIdentifier` | Yes | Grade definition recorded by this change. |
| `grade_change_reason_identifier` | `TEXT` | FK → `GradeChangeReasonLookup.GradeChangeReasonIdentifier` | Yes | Governed reason for the change to the previously recorded grade. |
| `recorded_date` | `DATE` |  | Yes | Date the grade change was recorded. |
| `incomplete_extension_date` | `DATE` |  | Yes | Incomplete deadline associated with this historical grade state. |
| `incomplete_default_grade_value` | `TEXT` |  | Yes | Default final grade associated with this historical incomplete state. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical history row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical history row was last updated. |

## EnrollmentApproval

**SQL identifier:** `academics.enrollment_approval`

One source-reported approval associated with a person-to-section enrollment; approval entity and type remain source-defined for MVP.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `enrollment_identifier` | `TEXT` | PK, FK → `Enrollment.EnrollmentIdentifier` | No | Registration to which the approval applies. |
| `sequence_number` | `TEXT` | PK | No | Deterministic source-order sequence for the approval member. |
| `approval_entity` | `TEXT` |  | Yes | Source-defined entity or party granting approval. |
| `approval_type` | `TEXT` |  | Yes | Source-defined type of approval granted. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## EquivalencyRule

**SQL identifier:** `academics.equivalency_rule`

A table associating from institution and to institution courses in a transfer course equivalency rule.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `equivalency_rule_identifier` | `TEXT` | PK | No | Unique identifier for a transfer course equivalency rule |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `minimum_from_total_hours` | `NUMERIC` |  | Yes | Minimum total number of hours for all from courses for this rule to apply |
| `minimum_from_all_grades_required` | `TEXT` |  | Yes | Minimum grade for all from courses for this rule to apply |
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

## EquivalencyRuleFromCourse

**SQL identifier:** `academics.equivalency_rule_from_course`

A table containing one or more from institution courses for an individual transfer course equivalency rule.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `equivalency_rule_identifier` | `TEXT` | FK → `EquivalencyRule.EquivalencyRuleIdentifier` | No | Unique identifier for a transfer course equivalency rule |
| `equivalency_rule_from_course_identifier` | `TEXT` | PK | No | Unique identifier for a from course rule member |
| `from_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `from_course_subject_abbreviation` | `TEXT` |  | No | The alphabetic abbreviation of the academic department or discipline offering the course |
| `from_course_number` | `TEXT` |  | No | The identifying number assigned to a course |
| `from_effective_begin_year_month` | `TEXT` |  | Yes | Beginning effective year and month of the source course |
| `from_effective_end_year_month` | `TEXT` |  | Yes | Expiration month and year of the source course |
| `from_minimum_course_hours` | `NUMERIC` |  | Yes | Minimum course hours for course |
| `from_minimum_course_grade_required` | `TEXT` |  | Yes | Minimum grade for course |
| `from_matching_course_title` | `TEXT` |  | Yes | Title required for course to match the rule |
| `from_course_operator` | `TEXT` |  | Yes | Operator that connects the trailing from course to this course |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## EquivalencyRuleFromExam

**SQL identifier:** `academics.equivalency_rule_from_exam`

A table containing standardized exams for an individual equivalency rule.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `equivalency_rule_identifier` | `TEXT` | FK → `EquivalencyRule.EquivalencyRuleIdentifier` | No | Unique identifier for a transfer course equivalency rule |
| `equivalency_rule_from_exam_identifier` | `TEXT` | PK | No | Unique identifier for a from exam rule member |
| `standardized_test_identifier` | `TEXT` | FK → `StandardizedTestLookup.StandardizedTestIdentifier` | No | Unique identifier for the standardized test |
| `exam_minimum_score` | `NUMERIC` |  | Yes | Minimum score required |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## EquivalencyRuleToCourse

**SQL identifier:** `academics.equivalency_rule_to_course`

A table containing one or more to institution courses for an individual transfer course equivalency rule.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `equivalency_rule_to_course_identifier` | `TEXT` | PK | No | Unique identifier for a to course rule member |
| `equivalency_rule_identifier` | `TEXT` | FK → `EquivalencyRule.EquivalencyRuleIdentifier` | No | Unique identifier for a transfer course equivalency rule |
| `to_course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | Unique identifier for a course |
| `to_elective_indicator` | `BOOLEAN` |  | Yes | Indicator that the target course is a general or departmental elective |
| `to_course_operator` | `TEXT` |  | Yes | Operator that connects the trailing to course to this course |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## FlashCard

**SQL identifier:** `academics.flash_card`

A table containing individual flashcards used to master learning content.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `flash_card_identifier` | `TEXT` | PK | No | Unique identifier for the flash card |
| `flash_card_set_identifier` | `TEXT` | FK → `FlashCardSet.FlashCardSetIdentifier` | No | Unique identifier for the flash card set |
| `front_text` | `TEXT` |  | Yes | Text for the question, prompt, or term |
| `back_text` | `TEXT` |  | Yes | Text for the answer, explanation, or definition |
| `image_url` | `TEXT` |  | Yes | URL to an image associated with the question, prompt, or term |
| `image_placement` | `TEXT` |  | Yes | Indicator of whether the image belongs on the front or back |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## FlashCardSet

**SQL identifier:** `academics.flash_card_set`

A table indicating a collection of flashcards that should be grouped together.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `flash_card_set_identifier` | `TEXT` | PK | No | Unique identifier for the flash card set |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the assessment or assignment |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
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
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Revision of the Assessment referenced by this record. |

## GeneralEducationCategory

**SQL identifier:** `academics.general_education_category`

A lookup table containing descriptions of general education categories for an organization's general education program.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `general_education_category_identifier` | `TEXT` | PK | No | Unique identifier for the general education category |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `general_education_code` | `TEXT` |  | No | Institutional code used to represent the general education category |
| `general_education_code_status` | `TEXT` |  | No | Status of general education category |
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

## GradeChangeReasonLookup

**SQL identifier:** `academics.grade_change_reason_lookup`

Governed institution-defined reasons for changing a previously recorded academic grade.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `grade_change_reason_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier for the grade-change reason. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the grade-change reason. |
| `title` | `TEXT` |  | No | Human-readable name of the grade-change reason. |
| `description` | `TEXT` |  | Yes | Optional fuller explanation of the grade-change reason. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed reason. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the grade-change reason. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was last updated. |

## GradeDefinitionEquivalent

**SQL identifier:** `academics.grade_definition_equivalent`

Associates a grade definition with a grade considered equivalent under another grading scheme.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `grade_definition_identifier` | `TEXT` | PK, FK → `GradeDefinitionLookup.GradeDefinitionIdentifier` | No | Grade definition for which an equivalent grade is declared. |
| `equivalent_grade_definition_identifier` | `TEXT` | PK, FK → `GradeDefinitionLookup.GradeDefinitionIdentifier` | No | Grade definition considered equivalent in another grading scheme. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was last updated. |

## GradeDefinitionLookup

**SQL identifier:** `academics.grade_definition_lookup`

Governed grade values or numeric/range definitions belonging to a grade scheme, independent of any particular learner outcome.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `grade_definition_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier for one allowable grade definition. |
| `grade_scheme_identifier` | `TEXT` | FK → `GradeSchemeLookup.GradeSchemeIdentifier` | No | Governed grade scheme within which this grade definition is valid. |
| `grade_value_expression` | `TEXT` |  | No | Literal grade value or source-defined numeric/range expression for the grade definition. |
| `credit_applicability` | `TEXT` |  | Yes | Source-governed indication of the degree of academic credit for which the grade qualifies. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the grade definition. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the grade definition. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was last updated. |

## GradeModeLookup

**SQL identifier:** `academics.grade_mode_lookup`

Governed grade modes referenced by grade schemes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `grade_mode_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed grade-mode code. |
| `title` | `TEXT` |  | No | Human-readable name of the grade mode. |
| `description` | `TEXT` |  | Yes | Description of the grade mode. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## GradeSchemeLookup

**SQL identifier:** `academics.grade_scheme_lookup`

Governed grading schemes available for courses and sections.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `grade_scheme_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed grade-scheme code. |
| `title` | `TEXT` |  | No | Human-readable name of the grade scheme. |
| `description` | `TEXT` |  | Yes | Description of the grade scheme. |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Academic level associated with the grade scheme. |
| `grade_mode_identifier` | `TEXT` | FK → `GradeModeLookup.GradeModeIdentifier` | Yes | Governed grade mode associated with the grade scheme. |
| `start_date` | `DATE` |  | Yes | Date after which the scheme may be used. |
| `end_date` | `DATE` |  | Yes | Date after which the scheme may no longer be used. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## InstructionalDeliveryMethodLookup

**SQL identifier:** `academics.instructional_delivery_method_lookup`

Governed instructional-delivery modes such as face-to-face, online, or hybrid.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `instructional_delivery_method_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed delivery-method code. |
| `title` | `TEXT` |  | No | Display title. |
| `description` | `TEXT` |  | Yes | Description of the delivery method. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## InstructionalMethodLookup

**SQL identifier:** `academics.instructional_method_lookup`

Governed instructional methods such as lecture, laboratory, seminar, or clinical.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `instructional_method_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `abbreviation` | `TEXT` |  | Yes | Human-readable abbreviation. |
| `title` | `TEXT` |  | No | Human-readable name of the instructional method. |
| `description` | `TEXT` |  | Yes | Description of the instructional method. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## InstructionalPlatformLookup

**SQL identifier:** `academics.instructional_platform_lookup`

Governed technology platforms used to administer or deliver sections.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `instructional_platform_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed platform code. |
| `title` | `TEXT` |  | No | Human-readable name of the instructional platform. |
| `description` | `TEXT` |  | Yes | Description of the instructional platform. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## LearnerAcademicCredit

**SQL identifier:** `academics.learner_academic_credit`

One institutionally recognized award of academic credit to a learner, independent of the academic fact or evaluation that caused the credit to be recognized.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_academic_credit_identifier` | `TEXT` | PK | No | Unique identifier for one institutionally recognized award of academic credit to a learner. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner for whom the institution recognizes the academic credit. |
| `academic_credit_basis_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed broad basis on which the institution recognized this academic credit. |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | Receiving-institution course represented by the recognized credit when the credit has a specific institutional course equivalency. |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Academic level assigned to the recognized credit when applicable. |
| `credit_value` | `NUMERIC` |  | No | Quantity of academic credit recognized by the institution. |
| `credit_unit_type` | `TEXT` |  | Yes | Unit or measure in which the recognized academic credit is expressed. |
| `recognition_date` | `DATE` |  | Yes | Date on which the institution recognized the academic credit for the learner. |
| `revocation_date` | `DATE` |  | Yes | Date on which previously recognized academic credit was revoked or ceased to be recognized. |
| `revocation_reason` | `TEXT` |  | Yes | Institutional reason the recognized credit was revoked, when applicable. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerAcademicCreditLocalCourseOutcome

**SQL identifier:** `academics.learner_academic_credit_local_course_outcome`

Associates recognized learner academic credit with the institutional final-grade result that directly produced it.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_academic_credit_identifier` | `TEXT` | PK, FK → `LearnerAcademicCredit.LearnerAcademicCreditIdentifier` | No | Recognized learner academic credit whose academic provenance is identified. |
| `enrollment_academic_outcome_identifier` | `TEXT` | FK → `EnrollmentAcademicOutcome.EnrollmentAcademicOutcomeIdentifier` | No | Academic provenance: institutional enrollment-level academic outcome that caused the credit to be recognized. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerAcademicCreditPriorLearningEvaluation

**SQL identifier:** `academics.learner_academic_credit_prior_learning_evaluation`

Associates recognized learner academic credit with the learner-specific prior-learning evaluation that produced it.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_academic_credit_identifier` | `TEXT` | PK, FK → `LearnerAcademicCredit.LearnerAcademicCreditIdentifier` | No | Recognized learner academic credit whose academic provenance is identified. |
| `learner_prior_learning_evaluation_identifier` | `TEXT` | FK → `LearnerPriorLearningEvaluation.LearnerPriorLearningEvaluationIdentifier` | No | Academic provenance prior-learning evaluation that caused the credit to be recognized. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerAcademicCreditTestEvaluation

**SQL identifier:** `academics.learner_academic_credit_test_evaluation`

Associates recognized learner academic credit with the learner-specific test-credit evaluation that produced it.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_academic_credit_identifier` | `TEXT` | PK, FK → `LearnerAcademicCredit.LearnerAcademicCreditIdentifier` | No | Recognized learner academic credit whose academic provenance is identified. |
| `learner_test_credit_evaluation_identifier` | `TEXT` | FK → `LearnerTestCreditEvaluation.LearnerTestCreditEvaluationIdentifier` | No | Academic provenance test-credit evaluation that caused the credit to be recognized. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerAcademicCreditTransferEvaluation

**SQL identifier:** `academics.learner_academic_credit_transfer_evaluation`

Associates recognized learner academic credit with the learner-specific transfer-credit evaluation that produced it.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_academic_credit_identifier` | `TEXT` | PK, FK → `LearnerAcademicCredit.LearnerAcademicCreditIdentifier` | No | Recognized learner academic credit whose academic provenance is identified. |
| `learner_transfer_credit_evaluation_identifier` | `TEXT` | FK → `LearnerTransferCreditEvaluation.LearnerTransferCreditEvaluationIdentifier` | No | Academic provenance transfer-credit evaluation that caused the credit to be recognized. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerAcademicStandingAndStatus

**SQL identifier:** `academics.learner_academic_standing_and_status`

A table containing a history of learner academic standing and status determinations at secondary and post-secondary schools and institutions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `academic_standing_and_status_identifier` | `TEXT` | PK | No | Unique identifier for the academic standing and status record |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifier for a term |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `postsecondary_academic_standing_status` | `TEXT` |  | No | Status of the learner academic standing (active, inactive) |
| `postsecondary_enrollment_type` | `TEXT` |  | No | The enrollment type associated with the enrollment award level of a person at the beginning of a term |
| `postsecondary_enrollment_status` | `TEXT` |  | No | An indication of the student's enrollment status for a particular term as defined by the institution |
| `math_placement` | `TEXT` |  | Yes | An indication of the student's college readiness for math as defined by the institution |
| `english_placement` | `TEXT` |  | Yes | An indication of the student's college readiness for english as defined by the institution |
| `reading_placement` | `TEXT` |  | Yes | An indication of the student's college readiness for reading as defined by the institution |
| `completed_developmental_math_requirements` | `BOOLEAN` |  | Yes | An indication of whether the student completed all developmental math requirements during the term |
| `completed_developmental_english_requirements` | `BOOLEAN` |  | Yes | An indication of whether the student completed all developmental english requirements during the term |
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

## LearnerAssessmentAlignment

**SQL identifier:** `academics.learner_assessment_alignment`

Represents one contextual alignment of a learner assessment revision to one or more pathway, career-plan-step, or skill concepts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_assessment_alignment_identifier` | `TEXT` | PK | No | Unique identifier for the learner's association of their assessment to relevant items such as career pathway or skill |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the assessment participating in this alignment. |
| `career_pathway_identifier` | `TEXT` | FK → `CareerPathway.CareerPathwayIdentifier` | Yes | Identifier for associated career pathway |
| `learner_career_plan_step_identifier` | `TEXT` | FK → `LearnerCareerPlanStep.LearnerCareerPlanStepIdentifier` | Yes | Unique identifier for the learner's career plan details |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | Yes | Unique identifier for the skill |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | SourceSystemIdentifier for LearnerAssessmentAlignment. |
| `source_system_key_value` | `TEXT` |  | Yes | SourceSystemKeyValue for LearnerAssessmentAlignment. |
| `source_system_created_date` | `DATE` |  | Yes | SourceSystemCreatedDate for LearnerAssessmentAlignment. |
| `source_system_updated_date` | `DATE` |  | Yes | SourceSystemUpdatedDate for LearnerAssessmentAlignment. |
| `source_system_deleted_date` | `DATE` |  | Yes | SourceSystemDeletedDate for LearnerAssessmentAlignment. |
| `created_by` | `INTEGER` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `INTEGER` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `INTEGER` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerAssessmentAttempt

**SQL identifier:** `academics.learner_assessment_attempt`

A table containing a record of a learner's attempt or submission of an assessment or assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_assessment_attempt_identifier` | `TEXT` | PK | No | Unique identifier for the learner's assessment attempt or submission |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Unique identifier for the class |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `learner_assessment_result_identifier` | `TEXT` | FK → `LearnerAssessmentResult.LearnerAssessmentResultIdentifier` | Yes | Unique identifier for the assessment result |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `count` | `INTEGER` |  | Yes | The total number of attempts inclusive of the current attempt that have been registered against the assigned digital resource |
| `started_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Attempt was commenced. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `ended_at_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | An ISO 8601 date and time value expressed with millisecond precision that describes when the Attempt was completed or terminated. The value MUST be expressed using the format YYYY-MM-DDTHH:mm:ss.SSSZ set to UTC with no offset specified. |
| `duration` | `TEXT` |  | Yes | A time interval that represents the time taken to complete the Attempt. If a duration is specified the value MUST conform to the ISO 8601 duration format. |
| `content_type` | `TEXT` |  | Yes | A string value drawn from the list of IANA approved media types and subtypes that identifies the file format of the resource |
| `url` | `TEXT` |  | Yes | A URL or link to the web resource that contains the attempt or submission content |
| `body` | `TEXT` |  | Yes | The text that the learner entered for the attempt or submission |
| `submission_type` | `TEXT` |  | Yes | The type of attempt or submission (e.g. text entry, URL, upload, media recording, LTI launch, etc.) |
| `status` | `TEXT` |  | Yes | The status of this learner's attempt (e.g. Not started, in progress, submitted, etc.) |
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
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |

## LearnerAssessmentResult

**SQL identifier:** `academics.learner_assessment_result`

A table containing a person's assessment results or grade.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_assessment_result_identifier` | `TEXT` | PK | No | Unique identifier for the learner's assessment result or grade |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | Yes | Unique identifier for skill |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the assessment |
| `person_grade_reporter_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier of the person reporting class grades |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Unique identifier for the score scale |
| `learner_assessment_attempt_identifier` | `TEXT` | FK → `LearnerAssessmentAttempt.LearnerAssessmentAttemptIdentifier` | Yes | Unique identifier for the learner's assessment attempt or submission |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `mastery_level` | `TEXT` |  | Yes | Mastery level for this outcome based on the skill mastery schema |
| `descriptive_feedback` | `TEXT` |  | Yes | Text provided by the grader of the assessment indicating feedback that supports the score or mastery level received by the learner |
| `assessment_name` | `TEXT` |  | No | The name of the assessment |
| `assessment_short_name` | `TEXT` |  | Yes | An short name for an assessment |
| `assessed_date` | `DATE` |  | No | When the assessment took place |
| `grading_type` | `TEXT` |  | Yes | Type of grading performed for a class (letter grade, numeric, pass-fail) |
| `grading_date` | `DATE` |  | Yes | Date measurement of learning was graded |
| `minimum_score` | `TEXT` |  | Yes | States the minimum score that it is possible to achieve on this assessment |
| `maximum_score` | `TEXT` |  | Yes | States the maximum score that it is possible to achieve on this assessment |
| `optimum_score` | `TEXT` |  | Yes | States the passing score for this assessment |
| `score` | `NUMERIC` |  | Yes | States the score received by the learner on this assessment |
| `text_score` | `TEXT` |  | Yes | An optional non-numeric score value. If a scoreScale is assigned then the value must align with the scale. |
| `score_percentile` | `NUMERIC` |  | Yes | The percentile rank of a score is the percentage of scores in its frequency distribution that are equal to or lower than it |
| `score_status` | `TEXT` |  | Yes | The status of the score |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `status` | `TEXT` |  | Yes | Status of learner's assessment result (unspecified, active, deleted) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | Yes | Revision of the Assessment referenced by this record. |

## LearnerAssessmentRubricCriterionResult

**SQL identifier:** `academics.learner_assessment_rubric_criterion_result`

A table containing a person's results for a rubric criterion as it pertains to a specific assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_assessment_rubric_criterion_result_identifier` | `TEXT` | PK | No | Unique identifier for the person's assessment rubric criterion result |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `rubric_criterion_level_identifier` | `TEXT` | FK → `RubricCriterionLevel.RubricCriterionLevelIdentifier` | No | Unique identifier for the rubric criterion level |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `learner_assessment_attempt_identifier` | `TEXT` | FK → `LearnerAssessmentAttempt.LearnerAssessmentAttemptIdentifier` | Yes | Unique identifier for the learner's assessment attempt or submission |
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
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |

## LearnerClassAttendance

**SQL identifier:** `academics.learner_class_attendance`

A table containing a history of learner attendance at scheduled class meetings and activities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_class_attendance_identifier` | `TEXT` | PK | No | Unique identifier for the class attendance item |
| `person_class_attendance_reporter_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person identifier of the person reporting class attendance |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `attendance_event_date` | `DATE` |  | No | The date on which an attendance event takes place |
| `attendance_event_type` | `TEXT` |  | No | The type of attendance event |
| `attendance_status` | `TEXT` |  | No | The status of a person's attendance associated with an Attendance Event Type and Attendance Event Date in an organization-person-role context |
| `attendance_notes` | `TEXT` |  | Yes | Notes about the attendance item |
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

## LearnerCredential

**SQL identifier:** `academics.learner_credential`

A table containing a history of certifications, credentials, badges, or programs of study for which a learner has pursued regardless of the outcome of completion.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_credential_identifier` | `TEXT` | PK | No | Unique identifier for the learner's credential history, either in-progress or completed credentials, covering certificates, diplomas, degrees, academic records, etc. |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | Yes | Unique identifier for the credential |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `person_program_identifier` | `TEXT` | FK → `PersonProgram.PersonProgramIdentifier` | Yes | Unique identifier for the person-program relationship associated with the awarded credential |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `person_document_identifier` | `TEXT` | FK → `PersonDocument.PersonDocumentIdentifier` | Yes | Unique identifier for a person's document |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | The name of the credential or academic award |
| `uri` | `TEXT` |  | Yes | Uniform resource identifier for the learner credential |
| `program_of_study_name` | `TEXT` |  | Yes | Name of the program of study offering |
| `cip_code_identifier` | `TEXT` | FK → `CIPCodeLookup.CIPCodeIdentifier` | Yes | Identifier of the canonical Classification of Instructional Programs (CIP) code associated with this record. |
| `date` | `DATE` |  | Yes | The year, month and day or year and month on which the credential or academic award was conferred |
| `grade_point_average_cumulative` | `NUMERIC` |  | Yes | Cumulative grade point average |
| `grade_point_average_weighted_indicator` | `BOOLEAN` |  | No | Indicator that a grade point average was calculated with weighted factors |
| `grade_point_average_official_indicator` | `BOOLEAN` |  | Yes | Indicator that the GradePointAverage was from an official source |
| `high_school_diploma_type` | `TEXT` |  | Yes | The type of diploma/credential that is awarded to a person in recognition of his/her completion of the curricular requirements |
| `cohort_year` | `TEXT` |  | Yes | The school year in which the student entered the baseline group used for computing completion rates (e.g. high school, program) |
| `pesc_award_level_type` | `TEXT` |  | Yes | The category of award conferred by a college, university, or other postsecondary education institution as official recognition for the successful completion of a program of study |
| `ob_achievement_type` | `TEXT` |  | Yes | The type of achievement |
| `postsecondary_program_level` | `TEXT` |  | Yes | Level of the degree program |
| `level_conferred` | `TEXT` |  | Yes | The category of award conferred by a college, university, or other postsecondary education institution as official recognition for the successful completion of a program of study |
| `prerequisite_type` | `TEXT` |  | Yes | Prerequisite conditions for earning an credential or academic award |
| `requirements_url` | `TEXT` |  | Yes | A URL to a page that describes the requirements for the credential |
| `credit_hours_applied_other_program` | `TEXT` |  | Yes | Codes identifying the set of credit hours taken in other programs or degrees that were applied to the individual's degree |
| `dqp_categories_of_learning` | `TEXT` |  | Yes | The Lumina Foundation's Degree Qualifications Profile offers reference points for what students should know and be able to do upon completion of associate, bachelor's and master's degrees – in any field of study. The DQP Categories of Learning provide a profile of what degrees mean within which specific proficiencies may be defined |
| `professional_or_technical_academic_credential_conferred` | `TEXT` |  | Yes | The category of credential conferred by a state occupational licensing entity or industry organization for competency in a specific area measured by a set of pre-established standards |
| `high_school_student_class_rank` | `INTEGER` |  | Yes | The academic rank of a student in relation to his or her high school graduating class (e.g. 1, 2, 3) based on high school GPA |
| `size_of_high_school_graduating_class` | `INTEGER` |  | Yes | Size of the learner's high school graduation class |
| `grade_point_average` | `NUMERIC` |  | Yes | The value of the total quality points divided by the Credit Hours for Grade Point Average |
| `dual_credit_dual_enrollment_credits_awarded` | `NUMERIC` |  | Yes | The number of credits awarded a student by the postsecondary institution based on successful completion of dual credit/dual enrollment courses |
| `advanced_placement_credits_awarded` | `NUMERIC` |  | Yes | The number of credits awarded for an advanced placement exam |
| `course_total` | `INTEGER` |  | Yes | The total number of courses listed on a transcript. Used as a check digit for integrity purposes. |
| `credits_attempted_cumulative` | `NUMERIC` |  | Yes | The cumulative number of credits a person attempts to earn by taking courses during their enrollment in their current education institution as well as those credits transferred from an education institution in which the person had been previously enrolled |
| `credits_earned_cumulative` | `NUMERIC` |  | Yes | The cumulative number of credits a person earns by completing courses or examinations during their enrollment in the current education institution as well as those credits transferred from an education institution in which the person had been previously enrolled |
| `number_of_credits_attempted` | `NUMERIC` |  | Yes | The number of credits that a student can earn for enrolling in and completing a given course |
| `number_of_credits_earned` | `NUMERIC` |  | Yes | The number of credits an individual earns by the successful completion of a course |
| `doctoral_exams_required_type` | `TEXT` |  | Yes | A qualifier identifying the types of exams required of doctoral level individuals |
| `doctoral_exam_taken_date` | `DATE` |  | Yes | The date on which the individual took an exam for advancement in, continuation or completion of a doctoral program |
| `graduate_or_doctoral_exam_results_status` | `TEXT` |  | Yes | The individual's status in completing exams required for graduate or doctoral degree programs |
| `doctoral_candidacy_admit_indicator` | `TEXT` |  | Yes | The individual's status in being admitted as a doctoral candidate |
| `doctoral_candidacy_date` | `DATE` |  | Yes | The date on which the individual was admitted to doctoral candidate status |
| `thesis_or_dissertation_title` | `TEXT` |  | Yes | The title of the thesis or dissertation |
| `oral_defense_date` | `DATE` |  | Yes | The date on which the individual gave an oral defense |
| `oral_defense_completed_indicator` | `BOOLEAN` |  | No | An indication of the individual's completion of an oral defense. The requirement to conduct an oral defense by doctoral individuals may vary across institutions, programs, or fields of study. |
| `receiving_location_of_instruction` | `TEXT` |  | Yes | The type of location at which instruction or service takes place |
| `naics_code` | `TEXT` |  | Yes | ONET/OEWS: North American Industry Classification System (NAICS) code for the given industry |
| `format` | `TEXT` |  | Yes | The format in which the academic award or credential exists (e.g. OpenBadges 2.0) |
| `credential_first_issued_date` | `DATE` |  | Yes | Date of the first time the learner was issued this credential |
| `credential_issuance_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Timestamp of when the credential becomes valid |
| `credential_expiration_date` | `DATE` |  | Yes | The year, month and day on which an active credential held by a person will expire |
| `credential_description` | `TEXT` |  | Yes | The description of the academic award or credential |
| `credential_award_evidence_url` | `TEXT` |  | Yes | A URL to a page that describes the evidence that the learner met the criteria for attainment of the credential award |
| `credential_revoked_indicator` | `BOOLEAN` |  | No | Indicates whether the credential has been revoked by the credential provider |
| `credential_revoked_reason` | `TEXT` |  | Yes | Published reason for revocation of a credential award |
| `self_asserted_indicator` | `BOOLEAN` |  | No | Indicates whether the credential is self asserted or not |
| `status` | `TEXT` |  | Yes | Indicates the status of the credential or academic award in the process between the learner selecting to achieve it and the achievement being issued, rejected, or revoked |
| `narrative` | `TEXT` |  | Yes | A narrative that connects multiple pieces of evidence |
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

## LearnerCredentialDetails

**SQL identifier:** `academics.learner_credential_details`

A table detailing the learner credential evidence and activities associated with their credential.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_credential_details_identifier` | `TEXT` | PK | No | Unique identifier for the learner's credential details, including associations to credential evidence |
| `learner_credential_evidence_identifier` | `TEXT` | FK → `LearnerCredentialEvidence.LearnerCredentialEvidenceIdentifier` | No | Unique identifier for the learner credential evidence |
| `learner_credential_identifier` | `TEXT` | FK → `LearnerCredential.LearnerCredentialIdentifier` | No | Unique identifier for the learner's credential history, either in-progress or completed credentials, covering certificates, diplomas, degrees, academic records, etc. |
| `person_activity_identifier` | `TEXT` | FK → `PersonActivity.PersonActivityIdentifier` | Yes | Unique identifier for learner activity details |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCredentialDiscipline

**SQL identifier:** `academics.learner_credential_discipline`

Tenant-scoped association between a learner credential and one or more academic disciplines or fields of study represented by canonical AcademicDiscipline records.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_credential_discipline_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a learner-credential-to-academic-discipline relationship |
| `learner_credential_identifier` | `TEXT` | FK → `LearnerCredential.LearnerCredentialIdentifier` | No | Learner credential to which the academic discipline applies |
| `academic_discipline_identifier` | `TEXT` | FK → `AcademicDiscipline.AcademicDisciplineIdentifier` | No | Canonical academic discipline or field of study associated with the learner credential |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the relationship |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the learner-credential discipline relationship when independently supplied or deterministically generated |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCredentialEvidence

**SQL identifier:** `academics.learner_credential_evidence`

A table describing the evidence of a learner's achievement towards a credential.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_credential_evidence_identifier` | `TEXT` | PK | No | Unique identifier for the learner credential evidence |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `uri` | `TEXT` |  | Yes | A Uniform Resource Identifier for the learner credential evidence |
| `narrative` | `TEXT` |  | Yes | A narrative that describes the evidence and process of achievement that led to an assertion |
| `genre` | `TEXT` |  | Yes | A string that describes the type of evidence (e.g. Poetry, Prose, Film) |
| `audience` | `TEXT` |  | Yes | A description of the intended audience for a piece of evidence |
| `url` | `TEXT` |  | Yes | A link to a webpage that contains the evidence |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCredentialHonor

**SQL identifier:** `academics.learner_credential_honor`

Tenant-scoped association recording that a learner credential carries or was awarded a canonical academic honor. Separates the reusable AcademicHonor definition from the learner-specific credential fact.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_credential_honor_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an academic honor associated with a learner credential |
| `learner_credential_identifier` | `TEXT` | FK → `LearnerCredential.LearnerCredentialIdentifier` | No | Learner credential to which the academic honor applies |
| `academic_honor_identifier` | `TEXT` | FK → `AcademicHonor.AcademicHonorIdentifier` | No | Canonical academic honor awarded or associated with the learner credential |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the learner-credential honor association |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerCredentialSharingLog

**SQL identifier:** `academics.learner_credential_sharing_log`

A table containing a log of details for every instance that a learner's credential is shared with another person or organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_credential_sharing_log_identifier` | `TEXT` | PK | No | Unique identifier for the learner credential sharing log |
| `learner_credential_identifier` | `TEXT` | FK → `LearnerCredential.LearnerCredentialIdentifier` | No | Unique identifier for the learner's credential history, either in-progress or completed credentials, covering certificates, diplomas, degrees, academic records, etc. |
| `shared_to_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Unique identifier of the organization with whom the learner credential was shared |
| `shared_to_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier of the person with whom the learner credential was shared |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `sharing_method` | `TEXT` |  | Yes | A description of how the learner credential was shared with the recipient such as via a certain application API |
| `sharing_purpose` | `TEXT` |  | Yes | A description of the purpose for sharing the learner credential |
| `sharing_status` | `TEXT` |  | Yes | An indicator of whether the sharing was successful or not |
| `sharing_timestamp` | `TIMESTAMP WITH TIME ZONE` |  | Yes | The timestamp at which the learner credential was shared with the recipient |
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

## LearnerDegreePlan

**SQL identifier:** `academics.learner_degree_plan`

A table containing details about a learner-specific plan for completing a program of study.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_degree_plan_identifier` | `TEXT` | PK | No | Unique identifier for the learner's degree plan |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the learner's degree plan |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Unique identifier for a program of study offering |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `learner_degree_plan_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `program_of_study_catalog_version` | `TEXT` |  | Yes | Catalog year of the associated credential |
| `program_of_study_name` | `TEXT` |  | No | Name of the program of study offering |
| `degree_plan_basis` | `TEXT` |  | Yes | Original source of the learner-specific degree plan details (e.g. Learner, Template, Staff, AI, Other) |
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

## LearnerDegreePlanAvailability

**SQL identifier:** `academics.learner_degree_plan_availability`

A table containing details of the day to day availability of a learner to attend classes. The availability is used to assist a learner with class registration.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_degree_plan_availability_identifier` | `TEXT` | PK | No | Unique identifier for a learner availability item |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the learner availability item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `learner_degree_plan_availability_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `available_day_of_week` | `TEXT` |  | No | Day of the week the learner is available |
| `available_start_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Start time of the available time range |
| `available_end_time` | `TIMESTAMP WITH TIME ZONE` |  | No | End time of the available time range |
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

## LearnerDegreePlanItem

**SQL identifier:** `academics.learner_degree_plan_item`

An item within a learner degree plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_degree_plan_item_identifier` | `TEXT` | PK | No | Unique identifier for the learner degree plan details |
| `learner_degree_plan_identifier` | `TEXT` | FK → `LearnerDegreePlan.LearnerDegreePlanIdentifier` | No | Unique identifier for the learner's degree plan |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifer for the term on the plan |
| `program_requirement_identifier` | `TEXT` | FK → `ProgramRequirement.ProgramRequirementIdentifier` | No | Unique identifier for the program requirement addressed by this degree-plan item. |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | Unique identifier for the course on the plan |
| `sequence_number` | `INTEGER` |  | Yes | Order or sequence number of the requirement course in a degree plan |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `learner_degree_plan_revision_identifier` | `TEXT` | FK → `LearnerDegreePlan.RevisionIdentifier` | No | Revision of the LearnerDegreePlan referenced by this record. |

## LearnerDegreePlanPreferences

**SQL identifier:** `academics.learner_degree_plan_preferences`

A table containing the details of preferences a learner has identified to assist with creating a degree plan, including summer terms, campuses, and modalities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_degree_plan_preferences_identifier` | `TEXT` | PK | No | Unique identifier for a learner degree plan preferences item |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the learner degree plan preferences item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `learner_degree_plan_preferences_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `maximum_hours_per_term` | `NUMERIC` |  | Yes | Maximum hours allowed per term for registration |
| `summer_term_registration_indicator` | `BOOLEAN` |  | No | Indicator that the learner intends to register for a summer term |
| `preferred_campus` | `TEXT` |  | Yes | Preferred campus of an organization for learning and participation |
| `preferred_communication_modality` | `TEXT` |  | Yes | Preferred modality for communication (email, push notification, SMS, paper) |
| `preferred_course_delivery_modality` | `TEXT` |  | Yes | Preferred modality for course delivery (online, in-person, hybrid) |
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

## LearnerExternalCourse

**SQL identifier:** `academics.learner_external_course`

One course-level academic experience completed by a learner at an external institution, preserving the external academic fact independently of the receiving institution transfer-credit decision.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_external_course_identifier` | `TEXT` | PK | No | Unique identifier for one course-level academic experience completed by a learner at an external institution. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner who completed the external academic work. |
| `external_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization at which the external course was completed. |
| `external_course_code` | `TEXT` |  | Yes | Course code or identifier assigned by the external institution. |
| `external_course_title` | `TEXT` |  | Yes | Title of the course as represented by the external institution. |
| `external_academic_period` | `TEXT` |  | Yes | Academic period at the external institution in which the course was taken, when available. |
| `external_credit_value` | `NUMERIC` |  | Yes | Quantity of credit represented on the external academic record. |
| `external_credit_unit_type` | `TEXT` |  | Yes | Unit or measure used for the external credit value. |
| `external_grade` | `TEXT` |  | Yes | Grade or mark reported for the external course. |
| `external_quality_points` | `NUMERIC` |  | Yes | Quality points reported or derived for the external course when supplied by the source academic record. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerFinalGradeResult

**SQL identifier:** `academics.learner_final_grade_result`

Legacy aggregate grade/result structure retained provisionally for term-, program-, and other non-enrollment aggregate outcomes. Enrollment-level transcriptable course outcomes are modeled canonically in EnrollmentAcademicOutcome.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_final_grade_result_identifier` | `TEXT` | PK | No | Unique identifier for the final grade result |
| `result_category_identifier` | `TEXT` | FK → `ResultCategory.ResultCategoryIdentifier` | Yes | Unique identifier for the result category |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | Yes | Unique identifier for a program of study offering |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Unique identifier for the score scale |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `type` | `TEXT` |  | Yes | Indicates what this is the final grade of (e.g. class, course, term, program, competency, etc.) |
| `grading_status` | `TEXT` |  | Yes | The status of the grading process |
| `score` | `NUMERIC` |  | Yes | The score for the result. If a scoreScale is assigned then the value must align with the scale. |
| `text_score` | `TEXT` |  | Yes | An optional non-numeric score value. If a scoreScale is assigned then the value must align with the scale. |
| `score_date` | `DATE` |  | Yes | The date at which the score is assigned or there is an update to the result. The format is YYYY-MM-DD as defined in [ISO 8601]. |
| `comment` | `TEXT` |  | Yes | A human readable comment about the score |
| `earned_credit_type` | `TEXT` |  | Yes | Type of credit a learner earned and was awarded |
| `number_of_credits_attempted` | `NUMERIC` |  | Yes | The number of credits that a student can earn for enrolling in and completing a given course |
| `number_of_credits_earned` | `NUMERIC` |  | Yes | The number of credits an individual earns by the successful completion of a course |
| `course_gpa_applicability` | `TEXT` |  | Yes | An indicator of whether or not this course being described is included in the computation of the student’s Grade Point Average (GPA) |
| `course_grade_status_code` | `TEXT` |  | Yes | Additional information regarding the context of the given grade. (e.g. AuditedCourse, HonorsGrade, Incomplete, PassFailPass, PassFailFail, Withdrew, etc.) |
| `dual_enrollment_indicator` | `BOOLEAN` |  | Yes | An indicator of whether final grade result pertains to the learner's dual enrollment status |
| `course_override_school` | `TEXT` |  | Yes | The school where the credit was earned if different from the institution reporting |
| `total_number_of_courses` | `INTEGER` |  | Yes | The total number of courses listed on a transcript. Used as a check digit for integrity purposes. |
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

## LearnerFlashCardProgress

**SQL identifier:** `academics.learner_flash_card_progress`

A table storing a learner's progress in mastering the knowledge in the flashcard.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `flash_card_progress_identifier` | `TEXT` | PK | No | Unique identifier for the flash card progress record |
| `flash_card_identifier` | `TEXT` | FK → `FlashCard.FlashCardIdentifier` | No | Unique identifier for the flash card |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `last_reviewed_timestamp` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Timestamp of when the learner last reviewed the card |
| `progress_status` | `TEXT` |  | Yes | Indicates whether the learner marked the flash card as New, Learning, Reviewing, or Mastered |
| `review_count` | `INTEGER` |  | Yes | Number of times the learner has reviewed the card |
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

## LearnerInstructorClassRating

**SQL identifier:** `academics.learner_instructor_class_rating`

A table containing learner ratings of instructors and classes.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_instructor_class_rating_identifier` | `TEXT` | PK | No | Unique identifier for the instructor or class rating |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Unique identifier for the class |
| `instructor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person serving as the instructor associated with this class rating. |
| `hidden_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that hid the record |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `rater_anonymous_indicator` | `BOOLEAN` |  | Yes | Indicates whether the rater is anonymous |
| `rating_type` | `TEXT` |  | No | Indicates whether the rating is for the instructor, class, or both |
| `rating_value` | `TEXT` |  | Yes | Numeric or enumerated rating value |
| `rating_description` | `TEXT` |  | Yes | Description of rating value |
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

## LearnerInstructorClassRatingComment

**SQL identifier:** `academics.learner_instructor_class_rating_comment`

A table containing comments on instructor or class ratings.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_instructor_class_rating_comment_identifier` | `TEXT` | PK | No | Unique identifier for the instructor or class rating comment |
| `learner_instructor_class_rating_identifier` | `TEXT` | FK → `LearnerInstructorClassRating.LearnerInstructorClassRatingIdentifier` | No | Unique identifier for the associated instructor class rating |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `parent_instructor_class_rating_comment_identifier` | `TEXT` | FK → `LearnerInstructorClassRatingComment.LearnerInstructorClassRatingCommentIdentifier` | Yes | Unique identifier for the parent instructor class rating comment |
| `hidden_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that hid the record |
| `comment` | `TEXT` |  | No | The text of the comment |
| `plans_to_adjust_class_indicator` | `BOOLEAN` |  | Yes | States whether the instructor plans to adjust the class based on the feedback in the rating |
| `plans_to_adjust_instruction_methods_indicator` | `BOOLEAN` |  | Yes | States whether the instructor plans to adjust the instruction method based on the feedback in the rating |
| `hidden_indicator` | `BOOLEAN` |  | No | Indicates whether the comment is hidden from public view |
| `hidden_date` | `DATE` |  | Yes | Date record was hidden |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerPriorLearningEvaluation

**SQL identifier:** `academics.learner_prior_learning_evaluation`

One institutional evaluation of a learner prior-learning claim or evidence for academic recognition.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_prior_learning_evaluation_identifier` | `TEXT` | PK | No | Unique identifier for one institutional evaluation of learner prior learning. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner whose prior learning is being evaluated. |
| `evaluation_date` | `DATE` |  | Yes | Date on which the institution evaluated the prior learning. |
| `evaluation_outcome` | `TEXT` |  | No | Outcome of the learner-specific prior-learning evaluation. |
| `comment` | `TEXT` |  | Yes | Optional explanation of the prior-learning evaluation. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerPriorLearningEvaluationEvidence

**SQL identifier:** `academics.learner_prior_learning_evaluation_evidence`

Associates one or more prior-learning evidence items with a learner-specific prior-learning evaluation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_prior_learning_evaluation_identifier` | `TEXT` | PK, FK → `LearnerPriorLearningEvaluation.LearnerPriorLearningEvaluationIdentifier` | No | Learner-specific prior-learning evaluation. |
| `learner_prior_learning_evidence_identifier` | `TEXT` | PK, FK → `LearnerPriorLearningEvidence.LearnerPriorLearningEvidenceIdentifier` | No | Prior-learning evidence item considered in the evaluation. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerPriorLearningEvidence

**SQL identifier:** `academics.learner_prior_learning_evidence`

One documented item or body of prior-learning evidence submitted or recognized for learner-specific prior-learning evaluation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_prior_learning_evidence_identifier` | `TEXT` | PK | No | Unique identifier for one documented prior-learning evidence item. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner to whom the prior-learning evidence pertains. |
| `evidence_type` | `TEXT` |  | Yes | Broad kind of prior-learning evidence. |
| `name` | `TEXT` |  | No | Human-readable name for the prior-learning evidence. |
| `description` | `TEXT` |  | Yes | Description of the prior-learning evidence. |
| `uri` | `TEXT` |  | Yes | URI or location of the evidence when externally addressable. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerStandardizedTestResult

**SQL identifier:** `academics.learner_standardized_test_result`

A table containing a person's standardized test results or scores.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `standardized_test_result_identifier` | `TEXT` | PK | No | Unique identifier for the standardized test result |
| `standardized_test_identifier` | `TEXT` | FK → `StandardizedTestLookup.StandardizedTestIdentifier` | No | Unique identifier for the standardized test |
| `administering_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `person_document_identifier` | `TEXT` | FK → `PersonDocument.PersonDocumentIdentifier` | Yes | Unique identifier for a person's document |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `test_date` | `DATE` |  | No | Date of the test |
| `test_name` | `TEXT` |  | No | Name identifying the test |
| `test_acronym` | `TEXT` |  | Yes | Abbreviation to identify the test |
| `test_type` | `TEXT` |  | Yes | Type of test completed |
| `test_score` | `TEXT` |  | No | Score awarded for completing the test |
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

## LearnerStudyPlan

**SQL identifier:** `academics.learner_study_plan`

A table representing a learner's study plan including as it may pertain to an assessment or goal.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_study_plan_identifier` | `TEXT` | PK | No | Unique identifier for the study plan |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | Yes | Unique identifier for the assessment |
| `person_goal_identifier` | `TEXT` | FK → `PersonGoal.PersonGoalIdentifier` | Yes | Unique identifier for the person goal |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `start_date` | `DATE` |  | Yes | Date the study plan starts |
| `end_date` | `DATE` |  | Yes | Date the study plan ends |
| `status` | `TEXT` |  | Yes | Completion status of the study plan |
| `percentage_complete` | `NUMERIC` |  | Yes | Percentage of the study plan topics that the person has completed |
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

## LearnerStudySession

**SQL identifier:** `academics.learner_study_session`

A table representing planned time periods for which a learner expects to study a particular topic.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_study_session_identifier` | `TEXT` | PK | No | Unique identifier for the study session |
| `study_topic_identifier` | `TEXT` | FK → `StudyTopic.StudyTopicIdentifier` | Yes | Unique identifier for the study topic |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `planned_start_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the person plans to start the study session |
| `actual_start_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the person actually started the study session |
| `planned_duration` | `NUMERIC` |  | Yes | Planned duration of the study session in hours |
| `actual_duration` | `NUMERIC` |  | Yes | Actual duration of the study session in hours |
| `completion_status` | `TEXT` |  | Yes | Completion status of the study session |
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

## LearnerTestCreditEvaluation

**SQL identifier:** `academics.learner_test_credit_evaluation`

One institutional evaluation of a learner standardized-test result for academic credit or course equivalency.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_test_credit_evaluation_identifier` | `TEXT` | PK | No | Unique identifier for one learner-specific test-credit evaluation. |
| `standardized_test_result_identifier` | `TEXT` | FK → `LearnerStandardizedTestResult.StandardizedTestResultIdentifier` | No | Standardized-test result serving as the academic basis of the evaluation. |
| `equivalency_rule_identifier` | `TEXT` | FK → `EquivalencyRule.EquivalencyRuleIdentifier` | Yes | Reusable exam equivalency rule used in the evaluation when applicable. |
| `evaluation_date` | `DATE` |  | Yes | Date on which the institution evaluated the test result for academic recognition. |
| `evaluation_outcome` | `TEXT` |  | No | Outcome of the learner-specific test-credit evaluation. |
| `comment` | `TEXT` |  | Yes | Optional explanation of the test-credit decision. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerTransferCreditEvaluation

**SQL identifier:** `academics.learner_transfer_credit_evaluation`

One receiving-institution evaluation of external academic work for a learner, representing the learner-specific articulation or recognition decision.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_transfer_credit_evaluation_identifier` | `TEXT` | PK | No | Unique identifier for one learner-specific transfer-credit evaluation. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Learner whose external academic work is being evaluated. |
| `equivalency_rule_identifier` | `TEXT` | FK → `EquivalencyRule.EquivalencyRuleIdentifier` | Yes | Reusable equivalency rule used in the evaluation when applicable. |
| `evaluation_date` | `DATE` |  | Yes | Date on which the receiving institution made or recorded the transfer-credit evaluation. |
| `evaluation_outcome` | `TEXT` |  | No | Outcome of the learner-specific articulation decision. |
| `comment` | `TEXT` |  | Yes | Optional human-readable explanation of the learner-specific transfer-credit decision. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerTransferCreditEvaluationEquivalentCourse

**SQL identifier:** `academics.learner_transfer_credit_evaluation_equivalent_course`

Associates zero or more receiving-institution courses with a learner-specific transfer-credit evaluation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_transfer_credit_evaluation_identifier` | `TEXT` | PK, FK → `LearnerTransferCreditEvaluation.LearnerTransferCreditEvaluationIdentifier` | No | Learner-specific transfer-credit evaluation. |
| `course_identifier` | `TEXT` | PK, FK → `CourseLookup.CourseIdentifier` | No | Receiving-institution course recognized as equivalent in this evaluation. |
| `recognized_credit_value` | `NUMERIC` |  | Yes | Credit amount associated with this equivalent course in the evaluation when explicitly allocated. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearnerTransferCreditEvaluationSourceCourse

**SQL identifier:** `academics.learner_transfer_credit_evaluation_source_course`

Associates one or more learner external courses with a learner-specific transfer-credit evaluation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_transfer_credit_evaluation_identifier` | `TEXT` | PK, FK → `LearnerTransferCreditEvaluation.LearnerTransferCreditEvaluationIdentifier` | No | Learner-specific transfer-credit evaluation. |
| `learner_external_course_identifier` | `TEXT` | PK, FK → `LearnerExternalCourse.LearnerExternalCourseIdentifier` | No | External course considered as source academic work in the evaluation. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## LearningOutcome

**SQL identifier:** `academics.learning_outcome`

A lookup table containing descriptions of learning outcomes that may be associated to skills, assessments, credentials, activities, courses, and programs of study.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_identifier` | `TEXT` | PK | No | Unique identifier for learning outcome |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `type` | `TEXT` |  | No | Type of the learning outcome |
| `uri` | `TEXT` |  | Yes | Resource identifier for the learning outcome definition |
| `status` | `TEXT` |  | No | Status of the learning outcome (unspecified, active, deleted, retired) |
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

## LearningOutcomeAssessmentAssociation

**SQL identifier:** `academics.learning_outcome_assessment_association`

A table associating a learning outcome to an assessment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_assessment_association_identifier` | `TEXT` | PK | No | Unique identifier for the learning outcome to assessment association |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |

## LearningOutcomeCourseAssociation

**SQL identifier:** `academics.learning_outcome_course_association`

A table associating a learning outcome to one or more course.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_course_association_identifier` | `TEXT` | PK | No | Unique identifier for the learning outcome to course association |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearningOutcomeProgramOfStudyAssociation

**SQL identifier:** `academics.learning_outcome_program_of_study_association`

A table associating a learning outcome to one or more program of study.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_program_of_study_association_identifier` | `TEXT` | PK | No | Unique identifier for the learning outcome to program of study association |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Unique identifier for a term |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Unique identifier for a program of study offering |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearningOutcomeSkillAssociation

**SQL identifier:** `academics.learning_outcome_skill_association`

A table associating learning outcomes to skills.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_outcome_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the learning outcome to skill association |
| `learning_outcome_identifier` | `TEXT` | FK → `LearningOutcome.LearningOutcomeIdentifier` | No | Unique identifier for learning outcome |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `mastery_level` | `TEXT` |  | Yes | Mastery level for this outcome based on the skill mastery schema |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearningResourceLookup

**SQL identifier:** `academics.learning_resource_lookup`

A lookup table containing a list of learning resources, including library books, textbooks, LMS course content, videos, articles, chapters, reports, study guides, slide decks, practice exams, websites, and others.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learning_resource_identifier` | `TEXT` | PK | No | Unique identifier for the learning resource |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the learning resource |
| `learning_resource_parent_identifier` | `BIGINT` |  | Yes | Unique identifier for the parent of the learning resource |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `locked_for_editing_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that locked the record for editing |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `author_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Unique identifier of the author of the learning resource. |
| `name` | `TEXT` |  | No | A name for the record |
| `short_name` | `TEXT` |  | Yes | A short name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `learning_resource_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `author` | `TEXT` |  | Yes | The author(s) of the learning resource |
| `publisher` | `TEXT` |  | Yes | The name of the publisher of the learning resource |
| `editor` | `TEXT` |  | Yes | The name of the editor(s) of the learning resource |
| `type` | `TEXT` |  | Yes | Category of the format of the learning material |
| `url` | `TEXT` |  | Yes | The URL of the learning resource |
| `isbn` | `TEXT` |  | Yes | The International Standard Book Number |
| `doi` | `TEXT` |  | Yes | The digital object identifier for the learning resource |
| `issn` | `TEXT` |  | Yes | The International Standard Serial Number for the learning resource |
| `edition` | `TEXT` |  | Yes | The edition of the learning resource |
| `volume` | `TEXT` |  | Yes | The volume number |
| `issue` | `TEXT` |  | Yes | Issue number within the volume |
| `publication_year` | `TEXT` |  | Yes | The publication year of the learning resource |
| `page_start` | `INTEGER` |  | Yes | The page on which the learning resource starts |
| `page_end` | `INTEGER` |  | Yes | The page on which the learning resource ends |
| `library_of_congress_classification` | `TEXT` |  | Yes | The library of congress classification of the learning resource |
| `dewey_decimal_classification` | `TEXT` |  | Yes | The Dewey Decimal classification of the learning resource |
| `access_type` | `TEXT` |  | Yes | Indicates whether the access type is open, subscription, or restricted |
| `license_type` | `TEXT` |  | Yes | Indicates the type of license for the learning resource |
| `language` | `TEXT` |  | Yes | The language of the learning resource |
| `keywords` | `TEXT` |  | Yes | Keywords that categorize or relate to the learning resource |
| `purchase_url` | `TEXT` |  | Yes | The URL of a location to purchase the learning resource |
| `content` | `TEXT` |  | Yes | The body or HTML content of the learning resource |
| `sequence_number` | `INTEGER` |  | Yes | Number indicating where, within the collection of learning resources belonging to the parent, this one should be placed |
| `class_completion_requirement_indicator` | `BOOLEAN` |  | Yes | Indicates whether the class in which the learning resource is associated has the requirement that this resource is completed |
| `published_to_class_indicator` | `BOOLEAN` |  | Yes | Indicates whether the learning resource is visible to learners within the associated class |
| `class_unlock_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the learning resource becomes accessible to learners in the associated class |
| `class_lock_date_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time at which the learning resource stops being accessible to learners in the associated class |
| `for_instructional_design_indicator` | `BOOLEAN` |  | Yes | Indicates whether this learning resource is for assisting those working on instructional design or curriculum design for the organization |
| `version` | `TEXT` |  | Yes | The version of the learning resource |
| `current_version_indicator` | `BOOLEAN` |  | No | Indicates that this is the most current version of the learning resource |
| `accessibility_features` | `TEXT` |  | Yes | Metadata indicating what accessibility features the learning resource has, such as WCAG compliance |
| `locked_for_editing_indicator` | `BOOLEAN` |  | Yes | Indicates whether the learning resource is locked for editing |
| `workforce_endorsed_indicator` | `BOOLEAN` |  | Yes | Indicates whether this learning resource is endorsed and approved by a workforce partner of the organization |
| `status` | `TEXT` |  | No | Status of the lookup item (active, inactive) |
| `publish_date` | `DATE` |  | Yes | Date the learning resource was published |
| `media_type` | `TEXT` |  | Yes | The media type, or MIME type, of the learning resource |
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

## OrganizationLearningResourceAssociation

**SQL identifier:** `academics.organization_learning_resource_association`

A table associating an organization and a learning resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_learning_resource_identifier` | `TEXT` | PK | No | Unique identifier for the organization to learning resource association |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `status` | `TEXT` |  | No | Status of the organization to learning resource association (active, inactive) |
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
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## PersonAcademicLevelClassification

**SQL identifier:** `academics.person_academic_level_classification`

Associates a person with the latest governed student classification for an academic level.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonLookup.PersonIdentifier` | No | Person. |
| `academic_level_identifier` | `TEXT` | PK, FK → `AcademicLevelLookup.AcademicLevelIdentifier` | No | Academic level. |
| `student_classification_identifier` | `TEXT` | FK → `StudentClassificationLookup.StudentClassificationIdentifier` | No | Latest classification. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## PersonAcademicPeriod

**SQL identifier:** `academics.person_academic_period`

Tenant-scoped record representing one person in one academic period and serving as the parent for period-specific academic level, load, status, standing, and related facts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_academic_period_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person academic-period record |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person associated with the academic period |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Academic period associated with the person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the person academic-period record |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonAcademicPeriodAcademicLevel

**SQL identifier:** `academics.person_academic_period_academic_level`

Tenant-scoped association of a person academic-period record to one academic level, including an optional source-designated primary-level indicator.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_academic_period_identifier` | `TEXT` | PK, FK → `PersonAcademicPeriod.PersonAcademicPeriodIdentifier` | No | Person academic-period record to which the academic level applies |
| `academic_level_identifier` | `TEXT` | PK, FK → `AcademicLevelLookup.AcademicLevelIdentifier` | No | Academic level associated with the person in the academic period |
| `primary_academic_level_indicator` | `BOOLEAN` |  | Yes | Indicates whether this is the source-designated primary academic level for the person in the academic period |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association row was last updated |

## PersonAcademicPeriodAcademicLoad

**SQL identifier:** `academics.person_academic_period_academic_load`

Tenant-scoped calculated academic-load determination for one person in one academic period, optionally qualified by academic level.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_academic_period_academic_load_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person academic-load determination |
| `person_academic_period_identifier` | `TEXT` | FK → `PersonAcademicPeriod.PersonAcademicPeriodIdentifier` | No | Person academic-period record to which the load determination applies |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Optional academic level qualifying a by-level academic-load determination |
| `academic_load_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed calculated academic-load classification for the person and period |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the academic-load row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the academic-load row was last updated |

## PersonAcademicPeriodAcademicStatus

**SQL identifier:** `academics.person_academic_period_academic_status`

Tenant-scoped institution-defined academic-status determination for one person in one academic period, optionally qualified by academic level.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_academic_period_academic_status_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person academic-status determination |
| `person_academic_period_identifier` | `TEXT` | FK → `PersonAcademicPeriod.PersonAcademicPeriodIdentifier` | No | Person academic-period record to which the status determination applies |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Optional academic level qualifying a by-level academic-status determination |
| `academic_period_status_identifier` | `TEXT` | FK → `StudentAcademicPeriodStatusLookup.StudentAcademicPeriodStatusIdentifier` | No | Governed institution-defined academic status for the person and period |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the academic-status row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the academic-status row was last updated |

## PersonExternalEducation

**SQL identifier:** `academics.person_external_education`

A person-specific summary of prior or external postsecondary education at an institution outside the tenant, including attendance, credential, aggregate performance, and transcript-receipt facts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_external_education_identifier` | `TEXT` | PK | No | Unique GUIDE-owned identifier for one person-specific period or course of study at an external educational institution. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person whose external education is being represented. |
| `external_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | External educational institution at which the person studied. |
| `start_date` | `DATE` |  | Yes | Date the person began the represented course or period of study at the external institution. |
| `end_date` | `DATE` |  | Yes | Date the represented course or period of study at the external institution ended. |
| `graduation_date` | `DATE` |  | Yes | Date the person graduated from the external institution, when applicable. |
| `external_credential_name` | `TEXT` |  | Yes | Name or description of the academic credential awarded by the external institution. |
| `credential_award_date` | `DATE` |  | Yes | Date the external institution awarded the represented credential. |
| `credits_earned` | `NUMERIC` |  | Yes | Total credit amount reported for the represented external course of study. |
| `performance_measure` | `TEXT` |  | Yes | Source-reported overall performance measure for the external education, such as GPA. |
| `class_rank` | `INTEGER` |  | Yes | Reported ordinal class rank associated with the external course of study. |
| `class_size` | `INTEGER` |  | Yes | Reported size of the comparison class associated with ClassRank or ClassPercentile. |
| `class_percentile` | `NUMERIC` |  | Yes | Reported class percentile associated with the external course of study. |
| `thesis_title` | `TEXT` |  | Yes | Title of the thesis or dissertation associated with the external education, when applicable. |
| `transcript_received_date` | `DATE` |  | Yes | Date the tenant institution received the transcript documenting this external education. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the external education fact. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the external education record. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## PersonExternalEducationDiscipline

**SQL identifier:** `academics.person_external_education_discipline`

Associates a person external-education record with one or more canonical academic disciplines or fields of study.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_external_education_discipline_identifier` | `TEXT` | PK | No | Unique identifier for an external-education-to-discipline association. |
| `person_external_education_identifier` | `TEXT` | FK → `PersonExternalEducation.PersonExternalEducationIdentifier` | No | External education fact to which the discipline applies. |
| `academic_discipline_identifier` | `TEXT` | FK → `AcademicDiscipline.AcademicDisciplineIdentifier` | No | Canonical academic discipline or field of study associated with the external education. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## PersonExternalEducationHonor

**SQL identifier:** `academics.person_external_education_honor`

Associates a person external-education record with one or more canonical academic honors or recognitions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_external_education_honor_identifier` | `TEXT` | PK | No | Unique identifier for an external-education-to-academic-honor association. |
| `person_external_education_identifier` | `TEXT` | FK → `PersonExternalEducation.PersonExternalEducationIdentifier` | No | External education fact to which the academic honor applies. |
| `academic_honor_identifier` | `TEXT` | FK → `AcademicHonor.AcademicHonorIdentifier` | No | Canonical academic honor or recognition associated with the external education. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## PersonOfficeHours

**SQL identifier:** `academics.person_office_hours`

A table indicating when and where a person's office hours are offered.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_office_hours_identifier` | `TEXT` | PK | No | Unique identifier for the person office hours |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `start_date` | `DATE` |  | Yes | Start date for the office hours |
| `start_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Start time for the office hours |
| `end_date` | `DATE` |  | Yes | End date for the office hours |
| `end_time` | `TIMESTAMP WITH TIME ZONE` |  | Yes | End time for the office hours |
| `monday_indicator` | `BOOLEAN` |  | Yes | Monday meeting indicator |
| `tuesday_indicator` | `BOOLEAN` |  | Yes | Tuesday meeting indicator |
| `wednesday_indicator` | `BOOLEAN` |  | Yes | Wednesday meeting indicator |
| `thursday_indicator` | `BOOLEAN` |  | Yes | Thursday meeting indicator |
| `friday_indicator` | `BOOLEAN` |  | Yes | Friday meeting indicator |
| `saturday_indicator` | `BOOLEAN` |  | Yes | Saturday meeting indicator |
| `sunday_indicator` | `BOOLEAN` |  | Yes | Sunday meeting indicator |
| `building_key` | `TEXT` |  | Yes | Unique identifier for the building |
| `building_name` | `TEXT` |  | Yes | Common name of the building |
| `building_address` | `TEXT` |  | Yes | Address of the building |
| `building_room_number` | `TEXT` |  | Yes | Room number of the building |
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

## PersonPriorityRegistrationTimeSlot

**SQL identifier:** `academics.person_priority_registration_time_slot`

One priority-registration appointment or access window assigned to a person for an academic term.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonRegistrationEligibility.PersonIdentifier` | No | Person assigned the priority-registration window |
| `term_identifier` | `TEXT` | PK, FK → `PersonRegistrationEligibility.TermIdentifier` | No | Academic term for the priority-registration window |
| `time_slot_sequence_number` | `TEXT` | PK | No | Deterministic sequence of the priority-registration window in source order |
| `priority_registration_start_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the assigned priority-registration window begins |
| `priority_registration_end_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the assigned priority-registration window ends |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated |

## PersonProgram

**SQL identifier:** `academics.person_program`

Tenant-scoped relationship between a person and an academic program across recruitment, application, matriculation, and outcome stages, including the governing academic catalog and exact program curriculum when known.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person-program relationship |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person associated with the academic program |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Academic program associated with the person |
| `program_objective_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed classification of the lifecycle objective of the person-program relationship |
| `program_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed current status of the person-program relationship |
| `program_enrollment_status_identifier` | `TEXT` | FK → `ProgramEnrollmentStatusLookup.ProgramEnrollmentStatusIdentifier` | Yes | Institution-defined detailed status of the person-program enrollment |
| `admission_category_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed admission or entry category associated with the person-program relationship, such as first-time, transfer, or returning. |
| `program_start_date` | `DATE` |  | Yes | Actual or institutionally recognized beginning date of the person-program relationship |
| `program_end_date` | `DATE` |  | Yes | Actual or institutionally recognized ending date of the person-program relationship |
| `reporting_start_date` | `DATE` |  | Yes | Alternate effective start date used for reporting |
| `reporting_end_date` | `DATE` |  | Yes | Alternate effective end date used for reporting |
| `expected_graduation_date` | `DATE` |  | Yes | Expected calendar date of completion of the academic program |
| `starting_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Academic period associated with the beginning of the person-program relationship |
| `expected_graduation_term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Academic period in which program completion is expected |
| `primary_program_indicator` | `BOOLEAN` |  | No | Indicates whether this is the person's designated primary academic program relationship |
| `academic_level_identifier` | `TEXT` | FK → `AcademicLevelLookup.AcademicLevelIdentifier` | Yes | Current or source-designated academic level associated with the person-program relationship |
| `site_identifier` | `TEXT` | FK → `SiteLookup.SiteIdentifier` | Yes | Institutional site or campus associated with the person-program relationship |
| `academic_catalog_identifier` | `TEXT` | FK → `AcademicCatalog.AcademicCatalogIdentifier` | Yes | Academic catalog edition governing or associated with the person-program relationship. |
| `program_curriculum_identifier` | `TEXT` | FK → `ProgramCurriculum.ProgramCurriculumIdentifier` | Yes | Exact program curriculum against which this person-program relationship is governed or evaluated. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the person-program relationship |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `program_owner_organization_unit_identifier` | `TEXT` | FK → `OrganizationUnit.OrganizationUnitIdentifier` | Yes | Organizational unit administratively responsible for the person-program relationship |

## PersonProgramCredential

**SQL identifier:** `academics.person_program_credential`

Tenant-scoped relationship identifying the intended or selected credential outcome for a person-program relationship; distinct from an awarded learner credential.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_credential_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person-program credential target |
| `person_program_identifier` | `TEXT` | FK → `PersonProgram.PersonProgramIdentifier` | No | Person-program relationship for which the credential is intended or selected |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Credential definition intended or selected for the person-program relationship |
| `primary_credential_indicator` | `BOOLEAN` |  | Yes | Indicates whether this is the primary intended credential for the person-program relationship |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the relationship |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the person-program credential relationship when independently supplied |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonProgramDiscipline

**SQL identifier:** `academics.person_program_discipline`

Tenant-scoped dated relationship between a person-program record and an academic discipline, with optional administering unit and governed status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_discipline_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a person-program discipline relationship |
| `person_program_identifier` | `TEXT` | FK → `PersonProgram.PersonProgramIdentifier` | No | Person-program relationship to which the academic discipline applies |
| `academic_discipline_identifier` | `TEXT` | FK → `AcademicDiscipline.AcademicDisciplineIdentifier` | No | Institutionally governed academic discipline associated with the person-program relationship |
| `parent_person_program_discipline_identifier` | `TEXT` | FK → `PersonProgramDiscipline.PersonProgramDisciplineIdentifier` | Yes | Optional parent discipline relationship within the same person-program context, supporting hierarchies such as a concentration nested under a major. |
| `administering_organization_unit_identifier` | `TEXT` | FK → `OrganizationUnit.OrganizationUnitIdentifier` | Yes | Optional internal organization unit that administers the discipline for this person-program relationship |
| `discipline_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed status of the person-program discipline relationship |
| `start_date` | `DATE` |  | Yes | Date on which the academic discipline relationship begins |
| `end_date` | `DATE` |  | Yes | Date on which the academic discipline relationship ends |
| `reporting_start_date` | `DATE` |  | Yes | Alternate starting date for the academic discipline relationship used for institutional or regulatory reporting |
| `reporting_end_date` | `DATE` |  | Yes | Alternate ending date for the academic discipline relationship used for institutional or regulatory reporting |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the relationship |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key for the relationship when independently supplied or deterministically generated |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## PersonProgramProgressEvaluation

**SQL identifier:** `academics.person_program_progress_evaluation`

One authoritative evaluation of a person program against the exact governing program curriculum at a point in time, including overall unique-credit progress and aggregate requirement satisfaction.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_progress_evaluation_identifier` | `TEXT` | PK | No | Unique identifier for one authoritative evaluation of a person program against a governing curriculum. |
| `person_program_identifier` | `TEXT` | FK → `PersonProgram.PersonProgramIdentifier` | No | Person-program relationship whose progress is evaluated. |
| `program_curriculum_identifier` | `TEXT` | FK → `ProgramCurriculum.ProgramCurriculumIdentifier` | No | Exact program curriculum whose requirements were used for this evaluation. |
| `evaluation_date_time` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time at which the authoritative program-progress result was evaluated. |
| `total_credits_required` | `NUMERIC` |  | Yes | Overall number of unique academic credits required under this evaluation when the curriculum is credit-based. |
| `total_credits_applied` | `NUMERIC` |  | Yes | Overall number of unique academic credits recognized by this evaluation as counting toward the curriculum total. |
| `requirements_satisfied_indicator` | `BOOLEAN` |  | No | Indicates whether all requirements represented by this authoritative program-progress evaluation are satisfied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system that supplied the authoritative evaluation. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this evaluation in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## PersonProgramRequirementEvaluation

**SQL identifier:** `academics.person_program_requirement_evaluation`

The authoritative evaluated result for one program requirement within a person program progress evaluation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_requirement_evaluation_identifier` | `TEXT` | PK | No | Unique identifier for one evaluated program requirement within an authoritative program-progress evaluation. |
| `person_program_progress_evaluation_identifier` | `TEXT` | FK → `PersonProgramProgressEvaluation.PersonProgramProgressEvaluationIdentifier` | No | Authoritative program-progress evaluation containing this requirement result. |
| `program_requirement_identifier` | `TEXT` | FK → `ProgramRequirement.ProgramRequirementIdentifier` | No | Program requirement whose satisfaction was evaluated. |
| `requirement_satisfaction_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed evaluated satisfaction state of the program requirement. |
| `credits_satisfied` | `NUMERIC` |  | Yes | Credits recognized as satisfying this requirement when the requirement evaluation expresses a credit quantity. |
| `courses_satisfied` | `INTEGER` |  | Yes | Number of courses recognized as satisfying this requirement when the requirement evaluation expresses a course count. |
| `exception_applied_indicator` | `BOOLEAN` |  | No | Indicates that an approved learner-specific exception altered the ordinary interpretation or satisfaction of this requirement. |
| `evaluation_note` | `TEXT` |  | Yes | Optional human-readable explanation of the evaluated requirement result. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system that supplied the requirement evaluation. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this requirement evaluation in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## PersonProgramRequirementEvidence

**SQL identifier:** `academics.person_program_requirement_evidence`

One item of evidence recognized by an authoritative requirement evaluation as contributing to the evaluated result; credit-bearing evidence references LearnerAcademicCredit so provenance remains traceable.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_program_requirement_evidence_identifier` | `TEXT` | PK | No | Unique identifier for one item of evidence recognized as contributing to an evaluated program requirement. |
| `person_program_requirement_evaluation_identifier` | `TEXT` | FK → `PersonProgramRequirementEvaluation.PersonProgramRequirementEvaluationIdentifier` | No | Requirement evaluation to which this evidence contributed. |
| `evidence_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed broad classification of the evidence recognized by the requirement evaluation. |
| `learner_academic_credit_identifier` | `TEXT` | FK → `LearnerAcademicCredit.LearnerAcademicCreditIdentifier` | Yes | Recognized learner academic credit used as evidence when the requirement is satisfied wholly or partly by credit-bearing academic work. |
| `credits_counted` | `NUMERIC` |  | Yes | Amount of the referenced learner academic credit counted toward this requirement when explicitly reported by the authoritative evaluation. |
| `evidence_description` | `TEXT` |  | Yes | Optional authoritative description of non-credit evidence or other evidence context not represented by LearnerAcademicCredit. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system that supplied the requirement-evidence result. |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this requirement-evidence record in the source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was logically deleted. |

## PersonRegistrationEligibility

**SQL identifier:** `academics.person_registration_eligibility`

Tenant-scoped calculated registration-eligibility result for one person and academic term, including the student-specific registration window and alternate-PIN requirement.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonLookup.PersonIdentifier` | No | Person whose registration eligibility is evaluated |
| `term_identifier` | `TEXT` | PK, FK → `TermLookup.TermIdentifier` | No | Academic term for which registration eligibility is evaluated |
| `registration_eligibility_status` | `TEXT` |  | No | Calculated registration-eligibility status for the person and term |
| `alternate_pin_required_indicator` | `BOOLEAN` |  | No | Indicates whether an alternate registration PIN is required |
| `registration_start_date` | `DATE` |  | Yes | First date the person may register for the term |
| `registration_end_date` | `DATE` |  | Yes | Last date the person may register for the term |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the registration-eligibility result |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated |

## PersonRegistrationIneligibilityReason

**SQL identifier:** `academics.person_registration_ineligibility_reason`

One source-reported reason associated with a person-term registration-ineligibility result; it does not itself establish an authoritative PersonServiceRestriction or other underlying cause record.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonRegistrationEligibility.PersonIdentifier` | No | Person associated with the registration-eligibility result |
| `term_identifier` | `TEXT` | PK, FK → `PersonRegistrationEligibility.TermIdentifier` | No | Academic term associated with the registration-eligibility result |
| `reason_sequence_number` | `TEXT` | PK | No | Deterministic sequence of the source-reported reason within the eligibility result |
| `ineligibility_reason` | `TEXT` |  | No | Source-reported reason the person is not eligible to register |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated |

## PersonSkill

**SQL identifier:** `academics.person_skill`

A table containing details of a person and assigned skills.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_skill_identifier` | `TEXT` | PK | No | Unique identifier of the person skills item |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | Yes | Unique identifier for skill |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `input` | `TEXT` |  | Yes | Free-form input to describe the person skills |
| `years_of_experience` | `NUMERIC` |  | Yes | Indicates the number of years of experience the person has with the skill |
| `interest_level` | `INTEGER` |  | Yes | Indicates the person's interest level in the skill on a scale from 0 to 100 |
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

## PersonSkillEndorser

**SQL identifier:** `academics.person_skill_endorser`

A table containing an association between a person's skill and an organization or person endorsing the skill.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_skill_endorser_identifier` | `TEXT` | PK | No | Unique identifier for the endorser of the person's skill |
| `person_skill_identifier` | `TEXT` | FK → `PersonSkill.PersonSkillIdentifier` | No | Unique identifier of the person skills item |
| `endorser_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `endorser_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `comments` | `TEXT` |  | Yes | Comments from the endorser about the person's skill |
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

## PersonStudentType

**SQL identifier:** `academics.person_student_type`

Effective assignment of a governed student type to a person, optionally beginning in an administrative period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK, FK → `PersonLookup.PersonIdentifier` | No | Person. |
| `student_type_identifier` | `TEXT` | PK, FK → `StudentTypeLookup.StudentTypeIdentifier` | No | Governed student type. |
| `start_date` | `DATE` |  | No | Effective start date. |
| `administrative_period_identifier` | `TEXT` | FK → `AdministrativePeriodLookup.AdministrativePeriodIdentifier` | Yes | Starting administrative period. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## ProgramCredential

**SQL identifier:** `academics.program_credential`

Canonical tenant-scoped relationship identifying a credential outcome offered by or associated with an academic program of study, with optional effective dating and primary-outcome designation.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_credential_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a program-to-credential relationship |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Academic program of study that offers or leads to the credential |
| `credential_identifier` | `TEXT` | FK → `CredentialLookup.CredentialIdentifier` | No | Credential definition offered by or associated with the academic program |
| `primary_credential_indicator` | `BOOLEAN` |  | Yes | Indicates whether this credential is the primary credential outcome of the program relationship |
| `effective_start_date` | `DATE` |  | Yes | Date on which the program-to-credential relationship becomes effective |
| `effective_end_date` | `DATE` |  | Yes | Date on which the program-to-credential relationship ceases to be effective |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the relationship |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the program-to-credential relationship when independently supplied |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was created |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source relationship was last modified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ProgramCurriculum

**SQL identifier:** `academics.program_curriculum`

One institutionally defined requirement set applicable to a program, optionally associated with a formal academic catalog edition and carrying the authoritative overall credit requirement when credit-based.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_curriculum_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a program curriculum. |
| `program_of_study_identifier` | `TEXT` | FK → `ProgramOfStudyLookup.ProgramOfStudyIdentifier` | No | Durable program of study to which this curriculum belongs. |
| `academic_catalog_identifier` | `TEXT` | FK → `AcademicCatalog.AcademicCatalogIdentifier` | Yes | Academic catalog edition with which this curriculum is associated, when a formal catalog governs the curriculum. |
| `curriculum_code` | `TEXT` |  | Yes | Institutionally governed code identifying this curriculum when one exists. |
| `curriculum_name` | `TEXT` |  | Yes | Human-readable name for the curriculum. |
| `description` | `TEXT` |  | Yes | Narrative description of the curriculum and its applicability. |
| `total_credits_required` | `NUMERIC` |  | Yes | Overall number of unique academic credits required to complete this curriculum, when the curriculum is credit-based. |
| `effective_start_date` | `DATE` |  | Yes | Optional date on which this curriculum becomes applicable. |
| `effective_end_date` | `DATE` |  | Yes | Optional date on which this curriculum ceases to be applicable. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the curriculum. |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was created. |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was last modified. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## ProgramEnrollmentStatusLookup

**SQL identifier:** `academics.program_enrollment_status_lookup`

Institution-defined detailed statuses for a person’s academic-program enrollment, each rolling up to a governed broad program status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_enrollment_status_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an institution-defined program enrollment status |
| `code` | `TEXT` |  | No | Institutionally governed code for the detailed program enrollment status |
| `title` | `TEXT` |  | No | Display title of the detailed program enrollment status |
| `description` | `TEXT` |  | Yes | Description of the detailed program enrollment status |
| `program_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed broad status to which this institution-defined enrollment status rolls up |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | No | Identifier of the source system that supplied the record |
| `source_system_key_value` | `TEXT` |  | No | Source-system identifier for the program enrollment status definition |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## ProgramOfStudyLookup

**SQL identifier:** `academics.program_of_study_lookup`

A lookup table containing descriptions of programs of study, majors, or minors offered by organizations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_of_study_identifier` | `TEXT` | PK | No | Unique identifier for a program of study offering |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `offering_start_date` | `DATE` |  | Yes | The date the program of study was first officially offered by the sending institution |
| `offering_end_date` | `DATE` |  | Yes | The date the program of study was no longer officially offered by the sending institution |
| `accreditation_agency_name` | `TEXT` |  | Yes | The full name of an agency that accredited a school |
| `accreditation_expiration_date` | `DATE` |  | Yes | The year, month and day when an accreditation expires |
| `accreditation_award_date` | `DATE` |  | Yes | The year, month and day when an accreditation was awarded |
| `postsecondary_program_level` | `TEXT` |  | Yes | Level of the degree program |
| `outcomes` | `TEXT` |  | Yes | Text description of the completion outcomes |
| `cip_code_identifier` | `TEXT` | FK → `CIPCodeLookup.CIPCodeIdentifier` | Yes | Identifier of the canonical Classification of Instructional Programs (CIP) code associated with this record. |
| `offering_modality` | `TEXT` |  | Yes | Modalities for which this program of study can be pursued |
| `standard_occupation_classification_code` | `TEXT` |  | Yes | The Standard Occupation Classification code associated to the degree program |
| `url` | `TEXT` |  | Yes | Website for the program of study |
| `status` | `TEXT` |  | No | Offering status of the program of study (active, inactive) |
| `program_duration` | `NUMERIC` |  | Yes | The normal length in credit/contact hours of a person's program as published in the institution's catalogue, website, or other official documents |
| `program_duration_type` | `TEXT` |  | Yes | The type of hours (credit or contact) by which the normal length of a program of study is measured |
| `program_language_of_instruction` | `TEXT` |  | Yes | The primary language or languages of the entity, even if it makes use of other languages (e.g. a course offered in English to teach Spanish would have an inLanguage of English, while a credential in Quebec could have an inLanguage of both French and English) |
| `alternate_name` | `TEXT` |  | Yes | Alias for the entity including acronyms, alpha-numeric notations, and other forms of name abbreviations in common use such as PhD, MA, and BA |
| `specialization` | `TEXT` |  | Yes | Words or brief phrases describing the topicality of the entity; select subject terms from an existing enumeration of such terms |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ProgramRequirement

**SQL identifier:** `academics.program_requirement`

An identifiable academic obligation belonging to a program curriculum. Requirements may be hierarchical and may state broad credit/course expectations without encoding a universal degree-audit rules language.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_requirement_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a program requirement. |
| `program_curriculum_identifier` | `TEXT` | FK → `ProgramCurriculum.ProgramCurriculumIdentifier` | No | Curriculum to which this academic requirement belongs. |
| `parent_program_requirement_identifier` | `TEXT` | FK → `ProgramRequirement.ProgramRequirementIdentifier` | Yes | Optional parent requirement used to organize requirement groups or hierarchies. |
| `requirement_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed broad classification of the academic obligation. |
| `code` | `TEXT` |  | Yes | Institutionally governed code for the requirement when one exists. |
| `name` | `TEXT` |  | No | Name of the academic requirement. |
| `description` | `TEXT` |  | Yes | Narrative description of the academic obligation. |
| `minimum_credits` | `NUMERIC` |  | Yes | Minimum credits required for this requirement when credit-based. |
| `maximum_credits` | `NUMERIC` |  | Yes | Maximum credits that may be applied to this requirement when applicable. |
| `minimum_courses` | `INTEGER` |  | Yes | Minimum number of courses required when course-count based. |
| `sequence_number` | `INTEGER` |  | Yes | Optional display or logical ordering within the curriculum or parent requirement. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the requirement. |
| `source_system_created_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was created. |
| `source_system_updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the source record was last modified. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## ProgramRequirementCourse

**SQL identifier:** `academics.program_requirement_course`

An explicit descriptive association between a program requirement and a course that may be used by institutional curriculum or degree-audit processes; the association does not itself determine learner-specific satisfaction.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `program_requirement_course_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an explicit course-to-requirement association. |
| `program_requirement_identifier` | `TEXT` | FK → `ProgramRequirement.ProgramRequirementIdentifier` | No | Program requirement with which the course is explicitly associated. |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | No | Course explicitly associated with the program requirement. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the association. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted. |

## ResultCategory

**SQL identifier:** `academics.result_category`

A category given to a grouping of results or grade items (e.g. "Homework", "Exams").

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `result_category_identifier` | `TEXT` | PK | No | Unique identifier for the result category |
| `course_identifier` | `TEXT` | FK → `CourseLookup.CourseIdentifier` | Yes | The actual code that identifies the organization of subject matter and related learning experiences provided for the instruction of students |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | Yes | Unique identifier for the class |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `weight` | `NUMERIC` |  | Yes | Total weight of this grading category in calculation of the course final score |
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

## Rubric

**SQL identifier:** `academics.rubric`

A table to describe a grouping of criterion for guiding the evaluation of an assessment or assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `rubric_identifier` | `TEXT` | PK | No | Unique identifier for the rubric |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `url` | `TEXT` |  | Yes | The URL location where the rubric may be found |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `status` | `TEXT` |  | No | Status of the rubric (unspecified, active, deleted, archived, draft) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## RubricCriterion

**SQL identifier:** `academics.rubric_criterion`

A table containing a specific evaluation component within a rubric.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `rubric_criterion_identifier` | `TEXT` | PK | No | Unique identifier for the rubric criterion |
| `rubric_identifier` | `TEXT` | FK → `Rubric.RubricIdentifier` | No | Unique identifier for the rubric |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `category` | `TEXT` |  | Yes | A textual label for category by which the rubric criterion may be grouped |
| `sequence_number` | `INTEGER` |  | Yes | A numeric value representing this criterion's position in the criteria list for this rubric |
| `weight` | `NUMERIC` |  | Yes | A numeric weight assigned to this rubric criterion, used for scored rubrics |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## RubricCriterionLevel

**SQL identifier:** `academics.rubric_criterion_level`

A table containing predefined performance levels representing a specific degree of achievement of the rubric criterion.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `rubric_criterion_level_identifier` | `TEXT` | PK | No | Unique identifier for the rubric criterion level |
| `rubric_criterion_identifier` | `TEXT` | FK → `RubricCriterion.RubricCriterionIdentifier` | No | Unique identifier for the rubric criterion |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `feedback` | `TEXT` |  | Yes | Pre-defined feedback text to be relayed to the person or organization being evaluated This may include guidance and suggestions for improvement or development |
| `sequence_number` | `INTEGER` |  | Yes | A numeric value representing the level's position in the list of levels defined for the Rubric Criterion |
| `quality_label` | `TEXT` |  | No | A qualitative description of this degree of achievement used for column headers or row labels in tabular rubrics |
| `score` | `NUMERIC` |  | No | The points awarded for achieving this level |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ScoreScale

**SQL identifier:** `academics.score_scale`

A score scale or quality points scale available to be used with scored tests, assessments, and assignments (e.g. letter grades to percentage).

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `score_scale_identifier` | `TEXT` | PK | No | Unique identifier for the score scale |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `type` | `TEXT` |  | Yes | The type of score scale mapping. At present there is no predefined vocabulary. This should be used by an organization to differentiate between the score scales that it produces. |
| `status` | `TEXT` |  | No | Status of the score scale (active, inactive) |
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

## ScoreScaleValue

**SQL identifier:** `academics.score_scale_value`

The mapping between two score scales or quality points (e.g. from "A" to "90-100").

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `score_scale_value_identifier` | `TEXT` | PK | No | Unique identifier for the score scale value |
| `object_value_lhs` | `TEXT` |  | No | The left hand side value of the mapping relationship. The format is either a single value ('x') or a range ('x' - 'y'). In the case of a single value this is considered to be the inclusive lower value for the implied range. When a range is specified (lower-to-upper) the values are inclusive. |
| `object_value_rhs` | `TEXT` |  | No | The right hand side value of the mapping relationship. The format is either a single value ('x') or a range ('x' - 'y'). In the case of a single value this is considered to be the inclusive lower value for the implied range. When a range is specified (lower-to-upper) the values are inclusive. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## SectionDescriptionTypeLookup

**SQL identifier:** `academics.section_description_type_lookup`

Governed types for typed section descriptions.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `section_description_type_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed section-description-type code. |
| `title` | `TEXT` |  | No | Human-readable name of the section description type. |
| `description` | `TEXT` |  | Yes | Description of the description type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## SectionRegistrationStatusLookup

**SQL identifier:** `academics.section_registration_status_lookup`

Tenant-scoped governed definitions of person-to-section registration statuses, including headcount treatment and lifecycle availability.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `section_registration_status_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier for the status. |
| `code` | `TEXT` |  | No | Institutionally governed registration-status code. |
| `title` | `TEXT` |  | No | Display title of the registration status. |
| `description` | `TEXT` |  | Yes | Description of the registration status. |
| `headcount_status_indicator` | `BOOLEAN` |  | No | Indicates whether registrations with this status count toward section headcount. |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the status definition is available for current use. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | No | Source system supplying the definition. |
| `source_system_key_value` | `TEXT` |  | No | Source-system identifier for the status definition. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## SectionStatusLookup

**SQL identifier:** `academics.section_status_lookup`

Governed section statuses with source lineage and higher-level category.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `section_status_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed section-status code. |
| `title` | `TEXT` |  | No | Human-readable name of the section status. |
| `description` | `TEXT` |  | Yes | Description of the section status. |
| `category` | `TEXT` |  | Yes | Higher-level source category of the section status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## SectionTitleTypeLookup

**SQL identifier:** `academics.section_title_type_lookup`

Governed types for typed section titles.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `section_title_type_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier. |
| `code` | `TEXT` |  | No | Governed section-title-type code. |
| `title` | `TEXT` |  | No | Human-readable name of the section title type. |
| `description` | `TEXT` |  | Yes | Description of the title type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed value. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed value. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical row was created. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical row was updated. |

## SiteLookup

**SQL identifier:** `academics.site_lookup`

Governed institutional sites or campuses used to associate academic activity with a delivery or administrative location.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `site_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an institutional site or campus |
| `site_code` | `TEXT` |  | No | Institutionally governed code for the site |
| `site_name` | `TEXT` |  | No | Display name of the institutional site or campus |
| `site_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Optional governed classification of the institutional site |
| `active_indicator` | `BOOLEAN` |  | No | Indicates whether the site remains available for use |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Identifier of the source system that supplied the record |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the site |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## SkillAssociation

**SQL identifier:** `academics.skill_association`

A table associating primary and secondary skills.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `skill_association_identifier` | `TEXT` | PK | No | Unique identifier for skill connection |
| `primary_skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique primary identifier for skill |
| `secondary_skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | Yes | Unique secondary identifier for skill |
| `relationship` | `TEXT` |  | Yes | Relationship type from primary to secondary skill. Used to build ontology of skill hierarchy. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## SkillLookup

**SQL identifier:** `academics.skill_lookup`

A lookup table containing descriptions of skills that a person may have.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `skill_identifier` | `TEXT` | PK | No | Unique identifier for skill |
| `information_source_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | Yes | Organization identifier for the source of the information provided |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `mastery_schema` | `TEXT` |  | Yes | Identifier to a shema applicable to this skill (2-level mastery, 4-level mastery) |
| `bloom_taxonomy` | `TEXT` |  | Yes | One of: Knowledge, Comprehension, Application, Analysis, Synthesis or Evaluation |
| `uri` | `TEXT` |  | Yes | URI to external definition of Skill |
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

## SkillTag

**SQL identifier:** `academics.skill_tag`

A table containing the tag assigned to a skill primarily for searching and categorizing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `skill_tag_identifier` | `TEXT` | PK | No | Unique identifier for skill tag |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## SkillTagSkillAssociation

**SQL identifier:** `academics.skill_tag_skill_association`

A table associating a skill and skill tag.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `skill_tag_skill_association_identifier` | `TEXT` | PK | No | Unique identifier for the skill to tag association |
| `skill_identifier` | `TEXT` | FK → `SkillLookup.SkillIdentifier` | No | Unique identifier for skill |
| `skill_tag_identifier` | `TEXT` | FK → `SkillTag.SkillTagIdentifier` | No | Unique identifier for skill tag |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StandardizedTestLearningResourceAssociation

**SQL identifier:** `academics.standardized_test_learning_resource_association`

A table associating standardized tests to learning resources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `standardized_test_learning_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the standardized test to learning resource association |
| `standardized_test_identifier` | `TEXT` | FK → `StandardizedTestLookup.StandardizedTestIdentifier` | No | Unique identifier for the standardized test |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## StandardizedTestLookup

**SQL identifier:** `academics.standardized_test_lookup`

A lookup table containing information about standardized tests and professional examinations that may be required or encouraged for certain academic and career pathways.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `standardized_test_identifier` | `TEXT` | PK | No | Unique identifier for the standardized test |
| `provider_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to a school, school system, a state, business, or other agency or entity |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `subname` | `TEXT` |  | Yes | The full official subname of the test or exam |
| `acronym` | `TEXT` |  | Yes | The acronym or abbreviation for the test or exam |
| `scoring_method` | `TEXT` |  | Yes | A description of how the test is scored (e.g. "0-180 scale" or "Pass/Fail") |
| `minimum_passing_score` | `TEXT` |  | Yes | The minimum score required to pass the test according to the scoring method |
| `duration` | `NUMERIC` |  | Yes | The length in hours of the exam |
| `frequency` | `TEXT` |  | Yes | How often the test is administered |
| `eligibility_criteria` | `TEXT` |  | Yes | A description of the requirements one must meet in order to be eligible to take the exam |
| `cost` | `NUMERIC` |  | Yes | The registration fee in dollars to take the exam |
| `registration_url` | `TEXT` |  | Yes | The link to the web page to register for the exam |
| `accommodations` | `TEXT` |  | Yes | A description of the accommodations available for the exam |
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

## StudentAcademicPeriodStatusLookup

**SQL identifier:** `academics.student_academic_period_status_lookup`

Tenant-scoped governed definition of an institution-defined student academic-period status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_academic_period_status_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a student academic-period status |
| `code` | `TEXT` |  | No | Institutionally governed code for the student academic-period status |
| `title` | `TEXT` |  | No | Display title of the student academic-period status |
| `description` | `TEXT` |  | Yes | Description of the student academic-period status |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | No | Identifier of the source system that supplied the record |
| `source_system_key_value` | `TEXT` |  | No | Source-system identifier for the status definition |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## StudentAcademicPeriodStatusUsage

**SQL identifier:** `academics.student_academic_period_status_usage`

Natural-key association preserving each source-defined usage assigned to a student academic-period status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_academic_period_status_identifier` | `TEXT` | PK, FK → `StudentAcademicPeriodStatusLookup.StudentAcademicPeriodStatusIdentifier` | No | Status definition to which the source usage applies |
| `usage` | `TEXT` | PK | No | Source-defined context in which the status may be used |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association was updated |

## StudentClassificationLookup

**SQL identifier:** `academics.student_classification_lookup`

Governed studentclassification definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_classification_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying a student's academic classification, such as first-year, sophomore, or graduate. |
| `title` | `TEXT` |  | No | Human-readable name of the student academic classification. |
| `description` | `TEXT` |  | Yes | Detailed description of the student academic classification. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the student academic classification value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## StudentStatusLookup

**SQL identifier:** `academics.student_status_lookup`

Governed studentstatus definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the student enrollment or standing status. |
| `title` | `TEXT` |  | No | Human-readable name of the student enrollment or standing status. |
| `description` | `TEXT` |  | Yes | Detailed description of an institutional student enrollment or standing status. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the student enrollment or standing status value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## StudentTypeLookup

**SQL identifier:** `academics.student_type_lookup`

Governed studenttype definitions with source lineage.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `student_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier. |
| `code` | `TEXT` |  | No | Institution-defined code identifying the institution-defined student type. |
| `title` | `TEXT` |  | No | Human-readable name of the institution-defined student type. |
| `description` | `TEXT` |  | Yes | Detailed description of the institution-defined student type. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system. |
| `source_system_key_value` | `TEXT` |  | Yes | Identifier assigned to the institution-defined student type value by the originating source system. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Creation timestamp. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Update timestamp. |

## StudyTopic

**SQL identifier:** `academics.study_topic`

A table representing a study topic available for assigned to a study plan.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `study_topic_identifier` | `TEXT` | PK | No | Unique identifier for the study topic |
| `learner_study_plan_identifier` | `TEXT` | FK → `LearnerStudyPlan.LearnerStudyPlanIdentifier` | No | Unique identifier for the study plan |
| `name` | `TEXT` |  | Yes | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `priority` | `TEXT` |  | Yes | Priority of the topic to be studied (e.g. high, medium, low) |
| `status` | `TEXT` |  | Yes | Completion status of the study topic |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## StudyTopicLearningResourceAssociation

**SQL identifier:** `academics.study_topic_learning_resource_association`

A table associating study topics to one or more learning resources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `study_topic_learning_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the study topic to study resource association |
| `study_topic_identifier` | `TEXT` | FK → `StudyTopic.StudyTopicIdentifier` | No | Unique identifier for the study topic |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the study resource |
| `completion_status` | `TEXT` |  | Yes | Indicates the learner's completion status of the learning resource for this study topic |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## Syllabus

**SQL identifier:** `academics.syllabus`

A table containing information found on the class syllabus.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus |
| `class_identifier` | `TEXT` | FK → `ClassLookup.ClassIdentifier` | No | Unique identifier for the class |
| `instructor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `score_scale_identifier` | `TEXT` | FK → `ScoreScale.ScoreScaleIdentifier` | Yes | Unique identifier for the score scale |
| `locked_for_editing_by_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | Yes | Person identifier that locked the record for editing |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `description` | `TEXT` |  | Yes | A description for the record |
| `syllabus_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `language` | `TEXT` |  | Yes | The language in which the syllabus was written |
| `media_type` | `TEXT` |  | Yes | A string value drawn from the list of IANA approved media types and subtypes that identifies the file format of the syllabus |
| `instructor_office_hours` | `TEXT` |  | Yes | Text describing when the instructor's office hours take place |
| `teaching_assistant_office_hours` | `TEXT` |  | Yes | Text describing when the teaching assistant office hours take place |
| `prerequisite_knowledge_description` | `TEXT` |  | Yes | Description of prerequisite courses or knowledge required for the class |
| `course_objectives_description` | `TEXT` |  | Yes | Description of the primary course objectives |
| `course_format_philosophy_description` | `TEXT` |  | Yes | Description of the course format and instructor's teaching philosophy |
| `grading_procedures_description` | `TEXT` |  | Yes | Description of the grading procedures for the course |
| `student_workload_estimate` | `NUMERIC` |  | Yes | Estimate of the number of hours of outside study per credit hour required to pass the course |
| `learning_resource_study_recommendations_description` | `TEXT` |  | Yes | Description of recommendations the instructor has for learning resources and recommendations on how to study for the class |
| `version` | `TEXT` |  | Yes | The version of the syllabus |
| `current_version_indicator` | `BOOLEAN` |  | No | Indicates that this is the most current version of the syllabus |
| `locked_for_editing_indicator` | `BOOLEAN` |  | No | Indicates whether this record is locked for editing |
| `workforce_endorsed_indicator` | `BOOLEAN` |  | Yes | Indicates whether this syllabus is endorsed and approved by a workforce partner of the organization |
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

## SyllabusAcademicField

**SQL identifier:** `academics.syllabus_academic_field`

A table containing information about the academic field associated with the syllabus.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_academic_field_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus academic field |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus academic field |
| `syllabus_identifier` | `TEXT` | FK → `Syllabus.SyllabusIdentifier` | No | Unique identifier for the syllabus |
| `syllabus_academic_field_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `field_name` | `TEXT` |  | Yes | The name of the field |
| `cip_code_identifier` | `TEXT` | FK → `CIPCodeLookup.CIPCodeIdentifier` | Yes | Identifier of the canonical Classification of Instructional Programs (CIP) code associated with this record. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_revision_identifier` | `TEXT` | FK → `Syllabus.RevisionIdentifier` | No | Revision of the Syllabus referenced by this record. |

## SyllabusCompetencyAssociation

**SQL identifier:** `academics.syllabus_competency_association`

A table associating a competency or learning objective to a syllabus.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_competency_association_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus to competency association |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus to competency association |
| `syllabus_identifier` | `TEXT` | FK → `Syllabus.SyllabusIdentifier` | No | Unique identifier for the syllabus |
| `competency_identifier` | `TEXT` | FK → `Competency.CompetencyIdentifier` | No | Unique identifier for the competency or learning objective |
| `syllabus_competency_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_revision_identifier` | `TEXT` | FK → `Syllabus.RevisionIdentifier` | No | Revision of the Syllabus referenced by this record. |
| `competency_revision_identifier` | `TEXT` | FK → `Competency.RevisionIdentifier` | No | Revision of the Competency referenced by this record. |

## SyllabusLearningResourceAssociation

**SQL identifier:** `academics.syllabus_learning_resource_association`

A table associating a syllabus to a learning resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_learning_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus to learning resource association record |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus to learning resource association record |
| `syllabus_identifier` | `TEXT` | FK → `Syllabus.SyllabusIdentifier` | No | Unique identifier for the syllabus |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the learning resource |
| `syllabus_learning_resource_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `learning_resource_required_indicator` | `BOOLEAN` |  | Yes | Indicates whether the learning resource is required |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_revision_identifier` | `TEXT` | FK → `Syllabus.RevisionIdentifier` | No | Revision of the Syllabus referenced by this record. |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## SyllabusPolicy

**SQL identifier:** `academics.syllabus_policy`

A table containing policies for one or more syllabus.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_policy_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus policy |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus policy |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `syllabus_policy_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `text` | `TEXT` |  | Yes | The text describing and explaining the syllabus policy |
| `scope` | `TEXT` |  | Yes | Indicates whether the policy is scoped to the university, the department, the course, or the class |
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

## SyllabusPolicySyllabusAssociation

**SQL identifier:** `academics.syllabus_policy_syllabus_association`

A table associating a syllabus policy to a syllabus.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_policy_syllabus_association_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus policy to syllabus association |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus policy to syllabus association |
| `syllabus_identifier` | `TEXT` | FK → `Syllabus.SyllabusIdentifier` | No | Unique identifier for the syllabus |
| `syllabus_policy_identifier` | `TEXT` | FK → `SyllabusPolicy.SyllabusPolicyIdentifier` | No | Unique identifier for the syllabus policy |
| `syllabus_policy_syllabus_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_revision_identifier` | `TEXT` | FK → `Syllabus.RevisionIdentifier` | No | Revision of the Syllabus referenced by this record. |
| `syllabus_policy_revision_identifier` | `TEXT` | FK → `SyllabusPolicy.RevisionIdentifier` | No | Revision of the SyllabusPolicy referenced by this record. |

## SyllabusScheduleItem

**SQL identifier:** `academics.syllabus_schedule_item`

A table indicating an individual item that is outlined in the syllabus schedule. It may refer to weekly schedule items, course modules, textbook chapters/sections, or any other division of coursework outlined by the instructor over time.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_schedule_item_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus schedule item |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus schedule item |
| `syllabus_identifier` | `TEXT` | FK → `Syllabus.SyllabusIdentifier` | No | Unique identifier for the syllabus |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `syllabus_schedule_item_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `sequence_number` | `INTEGER` |  | Yes | Number indicating when, within the collection of scheduled items associated with this syllabus, this one should be completed |
| `date` | `DATE` |  | Yes | The date on which the scheduled item takes place according to the syllabus |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_revision_identifier` | `TEXT` | FK → `Syllabus.RevisionIdentifier` | No | Revision of the Syllabus referenced by this record. |

## SyllabusScheduleItemAssessmentAssociation

**SQL identifier:** `academics.syllabus_schedule_item_assessment_association`

A table associating a syllabus schedule item to an assessment or assignment.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_schedule_item_assessment_association_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus schedule item to assessment association record |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus schedule item to assessment association record |
| `syllabus_schedule_item_identifier` | `TEXT` | FK → `SyllabusScheduleItem.SyllabusScheduleItemIdentifier` | No | Unique identifier for the syllabus schedule item |
| `assessment_identifier` | `TEXT` | FK → `Assessment.AssessmentIdentifier` | No | Unique identifier for the assessment or assignment |
| `syllabus_schedule_item_assessment_association_revision_status` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_schedule_item_revision_identifier` | `TEXT` | FK → `SyllabusScheduleItem.RevisionIdentifier` | No | Revision of the SyllabusScheduleItem referenced by this record. |
| `assessment_revision_identifier` | `TEXT` | FK → `Assessment.RevisionIdentifier` | No | Revision of the Assessment referenced by this record. |

## SyllabusScheduleItemLearningResourceAssociation

**SQL identifier:** `academics.syllabus_schedule_item_learning_resource_association`

A table associating a syllabus schedule item to a learning resource.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `syllabus_schedule_item_learning_resource_association_identifier` | `TEXT` | PK | No | Unique identifier for the syllabus schedule item to learning resource association record |
| `revision_identifier` | `TEXT` | PK | No | Unique identifier for the revision to the syllabus schedule item to learning resource association record |
| `syllabus_schedule_item_identifier` | `TEXT` | FK → `SyllabusScheduleItem.SyllabusScheduleItemIdentifier` | No | Unique identifier for the syllabus schedule item |
| `learning_resource_identifier` | `TEXT` | FK → `LearningResourceLookup.LearningResourceIdentifier` | No | Unique identifier for the learning resource |
| `syllabus_schedule_item_learning_resource_association_r_96227eaa` | `TEXT` |  | Yes | The status of the revision (e.g. draft, under review, accepted, rejected, published, closed) |
| `note` | `TEXT` |  | Yes | A text note with additional information about the relationship between the syllabus schedule item and learning resource (e.g. "Only read Ch 2") |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `syllabus_schedule_item_revision_identifier` | `TEXT` | FK → `SyllabusScheduleItem.RevisionIdentifier` | No | Revision of the SyllabusScheduleItem referenced by this record. |
| `learning_resource_revision_identifier` | `TEXT` | FK → `LearningResourceLookup.RevisionIdentifier` | No | Revision of the LearningResource referenced by this record. |

## TermLookup

**SQL identifier:** `academics.term_lookup`

A lookup table that describes the academic terms offered by an organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `term_identifier` | `TEXT` | PK | No | Unique identifier for a term |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `code` | `TEXT` |  | No | Code identifying the academic year and term |
| `code_name` | `TEXT` |  | No | Name of the academic term designator |
| `begin_date` | `DATE` |  | Yes | Begin date for an academic term |
| `end_date` | `DATE` |  | Yes | End date for an academic term |
| `type` | `TEXT` |  | Yes | Type of the academic term (quarter, semester, trimester, other) |
| `code_description` | `TEXT` |  | Yes | Description of the academic term designator |
| `registration_start_date` | `DATE` |  | Yes | First date registration is open |
| `registration_end_date` | `DATE` |  | Yes | Last date registration is open |
| `withdrawal_deadline_date` | `DATE` |  | Yes | Normal withdrawal deadline date |
| `late_withdrawal_date` | `DATE` |  | Yes | Late withdrawal deadline date |
| `school_financial_aid_application_due_date` | `DATE` |  | Yes | Due date for financial aid application submission |
| `weighted_gpa_scale` | `NUMERIC` |  | Yes | Indicates the weighted GPA scale used during this term, such as 4.0, 5.0, 100, Other, School doesn't calculate |
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
| `academic_period_category` | `TEXT` |  | Yes | Category of the academic period in the source hierarchy. |
| `registration_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Governed registration status for the academic period. |
