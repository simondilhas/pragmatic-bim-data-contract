---
search:
  boost: 5.0
---

# Slot: priced_for_customer 


_Optional customer for a customer-specific catalog price when cost_record_role is price._



<div data-search-exclude markdown="1">



URI: [pbs:priced_for_customer](https://schema.pragmaticbim.ch/priced_for_customer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation, catalog pricing, and calculation. Use cost_record_role to distinguish catalog cost/price (on Product) from project estimate/actual lines. Populate component_cost_items to act as an assembly (aggregated unit price). |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:priced_for_customer |
| native | pbs:priced_for_customer |




## LinkML Source

<details>
```yaml
name: priced_for_customer
description: Optional customer for a customer-specific catalog price when cost_record_role
  is price.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: Company
inlined: false

```
</details></div>