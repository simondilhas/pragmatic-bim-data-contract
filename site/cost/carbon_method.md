---
search:
  boost: 5.0
---

# Slot: carbon_method 


_Method used to normalize carbon to the price unit._



<div data-search-exclude markdown="1">



URI: [cost:carbon_method](https://schema.pragmaticbim.ch/cost/carbon_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KbobCarbonReference](KbobCarbonReference.md) | Reference to KBOB ecobilans benchmark concept IRIs. Indicator values are resolved from kbob-ecobilans-lca-factors.json, not stored here. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CarbonMethodEnum](CarbonMethodEnum.md) |
| Domain Of | [KbobCarbonReference](KbobCarbonReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:carbon_method |
| native | cost:carbon_method |




## LinkML Source

<details>
```yaml
name: carbon_method
description: Method used to normalize carbon to the price unit.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- KbobCarbonReference
range: CarbonMethodEnum

```
</details></div>