---
search:
  boost: 5.0
---

# Slot: classifications 


_Classification entries from IFC and other schemes._



<div data-search-exclude markdown="1">



URI: [pbs:classifications](https://schema.pragmaticbim.ch/classifications)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Entity](Entity.md) | Common base class for all schema entities |  no  |
| [Document](Document.md) | Reference to an external document stored in a file system, DMS, object storag... |  no  |
| [Agent](Agent.md) | Abstract base class for people or organizations acting in workflow and commun... |  no  |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represent... |  no  |
| [Company](Company.md) | Organization, company, or legal entity participating in the project or asset ... |  no  |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and trac... |  no  |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level cont... |  no  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators) |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering) |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |
| [VirtualEntity](VirtualEntity.md) | Abstract base class for non-physical, conceptual, or informational entities |  no  |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, l... |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics |  no  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structu... |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics |  no  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis |  no  |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements |  no  |
| [ScheduleTemplate](ScheduleTemplate.md) | Reusable schedule container defining items, milestones, and dependencies for ... |  no  |
| [ScheduleItem](ScheduleItem.md) | Planned work item with baseline and actual dates, linked to a schedule templa... |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a schedule |  no  |
| [ScheduleDependency](ScheduleDependency.md) | Precedence relationship between two schedule items, optionally with lag |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Classification](Classification.md) |
| Domain Of | [Entity](Entity.md), [Document](Document.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:classifications |
| native | pbs:classifications |




## LinkML Source

<details>
```yaml
name: classifications
description: Classification entries from IFC and other schemes.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Entity
- Document
range: Classification
multivalued: true
inlined: true

```
</details></div>