

# Slot: unit_cost 


_Unit cost for this cost item._





URI: [pbs:unit_cost](https://example.org/pragmatic-bim-data-contract/unit_cost)
Alias: unit_cost

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
| Required | Yes |
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
| self | pbs:unit_cost |
| native | pbs:unit_cost |




## LinkML Source

<details>
```yaml
name: unit_cost
description: Unit cost for this cost item.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: unit_cost
domain_of:
- AbstractCostRecord
range: double
required: true
minimum_value: 0

```
</details>