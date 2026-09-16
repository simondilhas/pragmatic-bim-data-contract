---
search:
  boost: 5.0
---

# Slot: target_value_number 


_Numeric target value when applicable._



<div data-search-exclude markdown="1">



URI: [pbs:target_value_number](https://schema.pragmaticbim.ch/target_value_number)
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
| Range | [Double](Double.md) |
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
| self | pbs:target_value_number |
| native | pbs:target_value_number |




## LinkML Source

<details>
```yaml
name: target_value_number
description: Numeric target value when applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
- CostRequirement
range: double

```
</details></div>