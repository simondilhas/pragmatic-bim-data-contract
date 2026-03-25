

# Slot: geometry_format 


_Optional serialization/encoding format (for example ifc, gltf, wkt, geojson), independent of representation kind._





URI: [pbs:geometry_format](https://example.org/pragmatic-bim-data-contract/geometry_format)
Alias: geometry_format

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:geometry_format |
| native | pbs:geometry_format |




## LinkML Source

<details>
```yaml
name: geometry_format
description: Optional serialization/encoding format (for example ifc, gltf, wkt, geojson),
  independent of representation kind.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: geometry_format
domain_of:
- GeometryRepresentation
range: string

```
</details>