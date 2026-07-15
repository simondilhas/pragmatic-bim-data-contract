---
search:
  boost: 5.0
---

# Slot: offsite_labor_hours_high 


_Derived upper offsite labor hours per price unit._



<div data-search-exclude markdown="1">



URI: [cost:offsite_labor_hours_high](https://schema.pragmaticbim.ch/cost/offsite_labor_hours_high)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceUncertainty](PriceUncertainty.md) | Relative uncertainty band around point material cost and labor hours. Percent slots are signed fractions relative to the point estimate (for example material_low_pct -0.12 → low = point × 0.88). Derived EUR and hour bounds are optional generator output for convenience. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [PriceUncertainty](PriceUncertainty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:offsite_labor_hours_high |
| native | cost:offsite_labor_hours_high |




## LinkML Source

<details>
```yaml
name: offsite_labor_hours_high
description: Derived upper offsite labor hours per price unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceUncertainty
range: float

```
</details></div>