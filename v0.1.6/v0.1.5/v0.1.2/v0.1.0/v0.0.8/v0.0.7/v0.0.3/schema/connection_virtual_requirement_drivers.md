

# Slot: connection_virtual_requirement_drivers 


_Main requirement drivers for this virtual connection._





URI: [pbs:connection_virtual_requirement_drivers](https://example.org/pragmatic-bim-data-contract/connection_virtual_requirement_drivers)
Alias: connection_virtual_requirement_drivers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionRequirementDriver](ConnectionRequirementDriver.md) |
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
| self | pbs:connection_virtual_requirement_drivers |
| native | pbs:connection_virtual_requirement_drivers |




## LinkML Source

<details>
```yaml
name: connection_virtual_requirement_drivers
description: Main requirement drivers for this virtual connection.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: connection_virtual_requirement_drivers
domain_of:
- ConnectionVirtual
range: ConnectionRequirementDriver
multivalued: true

```
</details>