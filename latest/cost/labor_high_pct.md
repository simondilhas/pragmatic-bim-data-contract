---
search:
  boost: 5.0
---

# Slot: labor_high_pct 


_Upper labor bound as signed fraction of labor hours (≥ 0)._



<div data-search-exclude markdown="1">



URI: [cost:labor_high_pct](https://schema.pragmaticbim.ch/cost/labor_high_pct)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceUncertainty](PriceUncertainty.md) | Relative uncertainty band around point material cost and labor hours. Percent slots are signed fractions relative to the point estimate (for example material_low_pct -0.12 → low = point × 0.88). Derived EUR and hour bounds are optional generator output for convenience. |  yes  |






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
| self | cost:labor_high_pct |
| native | cost:labor_high_pct |




## LinkML Source

<details>
```yaml
name: labor_high_pct
description: Upper labor bound as signed fraction of labor hours (≥ 0).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceUncertainty
range: float

```
</details></div>