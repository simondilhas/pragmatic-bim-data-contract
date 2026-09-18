---
search:
  boost: 5.0
---

# Slot: contract_status 


_Contract status expressed as a URI/CURIE (for example draft, signed, active, terminated, superseded)._



<div data-search-exclude markdown="1">



URI: [adms:status](http://www.w3.org/ns/adms#status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Contract](Contract.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | pbs:contract_status |




## LinkML Source

<details>
```yaml
name: contract_status
description: Contract status expressed as a URI/CURIE (for example draft, signed,
  active, terminated, superseded).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: adms:status
domain_of:
- Contract
range: uriorcurie

```
</details></div>