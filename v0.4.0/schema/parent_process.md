---
search:
  boost: 5.0
---

# Slot: parent_process 


_Optional BPMN process instance that owns or spawned this task._



<div data-search-exclude markdown="1">



URI: [pbs:parent_process](https://schema.pragmaticbim.ch/parent_process)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Process](Process.md) |
| Domain Of | [Task](Task.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_process |
| native | pbs:parent_process |




## LinkML Source

<details>
```yaml
name: parent_process
description: Optional BPMN process instance that owns or spawned this task.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Task
range: Process
inlined: false

```
</details></div>