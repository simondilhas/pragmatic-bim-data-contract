

# Slot: sent_at 


_Timestamp when the message was sent._





URI: [schema:dateSent](https://schema.org/dateSent)
Alias: sent_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:dateSent](https://schema.org/dateSent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:dateSent |
| native | pbs:sent_at |




## LinkML Source

<details>
```yaml
name: sent_at
description: Timestamp when the message was sent.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:dateSent
alias: sent_at
domain_of:
- Message
range: datetime

```
</details>