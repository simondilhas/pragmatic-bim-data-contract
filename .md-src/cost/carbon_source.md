---
search:
  boost: 5.0
---

# Slot: carbon_source 


_Human-readable name of the carbon reference database._



<div data-search-exclude markdown="1">



URI: [cost:carbon_source](https://schema.pragmaticbim.ch/cost/carbon_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BaselinePriceBook](BaselinePriceBook.md) | Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark. |  no  |






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
| self | cost:carbon_source |
| native | cost:carbon_source |




## LinkML Source

<details>
```yaml
name: carbon_source
description: Human-readable name of the carbon reference database.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- BaselinePriceBook
range: string

```
</details></div>