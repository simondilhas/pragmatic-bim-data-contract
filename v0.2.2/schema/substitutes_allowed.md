---
search:
  boost: 5.0
---

# Slot: substitutes_allowed 


_Whether equivalent or substitute materials are permitted._



<div data-search-exclude markdown="1">



URI: [pbs:substitutes_allowed](https://schema.pragmaticbim.ch/substitutes_allowed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialRequirement](MaterialRequirement.md) | Material or product specification requirement for matching against assigned materials. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
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
| self | pbs:substitutes_allowed |
| native | pbs:substitutes_allowed |




## LinkML Source

<details>
```yaml
name: substitutes_allowed
description: Whether equivalent or substitute materials are permitted.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MaterialRequirement
range: boolean

```
</details></div>