

# Slot: connects_physical_elements 


_Physical elements connected by this virtual connection (for example wall-wall, wall-slab)._





URI: [pbs:connects_physical_elements](https://example.org/pragmatic-bim-data-contract/connects_physical_elements)
Alias: connects_physical_elements

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [ConnectionVirtual](ConnectionVirtual.md) |

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
| self | pbs:connects_physical_elements |
| native | pbs:connects_physical_elements |




## LinkML Source

<details>
```yaml
name: connects_physical_elements
description: Physical elements connected by this virtual connection (for example wall-wall,
  wall-slab).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: connects_physical_elements
domain_of:
- ConnectionVirtual
range: PhysicalElement
multivalued: true

```
</details>