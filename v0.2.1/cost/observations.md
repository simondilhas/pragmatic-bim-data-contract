---
search:
  boost: 5.0
---

# Slot: observations 


_Optional contributor or reference observations for canonical slot values. Parent entry scalars remain the resolved benchmark for costing._



<div data-search-exclude markdown="1">



URI: [cost:observations](https://schema.pragmaticbim.ch/cost/observations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | cost:observations |
| native | cost:observations |




## LinkML Source

<details>
```yaml
name: observations
description: Optional contributor or reference observations for canonical slot values.
  Parent entry scalars remain the resolved benchmark for costing.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: string

```
</details></div>