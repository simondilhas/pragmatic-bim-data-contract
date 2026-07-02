---
search:
  boost: 5.0
---

# Slot: gwp_kg_co2eq 


_Global warming potential in kg CO2eq per price unit._



<div data-search-exclude markdown="1">



URI: [cost:gwp_kg_co2eq](https://schema.pragmaticbim.ch/cost/gwp_kg_co2eq)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CarbonEstimate](CarbonEstimate.md) | Generated embodied-carbon estimate per price unit (optional output). Unit-conversion geometry is stored in typed slots — not in assumptions. density_kg_m3 for method density; mass_per_area_kg_m2 for area_yield; area_per_piece_m2 for piece_area. Optional thickness_m documents derived mass_per_area when thickness × density was used. |  no  |
| [CarbonComponent](CarbonComponent.md) | One layer or row contributing to a layer_recipe_sum carbon total. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [CarbonEstimate](CarbonEstimate.md), [CarbonComponent](CarbonComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:gwp_kg_co2eq |
| native | cost:gwp_kg_co2eq |




## LinkML Source

<details>
```yaml
name: gwp_kg_co2eq
description: Global warming potential in kg CO2eq per price unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonEstimate
- CarbonComponent
range: float

```
</details></div>