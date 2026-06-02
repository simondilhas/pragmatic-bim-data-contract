---
search:
  boost: 5.0
---

# Slot: related_time_record 


_Optional TimeRecord plan item this schedule requirement aligns with or must satisfy._



<div data-search-exclude markdown="1">



URI: [pbs:related_time_record](https://schema.pragmaticbim.ch/related_time_record)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleRequirement](ScheduleRequirement.md) | Schedule obligation requirement (deadline, milestone, or start/finish window). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [ScheduleRequirement](ScheduleRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_time_record |
| native | pbs:related_time_record |




## LinkML Source

<details>
```yaml
name: related_time_record
description: Optional TimeRecord plan item this schedule requirement aligns with or
  must satisfy.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleRequirement
range: Entity
inlined: false

```
</details></div>