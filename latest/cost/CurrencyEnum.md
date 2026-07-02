---
search:
  boost: 2.0
---


# Enum: CurrencyEnum 




_ISO 4217 currency for regional labor rates. Price-book material is always EUR._



<div data-search-exclude markdown="1">

URI: [cost:CurrencyEnum](https://schema.pragmaticbim.ch/cost/CurrencyEnum)

**Enum URI:** [cost:CurrencyEnum](https://schema.pragmaticbim.ch/cost/CurrencyEnum)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| EUR | None |  | Title: Euro<br>|
| CHF | None |  | Title: Swiss franc<br>|
| GBP | None |  | Title: Pound sterling<br>|
| USD | None |  | Title: US dollar<br>|




## Slots

| Name | Description |
| ---  | --- |
| [currency](currency.md) | Local currency for labor rates and installed-cost total. |
| [currency](currency.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost






## LinkML Source

<details>
```yaml
name: CurrencyEnum
description: ISO 4217 currency for regional labor rates. Price-book material is always
  EUR.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
enum_uri: cost:CurrencyEnum
permissible_values:
  EUR:
    text: EUR
    title: Euro
  CHF:
    text: CHF
    title: Swiss franc
  GBP:
    text: GBP
    title: Pound sterling
  USD:
    text: USD
    title: US dollar

```
</details>

</div>