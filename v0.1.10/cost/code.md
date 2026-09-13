---
search:
  boost: 5.0
---

# Slot: code 


_Region code (for example CH_ZH, DE_MU)._



<div data-search-exclude markdown="1">



URI: [cost:code](https://schema.pragmaticbim.ch/cost/code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegionalBenchmark](RegionalBenchmark.md) | Material and labor factors for one region. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | cost:code |
| native | cost:code |




## LinkML Source

<details>
```yaml
name: code
description: Region code (for example CH_ZH, DE_MU).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: string

```
</details></div>