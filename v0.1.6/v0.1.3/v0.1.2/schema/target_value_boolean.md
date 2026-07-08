---
search:
  boost: 5.0
---

# Slot: target_value_boolean 


_Boolean target value when applicable._



<div data-search-exclude markdown="1">



URI: [pbs:target_value_boolean](https://schema.pragmaticbim.ch/target_value_boolean)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). Boolean targets use target_value_boolean with requirement_property_key aligned to entity slot names where applicable (for example is_heated on Space). Application pipelines compare the subject entity slot to the requirement target and record the outcome as MatchChange (match_status met, unmet, or unknown). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [PerformanceRequirement](PerformanceRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:target_value_boolean |
| native | pbs:target_value_boolean |




## LinkML Source

<details>
```yaml
name: target_value_boolean
description: Boolean target value when applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
range: boolean

```
</details></div>