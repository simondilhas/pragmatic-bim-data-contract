---
search:
  boost: 5.0
---

# Slot: onsite_labor_hours_per_unit 


_Onsite installation labor in person-hours per price_unit._



<div data-search-exclude markdown="1">



URI: [cost:onsite_labor_hours_per_unit](https://schema.pragmaticbim.ch/cost/onsite_labor_hours_per_unit)
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
| self | cost:onsite_labor_hours_per_unit |
| native | cost:onsite_labor_hours_per_unit |




## LinkML Source

<details>
```yaml
name: onsite_labor_hours_per_unit
description: Onsite installation labor in person-hours per price_unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: float

```
</details></div>