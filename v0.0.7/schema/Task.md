---
search:
  boost: 10.0
---

# Class: Task 


_Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities._

__



<div data-search-exclude markdown="1">



URI: [pbs:Task](https://schema.pragmaticbim.ch/Task)





```mermaid
 classDiagram
    class Task
    click Task href "./Task.html"
      Entity <|-- Task
        click Entity href "./Entity.html"
      Task : applies_to_entities
        Task --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      Task : assignee
        Task --> "0..1" Agent : assignee
        click Agent href "./Agent.html"
      Task : classifications
        Task --> "*" Classification : classifications
        click Classification href "./Classification.html"
      Task : content_kind
      Task : created_at
      Task : description
      Task : due_at
      Task : geometry_representations
        Task --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      Task : id
      Task : ifc_global_id
      Task : localized_descriptions
        Task --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      Task : localized_names
        Task --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      Task : meaning_uri
      Task : metadata
        Task --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      Task : modified_at
      Task : name
      Task : performance_properties
        Task --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      Task : quantity_values
        Task --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      Task : related_decision
        Task --> "0..1" Decision : related_decision
        click Decision href "./Decision.html"
      Task : revision
      Task : status
        Task --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      Task : task_notes
      Task : task_status
      Task : task_type
```





## Inheritance
* [Entity](Entity.md)
    * **Task**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Task](https://schema.pragmaticbim.ch/Task) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [task_type](task_type.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Task type expressed as a URI/CURIE from a controlled vocabulary. | direct |
| [task_status](task_status.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Task status URI/CURIE aligned with action status vocabularies. | direct |
| [assignee](assignee.md) | 0..1 <br/> [Agent](Agent.md) | Responsible agent. | direct |
| [due_at](due_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Due timestamp for task completion. | direct |
| [related_decision](related_decision.md) | 0..1 <br/> [Decision](Decision.md) | Optional reference to a decision that informs or drives this task. | direct |
| [task_notes](task_notes.md) | 0..1 <br/> [String](String.md) | Additional notes or implementation details for the task. | direct |
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
| [Change](Change.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [PropertyChange](PropertyChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [GeometryChange](GeometryChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [RequirementChange](RequirementChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [MatchChange](MatchChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [AdditionChange](AdditionChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |
| [DeletionChange](DeletionChange.md) | [triggered_task](triggered_task.md) | range | [Task](Task.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Task |
| native | pbs:Task |
| exact | schema:Action, prov:Activity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Task
description: 'Task entity for implementation and follow-up workflows. Entity.status
  covers lifecycle; task_status uses action status vocabulary URIs. Links to related
  entities via applies_to_entities.

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- schema:Action
- prov:Activity
is_a: Entity
slots:
- task_type
- task_status
- assignee
- due_at
- related_decision
- task_notes
slot_usage:
  content_kind:
    name: content_kind
    equals_string: task
class_uri: pbs:Task

```
</details>

### Induced

<details>
```yaml
name: Task
description: 'Task entity for implementation and follow-up workflows. Entity.status
  covers lifecycle; task_status uses action status vocabulary URIs. Links to related
  entities via applies_to_entities.

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- schema:Action
- prov:Activity
is_a: Entity
slot_usage:
  content_kind:
    name: content_kind
    equals_string: task
attributes:
  task_type:
    name: task_type
    description: Task type expressed as a URI/CURIE from a controlled vocabulary.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: dcterms:type
    owner: Task
    domain_of:
    - Task
    range: uriorcurie
  task_status:
    name: task_status
    description: Task status URI/CURIE aligned with action status vocabularies.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: schema:actionStatus
    owner: Task
    domain_of:
    - Task
    range: uriorcurie
  assignee:
    name: assignee
    description: Responsible agent.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: schema:agent
    owner: Task
    domain_of:
    - Task
    range: Agent
    inlined: false
  due_at:
    name: due_at
    description: Due timestamp for task completion.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: schema:deadline
    owner: Task
    domain_of:
    - Task
    range: datetime
  related_decision:
    name: related_decision
    description: Optional reference to a decision that informs or drives this task.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: prov:used
    owner: Task
    domain_of:
    - Task
    range: Decision
    inlined: false
  task_notes:
    name: task_notes
    description: Additional notes or implementation details for the task.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: rdfs:comment
    owner: Task
    domain_of:
    - Task
    range: string
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: Task
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
    owner: Task
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: task
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
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
    owner: Task
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
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
    owner: Task
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
    owner: Task
    domain_of:
    - Entity
    - yamlDocument
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
    owner: Task
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
    owner: Task
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
    owner: Task
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
    owner: Task
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
    owner: Task
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
    owner: Task
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Task
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:Task

```
</details></div>