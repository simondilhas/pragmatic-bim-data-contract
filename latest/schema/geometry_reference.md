

# Slot: geometry_reference 


_URI/path/hash/pointer to geometry payload._





URI: [pbs:geometry_reference](https://example.org/pragmatic-bim-data-contract/geometry_reference)
Alias: geometry_reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeometryRepresentation](GeometryRepresentation.md) | Minimal geometry reference for an entity, separating representation from enco... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [GeometryRepresentation](GeometryRepresentation.md) |

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
| self | pbs:geometry_reference |
| native | pbs:geometry_reference |




## LinkML Source

<details>
```yaml
name: geometry_reference
description: URI/path/hash/pointer to geometry payload.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: geometry_reference
domain_of:
- GeometryRepresentation
range: string
required: true

```
</details>