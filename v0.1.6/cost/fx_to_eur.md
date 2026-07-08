---
search:
  boost: 5.0
---

# Slot: fx_to_eur 


_Material FX only. Multiply local currency → EUR (for example 1 CHF × 0.95). EUR book → local uses delivered_eur / fx_to_eur._



<div data-search-exclude markdown="1">



URI: [cost:fx_to_eur](https://schema.pragmaticbim.ch/cost/fx_to_eur)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegionalBenchmark](RegionalBenchmark.md) | Material and labor factors for one region. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [RegionalBenchmark](RegionalBenchmark.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:fx_to_eur |
| native | cost:fx_to_eur |




## LinkML Source

<details>
```yaml
name: fx_to_eur
description: Material FX only. Multiply local currency → EUR (for example 1 CHF ×
  0.95). EUR book → local uses delivered_eur / fx_to_eur.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: float

```
</details></div>