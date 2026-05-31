---
search:
  boost: 5.0
---

# Slot: triggered_process 


_External workflow process URI (for example yourcompanyos process instance)._



<div data-search-exclude markdown="1">



URI: [pbs:triggered_process](https://schema.pragmaticbim.ch/triggered_process)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:triggered_process |
| native | pbs:triggered_process |




## LinkML Source

<details>
```yaml
name: triggered_process
description: External workflow process URI (for example yourcompanyos process instance).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: uriorcurie

```
</details></div>