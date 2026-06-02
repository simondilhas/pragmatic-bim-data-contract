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
| requirement | pbs:content_kind_requirement | Prescriptive requirement record. | Title: Requirement<br>|
| document | pbs:content_kind_document | Document entity referencing external storage. | Title: Document<br>|
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
  requirement:
    text: requirement
    description: Prescriptive requirement record.
    meaning: pbs:content_kind_requirement
    alt_descriptions:
      de:
        source: de
        description: Anforderung
    title: Requirement
  document:
    text: document
    description: Document entity referencing external storage.
    meaning: pbs:content_kind_document
    alt_descriptions:
      de:
        source: de
        description: Dokument
    title: Document
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