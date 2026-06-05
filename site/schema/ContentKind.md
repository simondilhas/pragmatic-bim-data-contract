---
search:
  boost: 2.0
---


# Enum: ContentKind 




_Entity type discriminator for adapter projection and querying — not a module router._



<div data-search-exclude markdown="1">

URI: [pbs:ContentKind](https://schema.pragmaticbim.ch/ContentKind)

**Enum URI:** [pbs:ContentKind](https://schema.pragmaticbim.ch/ContentKind)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| physical | pbs:content_kind_physical | Tangible BIM element (SeparatorWall, Equipment, etc.). | Title: Physical<br>|
| virtual | pbs:content_kind_virtual | Non-physical conceptual entity (Space, System, TimeRecord, CostRecord, etc.). | Title: Virtual<br>|
| context | pbs:content_kind_context | Spatial context node (Building, Level, Zone, etc.). | Title: Context<br>|
| project | pbs:content_kind_project | Business delivery scope anchoring spatial context and workflow entities. | Title: Project<br>|
| program | pbs:content_kind_program | Portfolio or capital program scope grouping related projects. | Title: Program<br>|
| product | pbs:content_kind_product | Commercial product or service offering sold by a company. | Title: Product<br>|
| deliverable | pbs:content_kind_deliverable | Outcome or handover item produced within a project. | Title: Deliverable<br>|
| requirement | pbs:content_kind_requirement | Prescriptive requirement record. | Title: Requirement<br>|
| artifact | pbs:content_kind_artifact | External project artifact (text document, model, or plan) at storage_link. | Title: Artifact<br>|
| contract | pbs:content_kind_contract | Commercial agreement entity linking parties, scope, and signed artifacts. | Title: Contract<br>|
| decision | pbs:content_kind_decision | Decision entity for workflow and governance traceability. | Title: Decision<br>|
| task | pbs:content_kind_task | Task or action entity for implementation workflows. | Title: Task<br>|
| agent | pbs:content_kind_agent | Person or organization acting in the project. | Title: Agent<br>|
| message | pbs:content_kind_message | Message or communication entity for coordination. | Title: Message<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ContentKind
description: Entity type discriminator for adapter projection and querying — not a
  module router.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ContentKind
permissible_values:
  physical:
    text: physical
    description: Tangible BIM element (SeparatorWall, Equipment, etc.).
    meaning: pbs:content_kind_physical
    alt_descriptions:
      de:
        source: de
        description: Physisch
    title: Physical
  virtual:
    text: virtual
    description: Non-physical conceptual entity (Space, System, TimeRecord, CostRecord,
      etc.).
    meaning: pbs:content_kind_virtual
    alt_descriptions:
      de:
        source: de
        description: Virtuell
    title: Virtual
  context:
    text: context
    description: Spatial context node (Building, Level, Zone, etc.).
    meaning: pbs:content_kind_context
    alt_descriptions:
      de:
        source: de
        description: Kontext
    title: Context
  project:
    text: project
    description: Business delivery scope anchoring spatial context and workflow entities.
    meaning: pbs:content_kind_project
    alt_descriptions:
      de:
        source: de
        description: Projekt
    title: Project
  program:
    text: program
    description: Portfolio or capital program scope grouping related projects.
    meaning: pbs:content_kind_program
    alt_descriptions:
      de:
        source: de
        description: Programm
    title: Program
  product:
    text: product
    description: Commercial product or service offering sold by a company.
    meaning: pbs:content_kind_product
    alt_descriptions:
      de:
        source: de
        description: Produkt
    title: Product
  deliverable:
    text: deliverable
    description: Outcome or handover item produced within a project.
    meaning: pbs:content_kind_deliverable
    alt_descriptions:
      de:
        source: de
        description: Lieferobjekt
    title: Deliverable
  requirement:
    text: requirement
    description: Prescriptive requirement record.
    meaning: pbs:content_kind_requirement
    alt_descriptions:
      de:
        source: de
        description: Anforderung
    title: Requirement
  artifact:
    text: artifact
    description: External project artifact (text document, model, or plan) at storage_link.
    meaning: pbs:content_kind_artifact
    alt_descriptions:
      de:
        source: de
        description: Artefakt
    title: Artifact
  contract:
    text: contract
    description: Commercial agreement entity linking parties, scope, and signed artifacts.
    meaning: pbs:content_kind_contract
    alt_descriptions:
      de:
        source: de
        description: Vertrag
    title: Contract
  decision:
    text: decision
    description: Decision entity for workflow and governance traceability.
    meaning: pbs:content_kind_decision
    alt_descriptions:
      de:
        source: de
        description: Entscheid
    title: Decision
  task:
    text: task
    description: Task or action entity for implementation workflows.
    meaning: pbs:content_kind_task
    alt_descriptions:
      de:
        source: de
        description: Aufgabe
    title: Task
  agent:
    text: agent
    description: Person or organization acting in the project.
    meaning: pbs:content_kind_agent
    alt_descriptions:
      de:
        source: de
        description: Akteur
    title: Agent
  message:
    text: message
    description: Message or communication entity for coordination.
    meaning: pbs:content_kind_message
    alt_descriptions:
      de:
        source: de
        description: Nachricht
    title: Message

```
</details>

</div>