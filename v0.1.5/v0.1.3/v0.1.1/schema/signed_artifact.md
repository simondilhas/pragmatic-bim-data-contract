---
search:
  boost: 5.0
---

# Slot: signed_artifact 


_Optional signed contract artifact at storage_link._



<div data-search-exclude markdown="1">



URI: [pbs:signed_artifact](https://schema.pragmaticbim.ch/signed_artifact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Artifact](Artifact.md) |
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
| self | pbs:signed_artifact |
| native | pbs:signed_artifact |




## LinkML Source

<details>
```yaml
name: signed_artifact
description: Optional signed contract artifact at storage_link.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Contract
range: Artifact
inlined: false

```
</details></div>