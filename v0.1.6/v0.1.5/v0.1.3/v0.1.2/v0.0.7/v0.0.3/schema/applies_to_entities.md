

# Slot: applies_to_entities 


_Entities this cost item applies to._





URI: [pbs:applies_to_entities](https://example.org/pragmatic-bim-data-contract/applies_to_entities)
Alias: applies_to_entities

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
| Range | [Entity](Entity.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:applies_to_entities |
| native | pbs:applies_to_entities |




## LinkML Source

<details>
```yaml
name: applies_to_entities
description: Entities this cost item applies to.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: applies_to_entities
domain_of:
- AbstractCostRecord
range: Entity
multivalued: true

```
</details>