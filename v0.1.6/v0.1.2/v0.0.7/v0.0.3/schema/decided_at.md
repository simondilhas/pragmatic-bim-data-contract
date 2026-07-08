

# Slot: decided_at 


_Timestamp when the decision was made._





URI: [dcterms:created](http://purl.org/dc/terms/created)
Alias: decided_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:created |
| native | pbs:decided_at |




## LinkML Source

<details>
```yaml
name: decided_at
description: Timestamp when the decision was made.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: dcterms:created
alias: decided_at
domain_of:
- Decision
range: datetime

```
</details>