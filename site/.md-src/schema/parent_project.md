---
search:
  boost: 5.0
---

# Slot: parent_project 


_Parent project reference._



<div data-search-exclude markdown="1">



URI: [pbs:parent_project](https://schema.pragmaticbim.ch/parent_project)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Deliverable](Deliverable.md) | Outcome or handover item produced within a project. |  yes  |
| [SpatialContext](SpatialContext.md) | Context node used to represent perimeter, legal site, built asset, level, or zone. |  yes  |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  yes  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics. |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics. |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structures. |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics. |  no  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics. |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Project](Project.md) |
| Domain Of | [Deliverable](Deliverable.md), [SpatialContext](SpatialContext.md), [System](System.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_project |
| native | pbs:parent_project |




## LinkML Source

<details>
```yaml
name: parent_project
description: Parent project reference.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Deliverable
- SpatialContext
- System
range: Project

```
</details></div>