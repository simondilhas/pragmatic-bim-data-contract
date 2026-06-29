---
search:
  boost: 5.0
---

# Slot: target_operator 


_Comparison operator for the requirement target._



<div data-search-exclude markdown="1">



URI: [pbs:target_operator](https://schema.pragmaticbim.ch/target_operator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). Boolean targets use target_value_boolean with requirement_property_key aligned to entity slot names where applicable (for example is_heated on Space). Application pipelines compare the subject entity slot to the requirement target and record the outcome as MatchChange (match_status met, unmet, or unknown). |  no  |
| [CostRequirement](CostRequirement.md) | Cost or budget requirement (unit-cost cap, total budget limit, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RequirementTargetOperator](RequirementTargetOperator.md) |
| Domain Of | [PerformanceRequirement](PerformanceRequirement.md), [CostRequirement](CostRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:target_operator |
| native | pbs:target_operator |




## LinkML Source

<details>
```yaml
name: target_operator
description: Comparison operator for the requirement target.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
- CostRequirement
range: RequirementTargetOperator

```
</details></div>