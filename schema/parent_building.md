

# Slot: parent_building 


_Parent building context reference._





URI: [pbs:parent_building](https://example.org/pragmatic-bim-data-contract/parent_building)
Alias: parent_building

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, l... |  yes  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators) |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element |  no  |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level cont... |  yes  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structu... |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering) |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |
| [System](System.md) | Building service system grouping that serves spaces or zones |  yes  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis |  yes  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [PhysicalElement](PhysicalElement.md), [SpatialContext](SpatialContext.md), [Space](Space.md), [System](System.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_building |
| native | pbs:parent_building |




## LinkML Source

<details>
```yaml
name: parent_building
description: Parent building context reference.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: parent_building
domain_of:
- PhysicalElement
- SpatialContext
- Space
- System
range: Entity

```
</details>