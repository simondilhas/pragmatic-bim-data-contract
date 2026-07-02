

# Slot: contained_entities 


_Generic containment for associated entities._





URI: [pbs:contained_entities](https://example.org/pragmatic-bim-data-contract/contained_entities)
Alias: contained_entities

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [Space](Space.md), [System](System.md) |

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
| self | pbs:contained_entities |
| native | pbs:contained_entities |




## LinkML Source

<details>
```yaml
name: contained_entities
description: Generic containment for associated entities.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: contained_entities
domain_of:
- Space
- System
range: Entity
multivalued: true

```
</details>