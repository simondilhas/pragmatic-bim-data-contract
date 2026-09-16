---
search:
  boost: 5.0
---

# Slot: is_above_ground 


_Whether the space is above ground level. When unset, consumers may derive from parent_level elevation relative to project datum._



<div data-search-exclude markdown="1">



URI: [pbs:is_above_ground](https://schema.pragmaticbim.ch/is_above_ground)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
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
| self | pbs:is_above_ground |
| native | pbs:is_above_ground |




## LinkML Source

<details>
```yaml
name: is_above_ground
description: Whether the space is above ground level. When unset, consumers may derive
  from parent_level elevation relative to project datum.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Space
range: boolean

```
</details></div>