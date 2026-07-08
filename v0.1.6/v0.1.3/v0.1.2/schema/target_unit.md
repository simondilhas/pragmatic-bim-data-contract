---
search:
  boost: 5.0
---

# Slot: target_unit 


_Unit for numeric targets (for example W/m2K, min, dB)._



<div data-search-exclude markdown="1">



URI: [pbs:target_unit](https://schema.pragmaticbim.ch/target_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). Boolean targets use target_value_boolean with requirement_property_key aligned to entity slot names where applicable (for example is_heated on Space). Application pipelines compare the subject entity slot to the requirement target and record the outcome as MatchChange (match_status met, unmet, or unknown). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:target_unit |
| native | pbs:target_unit |




## LinkML Source

<details>
```yaml
name: target_unit
description: Unit for numeric targets (for example W/m2K, min, dB).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
range: string

```
</details></div>