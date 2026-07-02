---
search:
  boost: 5.0
---

# Slot: process_definition_uri 


_URI identifying the BPMN process definition (for example engine definition key or BPMN artifact URI)._



<div data-search-exclude markdown="1">



URI: [pbs:process_definition_uri](https://schema.pragmaticbim.ch/process_definition_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Process](Process.md) | Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Process](Process.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:process_definition_uri |
| native | pbs:process_definition_uri |




## LinkML Source

<details>
```yaml
name: process_definition_uri
description: URI identifying the BPMN process definition (for example engine definition
  key or BPMN artifact URI).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Process
range: uriorcurie
required: true

```
</details></div>