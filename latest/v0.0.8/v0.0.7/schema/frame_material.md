---
search:
  boost: 5.0
---

# Slot: frame_material 


_Material of the frame or casing surrounding the opening. Applies to opening-type connectors (door, window)._



<div data-search-exclude markdown="1">



URI: [pbs:frame_material](https://schema.pragmaticbim.ch/frame_material)
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
| self | pbs:frame_material |
| native | pbs:frame_material |




## LinkML Source

<details>
```yaml
name: frame_material
description: Material of the frame or casing surrounding the opening. Applies to opening-type
  connectors (door, window).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: Material
inlined: false

```
</details></div>