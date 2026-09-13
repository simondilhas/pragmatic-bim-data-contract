---
search:
  boost: 5.0
---

# Slot: aspect 


_Canonical slot this observation applies to._



<div data-search-exclude markdown="1">



URI: [cost:aspect](https://schema.pragmaticbim.ch/cost/aspect)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PriceObservationAspectEnum](PriceObservationAspectEnum.md) |
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
| self | cost:aspect |
| native | cost:aspect |




## LinkML Source

<details>
```yaml
name: aspect
description: Canonical slot this observation applies to.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceObservation
range: PriceObservationAspectEnum

```
</details></div>