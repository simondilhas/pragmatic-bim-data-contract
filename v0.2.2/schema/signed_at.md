---
search:
  boost: 5.0
---

# Slot: signed_at 


_Timestamp when the contract was signed._



<div data-search-exclude markdown="1">



URI: [pbs:signed_at](https://schema.pragmaticbim.ch/signed_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Contract](Contract.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:signed_at |
| native | pbs:signed_at |




## LinkML Source

<details>
```yaml
name: signed_at
description: Timestamp when the contract was signed.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Contract
range: datetime

```
</details></div>