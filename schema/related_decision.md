

# Slot: related_decision 


_Optional reference to a decision that informs or drives this task._





URI: [prov:used](http://www.w3.org/ns/prov#used)
Alias: related_decision

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decision](Decision.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [prov:used](http://www.w3.org/ns/prov#used) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:used |
| native | pbs:related_decision |




## LinkML Source

<details>
```yaml
name: related_decision
description: Optional reference to a decision that informs or drives this task.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: prov:used
alias: related_decision
domain_of:
- Task
range: Decision

```
</details>