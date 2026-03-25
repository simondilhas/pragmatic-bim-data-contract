

# Slot: space_type 


_Classification of space (void, circulation, usable, service)._





URI: [pbs:space_type](https://example.org/pragmatic-bim-data-contract/space_type)
Alias: space_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpaceType](SpaceType.md) |
| Domain Of | [Space](Space.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:space_type |
| native | pbs:space_type |




## LinkML Source

<details>
```yaml
name: space_type
description: Classification of space (void, circulation, usable, service).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: space_type
domain_of:
- Space
range: SpaceType
required: true

```
</details>