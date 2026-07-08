---
search:
  boost: 5.0
---

# Slot: deliverable_format 


_Required deliverable format or encoding (for example IFC4, PDF, COBie)._



<div data-search-exclude markdown="1">



URI: [pbs:deliverable_format](https://schema.pragmaticbim.ch/deliverable_format)
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
| self | pbs:deliverable_format |
| native | pbs:deliverable_format |




## LinkML Source

<details>
```yaml
name: deliverable_format
description: Required deliverable format or encoding (for example IFC4, PDF, COBie).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- DeliverableRequirement
range: string

```
</details></div>