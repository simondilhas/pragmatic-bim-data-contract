---
search:
  boost: 5.0
---

# Slot: quantity_per_price_unit 


_Layer quantity per one parent price unit._



<div data-search-exclude markdown="1">



URI: [cost:quantity_per_price_unit](https://schema.pragmaticbim.ch/cost/quantity_per_price_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CarbonComponent](CarbonComponent.md) | One layer or row contributing to a layer_recipe_sum carbon total. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [CarbonComponent](CarbonComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:quantity_per_price_unit |
| native | cost:quantity_per_price_unit |




## LinkML Source

<details>
```yaml
name: quantity_per_price_unit
description: Layer quantity per one parent price unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonComponent
range: float

```
</details></div>