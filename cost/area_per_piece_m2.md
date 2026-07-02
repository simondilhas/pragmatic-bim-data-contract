---
search:
  boost: 5.0
---

# Slot: area_per_piece_m2 


_Area per piece (m²/pcs) used when method is piece_area (price pcs, KBOB m²)._



<div data-search-exclude markdown="1">



URI: [cost:area_per_piece_m2](https://schema.pragmaticbim.ch/cost/area_per_piece_m2)
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
| self | cost:area_per_piece_m2 |
| native | cost:area_per_piece_m2 |




## LinkML Source

<details>
```yaml
name: area_per_piece_m2
description: Area per piece (m²/pcs) used when method is piece_area (price pcs, KBOB
  m²).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonEstimate
range: float

```
</details></div>