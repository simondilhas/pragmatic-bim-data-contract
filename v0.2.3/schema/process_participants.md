---
search:
  boost: 5.0
---

# Slot: process_participants 


_Agents participating in this BPMN process instance (for example assignees mapped from lane roles)._



<div data-search-exclude markdown="1">



URI: [pbs:process_participants](https://schema.pragmaticbim.ch/process_participants)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Process](Process.md) | Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Process](Process.md) |

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
| self | pbs:process_participants |
| native | pbs:process_participants |




## LinkML Source

<details>
```yaml
name: process_participants
description: Agents participating in this BPMN process instance (for example assignees
  mapped from lane roles).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Process
range: Agent
multivalued: true
inlined: false

```
</details></div>