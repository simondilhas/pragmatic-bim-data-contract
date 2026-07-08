---
search:
  boost: 5.0
---

# Slot: connection_functional_types 


_Functional connection role(s) between spaces (for example access, visual, ventilation, heating). Multiple values allowed (for example glazed door as access plus visual)._



<div data-search-exclude markdown="1">



URI: [pbs:connection_functional_types](https://schema.pragmaticbim.ch/connection_functional_types)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionFunctionalType](ConnectionFunctionalType.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:connection_functional_types |
| native | pbs:connection_functional_types |




## LinkML Source

<details>
```yaml
name: connection_functional_types
description: Functional connection role(s) between spaces (for example access, visual,
  ventilation, heating). Multiple values allowed (for example glazed door as access
  plus visual).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: ConnectionFunctionalType
required: true
multivalued: true

```
</details></div>