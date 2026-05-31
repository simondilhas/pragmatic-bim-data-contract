---
search:
  boost: 5.0
---

# Slot: planned_finish_at 


_Planned finish timestamp for the schedule item._



<div data-search-exclude markdown="1">



URI: [pbs:planned_finish_at](https://schema.pragmaticbim.ch/planned_finish_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleItem](ScheduleItem.md) | Planned work item with baseline and actual dates, linked to a schedule templa... |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a schedule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [ScheduleItem](ScheduleItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:planned_finish_at |
| native | pbs:planned_finish_at |




## LinkML Source

<details>
```yaml
name: planned_finish_at
description: Planned finish timestamp for the schedule item.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleItem
range: datetime

```
</details></div>