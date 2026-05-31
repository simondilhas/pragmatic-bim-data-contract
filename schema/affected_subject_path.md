---
search:
  boost: 5.0
---

# Slot: affected_subject_path 


_Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1)._

__



<div data-search-exclude markdown="1">



URI: [pbs:affected_subject_path](https://schema.pragmaticbim.ch/affected_subject_path)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:affected_subject_path |
| native | pbs:affected_subject_path |




## LinkML Source

<details>
```yaml
name: affected_subject_path
description: 'Optional JSON-pointer-style path for nested targets (for example documents[2],
  localized_descriptions[de], section.4.2.paragraph_1).

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: string

```
</details></div>