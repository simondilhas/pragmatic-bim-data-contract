---
search:
  boost: 5.0
---

# Slot: schedule_template 


_Parent schedule template this item or dependency belongs to._



<div data-search-exclude markdown="1">



URI: [pbs:schedule_template](https://schema.pragmaticbim.ch/schedule_template)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleItem](ScheduleItem.md) | Planned work item with baseline and actual dates, linked to a schedule templa... |  no  |
| [ScheduleDependency](ScheduleDependency.md) | Precedence relationship between two schedule items, optionally with lag |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a schedule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScheduleTemplate](ScheduleTemplate.md) |
| Domain Of | [ScheduleItem](ScheduleItem.md), [ScheduleDependency](ScheduleDependency.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:schedule_template |
| native | pbs:schedule_template |




## LinkML Source

<details>
```yaml
name: schedule_template
description: Parent schedule template this item or dependency belongs to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleItem
- ScheduleDependency
range: ScheduleTemplate
inlined: false

```
</details></div>