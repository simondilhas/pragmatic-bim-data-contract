

# Slot: boundary_type 


_Classification of boundary element (e.g., covering)._





URI: [pbs:boundary_type](https://example.org/pragmatic-bim-data-contract/boundary_type)
Alias: boundary_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BoundaryType](BoundaryType.md) |
| Domain Of | [Boundary](Boundary.md) |

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
| self | pbs:boundary_type |
| native | pbs:boundary_type |




## LinkML Source

<details>
```yaml
name: boundary_type
description: Classification of boundary element (e.g., covering).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: boundary_type
domain_of:
- Boundary
range: BoundaryType
required: true

```
</details>