---
search:
  boost: 5.0
---

# Slot: material_cost 


_Ex-works material cost per price_unit in EUR (net, VAT excluded)._



<div data-search-exclude markdown="1">



URI: [cost:material_cost](https://schema.pragmaticbim.ch/cost/material_cost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decimal](Decimal.md) |
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
| self | cost:material_cost |
| native | cost:material_cost |




## LinkML Source

<details>
```yaml
name: material_cost
description: Ex-works material cost per price_unit in EUR (net, VAT excluded).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: decimal

```
</details></div>