---
search:
  boost: 5.0
---

# Slot: labor_factor 


_Regional labor cost multiplier (default 1.0)._



<div data-search-exclude markdown="1">



URI: [cost:labor_factor](https://schema.pragmaticbim.ch/cost/labor_factor)
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
| self | cost:labor_factor |
| native | cost:labor_factor |




## LinkML Source

<details>
```yaml
name: labor_factor
description: Regional labor cost multiplier (default 1.0).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: float

```
</details></div>