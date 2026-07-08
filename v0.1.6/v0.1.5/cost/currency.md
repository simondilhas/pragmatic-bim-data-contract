---
search:
  boost: 5.0
---

# Slot: currency 


_Local currency for labor rates and installed-cost total._



<div data-search-exclude markdown="1">



URI: [cost:currency](https://schema.pragmaticbim.ch/cost/currency)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegionalBenchmark](RegionalBenchmark.md) | Material and labor factors for one region. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CurrencyEnum](CurrencyEnum.md) |
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
| self | cost:currency |
| native | cost:currency |




## LinkML Source

<details>
```yaml
name: currency
description: Local currency for labor rates and installed-cost total.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: CurrencyEnum

```
</details></div>