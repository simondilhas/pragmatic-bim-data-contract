---
search:
  boost: 5.0
---

# Slot: unit 


_Unit for demolition quantities._



<div data-search-exclude markdown="1">



URI: [cost:unit](https://schema.pragmaticbim.ch/cost/unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemolitionCost](DemolitionCost.md) | Disassembly/demolition labor and disposal per price unit (EUR, net, VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PriceUnitEnum](PriceUnitEnum.md) |
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
| self | cost:unit |
| native | cost:unit |




## LinkML Source

<details>
```yaml
name: unit
description: Unit for demolition quantities.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- DemolitionCost
range: PriceUnitEnum

```
</details></div>