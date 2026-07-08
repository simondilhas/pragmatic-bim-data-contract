

# Slot: decision_status 


_Decision status expressed as a URI/CURIE (for example proposed, accepted, rejected, superseded)._





URI: [adms:status](http://www.w3.org/ns/adms#status)
Alias: decision_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | pbs:decision_status |




## LinkML Source

<details>
```yaml
name: decision_status
description: Decision status expressed as a URI/CURIE (for example proposed, accepted,
  rejected, superseded).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: adms:status
alias: decision_status
domain_of:
- Decision
range: uriorcurie

```
</details>