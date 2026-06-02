---
search:
  boost: 5.0
---

# Slot: material_specification 


_Material grade, specification, or product description._



<div data-search-exclude markdown="1">



URI: [pbs:material_specification](https://schema.pragmaticbim.ch/material_specification)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialRequirement](MaterialRequirement.md) | Material or product specification requirement for matching against assigned materials. |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MaterialRequirement](MaterialRequirement.md), [Material](Material.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:material_specification |
| native | pbs:material_specification |




## LinkML Source

<details>
```yaml
name: material_specification
description: Material grade, specification, or product description.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MaterialRequirement
- Material
range: string

```
</details></div>