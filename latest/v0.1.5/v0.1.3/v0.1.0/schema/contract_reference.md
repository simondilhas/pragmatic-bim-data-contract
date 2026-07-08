---
search:
  boost: 5.0
---

# Slot: contract_reference 


_Human-readable contract number or external reference._



<div data-search-exclude markdown="1">



URI: [pbs:contract_reference](https://schema.pragmaticbim.ch/contract_reference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:contract_reference |
| native | pbs:contract_reference |




## LinkML Source

<details>
```yaml
name: contract_reference
description: Human-readable contract number or external reference.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Contract
range: string

```
</details></div>