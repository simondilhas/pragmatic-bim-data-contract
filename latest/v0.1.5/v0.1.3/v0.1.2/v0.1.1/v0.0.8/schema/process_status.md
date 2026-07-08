---
search:
  boost: 5.0
---

# Slot: process_status 


_Process instance status expressed as a URI/CURIE (for example active, suspended, completed, terminated)._



<div data-search-exclude markdown="1">



URI: [adms:status](http://www.w3.org/ns/adms#status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Process](Process.md) | Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Process](Process.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | pbs:process_status |




## LinkML Source

<details>
```yaml
name: process_status
description: Process instance status expressed as a URI/CURIE (for example active,
  suspended, completed, terminated).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: adms:status
domain_of:
- Process
range: uriorcurie

```
</details></div>