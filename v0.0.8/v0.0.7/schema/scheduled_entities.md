---
search:
  boost: 5.0
---

# Slot: scheduled_entities 


_Model entities that this schedule template or schedule item applies to._



<div data-search-exclude markdown="1">



URI: [pbs:scheduled_entities](https://schema.pragmaticbim.ch/scheduled_entities)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTemplate](ScheduleTemplate.md) | Reusable schedule container defining items, milestones, and dependencies for ... |  no  |
| [ScheduleItem](ScheduleItem.md) | Planned work item with baseline and actual dates, linked to a schedule templa... |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a schedule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [ScheduleTemplate](ScheduleTemplate.md), [ScheduleItem](ScheduleItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:scheduled_entities |
| native | pbs:scheduled_entities |




## LinkML Source

<details>
```yaml
name: scheduled_entities
description: Model entities that this schedule template or schedule item applies to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleTemplate
- ScheduleItem
range: Entity
multivalued: true
inlined: false

```
</details></div>