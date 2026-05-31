---
search:
  boost: 5.0
---

# Slot: change_source 


_URI identifying the tool or pipeline that produced this change record._



<div data-search-exclude markdown="1">



URI: [pbs:change_source](https://schema.pragmaticbim.ch/change_source)
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
| self | pbs:change_source |
| native | pbs:change_source |




## LinkML Source

<details>
```yaml
name: change_source
description: URI identifying the tool or pipeline that produced this change record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: uriorcurie

```
</details></div>