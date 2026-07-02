---
search:
  boost: 5.0
---

# Slot: catalog_cost_records 


_Catalog cost and price records for this product (cost_record_role cost or price)._



<div data-search-exclude markdown="1">



URI: [pbs:catalog_cost_records](https://schema.pragmaticbim.ch/catalog_cost_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Product](Product.md) | Commercial product or service offering sold by a company. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CostRecord](CostRecord.md) |
| Domain Of | [Product](Product.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:catalog_cost_records |
| native | pbs:catalog_cost_records |




## LinkML Source

<details>
```yaml
name: catalog_cost_records
description: Catalog cost and price records for this product (cost_record_role cost
  or price).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Product
range: CostRecord
multivalued: true
inlined: false

```
</details></div>