

# Slot: cost_category 


_Cost category label kept intentionally open pending classification-backed modeling._





URI: [pbs:cost_category](https://example.org/pragmatic-bim-data-contract/cost_category)
Alias: cost_category

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
| Range | [String](String.md) |
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
| self | pbs:cost_category |
| native | pbs:cost_category |




## LinkML Source

<details>
```yaml
name: cost_category
description: Cost category label kept intentionally open pending classification-backed
  modeling.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: cost_category
domain_of:
- AbstractCostRecord
range: string

```
</details>