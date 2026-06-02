---
search:
  boost: 5.0
---

# Slot: related_decision 


_Optional reference to a decision that informs or drives this task._



<div data-search-exclude markdown="1">



URI: [prov:used](http://www.w3.org/ns/prov#used)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decision](Decision.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [prov:used](http://www.w3.org/ns/prov#used) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:used |
| native | pbs:related_decision |




## LinkML Source

<details>
```yaml
name: related_decision
description: Optional reference to a decision that informs or drives this task.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: prov:used
domain_of:
- Task
range: Decision
inlined: false

```
</details></div>