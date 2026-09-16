---
search:
  boost: 2.0
---


# Enum: CarbonMethodEnum 



<div data-search-exclude markdown="1">

URI: [cost:CarbonMethodEnum](https://schema.pragmaticbim.ch/cost/CarbonMethodEnum)

**Enum URI:** [cost:CarbonMethodEnum](https://schema.pragmaticbim.ch/cost/CarbonMethodEnum)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| direct | None |  | Title: direct<br>|
| density | None |  | Title: density<br>|
| area_yield | None |  | Title: area_yield<br>|
| piece_area | None |  | Title: piece_area<br>|
| layer_recipe_sum | None |  | Title: layer_recipe_sum<br>|
| unmapped | None |  | Title: unmapped<br>|
| unconverted | None |  | Title: unconverted<br>|




## Slots

| Name | Description |
| ---  | --- |
| [carbon_method](carbon_method.md) | Method used to normalize carbon to the price unit. |
| [method](method.md) | Carbon conversion method. |
| [method](method.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost






## LinkML Source

<details>
```yaml
name: CarbonMethodEnum
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
enum_uri: cost:CarbonMethodEnum
permissible_values:
  direct:
    text: direct
    title: direct
  density:
    text: density
    title: density
  area_yield:
    text: area_yield
    title: area_yield
  piece_area:
    text: piece_area
    title: piece_area
  layer_recipe_sum:
    text: layer_recipe_sum
    title: layer_recipe_sum
  unmapped:
    text: unmapped
    title: unmapped
  unconverted:
    text: unconverted
    title: unconverted

```
</details>

</div>