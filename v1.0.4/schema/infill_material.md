---
search:
  boost: 5.0
---

# Slot: infill_material 


_Material of the opening infill within the frame (for example glazing for windows, door leaf or panel for doors). Applies to opening-type connectors (door, window)._



<div data-search-exclude markdown="1">



URI: [pbs:infill_material](https://schema.pragmaticbim.ch/infill_material)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Material](Material.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:infill_material |
| native | pbs:infill_material |




## LinkML Source

<details>
```yaml
name: infill_material
description: Material of the opening infill within the frame (for example glazing
  for windows, door leaf or panel for doors). Applies to opening-type connectors (door,
  window).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: Material
inlined: false

```
</details></div>