---
search:
  boost: 5.0
---

# Slot: density_kg_m3 


_Material density (kg/m³) used when method is density (price m³, KBOB kg)._



<div data-search-exclude markdown="1">



URI: [cost:density_kg_m3](https://schema.pragmaticbim.ch/cost/density_kg_m3)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CarbonEstimate](CarbonEstimate.md) | Generated embodied-carbon estimate per price unit (optional output). Unit-conversion geometry is stored in typed slots — not in assumptions. density_kg_m3 for method density; mass_per_area_kg_m2 for area_yield; area_per_piece_m2 for piece_area. Optional thickness_m documents derived mass_per_area when thickness × density was used. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [CarbonEstimate](CarbonEstimate.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:density_kg_m3 |
| native | cost:density_kg_m3 |




## LinkML Source

<details>
```yaml
name: density_kg_m3
description: Material density (kg/m³) used when method is density (price m³, KBOB
  kg).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonEstimate
range: float

```
</details></div>