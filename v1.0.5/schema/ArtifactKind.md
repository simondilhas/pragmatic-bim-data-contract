---
search:
  boost: 2.0
---


# Enum: ArtifactKind 




_Kind of external project artifact referenced by storage_link._



<div data-search-exclude markdown="1">

URI: [pbs:ArtifactKind](https://schema.pragmaticbim.ch/ArtifactKind)

**Enum URI:** [pbs:ArtifactKind](https://schema.pragmaticbim.ch/ArtifactKind)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| text_document | pbs:artifact_kind_text_document | Text-based document (specification, contract, report, manual). | Title: Text document<br>|
| model | pbs:artifact_kind_model | BIM or coordination model file. | Title: Model<br>|
| plan | pbs:artifact_kind_plan | Drawing or plan sheet (floor plan, section, detail). | Title: Plan<br>|




## Slots

| Name | Description |
| ---  | --- |
| [artifact_kind](artifact_kind.md) | Kind of external artifact (text document, model, or plan). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ArtifactKind
description: Kind of external project artifact referenced by storage_link.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ArtifactKind
permissible_values:
  text_document:
    text: text_document
    description: Text-based document (specification, contract, report, manual).
    meaning: pbs:artifact_kind_text_document
    alt_descriptions:
      de:
        source: de
        description: Textdokument
    title: Text document
  model:
    text: model
    description: BIM or coordination model file.
    meaning: pbs:artifact_kind_model
    alt_descriptions:
      de:
        source: de
        description: Modell
    title: Model
  plan:
    text: plan
    description: Drawing or plan sheet (floor plan, section, detail).
    meaning: pbs:artifact_kind_plan
    alt_descriptions:
      de:
        source: de
        description: Plan
    title: Plan

```
</details>

</div>