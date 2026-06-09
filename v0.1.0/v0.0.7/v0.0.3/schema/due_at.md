

# Slot: due_at 


_Due timestamp for task completion._





URI: [schema:deadline](https://schema.org/deadline)
Alias: due_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:deadline](https://schema.org/deadline) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:deadline |
| native | pbs:due_at |




## LinkML Source

<details>
```yaml
name: due_at
description: Due timestamp for task completion.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:deadline
alias: due_at
domain_of:
- Task
range: datetime

```
</details>