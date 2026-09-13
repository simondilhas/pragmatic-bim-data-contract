---
search:
  boost: 5.0
---

# Slot: kbob_id 


_KBOB ecobilans row id (for example 05.005)._



<div data-search-exclude markdown="1">



URI: [cost:kbob_id](https://schema.pragmaticbim.ch/cost/kbob_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CarbonComponent](CarbonComponent.md) | One layer or row contributing to a layer_recipe_sum carbon total. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CarbonComponent](CarbonComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:kbob_id |
| native | cost:kbob_id |




## LinkML Source

<details>
```yaml
name: kbob_id
description: KBOB ecobilans row id (for example 05.005).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- CarbonComponent
range: string

```
</details></div>