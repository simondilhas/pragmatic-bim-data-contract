

# Slot: cost_quantity_type 


_Quantity type used as basis for this cost calculation._





URI: [pbs:cost_quantity_type](https://example.org/pragmatic-bim-data-contract/cost_quantity_type)
Alias: cost_quantity_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuantityType](QuantityType.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:cost_quantity_type |
| native | pbs:cost_quantity_type |




## LinkML Source

<details>
```yaml
name: cost_quantity_type
description: Quantity type used as basis for this cost calculation.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: cost_quantity_type
domain_of:
- AbstractCostRecord
range: QuantityType

```
</details>