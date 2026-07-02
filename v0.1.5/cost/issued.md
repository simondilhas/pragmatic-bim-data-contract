---
search:
  boost: 5.0
---

# Slot: issued 


_Publication date of this dataset edition._



<div data-search-exclude markdown="1">



URI: [cost:issued](https://schema.pragmaticbim.ch/cost/issued)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BaselinePriceBook](BaselinePriceBook.md) | Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark. |  yes  |
| [RegionalCostBenchmarkBook](RegionalCostBenchmarkBook.md) | Regional material and labor benchmarks paired with a BaselinePriceBook. Installed cost in regional currency uses fx_to_eur for material EUR→local and labor_unit_price in local currency. All monetary rates are net (VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [BaselinePriceBook](BaselinePriceBook.md), [RegionalCostBenchmarkBook](RegionalCostBenchmarkBook.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:issued |
| native | cost:issued |




## LinkML Source

<details>
```yaml
name: issued
description: Publication date of this dataset edition.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- BaselinePriceBook
- RegionalCostBenchmarkBook
range: date

```
</details></div>