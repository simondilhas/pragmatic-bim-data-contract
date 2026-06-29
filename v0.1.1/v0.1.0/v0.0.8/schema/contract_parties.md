---
search:
  boost: 5.0
---

# Slot: contract_parties 


_Agents party to the contract (for example client, contractor, consultant)._



<div data-search-exclude markdown="1">



URI: [pbs:contract_parties](https://schema.pragmaticbim.ch/contract_parties)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Contract](Contract.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:contract_parties |
| native | pbs:contract_parties |




## LinkML Source

<details>
```yaml
name: contract_parties
description: Agents party to the contract (for example client, contractor, consultant).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Contract
range: Agent
multivalued: true
inlined: false

```
</details></div>