---
search:
  boost: 5.0
---

# Slot: contributor 


_Person or team that supplied the observation._



<div data-search-exclude markdown="1">



URI: [cost:contributor](https://schema.pragmaticbim.ch/cost/contributor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PriceObservation](PriceObservation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:contributor |
| native | cost:contributor |




## LinkML Source

<details>
```yaml
name: contributor
description: Person or team that supplied the observation.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceObservation
range: string

```
</details></div>