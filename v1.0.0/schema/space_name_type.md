---
search:
  boost: 5.0
---

# Slot: space_name_type 


_Normalized abstract room name type (for example office, kitchen, corridor). Project-specific labels remain on name. When set, adapters may derive a BuildingSpaceActivityClassification entry in classifications[] via the room-name-to-activity mapping bridge._



<div data-search-exclude markdown="1">



URI: [pbs:space_name_type](https://schema.pragmaticbim.ch/space_name_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpaceNameType](SpaceNameType.md) |
| Domain Of | [Space](Space.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:space_name_type |
| native | pbs:space_name_type |




## LinkML Source

<details>
```yaml
name: space_name_type
description: Normalized abstract room name type (for example office, kitchen, corridor).
  Project-specific labels remain on name. When set, adapters may derive a BuildingSpaceActivityClassification
  entry in classifications[] via the room-name-to-activity mapping bridge.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Space
range: SpaceNameType

```
</details></div>