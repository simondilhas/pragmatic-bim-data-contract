---
search:
  boost: 5.0
---

# Slot: contract_type 


_Contract type expressed as a URI/CURIE from a controlled vocabulary (for example design, construction, supply)._



<div data-search-exclude markdown="1">



URI: [dcterms:type](http://purl.org/dc/terms/type)
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
| Slot URI | [dcterms:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:type |
| native | pbs:contract_type |




## LinkML Source

<details>
```yaml
name: contract_type
description: Contract type expressed as a URI/CURIE from a controlled vocabulary (for
  example design, construction, supply).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:type
domain_of:
- Contract
range: uriorcurie

```
</details></div>