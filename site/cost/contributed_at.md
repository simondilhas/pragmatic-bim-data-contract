---
search:
  boost: 5.0
---

# Slot: contributed_at 


_Date the observation was recorded or published._



<div data-search-exclude markdown="1">



URI: [cost:contributed_at](https://schema.pragmaticbim.ch/cost/contributed_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
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
| self | cost:contributed_at |
| native | cost:contributed_at |




## LinkML Source

<details>
```yaml
name: contributed_at
description: Date the observation was recorded or published.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceObservation
range: date

```
</details></div>