---
search:
  boost: 5.0
---

# Slot: offsite_labor_unit_price 


_Factory/offsite labor rate per hour in currency (net, VAT excluded)._



<div data-search-exclude markdown="1">



URI: [cost:offsite_labor_unit_price](https://schema.pragmaticbim.ch/cost/offsite_labor_unit_price)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegionalBenchmark](RegionalBenchmark.md) | Material and labor factors for one region. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decimal](Decimal.md) |
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
| self | cost:offsite_labor_unit_price |
| native | cost:offsite_labor_unit_price |




## LinkML Source

<details>
```yaml
name: offsite_labor_unit_price
description: Factory/offsite labor rate per hour in currency (net, VAT excluded).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- RegionalBenchmark
range: decimal

```
</details></div>