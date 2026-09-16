---
search:
  boost: 5.0
---

# Slot: regions 


_Regional benchmarks keyed by region code._



<div data-search-exclude markdown="1">



URI: [cost:regions](https://schema.pragmaticbim.ch/cost/regions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegionalCostBenchmarkBook](RegionalCostBenchmarkBook.md) | Regional material and labor benchmarks paired with a BaselinePriceBook. Installed cost in regional currency uses fx_to_eur for material EUR→local and labor_unit_price in local currency. All monetary rates are net (VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [RegionalCostBenchmarkBook](RegionalCostBenchmarkBook.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:regions |
| native | cost:regions |




## LinkML Source

<details>
```yaml
name: regions
description: Regional benchmarks keyed by region code.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalCostBenchmarkBook
range: string

```
</details></div>