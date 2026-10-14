# Entity: Learner Success

This page documents every table that belongs to the **Learner Success** entity in the GUIDE Data Model 1.0.0. Tables are listed alphabetically. Each table lists its columns, PostgreSQL types, primary/foreign keys, and descriptions, as they appear in the `Objects` records of the model JSON.

**Tables in this entity: 1**

## Table of contents

- [LearnerSuccessPlanItemTypeLookup](#learnersuccessplanitemtypelookup)

---

## LearnerSuccessPlanItemTypeLookup

**SQL identifier:** `learner_success.learner_success_plan_item_type_lookup`

Defines governed types for actionable or assessable items within learner success plans.

| Column | Type | Key | Nullable | Description |
|---|---|---|---|---|
| `tenant_identifier` | `UUID` | PK, FK → `Tenant.TenantIdentifier` | No | UUID identifying the tenant data-ownership and security boundary for this record. |
| `learner_success_plan_item_type_identifier` | `TEXT` | PK | No | LearnerSuccessPlanItemTypeIdentifier for LearnerSuccessPlanItemTypeLookup. |
| `code` | `TEXT` |  | No | Code for LearnerSuccessPlanItemTypeLookup. |
| `name` | `TEXT` |  | No | Name for LearnerSuccessPlanItemTypeLookup. |
| `description` | `TEXT` |  | Yes | Description for LearnerSuccessPlanItemTypeLookup. |
| `active_indicator` | `BOOLEAN` |  | No | ActiveIndicator for LearnerSuccessPlanItemTypeLookup. |
| `created_by` | `INTEGER` |  | No | CreatedBy for LearnerSuccessPlanItemTypeLookup. |
| `created_date` | `TIMESTAMP WITH TIME ZONE` |  | No | CreatedDate for LearnerSuccessPlanItemTypeLookup. |
| `updated_by` | `INTEGER` |  | Yes | UpdatedBy for LearnerSuccessPlanItemTypeLookup. |
| `updated_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | UpdatedDate for LearnerSuccessPlanItemTypeLookup. |
| `deleted_by` | `INTEGER` |  | Yes | DeletedBy for LearnerSuccessPlanItemTypeLookup. |
| `deleted_date` | `TIMESTAMP WITH TIME ZONE` |  | Yes | DeletedDate for LearnerSuccessPlanItemTypeLookup. |
