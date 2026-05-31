---
search:
  boost: 5.0
---

# Slot: applies_to_entities 


_Entities this cost item applies to._



<div data-search-exclude markdown="1">



URI: [pbs:applies_to_entities](https://schema.pragmaticbim.ch/applies_to_entities)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
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


* from schema: https://schema.pragmaticbim.ch




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
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- AbstractCostRecord
range: Entity
multivalued: true

```
</details></div>