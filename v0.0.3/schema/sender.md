

# Slot: sender 


_Agent that sent the message._





URI: [schema:sender](https://schema.org/sender)
Alias: sender

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
| Slot URI | [schema:sender](https://schema.org/sender) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:sender |
| native | pbs:sender |




## LinkML Source

<details>
```yaml
name: sender
description: Agent that sent the message.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:sender
alias: sender
domain_of:
- Message
range: Agent
inlined: false

```
</details>