---
search:
  boost: 5.0
---

# Slot: thickness_m 


_Optional layer thickness (m) when mass_per_area_kg_m2 was derived as thickness_m × density_kg_m3._



<div data-search-exclude markdown="1">



URI: [cost:thickness_m](https://schema.pragmaticbim.ch/cost/thickness_m)
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
| self | cost:thickness_m |
| native | cost:thickness_m |




## LinkML Source

<details>
```yaml
name: thickness_m
description: Optional layer thickness (m) when mass_per_area_kg_m2 was derived as
  thickness_m × density_kg_m3.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonEstimate
range: float

```
</details></div>