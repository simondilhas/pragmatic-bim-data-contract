

# Slot: material_specification 


_Material grade, specification, or product description._





URI: [pbs:material_specification](https://example.org/pragmatic-bim-data-contract/material_specification)
Alias: material_specification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Material](Material.md) | Material definition that can be associated with one or more entities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Material](Material.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:material_specification |
| native | pbs:material_specification |




## LinkML Source

<details>
```yaml
name: material_specification
description: Material grade, specification, or product description.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: material_specification
domain_of:
- Material
range: string

```
</details>