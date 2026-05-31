---
search:
  boost: 5.0
---

# Slot: triggered_task 


_Id of a Task record that this change triggered or should trigger._



<div data-search-exclude markdown="1">



URI: [pbs:triggered_task](https://schema.pragmaticbim.ch/triggered_task)
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
| self | pbs:triggered_task |
| native | pbs:triggered_task |




## LinkML Source

<details>
```yaml
name: triggered_task
description: Id of a Task record that this change triggered or should trigger.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: string

```
</details></div>