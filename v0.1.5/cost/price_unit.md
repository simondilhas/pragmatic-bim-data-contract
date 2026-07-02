---
search:
  boost: 5.0
---

# Slot: price_unit 


_Quantity unit the material cost refers to._



<div data-search-exclude markdown="1">



URI: [cost:price_unit](https://schema.pragmaticbim.ch/cost/price_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PriceUnitEnum](PriceUnitEnum.md) |
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
| self | cost:price_unit |
| native | cost:price_unit |




## LinkML Source

<details>
```yaml
name: price_unit
description: Quantity unit the material cost refers to.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: PriceUnitEnum

```
</details></div>