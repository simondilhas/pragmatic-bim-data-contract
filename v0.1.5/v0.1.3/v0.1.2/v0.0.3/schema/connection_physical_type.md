

# Slot: connection_physical_type 


_Classification of physical connector type (for example door, window, duct, pipe, cable)._





URI: [pbs:connection_physical_type](https://example.org/pragmatic-bim-data-contract/connection_physical_type)
Alias: connection_physical_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionPhysicalType](ConnectionPhysicalType.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

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
| self | pbs:connection_physical_type |
| native | pbs:connection_physical_type |




## LinkML Source

<details>
```yaml
name: connection_physical_type
description: Classification of physical connector type (for example door, window,
  duct, pipe, cable).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: connection_physical_type
domain_of:
- ConnectionPhysical
range: ConnectionPhysicalType
required: true

```
</details>