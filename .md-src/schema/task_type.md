---
search:
  boost: 5.0
---

# Slot: task_type 


_Task type expressed as a URI/CURIE from a controlled vocabulary._



<div data-search-exclude markdown="1">



URI: [dcterms:type](http://purl.org/dc/terms/type)
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
| Slot URI | [dcterms:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:type |
| native | pbs:task_type |




## LinkML Source

<details>
```yaml
name: task_type
description: Task type expressed as a URI/CURIE from a controlled vocabulary.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:type
domain_of:
- Task
range: uriorcurie

```
</details></div>