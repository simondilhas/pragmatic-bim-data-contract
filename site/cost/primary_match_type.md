---
search:
  boost: 5.0
---

# Slot: primary_match_type 


_SKOS mapping match type used for the primary carbon reference._



<div data-search-exclude markdown="1">



URI: [cost:primary_match_type](https://schema.pragmaticbim.ch/cost/primary_match_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KbobCarbonReference](KbobCarbonReference.md) | Reference to KBOB ecobilans benchmark concept IRIs. Indicator values are resolved from kbob-ecobilans-lca-factors.json, not stored here. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [KbobMatchTypeEnum](KbobMatchTypeEnum.md) |
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
| self | cost:primary_match_type |
| native | cost:primary_match_type |




## LinkML Source

<details>
```yaml
name: primary_match_type
description: SKOS mapping match type used for the primary carbon reference.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- KbobCarbonReference
range: KbobMatchTypeEnum

```
</details></div>