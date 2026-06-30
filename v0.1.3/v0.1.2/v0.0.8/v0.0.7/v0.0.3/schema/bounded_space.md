

# Slot: bounded_space 


_Space bounded by this boundary element._





URI: [pbs:bounded_space](https://example.org/pragmatic-bim-data-contract/bounded_space)
Alias: bounded_space

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [Boundary](Boundary.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [bounded_by](bounded_by.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:bounded_space |
| native | pbs:bounded_space |




## LinkML Source

<details>
```yaml
name: bounded_space
description: Space bounded by this boundary element.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: bounded_space
domain_of:
- Boundary
inverse: bounded_by
range: Space

```
</details>