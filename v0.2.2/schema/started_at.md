---
search:
  boost: 5.0
---

# Slot: started_at 


_Timestamp when the process instance started._



<div data-search-exclude markdown="1">



URI: [dcterms:created](http://purl.org/dc/terms/created)
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
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:created |
| native | pbs:started_at |




## LinkML Source

<details>
```yaml
name: started_at
description: Timestamp when the process instance started.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:created
domain_of:
- Process
range: datetime

```
</details></div>