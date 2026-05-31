---
search:
  boost: 5.0
---

# Slot: from_state_ref 


_Content state pointer at the source revision._



<div data-search-exclude markdown="1">



URI: [pbs:from_state_ref](https://schema.pragmaticbim.ch/from_state_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateRef](StateRef.md) |
| Domain Of | [Change](Change.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:from_state_ref |
| native | pbs:from_state_ref |




## LinkML Source

<details>
```yaml
name: from_state_ref
description: Content state pointer at the source revision.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: StateRef
inlined: true

```
</details></div>