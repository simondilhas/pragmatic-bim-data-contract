---
search:
  boost: 5.0
---

# Slot: source_artifact 


_Optional source artifact backing this requirement._



<div data-search-exclude markdown="1">



URI: [pbs:source_artifact](https://schema.pragmaticbim.ch/source_artifact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Requirement](Requirement.md) | Prescriptive requirement entity (content_kind requirement). Applies to model entities via applies_to_entities. Domain is discriminated by concrete subclass (PerformanceRequirement, SpatialRequirement, DeliverableRequirement, etc.), not a separate slot. |  no  |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  no  |
| [BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |  no  |
| [DeliverableRequirement](DeliverableRequirement.md) | Deliverable or documentation requirement (model LOD, O&M manual, export format, etc.). |  no  |
| [ScheduleRequirement](ScheduleRequirement.md) | Schedule obligation requirement (deadline, milestone, or start/finish window). |  no  |
| [CostRequirement](CostRequirement.md) | Cost or budget requirement (unit-cost cap, total budget limit, etc.). |  no  |
| [MaterialRequirement](MaterialRequirement.md) | Material or product specification requirement for matching against assigned materials. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Artifact](Artifact.md) |
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
| self | pbs:source_artifact |
| native | pbs:source_artifact |




## LinkML Source

<details>
```yaml
name: source_artifact
description: Optional source artifact backing this requirement.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Requirement
range: Artifact
inlined: false

```
</details></div>