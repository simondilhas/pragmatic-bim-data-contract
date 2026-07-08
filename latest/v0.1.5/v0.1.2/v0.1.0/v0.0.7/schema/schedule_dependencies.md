---
search:
  boost: 5.0
---

# Slot: schedule_dependencies 


_Dependency relationships used within this schedule template._



<div data-search-exclude markdown="1">



URI: [pbs:schedule_dependencies](https://schema.pragmaticbim.ch/schedule_dependencies)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTemplate](ScheduleTemplate.md) | Reusable schedule container defining items, milestones, and dependencies for ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScheduleDependency](ScheduleDependency.md) |
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
| self | pbs:schedule_dependencies |
| native | pbs:schedule_dependencies |




## LinkML Source

<details>
```yaml
name: schedule_dependencies
description: Dependency relationships used within this schedule template.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleTemplate
range: ScheduleDependency
multivalued: true
inlined: false

```
</details></div>