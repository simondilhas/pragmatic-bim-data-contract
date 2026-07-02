---
search:
  boost: 5.0
---

# Slot: hours_per_unit 


_Demolition labor hours per price unit._



<div data-search-exclude markdown="1">



URI: [cost:hours_per_unit](https://schema.pragmaticbim.ch/cost/hours_per_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemolitionCost](DemolitionCost.md) | Disassembly/demolition labor and disposal per price unit (EUR, net, VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [DemolitionCost](DemolitionCost.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:hours_per_unit |
| native | cost:hours_per_unit |




## LinkML Source

<details>
```yaml
name: hours_per_unit
description: Demolition labor hours per price unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- DemolitionCost
range: float

```
</details></div>