---
search:
  boost: 5.0
---

# Slot: product_uri 


_Derived SKOS concept IRI for the product notation._



<div data-search-exclude markdown="1">



URI: [cost:product_uri](https://schema.pragmaticbim.ch/cost/product_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | cost:product_uri |
| native | cost:product_uri |




## LinkML Source

<details>
```yaml
name: product_uri
description: Derived SKOS concept IRI for the product notation.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
range: uriorcurie

```
</details></div>