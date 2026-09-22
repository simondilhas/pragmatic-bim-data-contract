---
search:
  boost: 5.0
---

# Slot: completed_at 


_Timestamp when the process instance completed or terminated, when applicable._



<div data-search-exclude markdown="1">



URI: [pbs:completed_at](https://schema.pragmaticbim.ch/completed_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Process](Process.md) | Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Process](Process.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:completed_at |
| native | pbs:completed_at |




## LinkML Source

<details>
```yaml
name: completed_at
description: Timestamp when the process instance completed or terminated, when applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Process
range: datetime

```
</details></div>