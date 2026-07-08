

# Slot: message_type 


_Message type expressed as a URI/CURIE from a controlled vocabulary._





URI: [dcterms:type](http://purl.org/dc/terms/type)
Alias: message_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [dcterms:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:type |
| native | pbs:message_type |




## LinkML Source

<details>
```yaml
name: message_type
description: Message type expressed as a URI/CURIE from a controlled vocabulary.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: dcterms:type
alias: message_type
domain_of:
- Message
range: uriorcurie

```
</details>