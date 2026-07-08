---
search:
  boost: 5.0
---

# Slot: elevation 


_Storey elevation relative to project datum (metres)._



<div data-search-exclude markdown="1">



URI: [pbs:elevation](https://schema.pragmaticbim.ch/elevation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [LevelContext](LevelContext.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:elevation |
| native | pbs:elevation |




## LinkML Source

<details>
```yaml
name: elevation
description: Storey elevation relative to project datum (metres).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- LevelContext
range: double

```
</details></div>