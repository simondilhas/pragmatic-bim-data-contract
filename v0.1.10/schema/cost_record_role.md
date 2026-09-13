---
search:
  boost: 5.0
---

# Slot: cost_record_role 


_Role of this cost record (catalog cost, catalog price, project estimate, or actual)._



<div data-search-exclude markdown="1">



URI: [pbs:cost_record_role](https://schema.pragmaticbim.ch/cost_record_role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation, catalog pricing, and calculation. Use cost_record_role to distinguish catalog cost/price (on Product) from project estimate/actual lines. Populate component_cost_items to act as an assembly (aggregated unit price). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CostRecordRole](CostRecordRole.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:cost_record_role |
| native | pbs:cost_record_role |




## LinkML Source

<details>
```yaml
name: cost_record_role
description: Role of this cost record (catalog cost, catalog price, project estimate,
  or actual).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: CostRecordRole
required: true

```
</details></div>