---
search:
  boost: 5.0
---

# Slot: earliest_start_at 


_Earliest permitted start when a schedule requirement defines a start window._



<div data-search-exclude markdown="1">



URI: [pbs:earliest_start_at](https://schema.pragmaticbim.ch/earliest_start_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleRequirement](ScheduleRequirement.md) | Schedule obligation requirement (deadline, milestone, or start/finish window). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:earliest_start_at |
| native | pbs:earliest_start_at |




## LinkML Source

<details>
```yaml
name: earliest_start_at
description: Earliest permitted start when a schedule requirement defines a start
  window.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleRequirement
range: datetime

```
</details></div>