

# Slot: task_notes 


_Additional notes or implementation details for the task._





URI: [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)
Alias: task_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:comment |
| native | pbs:task_notes |




## LinkML Source

<details>
```yaml
name: task_notes
description: Additional notes or implementation details for the task.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: rdfs:comment
alias: task_notes
domain_of:
- Task
range: string

```
</details>