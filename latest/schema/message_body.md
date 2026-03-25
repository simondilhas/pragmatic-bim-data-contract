

# Slot: message_body 


_Human-readable message content._





URI: [schema:text](https://schema.org/text)
Alias: message_body

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
| Slot URI | [schema:text](https://schema.org/text) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:text |
| native | pbs:message_body |




## LinkML Source

<details>
```yaml
name: message_body
description: Human-readable message content.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:text
alias: message_body
domain_of:
- Message
range: string

```
</details>