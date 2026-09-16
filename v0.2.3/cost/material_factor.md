---
search:
  boost: 5.0
---

# Slot: material_factor 


_Regional material price level vs anchor region (DE_MU = 1.0)._



<div data-search-exclude markdown="1">



URI: [cost:material_factor](https://schema.pragmaticbim.ch/cost/material_factor)
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
| self | cost:material_factor |
| native | cost:material_factor |




## LinkML Source

<details>
```yaml
name: material_factor
description: Regional material price level vs anchor region (DE_MU = 1.0).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: float

```
</details></div>