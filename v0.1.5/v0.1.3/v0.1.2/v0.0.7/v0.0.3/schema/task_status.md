

# Slot: task_status 


_Task status URI/CURIE aligned with action status vocabularies._





URI: [schema:actionStatus](https://schema.org/actionStatus)
Alias: task_status

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
| Slot URI | [schema:actionStatus](https://schema.org/actionStatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:actionStatus |
| native | pbs:task_status |




## LinkML Source

<details>
```yaml
name: task_status
description: Task status URI/CURIE aligned with action status vocabularies.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:actionStatus
alias: task_status
domain_of:
- Task
range: uriorcurie

```
</details>