

# Slot: connection_virtual_type 


_Classification of virtual connection semantics (for example structural_joint, adjacency, access)._





URI: [pbs:connection_virtual_type](https://example.org/pragmatic-bim-data-contract/connection_virtual_type)
Alias: connection_virtual_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionVirtualType](ConnectionVirtualType.md) |
| Domain Of | [ConnectionVirtual](ConnectionVirtual.md) |

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
| self | pbs:connection_virtual_type |
| native | pbs:connection_virtual_type |




## LinkML Source

<details>
```yaml
name: connection_virtual_type
description: Classification of virtual connection semantics (for example structural_joint,
  adjacency, access).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: connection_virtual_type
domain_of:
- ConnectionVirtual
range: ConnectionVirtualType
required: true

```
</details>