

# Slot: task_type 


_Task type expressed as a URI/CURIE from a controlled vocabulary._





URI: [dcterms:type](http://purl.org/dc/terms/type)
Alias: task_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workf... |  no  |






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


* from schema: https://example.org/pragmatic-bim-data-contract




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
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: dcterms:type
alias: task_type
domain_of:
- Task
range: uriorcurie

```
</details>