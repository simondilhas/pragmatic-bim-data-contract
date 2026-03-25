

# Slot: assignee 


_Responsible agent._





URI: [schema:agent](https://schema.org/agent)
Alias: assignee

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:agent](https://schema.org/agent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:agent |
| native | pbs:assignee |




## LinkML Source

<details>
```yaml
name: assignee
description: Responsible agent.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:agent
alias: assignee
domain_of:
- Task
range: Agent
inlined: false

```
</details>