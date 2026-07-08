

# Slot: parent_space 


_Parent space where the equipment is located._





URI: [pbs:parent_space](https://example.org/pragmatic-bim-data-contract/parent_space)
Alias: parent_space

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [Equipment](Equipment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [contained_entities](contained_entities.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_space |
| native | pbs:parent_space |




## LinkML Source

<details>
```yaml
name: parent_space
description: Parent space where the equipment is located.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: parent_space
domain_of:
- Equipment
inverse: contained_entities
range: Space

```
</details>