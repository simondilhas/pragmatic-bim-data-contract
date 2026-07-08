---
search:
  boost: 5.0
---

# Slot: entries 


_Baseline unit-price entries keyed by product notation._



<div data-search-exclude markdown="1">



URI: [cost:entries](https://schema.pragmaticbim.ch/cost/entries)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BaselinePriceBook](BaselinePriceBook.md) | Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BaselinePriceBook](BaselinePriceBook.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:entries |
| native | cost:entries |




## LinkML Source

<details>
```yaml
name: entries
description: Baseline unit-price entries keyed by product notation.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- BaselinePriceBook
range: string

```
</details></div>