---
search:
  boost: 5.0
---

# Slot: kbob 


_KBOB ecobilans carbon reference for this product._



<div data-search-exclude markdown="1">



URI: [cost:kbob](https://schema.pragmaticbim.ch/cost/kbob)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [KbobCarbonReference](KbobCarbonReference.md) |
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
| self | cost:kbob |
| native | cost:kbob |




## LinkML Source

<details>
```yaml
name: kbob
description: KBOB ecobilans carbon reference for this product.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: KbobCarbonReference
inlined: true

```
</details></div>