---
search:
  boost: 5.0
---

# Slot: change_kind 


_Severity or category of change detected between two revisions._



<div data-search-exclude markdown="1">



URI: [pbs:change_kind](https://schema.pragmaticbim.ch/change_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChangeKind](ChangeKind.md) |
| Domain Of | [Change](Change.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:change_kind |
| native | pbs:change_kind |




## LinkML Source

<details>
```yaml
name: change_kind
description: Severity or category of change detected between two revisions.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: ChangeKind
required: true

```
</details></div>