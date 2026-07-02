---
search:
  boost: 5.0
---

# Slot: uncertainty 


_Relative uncertainty band for material cost and labor hours. Derived low/high amounts are computed from point estimates at generation time._



<div data-search-exclude markdown="1">



URI: [cost:uncertainty](https://schema.pragmaticbim.ch/cost/uncertainty)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PriceUncertainty](PriceUncertainty.md) |
| Domain Of | [UnitPriceEntry](UnitPriceEntry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:uncertainty |
| native | cost:uncertainty |




## LinkML Source

<details>
```yaml
name: uncertainty
description: Relative uncertainty band for material cost and labor hours. Derived
  low/high amounts are computed from point estimates at generation time.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: PriceUncertainty
inlined: true

```
</details></div>