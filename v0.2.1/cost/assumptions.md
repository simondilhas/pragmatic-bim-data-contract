---
search:
  boost: 5.0
---

# Slot: assumptions 


_Human-readable notes only (for example layer_recipe quantity_basis). Not used for unit conversion._



<div data-search-exclude markdown="1">



URI: [cost:assumptions](https://schema.pragmaticbim.ch/cost/assumptions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CarbonEstimate](CarbonEstimate.md) | Generated embodied-carbon estimate per price unit (optional output). Unit-conversion geometry is stored in typed slots — not in assumptions. density_kg_m3 for method density; mass_per_area_kg_m2 for area_yield; area_per_piece_m2 for piece_area. Optional thickness_m documents derived mass_per_area when thickness × density was used. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | cost:assumptions |
| native | cost:assumptions |




## LinkML Source

<details>
```yaml
name: assumptions
description: Human-readable notes only (for example layer_recipe quantity_basis).
  Not used for unit conversion.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonEstimate
range: string

```
</details></div>