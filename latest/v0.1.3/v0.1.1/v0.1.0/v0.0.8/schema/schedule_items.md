---
search:
  boost: 5.0
---

# Slot: schedule_items 


_Schedule items contained in this template; milestone instances may also appear through the ScheduleItem subtype._



<div data-search-exclude markdown="1">



URI: [pbs:schedule_items](https://schema.pragmaticbim.ch/schedule_items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTemplate](ScheduleTemplate.md) | Reusable schedule container defining items, milestones, and dependencies for ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScheduleItem](ScheduleItem.md) |
| Domain Of | [ScheduleTemplate](ScheduleTemplate.md) |

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
| self | pbs:schedule_items |
| native | pbs:schedule_items |




## LinkML Source

<details>
```yaml
name: schedule_items
description: Schedule items contained in this template; milestone instances may also
  appear through the ScheduleItem subtype.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleTemplate
range: ScheduleItem
multivalued: true
inlined: false

```
</details></div>