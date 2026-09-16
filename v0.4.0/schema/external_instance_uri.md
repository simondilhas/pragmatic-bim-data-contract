---
search:
  boost: 5.0
---

# Slot: external_instance_uri 


_URI of the corresponding process instance in an external workflow engine when applicable._



<div data-search-exclude markdown="1">



URI: [pbs:external_instance_uri](https://schema.pragmaticbim.ch/external_instance_uri)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:external_instance_uri |
| native | pbs:external_instance_uri |




## LinkML Source

<details>
```yaml
name: external_instance_uri
description: URI of the corresponding process instance in an external workflow engine
  when applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Process
range: uriorcurie

```
</details></div>