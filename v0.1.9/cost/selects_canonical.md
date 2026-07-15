---
search:
  boost: 5.0
---

# Slot: selects_canonical 


_Whether this observation was selected for the parent canonical value._



<div data-search-exclude markdown="1">



URI: [cost:selects_canonical](https://schema.pragmaticbim.ch/cost/selects_canonical)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
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
| self | cost:selects_canonical |
| native | cost:selects_canonical |




## LinkML Source

<details>
```yaml
name: selects_canonical
description: Whether this observation was selected for the parent canonical value.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceObservation
range: boolean

```
</details></div>