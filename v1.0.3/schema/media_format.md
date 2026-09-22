---
search:
  boost: 5.0
---

# Slot: media_format 


_Encoding or format label (for example IFC4, PDF, DWG)._



<div data-search-exclude markdown="1">



URI: [pbs:media_format](https://schema.pragmaticbim.ch/media_format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Artifact](Artifact.md) | External project artifact (text document, model, or plan) at storage_link. Used for provenance (Requirement.source_artifact). Not a modeled building element. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Artifact](Artifact.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:media_format |
| native | pbs:media_format |




## LinkML Source

<details>
```yaml
name: media_format
description: Encoding or format label (for example IFC4, PDF, DWG).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Artifact
range: string

```
</details></div>