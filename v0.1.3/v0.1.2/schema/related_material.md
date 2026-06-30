---
search:
  boost: 5.0
---

# Slot: related_material 


_Optional Material entity template this requirement must match or satisfy._



<div data-search-exclude markdown="1">



URI: [pbs:related_material](https://schema.pragmaticbim.ch/related_material)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialRequirement](MaterialRequirement.md) | Material or product specification requirement for matching against assigned materials. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [MaterialRequirement](MaterialRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_material |
| native | pbs:related_material |




## LinkML Source

<details>
```yaml
name: related_material
description: Optional Material entity template this requirement must match or satisfy.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MaterialRequirement
range: Entity
inlined: false

```
</details></div>