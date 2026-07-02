---
search:
  boost: 5.0
---

# Slot: delivered_material_cost 


_Derived delivered material cost in EUR (material_cost × (1 + waste_pct) × (1 + transport_pct)). Net, VAT excluded. Optional in authored input._



<div data-search-exclude markdown="1">



URI: [cost:delivered_material_cost](https://schema.pragmaticbim.ch/cost/delivered_material_cost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). |  no  |






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
| self | cost:delivered_material_cost |
| native | cost:delivered_material_cost |




## LinkML Source

<details>
```yaml
name: delivered_material_cost
description: Derived delivered material cost in EUR (material_cost × (1 + waste_pct)
  × (1 + transport_pct)). Net, VAT excluded. Optional in authored input.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: decimal

```
</details></div>