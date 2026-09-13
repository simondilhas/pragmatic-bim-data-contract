---
search:
  boost: 2.0
---


# Enum: PriceUnitEnum 




_Native trade unit for a baseline unit price._



<div data-search-exclude markdown="1">

URI: [cost:PriceUnitEnum](https://schema.pragmaticbim.ch/cost/PriceUnitEnum)

**Enum URI:** [cost:PriceUnitEnum](https://schema.pragmaticbim.ch/cost/PriceUnitEnum)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| m2 | None |  | Title: Square metre<br>|
| m3 | None |  | Title: Cubic metre<br>|
| pcs | None |  | Title: Piece<br>|




## Slots

| Name | Description |
| ---  | --- |
| [price_unit](price_unit.md) | Quantity unit the material cost refers to. |
| [unit](unit.md) | Unit for demolition quantities. |
| [price_unit](price_unit.md) |  |
| [unit](unit.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost






## LinkML Source

<details>
```yaml
name: PriceUnitEnum
description: Native trade unit for a baseline unit price.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
enum_uri: cost:PriceUnitEnum
permissible_values:
  m2:
    text: m2
    title: Square metre
  m3:
    text: m3
    title: Cubic metre
  pcs:
    text: pcs
    title: Piece

```
</details>

</div>