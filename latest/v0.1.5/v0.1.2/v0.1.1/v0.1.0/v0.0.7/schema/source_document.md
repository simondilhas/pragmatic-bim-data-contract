---
search:
  boost: 5.0
---

# Slot: source_document 


_Optional source document entity backing this requirement._



<div data-search-exclude markdown="1">



URI: [pbs:source_document](https://schema.pragmaticbim.ch/source_document)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Requirement](Requirement.md) | Prescriptive requirement entity (content_kind requirement). Applies to model entities via applies_to_entities. Domain is discriminated by concrete subclass (PerformanceRequirement, SpatialRequirement, etc.), not a separate slot. |  no  |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  no  |
| [BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [YamlDocument](YamlDocument.md) |
| Domain Of | [Requirement](Requirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:source_document |
| native | pbs:source_document |




## LinkML Source

<details>
```yaml
name: source_document
description: Optional source document entity backing this requirement.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Requirement
range: yamlDocument
inlined: false

```
</details></div>