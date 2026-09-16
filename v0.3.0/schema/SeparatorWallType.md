---
search:
  boost: 2.0
---


# Enum: SeparatorWallType 




_Classification of wall-based separator elements._



<div data-search-exclude markdown="1">

URI: [pbs:SeparatorWallType](https://schema.pragmaticbim.ch/SeparatorWallType)

**Enum URI:** [pbs:SeparatorWallType](https://schema.pragmaticbim.ch/SeparatorWallType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| unit_boundary | ifcowl:IfcWall | Wall separator that defines boundaries between occupancy units. | Title: Unit Boundary<br>|
| vertical_circulation_boundary | ifcowl:IfcWall | Wall separator that bounds or encloses vertical circulation areas. | Title: Vertical Circulation Boundary<br>|
| horizontal_circulation_boundary | ifcowl:IfcWall | Wall separator that bounds or structures horizontal circulation areas. | Title: Horizontal Circulation Boundary<br>|




## Slots

| Name | Description |
| ---  | --- |
| [separator_wall_type](separator_wall_type.md) | Classification of wall-based separator element. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SeparatorWallType
description: Classification of wall-based separator elements.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SeparatorWallType
permissible_values:
  unit_boundary:
    text: unit_boundary
    description: Wall separator that defines boundaries between occupancy units.
    meaning: ifcowl:IfcWall
    alt_descriptions:
      de:
        source: de
        description: Einheitstrennung
    title: Unit Boundary
  vertical_circulation_boundary:
    text: vertical_circulation_boundary
    description: Wall separator that bounds or encloses vertical circulation areas.
    meaning: ifcowl:IfcWall
    alt_descriptions:
      de:
        source: de
        description: Vertikale Erschliessungstrennung
    title: Vertical Circulation Boundary
  horizontal_circulation_boundary:
    text: horizontal_circulation_boundary
    description: Wall separator that bounds or structures horizontal circulation areas.
    meaning: ifcowl:IfcWall
    alt_descriptions:
      de:
        source: de
        description: Horizontale Erschliessungstrennung
    title: Horizontal Circulation Boundary

```
</details>

</div>