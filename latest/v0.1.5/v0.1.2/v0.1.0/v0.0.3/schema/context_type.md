

# Slot: context_type 


_Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone)._





URI: [pbs:context_type](https://example.org/pragmatic-bim-data-contract/context_type)
Alias: context_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, l... |  no  |
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
| Range | [ContextType](ContextType.md) |
| Domain Of | [SpatialContext](SpatialContext.md) |

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
| self | pbs:context_type |
| native | pbs:context_type |




## LinkML Source

<details>
```yaml
name: context_type
description: Classification of context entity (project, perimeter, legal_site, building,
  civil_structure, level, zone).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: context_type
domain_of:
- SpatialContext
range: ContextType
required: true

```
</details>