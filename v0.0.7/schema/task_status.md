---
search:
  boost: 5.0
---

# Slot: task_status 


_Task status URI/CURIE aligned with action status vocabularies._



<div data-search-exclude markdown="1">



URI: [schema:actionStatus](https://schema.org/actionStatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:actionStatus](https://schema.org/actionStatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:actionStatus |
| native | pbs:task_status |




## LinkML Source

<details>
```yaml
name: task_status
description: Task status URI/CURIE aligned with action status vocabularies.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:actionStatus
domain_of:
- Task
range: uriorcurie

```
</details></div>