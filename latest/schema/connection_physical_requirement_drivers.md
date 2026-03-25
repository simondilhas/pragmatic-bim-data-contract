

# Slot: connection_physical_requirement_drivers 


_Performance requirement drivers for this physical connection element. Multiple values are allowed because one connection may need to satisfy several requirements._

__





URI: [pbs:connection_physical_requirement_drivers](https://example.org/pragmatic-bim-data-contract/connection_physical_requirement_drivers)
Alias: connection_physical_requirement_drivers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionRequirementDriver](ConnectionRequirementDriver.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

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
| self | pbs:connection_physical_requirement_drivers |
| native | pbs:connection_physical_requirement_drivers |




## LinkML Source

<details>
```yaml
name: connection_physical_requirement_drivers
description: 'Performance requirement drivers for this physical connection element.
  Multiple values are allowed because one connection may need to satisfy several requirements.

  '
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: connection_physical_requirement_drivers
domain_of:
- ConnectionPhysical
range: ConnectionRequirementDriver
multivalued: true

```
</details>