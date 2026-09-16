---
search:
  boost: 10.0
---

# Class: Process 


_Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record._

__



<div data-search-exclude markdown="1">



URI: [pbs:Process](https://schema.pragmaticbim.ch/Process)





```mermaid
classDiagram
direction TB
class Process
click Process href "./Process.html" _blank
Entity <|-- Process
click Entity href "./Entity.html" _blank
click Entity href "./Entity.html" _blank
click Classification href "./Classification.html" _blank
click GeometryRepresentation href "./GeometryRepresentation.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click MetadataEntry href "./MetadataEntry.html" _blank
click Project href "./Project.html" _blank
click PerformanceProperty href "./PerformanceProperty.html" _blank
click Agent href "./Agent.html" _blank
click QuantityValue href "./QuantityValue.html" _blank
click StatusType href "./StatusType.html" _blank
```





## Inheritance
* [Entity](Entity.md)
    * **Process**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Process](https://schema.pragmaticbim.ch/Process) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [process_definition_uri](process_definition_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI identifying the BPMN process definition (for example engine definition key or BPMN artifact URI). | direct |
| [external_instance_uri](external_instance_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI of the corresponding process instance in an external workflow engine when applicable. | direct |
| [process_status](process_status.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Process instance status expressed as a URI/CURIE (for example active, suspended, completed, terminated). | direct |
| [started_at](started_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Timestamp when the process instance started. | direct |
| [completed_at](completed_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Timestamp when the process instance completed or terminated, when applicable. | direct |
| [process_participants](process_participants.md) | * <br/> [Agent](Agent.md) | Agents participating in this BPMN process instance (for example assignees mapped from lane roles). | direct |
| [parent_project](parent_project.md) | 0..1 <br/> [Project](Project.md) | Parent project reference. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Entity](Entity.md) |
| [content_kind](content_kind.md) | 1 <br/> [String](String.md) | Entity type discriminator for adapter projection and querying. Must be a ContentKind value. | [Entity](Entity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | [Entity](Entity.md) |
| [localized_names](localized_names.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of name. | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | [Entity](Entity.md) |
| [meaning_uri](meaning_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional semantic URI for linking the entity instance to an external ontology concept. | [Entity](Entity.md) |
| [localized_descriptions](localized_descriptions.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of description. | [Entity](Entity.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | [Entity](Entity.md) |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes. | [Entity](Entity.md) |
| [geometry_representations](geometry_representations.md) | * <br/> [GeometryRepresentation](GeometryRepresentation.md) | Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself. | [Entity](Entity.md) |
| [quantity_values](quantity_values.md) | * <br/> [QuantityValue](QuantityValue.md) | Quantities associated with the entity. | [Entity](Entity.md) |
| [metadata](metadata.md) | * <br/> [MetadataEntry](MetadataEntry.md) | Generic metadata container for IFC attributes/properties and project-specific extensions. | [Entity](Entity.md) |
| [performance_properties](performance_properties.md) | * <br/> [PerformanceProperty](PerformanceProperty.md) | Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values. | [Entity](Entity.md) |
| [applies_to_entities](applies_to_entities.md) | * <br/> [Entity](Entity.md) | Model entities this record applies to (requirements, cost items, schedule items, etc.). | [Entity](Entity.md) |
| [created_at](created_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Creation timestamp for this entity record. | [Entity](Entity.md) |
| [modified_at](modified_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Last modification timestamp for this entity record. | [Entity](Entity.md) |
| [revision](revision.md) | 0..1 <br/> [Integer](Integer.md) | Integer revision counter for change tracking. | [Entity](Entity.md) |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status. | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Task](Task.md) | [parent_process](parent_process.md) | range | [Process](Process.md) |
| [Change](Change.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [PropertyChange](PropertyChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [GeometryChange](GeometryChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [RequirementChange](RequirementChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [MatchChange](MatchChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [AdditionChange](AdditionChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |
| [DeletionChange](DeletionChange.md) | [triggered_process](triggered_process.md) | range | [Process](Process.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Process |
| native | pbs:Process |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Process
description: 'Running BPMN process instance in the project graph. Use process_definition_uri
  for the BPMN definition key or artifact. When orchestration state lives in an external
  engine, set external_instance_uri to that system of record.

  '
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
slots:
- process_definition_uri
- external_instance_uri
- process_status
- started_at
- completed_at
- process_participants
- parent_project
slot_usage:
  content_kind:
    name: content_kind
    equals_string: process
  process_definition_uri:
    name: process_definition_uri
    required: true
class_uri: pbs:Process

```
</details>

### Induced

<details>
```yaml
name: Process
description: 'Running BPMN process instance in the project graph. Use process_definition_uri
  for the BPMN definition key or artifact. When orchestration state lives in an external
  engine, set external_instance_uri to that system of record.

  '
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
slot_usage:
  content_kind:
    name: content_kind
    equals_string: process
  process_definition_uri:
    name: process_definition_uri
    required: true
attributes:
  process_definition_uri:
    name: process_definition_uri
    description: URI identifying the BPMN process definition (for example engine definition
      key or BPMN artifact URI).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Process
    range: uriorcurie
    required: true
  external_instance_uri:
    name: external_instance_uri
    description: URI of the corresponding process instance in an external workflow
      engine when applicable.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Process
    range: uriorcurie
  process_status:
    name: process_status
    description: Process instance status expressed as a URI/CURIE (for example active,
      suspended, completed, terminated).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: adms:status
    owner: Process
    domain_of:
    - Process
    range: uriorcurie
  started_at:
    name: started_at
    description: Timestamp when the process instance started.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: dcterms:created
    owner: Process
    domain_of:
    - Process
    range: datetime
  completed_at:
    name: completed_at
    description: Timestamp when the process instance completed or terminated, when
      applicable.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Process
    range: datetime
  process_participants:
    name: process_participants
    description: Agents participating in this BPMN process instance (for example assignees
      mapped from lane roles).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Process
    range: Agent
    multivalued: true
    inlined: false
  parent_project:
    name: parent_project
    description: Parent project reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Process
    - Deliverable
    - SpatialContext
    - System
    range: Project
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: Process
    domain_of:
    - Entity
    - Change
    range: string
    required: true
  content_kind:
    name: content_kind
    description: Entity type discriminator for adapter projection and querying. Must
      be a ContentKind value.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: process
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  description:
    name: description
    description: Default description text.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    - Change
    range: string
    pattern: ^[0-3][0-9A-Za-z_$]{21}$
  classifications:
    name: classifications
    description: Classification entries from IFC and other schemes.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    - Artifact
    range: Classification
    multivalued: true
    inlined: true
  geometry_representations:
    name: geometry_representations
    description: 'Geometry references associated with the entity. A single element
      may link to multiple geometry representations to serve different intents (authoring,
      coordination, analysis, visualization) without duplicating the element itself.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: GeometryRepresentation
    multivalued: true
    inlined: true
  quantity_values:
    name: quantity_values
    description: Quantities associated with the entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: QuantityValue
    multivalued: true
    inlined: true
  metadata:
    name: metadata
    description: Generic metadata container for IFC attributes/properties and project-specific
      extensions.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: MetadataEntry
    multivalued: true
    inlined: true
  performance_properties:
    name: performance_properties
    description: 'Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/
      security/material) extracted from raw IFC PropertySet values.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: PerformanceProperty
    multivalued: true
    inlined: true
  applies_to_entities:
    name: applies_to_entities
    description: Model entities this record applies to (requirements, cost items,
      schedule items, etc.).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    - TimeRecord
    - CostRecord
    range: Entity
    multivalued: true
    inlined: false
  created_at:
    name: created_at
    description: Creation timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Process
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:Process

```
</details></div>