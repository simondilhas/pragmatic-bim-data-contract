---
search:
  boost: 5.0
---

# Slot: product 


_Abstract product SKOS notation (for example WICP-WOOD). Foreign key into classification vocabularies._



<div data-search-exclude markdown="1">



URI: [cost:product](https://schema.pragmaticbim.ch/cost/product)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | cost:product |
| native | cost:product |




## LinkML Source

<details>
```yaml
name: product
description: Abstract product SKOS notation (for example WICP-WOOD). Foreign key into
  classification vocabularies.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: string

```
</details></div>