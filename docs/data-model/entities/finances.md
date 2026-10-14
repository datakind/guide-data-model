# Entity: Finances

This page documents every table that belongs to the **Finances** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 37**

## Table of contents

- [FinancialAidAcademicProgressStatusLookup](#financialaidacademicprogressstatuslookup)
- [FinancialAidAcademicProgressTypeLookup](#financialaidacademicprogresstypelookup)
- [FinancialAidAwardPeriod](#financialaidawardperiod)
- [FinancialAidFund](#financialaidfund)
- [FinancialAidFundAvailability](#financialaidfundavailability)
- [FinancialAidFundClassification](#financialaidfundclassification)
- [FinancialAidYear](#financialaidyear)
- [LearnerAccountCharge](#learneraccountcharge)
- [LearnerDebtAccount](#learnerdebtaccount)
- [LearnerDebtRepaymentSchedule](#learnerdebtrepaymentschedule)
- [LearnerFinancialAidAcademicProgressStatus](#learnerfinancialaidacademicprogressstatus)
- [LearnerFinancialAidApplication](#learnerfinancialaidapplication)
- [LearnerFinancialAidApplicationIndependenceCriterion](#learnerfinancialaidapplicationindependencecriterion)
- [LearnerFinancialAidApplicationOutcome](#learnerfinancialaidapplicationoutcome)
- [LearnerFinancialAidApplicationRecipient](#learnerfinancialaidapplicationrecipient)
- [LearnerFinancialAidAward](#learnerfinancialaidaward)
- [LearnerFinancialAidAwardAggregate](#learnerfinancialaidawardaggregate)
- [LearnerFinancialAidAwardPeriod](#learnerfinancialaidawardperiod)
- [LearnerFinancialAidAwardPeriodAcademicPeriod](#learnerfinancialaidawardperiodacademicperiod)
- [LearnerFinancialAidContributor](#learnerfinancialaidcontributor)
- [LearnerFinancialAidContributorFinancialProfile](#learnerfinancialaidcontributorfinancialprofile)
- [LearnerFinancialAidNeedByMethodology](#learnerfinancialaidneedbymethodology)
- [LearnerFinancialAidNeedSummary](#learnerfinancialaidneedsummary)
- [LearnerFinancialPlan](#learnerfinancialplan)
- [LearnerFinancialPlanExpense](#learnerfinancialplanexpense)
- [LearnerFinancialPlanIncomeSource](#learnerfinancialplanincomesource)
- [LearnerScholarship](#learnerscholarship)
- [LearnerThirdPartyBenefit](#learnerthirdpartybenefit)
- [LearnerVeteransBenefits](#learnerveteransbenefits)
- [OrganizationAttendanceCosts](#organizationattendancecosts)
- [OrganizationMedianAidAwardedByEFC](#organizationmedianaidawardedbyefc)
- [OrganizationTuition](#organizationtuition)
- [OrganizationTuitionFee](#organizationtuitionfee)
- [PersonFinances](#personfinances)
- [ScholarshipCollegeAssociation](#scholarshipcollegeassociation)
- [ScholarshipInformation](#scholarshipinformation)
- [ScholarshipLookup](#scholarshiplookup)

---

## FinancialAidAcademicProgressStatusLookup

**SQL identifier:** `finances.financial_aid_academic_progress_status_lookup`

Tenant-scoped governed definition of an institution financial-aid satisfactory academic progress status.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_academic_progress_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed SAP status |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed status |
| `code` | `TEXT` |  | No | Institution-defined code for the financial-aid SAP status |
| `title` | `TEXT` |  | No | Display title for the financial-aid SAP status |
| `description` | `TEXT` |  | Yes | Description of the financial-aid SAP status |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed status |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |

## FinancialAidAcademicProgressTypeLookup

**SQL identifier:** `finances.financial_aid_academic_progress_type_lookup`

Tenant-scoped governed definition of a financial-aid satisfactory academic progress evaluation type.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_academic_progress_type_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the governed SAP type |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the governed type |
| `code` | `TEXT` |  | No | Institution-defined code for the financial-aid academic-progress type |
| `title` | `TEXT` |  | No | Display title for the financial-aid academic-progress type |
| `description` | `TEXT` |  | Yes | Description of the financial-aid academic-progress type |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the governed type |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |

## FinancialAidAwardPeriod

**SQL identifier:** `finances.financial_aid_award_period`

Tenant-scoped governed financial-aid award period used to group and present awards independently from the broader financial-aid year and from academic-term or federal payment-period identity.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_award_period_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for a governed financial-aid award period |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system contributing the award-period definition |
| `code` | `TEXT` |  | No | Institution-defined code identifying the financial-aid award period |
| `title` | `TEXT` |  | No | Full institutional name of the financial-aid award period |
| `description` | `TEXT` |  | Yes | Institution-provided description of the financial-aid award period |
| `status` | `TEXT` |  | No | Operational lifecycle status of the award period |
| `start_date` | `DATE` |  | Yes | Date on which the financial-aid award period begins |
| `end_date` | `DATE` |  | Yes | Date on which the financial-aid award period ends |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier for the financial-aid award period |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## FinancialAidFund

**SQL identifier:** `finances.financial_aid_fund`

Tenant-scoped governed definition of a named financial-aid fund such as a grant, scholarship, loan, or work program.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_fund_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for a governed financial-aid fund |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system contributing the fund definition |
| `code` | `TEXT` |  | No | Institution-defined code identifying the financial-aid fund |
| `title` | `TEXT` |  | No | Full institutional name of the financial-aid fund |
| `description` | `TEXT` |  | Yes | Description of the financial-aid fund |
| `aid_type` | `TEXT` |  | No | Broad form of aid represented by the fund |
| `fund_category` | `TEXT` |  | Yes | Institution- or source-governed financial-aid fund category |
| `fund_source` | `TEXT` |  | Yes | Origin of the financial-aid fund |
| `privacy_level` | `TEXT` |  | Yes | Whether student awards from the fund are restricted from ordinary viewing |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier for the financial-aid fund |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## FinancialAidFundAvailability

**SQL identifier:** `finances.financial_aid_fund_availability`

Aid-year- and office-specific financial limits and availability configuration for a financial-aid fund.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_fund_identifier` | `TEXT` | PK, FK → `FinancialAidFund.FinancialAidFundIdentifier` | No | Financial-aid fund configured for the year and office |
| `financial_aid_year_identifier` | `TEXT` | PK, FK → `FinancialAidYear.FinancialAidYearIdentifier` | No | Financial-aid year for which the fund is configured |
| `financial_aid_office_organization_unit_identifier` | `TEXT` | PK, FK → `OrganizationUnit.OrganizationUnitIdentifier` | No | Institutional financial-aid office administering the fund |
| `budgeted_amount` | `NUMERIC` |  | Yes | Maximum total amount that may be accepted across students for the fund, year, and office |
| `budget_currency_code` | `TEXT` |  | Yes | ISO 4217 currency code supplied with the budgeted amount |
| `maximum_award_amount` | `NUMERIC` |  | Yes | Maximum amount that may be awarded to one student from the fund for the year and office |
| `maximum_offered_budget_amount` | `NUMERIC` |  | Yes | Maximum total amount that may be offered across students, including planned overcommitment |
| `minimum_award_amount` | `NUMERIC` |  | Yes | Minimum amount that may be awarded to one student from the fund for the year and office |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the availability record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the availability record was updated |

## FinancialAidFundClassification

**SQL identifier:** `finances.financial_aid_fund_classification`

Natural-key association of a financial-aid fund to one governed classification value.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_fund_identifier` | `TEXT` | PK, FK → `FinancialAidFund.FinancialAidFundIdentifier` | No | Financial-aid fund receiving the classification |
| `classification_identifier` | `TEXT` | PK | No | Governed classification assigned to the financial-aid fund |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the association was updated |

## FinancialAidYear

**SQL identifier:** `finances.financial_aid_year`

Tenant-scoped governed financial aid year used to organize applications, need, outcomes, and awards across a consistent reporting period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `financial_aid_year_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for a financial aid year |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `financial_aid_year_designator` | `TEXT` |  | No | Human-readable designation for the financial aid year |
| `title` | `TEXT` |  | Yes | Full institutional name of the financial aid year |
| `description` | `TEXT` |  | Yes | Institution-provided description of the financial aid year |
| `status` | `TEXT` |  | No | Lifecycle status governing whether the financial aid year is available for active institutional use |
| `start_date` | `DATE` |  | Yes | Date on which the financial aid year begins |
| `end_date` | `DATE` |  | Yes | Date on which the financial aid year ends |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |

## LearnerAccountCharge

**SQL identifier:** `finances.learner_account_charge`

Tenant-scoped assessed charge incurred by a person, preserving amount, liability date, optional academic period, description, and source identity separately from payments, balances, refunds, waivers, awards, or general-ledger detail.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_account_charge_identifier` | `TEXT` | PK | No | GUIDE-owned tenant-scoped identifier for the assessed charge. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person who incurred the charge. |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | Yes | Optional academic period in which the charge was incurred. |
| `charge_date` | `DATE` |  | No | Date on which the person became liable for the charge. |
| `charged_amount` | `NUMERIC` |  | No | Amount assessed to the person. |
| `description` | `TEXT` |  | Yes | Transaction-specific description or source override description. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the charge. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the charge. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the canonical record. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the canonical record was created. |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that last updated the canonical record. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was last updated. |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the canonical record. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the canonical record was deleted. |

## LearnerDebtAccount

**SQL identifier:** `finances.learner_debt_account`

A table for a learner to track their debt or loan accounts for financial planning.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_debt_account_identifier` | `TEXT` | PK | No | Unique identifier for the debt record |
| `learner_financial_plan_identifier` | `TEXT` | FK → `LearnerFinancialPlan.LearnerFinancialPlanIdentifier` | No | Unique identifier for the financial plan or budget |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `debt_type` | `TEXT` |  | Yes | Type of debt (e.g. Student Loan, Credit Card, Mortgage, Auto Loan, Personal Loan) |
| `lender_name` | `TEXT` |  | Yes | Name of the lender or institution issuing the loan |
| `original_loan_amount` | `NUMERIC` |  | Yes | The original amount borrowed |
| `current_balance` | `NUMERIC` |  | Yes | The remaining amount owed |
| `interest_rate` | `NUMERIC` |  | Yes | Interest rate applicable to the debt (as a percentage) |
| `minimum_monthly_payment` | `NUMERIC` |  | Yes | Minimum required monthly payment (dollars) |
| `loan_term_months` | `INTEGER` |  | Yes | Duration of the loan in months |
| `loan_start_date` | `DATE` |  | Yes | Date when the loan was issued |
| `loan_end_date` | `DATE` |  | Yes | Expected date of full repayment |
| `payment_frequency` | `TEXT` |  | Yes | How often payments are due (Monthly, Biweekly, Annually) |
| `debt_status` | `TEXT` |  | Yes | The status of the debt (e.g. Open, Paid Off, Delinquent, In Forbearance) |
| `auto_payment_enabled_indicator` | `BOOLEAN` |  | No | Indicates whether automatic payment is enabled |
| `late_fee_amount` | `NUMERIC` |  | Yes | Late fee incurred if payment is overdue |
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

## LearnerDebtRepaymentSchedule

**SQL identifier:** `finances.learner_debt_repayment_schedule`

A table containing a learner's schedule plan for repaying their debts.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_debt_repayment_schedule_identifier` | `TEXT` | PK | No | Unique identifier for debt repayment schedule |
| `learner_debt_account_identifier` | `TEXT` | FK → `LearnerDebtAccount.LearnerDebtAccountIdentifier` | No | Unique identifier for the debt record |
| `payment_due_date` | `DATE` |  | Yes | Scheduled date for a loan payment |
| `payment_amount` | `NUMERIC` |  | Yes | Amount due on the payment date (dollars) |
| `actual_payment_amount` | `NUMERIC` |  | Yes | Amount actually paid (dollars) |
| `payment_status` | `TEXT` |  | Yes | The current status of the payment (e.g. Pending, Paid, Late, Deferred) |
| `remaining_balance_after_payment` | `NUMERIC` |  | Yes | Outstanding balance after the payment is applied |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerFinancialAidAcademicProgressStatus

**SQL identifier:** `finances.learner_financial_aid_academic_progress_status`

Effective-dated financial-aid satisfactory academic progress determination for one person, distinct from general academic standing.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_academic_progress_status_identifier` | `TEXT` | PK | No | GUIDE-owned identifier for the person financial-aid SAP determination |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person whose financial-aid SAP status is recorded |
| `financial_aid_academic_progress_status_identifier` | `TEXT` | FK → `FinancialAidAcademicProgressStatusLookup.FinancialAidAcademicProgressStatusIdentifier` | No | Governed institution-defined SAP status |
| `financial_aid_academic_progress_type_identifier` | `TEXT` | FK → `FinancialAidAcademicProgressTypeLookup.FinancialAidAcademicProgressTypeIdentifier` | No | Governed financial-aid academic-progress type for the SAP determination |
| `assigned_date` | `DATE` |  | Yes | Date the financial-aid SAP status was assigned |
| `effective_date` | `DATE` |  | Yes | Date the financial-aid SAP status became effective |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system supplying the person SAP determination |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system identifier for the person SAP determination |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |

## LearnerFinancialAidApplication

**SQL identifier:** `finances.learner_financial_aid_application`

A table containing a history of prior financial aid applications and data for required inputs.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_financial_aid_application_identifier` | `TEXT` | PK | No | Unique identifier for the FAFSA or other financial aid application |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `financial_aid_application_type` | `TEXT` |  | No | The type of financial application completed by an individual |
| `federal_financial_aid_application_due_date` | `DATE` |  | No | Indicates the FAFSA Federal Due Date so that we can send reminders based on this date |
| `state_financial_aid_application_due_date` | `DATE` |  | Yes | State FAFSA due date |
| `financial_aid_application_status` | `TEXT` |  | Yes | Indicates whether the financial aid application is not started, in progress, complete, accepted/awarded, or declined. This will help to send out reminder notifications to the learner. |
| `parent_contribution_amount` | `NUMERIC` |  | Yes | The expected financial contribution in dollars from the parent(s) toward tuition and expenses |
| `financial_need` | `NUMERIC` |  | Yes | The amount of financial need as determined by an institution using the federal methodology and/or your institution's own standards |
| `financial_need_determination_methodology` | `TEXT` |  | Yes | The methodology used to determine an individual's financial need |
| `financial_aid_application_source` | `TEXT` |  | No | The intake source or processing channel of the financial aid application |
| `financial_aid_application_completed_date` | `DATE` |  | Yes | The date the financial aid application was completed |
| `housing_preference` | `TEXT` |  | Yes | The applicant-selected anticipated housing arrangement used for financial-aid planning and cost-of-attendance context |
| `work_study_interest` | `TEXT` |  | Yes | The applicant-reported level of interest in participating in a work-study program for this financial-aid application. |
| `financial_aid_award_status` | `TEXT` |  | Yes | An indication of whether the financial aid type being reported is aid that has been awarded, accepted or dispersed |
| `financial_aid_award_type` | `TEXT` |  | Yes | The classification of financial aid awarded to a person for the academic term/year |
| `financial_aid_award_amount` | `NUMERIC` |  | Yes | The amount of financial aid awarded to a person for the term/year |
| `financial_aid_income_level` | `NUMERIC` |  | Yes | The income level of an individual that is used by an institution's financial aid office to determine an individual's Expected Family Contribution (EFC). For dependent students this will include the parents' adjusted gross income and the student's adjusted gross income. For independent students this will include the student's adjusted gross income. |
| `family_income_calculation_method` | `TEXT` |  | Yes | The calculation method used by a program to determine total family income |
| `financial_aid_year_identifier` | `TEXT` | FK → `FinancialAidYear.FinancialAidYearIdentifier` | Yes | Tenant-scoped financial aid year governing the application |
| `financial_aid_year_designator` | `TEXT` |  | Yes | The school year for which the student's financial aid application and award data apply Generally, this is the 12-month period from July 1 to June 30 |
| `fafsa_student_aid_report_status` | `TEXT` |  | Yes | Indicates whether the Student Aid Report (SAR) returned from the FAFSA application indicates that the student needs to take actions to correct or update their FAFSA form in any way |
| `isir_received_indicator` | `BOOLEAN` |  | Yes | Indicates whether institution has received ISIR for the student for the academic year |
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

## LearnerFinancialAidApplicationIndependenceCriterion

**SQL identifier:** `finances.learner_financial_aid_application_independence_criterion`

One governed independence criterion reported for one financial-aid application and aid year. Preserves repeating support-relevant criteria without flattening them into general person demographics.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_application_identifier` | `TEXT` | PK, FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | No | Financial-aid application whose aid-year context governs the criterion |
| `independence_criterion_identifier` | `TEXT` | PK, FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | No | Governed independence criterion reported for the application |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## LearnerFinancialAidApplicationOutcome

**SQL identifier:** `finances.learner_financial_aid_application_outcome`

One processed analysis result for a financial-aid application and aid year, preserving calculated contribution, dependency, eligibility, verification, and processing outcomes separately from the submitted application and downstream awards.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_application_outcome_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for one processed financial-aid application outcome |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | No | Financial-aid application analyzed to produce this outcome |
| `financial_aid_year_identifier` | `TEXT` | FK → `FinancialAidYear.FinancialAidYearIdentifier` | No | Financial-aid year governing the outcome |
| `outcome_methodology` | `TEXT` |  | Yes | Methodology used to analyze the application and produce the outcome |
| `dependency_status` | `TEXT` |  | Yes | Dependency determination produced for the application outcome |
| `dependency_override_indicator` | `BOOLEAN` |  | Yes | Indicates that the dependency determination was overridden through authorized review |
| `automatic_zero_contribution_indicator` | `BOOLEAN` |  | Yes | Indicates that an automatic-zero contribution rule was applied |
| `expected_family_contribution_amount` | `NUMERIC` |  | Yes | Expected contribution from the family under the source methodology |
| `expected_student_contribution_amount` | `NUMERIC` |  | Yes | Expected contribution from the applicant under the source methodology |
| `expected_total_parent_contribution_amount` | `NUMERIC` |  | Yes | Expected total contribution from parent contributors under the source methodology |
| `expected_noncustodial_parent_contribution_amount` | `NUMERIC` |  | Yes | Expected contribution from the noncustodial parent under the source methodology |
| `applicant_home_equity_amount` | `NUMERIC` |  | Yes | Derived applicant home-equity amount used or reported in the outcome |
| `custodial_parent_home_equity_amount` | `NUMERIC` |  | Yes | Derived custodial-parent home-equity amount used or reported in the outcome |
| `noncustodial_parent_home_equity_amount` | `NUMERIC` |  | Yes | Derived noncustodial-parent home-equity amount used or reported in the outcome |
| `pell_eligibility_indicator` | `BOOLEAN` |  | Yes | Indicates that the outcome identifies potential Pell Grant eligibility |
| `professional_judgment_status` | `TEXT` |  | Yes | Status or result of professional-judgment processing for the application outcome |
| `application_rejection_status` | `TEXT` |  | Yes | Rejection status produced by application processing |
| `simplified_needs_test_indicator` | `BOOLEAN` |  | Yes | Indicates that the simplified-needs-test requirements were met |
| `student_aid_report_resolution_required_indicator` | `BOOLEAN` |  | Yes | Indicates that a Student Aid Report C-flag or comparable issue requires resolution |
| `total_income_amount` | `NUMERIC` |  | Yes | FISAP or source-defined total income used or produced by the outcome |
| `verification_category` | `TEXT` |  | Yes | Verification tracking category assigned to the application outcome |
| `verification_status` | `TEXT` |  | Yes | Verification selection or processing status for the application outcome |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system contributing the outcome |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier for the financial-aid application outcome |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## LearnerFinancialAidApplicationRecipient

**SQL identifier:** `finances.learner_financial_aid_application_recipient`

A table containing a history of the organizations to which a learner has requested that their financial aid application be sent.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_application_recipient_identifier` | `TEXT` | PK | No | Unique identifier for this association between a learner's financial aid application and a college organization |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | No | Unique identifier for the FAFSA application |
| `recipient_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | A unique number or alphanumeric code assigned to an organization by a school, school system, a state, or other agency or entity |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerFinancialAidAward

**SQL identifier:** `finances.learner_financial_aid_award`

A table containing a history of current and prior financial aid awards in the forms of scholarships, grants, and loans.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_financial_aid_award_identifier` | `TEXT` | PK | No | Unique identifier for a financial aid award item |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | Yes | Unique identifier for the FAFSA application |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `financial_aid_application_type` | `TEXT` |  | No | The type of financial application completed by an individual |
| `financial_aid_award_status` | `TEXT` |  | No | An indication of whether the financial aid type being reported is aid that has been awarded, accepted or dispersed |
| `financial_aid_award_type` | `TEXT` |  | No | The classification of financial aid awarded to a person for the academic term/year |
| `financial_aid_award_amount` | `NUMERIC` |  | No | The amount of financial aid awarded to a person for the term/year |
| `financial_aid_year_designator` | `TEXT` |  | Yes | The school year for which the student's financial aid application and award data apply Generally, this is the 12-month period from July 1 to June 30 |
| `disbursement_schedule` | `TEXT` |  | Yes | How frequently the funds are disbursed |
| `applicable_expenses` | `TEXT` |  | Yes | Description of the expenses to which the financial aid award can go towards |
| `financial_need` | `NUMERIC` |  | Yes | The amount of financial need as determined by an institution using the federal methodology and/or your institution's own standards |
| `financial_need_determination_methodology` | `TEXT` |  | Yes | The methodology used to determine an individual's financial need (e.g. Federal or Institutional) |
| `financial_aid_award_loan_interest_rate` | `NUMERIC` |  | Yes | Interest rate of the loan |
| `financial_aid_award_loan_servicer` | `TEXT` |  | Yes | Student loan servicer name |
| `financial_aid_award_loan_origination_fee` | `NUMERIC` |  | Yes | Origination fee of the loan |
| `financial_aid_award_loan_first_payment_due_date` | `DATE` |  | Yes | Date that payments are first due for the loan |
| `financial_aid_award_loan_payment_amount` | `NUMERIC` |  | Yes | Payment amount for the loan |
| `financial_aid_award_taxed_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not this financial aid award is taxed |
| `remaining_pell_amount` | `NUMERIC` |  | Yes | Remaining amount of Pell funds |
| `remaining_loan_amount` | `NUMERIC` |  | Yes | Remaining amount on current loan |
| `financial_aid_veterans_benefit_status` | `TEXT` |  | Yes | An indication of whether a person is receiving Veteran's benefits |
| `financial_aid_veterans_benefit_type` | `TEXT` |  | Yes | The type of Veteran's benefits a person is receiving |
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
| `financial_aid_year_identifier` | `TEXT` | FK → `FinancialAidYear.FinancialAidYearIdentifier` | No | Tenant-scoped financial-aid year governing the award |
| `financial_aid_fund_identifier` | `TEXT` | FK → `FinancialAidFund.FinancialAidFundIdentifier` | No | Tenant-scoped reusable financial-aid fund from which the award is made |
| `originally_offered_date` | `DATE` |  | Yes | Date on which the award was first offered to the student |

## LearnerFinancialAidAwardAggregate

**SQL identifier:** `finances.learner_financial_aid_award_aggregate`

A table containing aggregate sums of learner financial aid awards of a given type.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_financial_aid_award_aggregate_identifier` | `TEXT` | PK | No | A unique identifier for the learner financial aid award aggregate |
| `financial_aid_award_aggregate_type` | `TEXT` |  | Yes | Indicates specific type of aggregated financial aid award for the learner |
| `financial_aid_award_aggregate_amount` | `INTEGER` |  | Yes | Indicates an amount (rounded to nearest integer in dollars) for an aggregated financial aid award for the learner |
| `financial_aid_year_designator` | `TEXT` |  | Yes | Indicates the academic year for an aggregated financial aid award for the learner |
| `financial_aid_award_interest_rate` | `NUMERIC` |  | Yes | Interest rate percentage for the financial aid award aggregate, in the event that the award is a loan |
| `financial_aid_award_origination_fee` | `NUMERIC` |  | Yes | Origination fee of the financial aid award |
| `financial_aid_award_hours` | `INTEGER` |  | Yes | The number of hours per week required for the financial aid award in the event that it is a work study or on campus job |
| `contract_days_of_service_per_year` | `INTEGER` |  | Yes | The number of days per year that a person is expected to work as outlined specifically in his or her employment agreement |
| `wage_verification_code` | `TEXT` |  | Yes | An indication of whether the wage information has been verified |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerFinancialAidAwardPeriod

**SQL identifier:** `finances.learner_financial_aid_award_period`

Period-level amounts and status for one student financial-aid award within one governed award period.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_award_identifier` | `TEXT` | PK, FK → `LearnerFinancialAidAward.LearnerFinancialAidAwardIdentifier` | No | Parent student financial-aid award |
| `financial_aid_award_period_identifier` | `TEXT` | PK, FK → `FinancialAidAwardPeriod.FinancialAidAwardPeriodIdentifier` | No | Governed institutional award period for this portion of the student award |
| `award_status` | `TEXT` |  | No | Status of the student award within this award period |
| `original_offered_amount` | `NUMERIC` |  | Yes | Amount originally offered for this award period |
| `offered_amount` | `NUMERIC` |  | Yes | Current amount offered for this award period |
| `accepted_amount` | `NUMERIC` |  | Yes | Amount accepted for this award period |
| `declined_amount` | `NUMERIC` |  | Yes | Amount declined for this award period |
| `rejected_amount` | `NUMERIC` |  | Yes | Amount cancelled or rejected for this award period |
| `disbursed_amount` | `NUMERIC` |  | Yes | Amount actually disbursed for this award period |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |

## LearnerFinancialAidAwardPeriodAcademicPeriod

**SQL identifier:** `finances.learner_financial_aid_award_period_academic_period`

Natural-key association connecting a student award period to each applicable academic term.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_award_identifier` | `TEXT` | PK, FK → `LearnerFinancialAidAwardPeriod.LearnerFinancialAidAwardIdentifier` | No | Parent student financial-aid award |
| `financial_aid_award_period_identifier` | `TEXT` | PK, FK → `LearnerFinancialAidAwardPeriod.FinancialAidAwardPeriodIdentifier` | No | Award period associated with the academic period |
| `term_identifier` | `TEXT` | PK, FK → `TermLookup.TermIdentifier` | No | Academic period to which the award-period amount applies |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the association was created |

## LearnerFinancialAidContributor

**SQL identifier:** `finances.learner_financial_aid_contributor`

A table containing the details about contributors to a learner's federal financial aid application.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_contributor_identifier` | `TEXT` | PK | No | Unique identifier for a learner financial aid contributor item |
| `contributor_person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Person contributing information to the financial-aid application, such as a parent, spouse, or other required contributor. |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | No | Unique identifier for the FAFSA application |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerFinancialAidContributorFinancialProfile

**SQL identifier:** `finances.learner_financial_aid_contributor_financial_profile`

Application- and aid-year-specific household and income profile for the applicant, custodial parents, or noncustodial parents, optionally linked to a resolved financial-aid contributor.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_contributor_financial_profile_identifier` | `TEXT` | PK | No | Unique tenant-scoped identifier for an application-context financial profile |
| `learner_financial_aid_application_identifier` | `TEXT` | FK → `LearnerFinancialAidApplication.LearnerFinancialAidApplicationIdentifier` | No | Financial-aid application whose aid-year context governs the profile |
| `learner_financial_aid_contributor_identifier` | `TEXT` | FK → `LearnerFinancialAidContributor.LearnerFinancialAidContributorIdentifier` | Yes | Optional contributor record associated with the profile |
| `profile_subject_type` | `TEXT` |  | No | Whose household or income context the profile represents |
| `household_size` | `INTEGER` |  | Yes | Number of people in the subject household for the application aid year |
| `number_in_college` | `INTEGER` |  | Yes | Number of people in the subject household expected to attend college during the application aid year |
| `adjusted_gross_income_amount` | `NUMERIC` |  | Yes | Adjusted gross income for the profile subject where supplied |
| `earned_income_amount` | `NUMERIC` |  | Yes | Earned income for the primary person represented by the profile where supplied |
| `spouse_or_second_contributor_earned_income_amount` | `NUMERIC` |  | Yes | Earned income for a spouse or second contributor represented in the profile where supplied |
| `total_income_amount` | `NUMERIC` |  | Yes | Total income reported or calculated for the profile subject |
| `marital_status` | `TEXT` |  | Yes | Applicant marital status reported for the specific financial-aid application and aid year |
| `tax_return_filing_status` | `TEXT` |  | Yes | Tax-return filing status for the profile subject where supplied |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system contributing the profile |
| `source_system_key_value` | `TEXT` |  | Yes | Source key for the profile when one exists |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## LearnerFinancialAidNeedByMethodology

**SQL identifier:** `finances.learner_financial_aid_need_by_methodology`

One federal or institutional need calculation within a student financial-aid need summary, preserving the associated processed application outcome, budget duration, cost of attendance, contribution, gross need, and need reduction.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_need_summary_identifier` | `TEXT` | PK, FK → `LearnerFinancialAidNeedSummary.LearnerFinancialAidNeedSummaryIdentifier` | No | Parent student financial-aid need summary |
| `need_methodology` | `TEXT` | PK | No | Methodology under which the financial need was determined |
| `learner_financial_aid_application_outcome_identifier` | `TEXT` | FK → `LearnerFinancialAidApplicationOutcome.LearnerFinancialAidApplicationOutcomeIdentifier` | No | Processed application outcome used for this methodology-specific need determination |
| `budget_duration_months` | `INTEGER` |  | Yes | Number of months covered by the methodology-specific budget |
| `cost_of_attendance_amount` | `NUMERIC` |  | Yes | Estimated cost of attendance used for the methodology-specific need determination |
| `expected_family_contribution_amount` | `NUMERIC` |  | Yes | Expected family contribution used in the source need determination |
| `gross_need_amount` | `NUMERIC` |  | Yes | Source-calculated gross financial need for the methodology |
| `need_reduction_amount` | `NUMERIC` |  | Yes | Financial-aid-office-managed resources that reduce need under the methodology |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the child determination was created |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the child determination was updated |

## LearnerFinancialAidNeedSummary

**SQL identifier:** `finances.learner_financial_aid_need_summary`

Tenant-scoped summary of one applicant’s financial need for one aid year, including resources outside financial-aid-office management and serving as the parent for methodology-specific calculations.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_aid_need_summary_identifier` | `TEXT` | PK | No | Tenant-scoped identifier for one student financial-aid need summary |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | Applicant whose financial need is summarized |
| `financial_aid_year_identifier` | `TEXT` | FK → `FinancialAidYear.FinancialAidYearIdentifier` | No | Financial-aid year governing the need summary |
| `outside_resource_amount` | `NUMERIC` |  | Yes | Additional financial resources available to the applicant that are not managed by the financial aid office |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system contributing the need summary |
| `source_system_key_value` | `TEXT` |  | Yes | Source identifier for the student financial-aid need summary |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time the record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the record was deleted |

## LearnerFinancialPlan

**SQL identifier:** `finances.learner_financial_plan`

A table containing a history of the financial plans a learner created to identify resources to satisfy the financial requirements to support pursuing education.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `learner_financial_plan_identifier` | `TEXT` | PK | No | Unique identifier of a financial plan |
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | Yes | A name for the record |
| `time_period` | `TEXT` |  | Yes | Timeframe of the budget or financial plan (e.g. monthly, yearly) |
| `start_date` | `DATE` |  | Yes | Start date of the budget or financial plan time period |
| `end_date` | `DATE` |  | Yes | End date of the budget or financial plan time period |
| `projected_income_total` | `NUMERIC` |  | Yes | Total expected income for the budget for financial plan time period (calculated) |
| `projected_expenses_total` | `NUMERIC` |  | Yes | Total expected expenses for the budget or financial plan time period (calculated) |
| `projected_net_balance` | `NUMERIC` |  | Yes | Projected balance after income and expenses for the budget or financial plan time period |
| `actual_income_total` | `NUMERIC` |  | Yes | Total actual income for the budget or financial plan time period |
| `actual_expenses_total` | `NUMERIC` |  | Yes | Total actual expenses for the budget or financial plan time period |
| `actual_net_balance` | `NUMERIC` |  | Yes | Actual balance at the end of the budget or financial plan time period |
| `date_issued` | `DATE` |  | Yes | The month, day, and year that the College Financing Plan was created to notify the prospective student about their financial aid package |
| `type` | `TEXT` |  | No | Type of financial plan (organization provided plan, learner provided plan, actual expenditures) |
| `status` | `TEXT` |  | No | Status of a financial plan (active, inactive) |
| `estimated_terms_remaining` | `INTEGER` |  | Yes | Number of terms the learner estimates will be required for completion |
| `estimated_term_cost` | `NUMERIC` |  | Yes | Total cost a learner estimates for a term of enrollment |
| `financial_plan_history` | `TEXT` |  | Yes | Indicates whether this plan is for a current, previous, or future school year |
| `tuition_and_fees` | `NUMERIC` |  | Yes | Tuition and Fees; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `housing_and_food_on_campus` | `NUMERIC` |  | Yes | Housing and food on campus; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `housing_and_food_off_campus` | `NUMERIC` |  | Yes | Housing and food off campus; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `boarding_cost` | `NUMERIC` |  | Yes | Boarding costs (food only); This information is generated by the institution itself and should provide a clear undestanding of the costs associated with one year of enrollment at the institution for the learner (dollars) |
| `books_and_supplies` | `NUMERIC` |  | Yes | Books and supplies; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `transportation` | `NUMERIC` |  | Yes | Transportation; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `other_education_costs` | `NUMERIC` |  | Yes | Other education costs; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `estimated_costs_on_campus` | `NUMERIC` |  | Yes | Total estimated costs if the student lives on campus; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `estimated_costs_off_campus` | `NUMERIC` |  | Yes | Total estimated costs if the student lives off campus; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student. (dollars) |
| `student_aid_index_based_on_fafsa` | `NUMERIC` |  | Yes | Student Aid Index Based on FAFSA; At most institutions, the expected family contribution is based on the FAFSA results; however, if an institutional methodology is used, that result may be provided. (dollars) |
| `student_aid_index_based_on_institutional_method` | `NUMERIC` |  | Yes | Student Aid Index Based on Institutional Method; At most institutions, the expected family contribution is based on the FAFSA results; however, if an institutional methodology is used, that result may be provided. (dollars) |
| `parent_contribution_amount` | `NUMERIC` |  | Yes | Tuition and Fees; This information is generated by the institution itself and should provide a clear understanding of the costs associated with one year of enrollment at the institution for the named student |
| `net_price` | `NUMERIC` |  | Yes | This number reflects the net cost of attendance for the named student after grants and scholarships are taken into account |
| `tuition_payment_plan_indicator` | `BOOLEAN` |  | Yes | Tuition payment plan offered by the institution |
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

## LearnerFinancialPlanExpense

**SQL identifier:** `finances.learner_financial_plan_expense`

A table for a learner's budget or financial plan expenses.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_plan_expense_identifier` | `TEXT` | PK | No | Unique identifier for the budget or financial plan expense |
| `learner_financial_plan_identifier` | `TEXT` | FK → `LearnerFinancialPlan.LearnerFinancialPlanIdentifier` | No | Unique identifier for the financial plan or budget |
| `paid_by_financial_aid_award_identifier` | `TEXT` | FK → `LearnerFinancialAidAward.LearnerFinancialAidAwardIdentifier` | Yes | Unique identifier for a financial aid award item |
| `expense_category` | `TEXT` |  | Yes | Type of expense (e.g. rent, food, transportation, entertainment) |
| `expense_amount` | `NUMERIC` |  | Yes | Amount of the expense (dollars) |
| `expense_frequency` | `TEXT` |  | Yes | Frequency of expense (one-time, weekly, biweekly, monthly, annually) |
| `expense_date` | `DATE` |  | Yes | Date expense was incurred |
| `projected_expense` | `NUMERIC` |  | Yes | Expected expense amount for the time period specified in the financial plan |
| `actual_expense` | `NUMERIC` |  | Yes | Actual expense amount for the time period specified in the financial plan up to this point |
| `payment_method` | `TEXT` |  | Yes | The payment method used for the expense (e.g. Cash, Credit Card, Debit, Loan, Financial Aid, etc.) |
| `expense_notes` | `TEXT` |  | Yes | Additional details about the expense |
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

## LearnerFinancialPlanIncomeSource

**SQL identifier:** `finances.learner_financial_plan_income_source`

A table for a learner's budget or financial plan income sources.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_financial_plan_income_source_identifier` | `TEXT` | PK | No | Unique identifier for the budget or financial plan income |
| `learner_financial_plan_identifier` | `TEXT` | FK → `LearnerFinancialPlan.LearnerFinancialPlanIdentifier` | No | Unique identifier of a financial plan |
| `financial_aid_award_identifier` | `TEXT` | FK → `LearnerFinancialAidAward.LearnerFinancialAidAwardIdentifier` | Yes | Unique identifier for a financial aid award item |
| `income_source_name` | `TEXT` |  | Yes | Source of income (e.g. salary, scholarship, side gig) |
| `income_amount` | `NUMERIC` |  | Yes | Amount received from this source (dollars) |
| `income_frequency` | `TEXT` |  | Yes | Frequency of income (one-time, weekly, biweekly, monthly, annually) |
| `income_date` | `DATE` |  | Yes | Date income is received |
| `projected_income` | `NUMERIC` |  | Yes | Expected income from this source for the time period specified in the financial plan |
| `actual_income` | `NUMERIC` |  | Yes | Actual income received for the time period specified in the financial plan up to this point |
| `income_source_notes` | `TEXT` |  | Yes | Additional details about the income source |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerScholarship

**SQL identifier:** `finances.learner_scholarship`

A table containing a history of scholarships awarded to a learner.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_scholarship_identifier` | `TEXT` | PK | No | Unique identifier for the learner's scholarship item |
| `scholarship_identifier` | `TEXT` | FK → `ScholarshipLookup.ScholarshipIdentifier` | Yes | Unique identifier for the scholarship item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `type` | `TEXT` |  | Yes | Type of scholarship award |
| `award_amount` | `NUMERIC` |  | No | Dollar amount awarded with the scholarship |
| `amount_remaining` | `NUMERIC` |  | Yes | Remaining dollar amount of the awarded scholarship |
| `award_date` | `DATE` |  | Yes | Date a scholarship was awarded to a learner |
| `expiration_date` | `DATE` |  | Yes | Expiration date for a scholarship |
| `source_system_key_value` | `TEXT` |  | Yes | Unique identifier of this record in the source system |
| `source_system_created_date` | `DATE` |  | Yes | Date the record was created in the source system |
| `source_system_updated_date` | `DATE` |  | Yes | Date the record was last updated in the source system |
| `source_system_deleted_date` | `DATE` |  | Yes | Date the record was deleted from the source system |
| `created_by` | `BIGINT` |  | Yes | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerThirdPartyBenefit

**SQL identifier:** `finances.learner_third_party_benefit`

A table that stores learner-associated third-party education benefit, sponsorship, tuition reimbursement, employer reimbursement, voucher, or outside funding-support facts. This table captures benefit eligibility or sponsorship context without becoming the authoritative financial-aid award, billing, payment, or ledger transaction table.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | PK | No | Tenant-scoped person/learner identifier to whom the benefit belongs. |
| `sequence_number` | `TEXT` | PK | No | Sequence number for multiple benefit rows for the learner. |
| `benefit_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the type of third-party benefit. |
| `benefit_source_type_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the type of benefit source or provider. |
| `benefit_status_identifier` | `TEXT` | FK → `ReferenceCodeValue.ReferenceCodeValueIdentifier` | Yes | Reference-code value identifying the current known benefit status. |
| `benefit_available_indicator` | `BOOLEAN` |  | Yes | Indicates whether the source records a benefit or reimbursement as available. |
| `benefit_provider_name` | `TEXT` |  | Yes | Name of the organization or party providing the benefit, reimbursement, or sponsorship. |
| `employer_name` | `TEXT` |  | Yes | Employer name associated with the benefit when the benefit is employer-related. |
| `related_employment_sequence_number` | `INTEGER` |  | Yes | Optional sequence number linking the benefit to a related learner employment row. |
| `benefit_amount` | `NUMERIC` |  | Yes | Benefit amount recorded by the source, where available; not an authoritative financial balance. |
| `benefit_percent` | `NUMERIC` |  | Yes | Benefit percentage recorded by the source, where available. |
| `benefit_start_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the benefit started or became effective, where known. |
| `benefit_end_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time the benefit ended or expired, where known. |
| `source_raw_benefit_type` | `TEXT` |  | Yes | Source-system benefit type value preserved when canonical mapping is lossy. |
| `source_raw_benefit_source_type` | `TEXT` |  | Yes | Source-system benefit source type value preserved when canonical mapping is lossy. |
| `source_raw_benefit_status` | `TEXT` |  | Yes | Source-system benefit status value preserved when canonical mapping is lossy. |
| `source_raw_benefit_available` | `TEXT` |  | Yes | Source-system benefit availability or reimbursement value preserved as supplied. |
| `source_raw_benefit_provider` | `TEXT` |  | Yes | Source-system benefit provider value preserved as supplied. |
| `source_raw_employer` | `TEXT` |  | Yes | Source-system employer value preserved as supplied. |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Source system from which the third-party benefit row originated or can be reconciled. |
| `source_system_key_value` | `TEXT` |  | Yes | Source-system key value for the third-party benefit row. |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## LearnerVeteransBenefits

**SQL identifier:** `finances.learner_veterans_benefits`

A table containing a history of veterans benefits provided to a learner.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `learner_veterans_benefits_identifier` | `TEXT` | PK | No | Unique identifier for a learner veterans benefits item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `status` | `TEXT` |  | No | An indication of whether a person is receiving Veteran's benefits |
| `type` | `TEXT` |  | No | The type of Veteran's benefits a person is receiving |
| `amount` | `NUMERIC` |  | No | Total amount of veterans aid benefits awarded |
| `amount_remaining` | `NUMERIC` |  | Yes | Remaining dollar amount of veterans aid benefits |
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

## OrganizationAttendanceCosts

**SQL identifier:** `finances.organization_attendance_costs`

A table containing a history of average costs for tuition, housing, meals, and related costs at an organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_attendance_costs_identifier` | `TEXT` | PK | No | Unique identifier for the organization attendance costs |
| `tuition_identifier` | `TEXT` | FK → `OrganizationTuition.OrganizationTuitionIdentifier` | No | Unique identifier for the tuition related scheme |
| `tuition_effective_start_date` | `DATE` |  | Yes | Beginning effective date for the tuition scheme |
| `tuition_effective_end_date` | `DATE` |  | Yes | Ending effective date for the tuition scheme |
| `tuition_type` | `TEXT` |  | Yes | Type of tuition related cost scheme for the cost (in state, out of state, online) |
| `housing_cost_average` | `NUMERIC` |  | Yes | Average amount for costs per academic year |
| `housing_cost_on_campus_average` | `NUMERIC` |  | Yes | Average amount for costs on campus per academic year |
| `housing_cost_off_campus_average` | `NUMERIC` |  | Yes | Average amount for costs off campus per academic year |
| `food_cost_on_campus_average` | `NUMERIC` |  | Yes | Average amount for food costs on campus per academic year on campus |
| `food_cost_off_campus_average` | `NUMERIC` |  | Yes | Average amount for food costs off campus per academic year |
| `other_expenses_on_campus_average` | `NUMERIC` |  | Yes | Estimates of expense for other expenses on campus |
| `other_expenses_off_campus_average` | `NUMERIC` |  | Yes | Estimates of expense for other expenses off campus |
| `other_expenses_off_campus_with_family_average` | `NUMERIC` |  | Yes | Estimates of expense for other expenses off campus living with family |
| `transportation_cost_average` | `NUMERIC` |  | Yes | Average amount for transportation costs per academic year |
| `books_supplies_cost_average` | `NUMERIC` |  | Yes | Average amount for the cost of books and supplies |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## OrganizationMedianAidAwardedByEFC

**SQL identifier:** `finances.organization_median_aid_awarded_by_efc`

A table containing a history of details about the median aid amount the institution awards based on the learner's expected family contribution.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_median_aid_awarded_by_efc_identifier` | `TEXT` | PK | No | Unique identifier for an organization's median aid awarded by Expected Family Contribution (EFC) for a given term |
| `term_identifier` | `TEXT` | FK → `TermLookup.TermIdentifier` | No | Unique identifier for a term |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `efc_range` | `TEXT` |  | Yes | Expected Family Contribution (EFC) range |
| `efc_range_minimum` | `NUMERIC` |  | Yes | The minimum dollar amount in the EFC range |
| `efc_range_maximum` | `NUMERIC` |  | Yes | The maximum dollar amount in the EFC range |
| `in_district_on_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `in_district_off_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `in_district_off_campus_with_family` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `in_state_on_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `in_state_off_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `in_state_off_campus_with_family` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `out_of_state_on_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `out_of_state_off_campus` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
| `out_of_state_off_campus_with_family` | `NUMERIC` |  | Yes | Data should represent the median amount of both need and non-need grant and scholarship aid from Federal, State, or Local Governments, or the Institution (exclude private source grant or scholarship aid and work-study programs) awarded to full-time, first-time degree/certificate-seeking students with the indicated living and residency category for the Expected Family Contribution (EFC) range |
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

## OrganizationTuition

**SQL identifier:** `finances.organization_tuition`

A table containing a history of tuition fees at an organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_tuition_identifier` | `TEXT` | PK | No | Unique identifier for the tuition scheme |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `tuition_effective_start_date` | `DATE` |  | Yes | Beginning effective date for the tuition fee scheme |
| `tuition_effective_end_date` | `DATE` |  | Yes | Ending effective date for the tuition fee scheme |
| `tuition_type` | `TEXT` |  | No | Type of tuition scheme for the cost (in state, out of state, online) |
| `average_tuition_amount` | `NUMERIC` |  | Yes | Average amount of the tuition scheme |
| `credit_hour_amount` | `NUMERIC` |  | Yes | Cost per credit hour amount for non-flat rate tuition charges |
| `credit_hour_minimum_number` | `NUMERIC` |  | Yes | Minimum credit hours for the amount by hours to apply |
| `credit_hour_maximum_number` | `NUMERIC` |  | Yes | Maximum credit hours for the amount by hours to apply |
| `flat_rate_amount` | `NUMERIC` |  | Yes | Flat rate fee for tuition in a given term |
| `flat_rate_minimum_credit_hours` | `NUMERIC` |  | Yes | Minimum credit hours for the flat rate amount to apply |
| `flat_rate_maximum_credit_hours` | `NUMERIC` |  | Yes | Maximum credit hours for the flat rate amount to apply |
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

## OrganizationTuitionFee

**SQL identifier:** `finances.organization_tuition_fee`

A table containing a history of the tuition related fees at an organization.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `organization_tuition_fee_identifier` | `TEXT` | PK | No | Unique identifier for the tuition fee scheme |
| `tuition_identifier` | `TEXT` | FK → `OrganizationTuition.OrganizationTuitionIdentifier` | No | Unique identifier for the tuition related scheme |
| `name` | `TEXT` |  | No | A name for the record |
| `tuition_effective_start_date` | `DATE` |  | Yes | Beginning effective date for the tuition fee scheme |
| `tuition_effective_end_date` | `DATE` |  | Yes | Ending effective date for the tuition fee scheme |
| `tuition_fee_type` | `TEXT` |  | No | Type of tuition fee scheme for the fee (in state, out of state, online) |
| `fee_description` | `TEXT` |  | Yes | A description for the record |
| `fee_amount` | `NUMERIC` |  | Yes | Amount of the fee assessed |
| `fee_assessment_interval` | `TEXT` |  | Yes | Interval for the fee to be assessed (per term, course, academic year) |
| `credit_hour_minimum` | `NUMERIC` |  | Yes | Minimum credit hours for the fee to apply |
| `credit_hour_maximum` | `NUMERIC` |  | Yes | Maximum credit hours for the fee to apply |
| `residency_requirement` | `TEXT` |  | Yes | Required residency status for the fee to apply (in state, out of state, online) |
| `housing_requirement` | `TEXT` |  | Yes | Required housing status for the fee to apply (on campus, off campus, commuter) |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |
| `organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Real-world organization to which this record applies. |

## PersonFinances

**SQL identifier:** `finances.person_finances`

A table containing the details of a person's finances that may contribute to funding learning opportunities.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `person_identifier` | `TEXT` | FK → `PersonLookup.PersonIdentifier` | No | A unique number or alphanumeric code assigned to a person |
| `person_finances_identifier` | `TEXT` | PK | No | Unique identifier for a person finances item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `foreign_earned_income_exclusion` | `NUMERIC` |  | Yes | Foreign Earned Income Exclusion in dollars as per the Internal Revenue Service (IRS) |
| `total_cash_savings_checking_assets` | `NUMERIC` |  | Yes | Current total of cash, savings, and checking accounts in dollars, excluding student financial aid |
| `net_worth_of_business_and_investment_farms` | `NUMERIC` |  | Yes | Current net worth of businesses, investment farms, and for-profit agricultural operations in dollars. Net worth is the value of the businesses or farms minus any debts owed against them. |
| `net_worth_of_investments` | `NUMERIC` |  | Yes | Current net worth of investments in dollars, including real estate, but excluding the home the student lives in. Net worth is the value of the investments minus any debts owed against them. |
| `filed_irs1040_form_indicator` | `BOOLEAN` |  | Yes | Indicates whether the individual did or will file IRS Form 1040 or 1040-NR for the prior year |
| `grants_scholarships_ameri_corps_income` | `NUMERIC` |  | Yes | Amount of College Grants, Scholarships, or AmeriCorps Benefits Reported as Income to the IRS |
| `joint_tax_return_indicator` | `BOOLEAN` |  | Yes | Indicates whether the learner/parent did or will file last year's tax return jointly with their current spouse |
| `earned_income_tax_credit_indicator` | `BOOLEAN` |  | Yes | Indicates whether the student's parent received the Earned Income Tax Credit (EITC) on last year's tax return |
| `fafsa_consent_indicator` | `BOOLEAN` |  | Yes | Indicates whether or not the person gives consent to the FAFSA application taking their data directly from the IRS. If all persons contributing to the application do not give consent, then the application will automatically be denied. |
| `annual_child_support_received` | `NUMERIC` |  | Yes | Indicates the total amount received in dollars in child support for the last complete calendar year |
| `federal_housing_assistance_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from federal housing assistance programs |
| `free_or_reduced_price_school_lunch_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, did the learner/contributor or anyone in the family receive benefits from the Free or Reduced Price School Lunch federal program |
| `medicaid_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from Medicaid |
| `refundable_credit_for_coverage_under_qualified_health__7ba8de61` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from the Refundable Credit for Coverage Under a Qualified Health Plan (QHP) federal program |
| `temporary_assistance_for_needy_families_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from the Temporary Assistance for Needy Families (TANF) federal program |
| `supplemental_nutrition_assistance_program_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from the Supplemental Nutrition Assistance Program (SNAP) |
| `special_supplemental_nutrition_program_for_wic_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) federal program |
| `irs_filing_status` | `TEXT` |  | Yes | IRS filing status (Single, Married filing jointly, Married filing separately, Head of household, Qualifying widow or widower with dependent child) |
| `supplemental_security_income_indicator` | `BOOLEAN` |  | Yes | Indicates whether, at any time last year or this year, the learner/contributor or anyone in the family received benefits from the Supplemental Security Income (SSI) federal program |
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

## ScholarshipCollegeAssociation

**SQL identifier:** `finances.scholarship_college_association`

A table associating an organization and scholarship.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `scholarship_college_association_identifier` | `TEXT` | PK | No | Unique identifier for the association of a scholarship and organization |
| `college_organization_identifier` | `TEXT` | FK → `Organization.OrganizationIdentifier` | No | Unique identifier for the college organization |
| `scholarship_identifier` | `TEXT` | FK → `ScholarshipLookup.ScholarshipIdentifier` | No | Unique identifier for the scholarship item |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ScholarshipInformation

**SQL identifier:** `finances.scholarship_information`

A table containing details of the attributes describing a scholarship.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `scholarship_information_identifier` | `TEXT` | PK | No | Unique identifier for a scholarship attribute |
| `scholarship_identifier` | `TEXT` | FK → `ScholarshipLookup.ScholarshipIdentifier` | No | Unique identifier for the scholarship item |
| `name` | `TEXT` |  | No | A name for the record |
| `description` | `TEXT` |  | Yes | A description for the record |
| `created_by` | `BIGINT` |  | No | Person identifier that created the record |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | Date and time record was created |
| `updated_by` | `BIGINT` |  | Yes | Person identifier that updated the record |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was updated |
| `deleted_by` | `BIGINT` |  | Yes | Person identifier that deleted the record |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | Date and time record was deleted |

## ScholarshipLookup

**SQL identifier:** `finances.scholarship_lookup`

A lookup table of scholarships details.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `scholarship_identifier` | `TEXT` | PK | No | Unique identifier for the scholarship item |
| `source_system_identifier` | `TEXT` | FK → `SourceSystemLookup.SourceSystemIdentifier` | Yes | Unique identifier for the source system |
| `name` | `TEXT` |  | No | A name for the record |
| `application_url` | `TEXT` |  | Yes | Link to the scholarship application |
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
