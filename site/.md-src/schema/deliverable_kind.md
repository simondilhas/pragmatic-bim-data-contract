---
search:
  boost: 5.0
---

# Slot: deliverable_kind 


_Deliverable type label (for example coordination model, O&M manual, as-built record)._



<div data-search-exclude markdown="1">



URI: [pbs:deliverable_kind](https://schema.pragmaticbim.ch/deliverable_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeliverableRequirement](DeliverableRequirement.md) | Deliverable or documentation requirement (model LOD, O&M manual, export format, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DeliverableRequirement](DeliverableRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:deliverable_kind |
| native | pbs:deliverable_kind |




## LinkML Source

<details>
```yaml
name: deliverable_kind
description: Deliverable type label (for example coordination model, O&M manual, as-built
  record).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- DeliverableRequirement
range: string

```
</details></div>