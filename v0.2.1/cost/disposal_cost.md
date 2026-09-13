---
search:
  boost: 5.0
---

# Slot: disposal_cost 


_Disposal cost per price unit in EUR (net, VAT excluded)._



<div data-search-exclude markdown="1">



URI: [cost:disposal_cost](https://schema.pragmaticbim.ch/cost/disposal_cost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemolitionCost](DemolitionCost.md) | Disassembly/demolition labor and disposal per price unit (EUR, net, VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decimal](Decimal.md) |
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
| self | cost:disposal_cost |
| native | cost:disposal_cost |




## LinkML Source

<details>
```yaml
name: disposal_cost
description: Disposal cost per price unit in EUR (net, VAT excluded).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- DemolitionCost
range: decimal

```
</details></div>