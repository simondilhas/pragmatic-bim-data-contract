---
search:
  boost: 5.0
---

# Slot: time_plans 


_Grouped time plans associated with this entity._



<div data-search-exclude markdown="1">



URI: [pbs:time_plans](https://schema.pragmaticbim.ch/time_plans)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
| [AbstractTimeRecord](AbstractTimeRecord.md) | Abstract base for reusable time/schedule record fields shared by atomic and g... |  no  |
| [TimeItem](TimeItem.md) | Planned work item with baseline and actual dates, optionally linked to model ... |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a time plan |  no  |
| [TimePlan](TimePlan.md) | Grouped schedule container defining component items, milestones, and dependen... |  no  |
| [TimeDependency](TimeDependency.md) | Precedence relationship between two time items within a plan, optionally with... |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimePlan](TimePlan.md) |
| Domain Of | [VirtualEntity](VirtualEntity.md) |

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
| self | pbs:time_plans |
| native | pbs:time_plans |




## LinkML Source

<details>
```yaml
name: time_plans
description: Grouped time plans associated with this entity.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- VirtualEntity
range: TimePlan
multivalued: true
inlined: false

```
</details></div>