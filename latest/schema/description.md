

# Slot: description 


_Default description text._





URI: [pbs:description](https://example.org/pragmatic-bim-data-contract/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, l... |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [VirtualEntity](VirtualEntity.md) | Abstract base class for non-physical, conceptual, or informational entities |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items |  no  |
| [Entity](Entity.md) | Common base class for all schema entities |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering) |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators) |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis |  no  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element |  no  |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level cont... |  no  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics |  no  |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements |  no  |
| [Company](Company.md) | Organization, company, or legal entity participating in the project or asset ... |  no  |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represent... |  no  |
| [Agent](Agent.md) | Abstract base class for people or organizations acting in workflow and commun... |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structu... |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:description |
| native | pbs:description |




## LinkML Source

<details>
```yaml
name: description
description: Default description text.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: description
domain_of:
- Entity
range: string

```
</details>