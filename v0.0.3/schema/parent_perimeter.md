

# Slot: parent_perimeter 


_Parent perimeter context reference._





URI: [pbs:parent_perimeter](https://example.org/pragmatic-bim-data-contract/parent_perimeter)
Alias: parent_perimeter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, l... |  yes  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics |  no  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structu... |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PerimeterContext](PerimeterContext.md) |
| Domain Of | [SpatialContext](SpatialContext.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_perimeter |
| native | pbs:parent_perimeter |




## LinkML Source

<details>
```yaml
name: parent_perimeter
description: Parent perimeter context reference.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: parent_perimeter
domain_of:
- SpatialContext
range: PerimeterContext

```
</details>