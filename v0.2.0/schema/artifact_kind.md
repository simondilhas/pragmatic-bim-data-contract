---
search:
  boost: 5.0
---

# Slot: artifact_kind 


_Kind of external artifact (text document, model, or plan)._



<div data-search-exclude markdown="1">



URI: [pbs:artifact_kind](https://schema.pragmaticbim.ch/artifact_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Artifact](Artifact.md) | External project artifact (text document, model, or plan) at storage_link. Used for provenance (Requirement.source_artifact). Not a modeled building element. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ArtifactKind](ArtifactKind.md) |
| Domain Of | [Artifact](Artifact.md) |

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
| self | pbs:artifact_kind |
| native | pbs:artifact_kind |




## LinkML Source

<details>
```yaml
name: artifact_kind
description: Kind of external artifact (text document, model, or plan).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Artifact
range: ArtifactKind
required: true

```
</details></div>