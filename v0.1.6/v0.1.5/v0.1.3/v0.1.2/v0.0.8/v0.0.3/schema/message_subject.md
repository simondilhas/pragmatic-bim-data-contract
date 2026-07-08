

# Slot: message_subject 


_Optional subject or headline for the message._





URI: [schema:headline](https://schema.org/headline)
Alias: message_subject

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:headline](https://schema.org/headline) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:headline |
| native | pbs:message_subject |




## LinkML Source

<details>
```yaml
name: message_subject
description: Optional subject or headline for the message.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:headline
alias: message_subject
domain_of:
- Message
range: string

```
</details>