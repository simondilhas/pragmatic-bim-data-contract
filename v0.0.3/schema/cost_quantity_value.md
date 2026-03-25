

# Slot: cost_quantity_value 


_Quantity magnitude used as basis for this cost calculation._





URI: [pbs:cost_quantity_value](https://example.org/pragmatic-bim-data-contract/cost_quantity_value)
Alias: cost_quantity_value

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
| Range | [Double](Double.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:cost_quantity_value |
| native | pbs:cost_quantity_value |




## LinkML Source

<details>
```yaml
name: cost_quantity_value
description: Quantity magnitude used as basis for this cost calculation.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: cost_quantity_value
domain_of:
- AbstractCostRecord
range: double
minimum_value: 0

```
</details>