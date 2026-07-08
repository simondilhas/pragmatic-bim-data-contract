

# Slot: recipients 


_Agents that received the message._





URI: [schema:recipient](https://schema.org/recipient)
Alias: recipients

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:recipient](https://schema.org/recipient) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:recipient |
| native | pbs:recipients |




## LinkML Source

<details>
```yaml
name: recipients
description: Agents that received the message.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:recipient
alias: recipients
domain_of:
- Message
range: Agent
multivalued: true
inlined: false

```
</details>