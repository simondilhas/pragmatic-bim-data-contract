# Enum: SeparatorWallType 




_Classification of wall-based separator elements._



URI: [pbs:SeparatorWallType](https://example.org/pragmatic-bim-data-contract/SeparatorWallType)

**Enum URI:** [pbs:SeparatorWallType](https://example.org/pragmatic-bim-data-contract/SeparatorWallType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| unit_boundary | ifcowl:IfcWall | Wall separator that defines boundaries between occupancy units |
| vertical_circulation_boundary | ifcowl:IfcWall | Wall separator that bounds or encloses vertical circulation areas |
| horizontal_circulation_boundary | ifcowl:IfcWall | Wall separator that bounds or structures horizontal circulation areas |




## Slots

| Name | Description |
| ---  | --- |
| [separator_wall_type](separator_wall_type.md) | Classification of wall-based separator element |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: SeparatorWallType
description: Classification of wall-based separator elements.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:SeparatorWallType
permissible_values:
  unit_boundary:
    text: unit_boundary
    description: Wall separator that defines boundaries between occupancy units.
    meaning: ifcowl:IfcWall
  vertical_circulation_boundary:
    text: vertical_circulation_boundary
    description: Wall separator that bounds or encloses vertical circulation areas.
    meaning: ifcowl:IfcWall
  horizontal_circulation_boundary:
    text: horizontal_circulation_boundary
    description: Wall separator that bounds or structures horizontal circulation areas.
    meaning: ifcowl:IfcWall

```
</details>