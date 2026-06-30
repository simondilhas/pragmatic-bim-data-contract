

# Slot: rationale 


_Human-readable rationale that explains why the decision was made._





URI: [dcterms:description](http://purl.org/dc/terms/description)
Alias: rationale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [dcterms:description](http://purl.org/dc/terms/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:description |
| native | pbs:rationale |




## LinkML Source

<details>
```yaml
name: rationale
description: Human-readable rationale that explains why the decision was made.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: dcterms:description
alias: rationale
domain_of:
- Decision
range: string

```
</details>