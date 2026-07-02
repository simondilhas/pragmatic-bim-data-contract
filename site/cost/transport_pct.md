---
search:
  boost: 5.0
---

# Slot: transport_pct 


_Transport-to-site (A4) allowance as a fraction of material cost (0–1)._



<div data-search-exclude markdown="1">



URI: [cost:transport_pct](https://schema.pragmaticbim.ch/cost/transport_pct)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [UnitPriceEntry](UnitPriceEntry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:transport_pct |
| native | cost:transport_pct |




## LinkML Source

<details>
```yaml
name: transport_pct
description: Transport-to-site (A4) allowance as a fraction of material cost (0–1).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: float

```
</details></div>