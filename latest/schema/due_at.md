---
search:
  boost: 5.0
---

# Slot: due_at 


_Due timestamp for task completion._



<div data-search-exclude markdown="1">



URI: [schema:deadline](https://schema.org/deadline)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:deadline](https://schema.org/deadline) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:deadline |
| native | pbs:due_at |




## LinkML Source

<details>
```yaml
name: due_at
description: Due timestamp for task completion.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:deadline
domain_of:
- Task
range: datetime

```
</details></div>