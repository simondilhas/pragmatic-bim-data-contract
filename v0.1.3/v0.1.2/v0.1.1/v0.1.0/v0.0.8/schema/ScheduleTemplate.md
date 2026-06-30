---
search:
  boost: 10.0
---

# Class: ScheduleTemplate 


_Reusable schedule container defining items, milestones, and dependencies for a scoped plan._



<div data-search-exclude markdown="1">



URI: [pbs:ScheduleTemplate](https://schema.pragmaticbim.ch/ScheduleTemplate)





```mermaid
 classDiagram
    class ScheduleTemplate
    click ScheduleTemplate href "../ScheduleTemplate/"
      Entity <|-- ScheduleTemplate
        click Entity href "../Entity/"
      
      ScheduleTemplate : classifications
        
          
    
        
        
        ScheduleTemplate --> "*" Classification : classifications
        click Classification href "../Classification/"
    

        
      ScheduleTemplate : created_at
        
      ScheduleTemplate : decisions
        
          
    
        
        
        ScheduleTemplate --> "*" Decision : decisions
        click Decision href "../Decision/"
    

        
      ScheduleTemplate : description
        
      ScheduleTemplate : documents
        
          
    
        
        
        ScheduleTemplate --> "*" Document : documents
        click Document href "../Document/"
    

        
      ScheduleTemplate : geometry_representations
        
          
    
        
        
        ScheduleTemplate --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "../GeometryRepresentation/"
    

        
      ScheduleTemplate : id
        
      ScheduleTemplate : ifc_global_id
        
      ScheduleTemplate : localized_descriptions
        
          
    
        
        
        ScheduleTemplate --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "../LocalizedText/"
    

        
      ScheduleTemplate : localized_names
        
          
    
        
        
        ScheduleTemplate --> "*" LocalizedText : localized_names
        click LocalizedText href "../LocalizedText/"
    

        
      ScheduleTemplate : meaning_uri
        
      ScheduleTemplate : messages
        
          
    
        
        
        ScheduleTemplate --> "*" Message : messages
        click Message href "../Message/"
    

        
      ScheduleTemplate : metadata
        
          
    
        
        
        ScheduleTemplate --> "*" MetadataEntry : metadata
        click MetadataEntry href "../MetadataEntry/"
    

        
      ScheduleTemplate : modified_at
        
      ScheduleTemplate : name
        
      ScheduleTemplate : performance_properties
        
          
    
        
        
        ScheduleTemplate --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "../PerformanceProperty/"
    

        
      ScheduleTemplate : quantity_values
        
          
    
        
        
        ScheduleTemplate --> "*" QuantityValue : quantity_values
        click QuantityValue href "../QuantityValue/"
    

        
      ScheduleTemplate : revision
        
      ScheduleTemplate : schedule_dependencies
        
          
    
        
        
        ScheduleTemplate --> "*" ScheduleDependency : schedule_dependencies
        click ScheduleDependency href "../ScheduleDependency/"
    

        
      ScheduleTemplate : schedule_items
        
          
    
        
        
        ScheduleTemplate --> "*" ScheduleItem : schedule_items
        click ScheduleItem href "../ScheduleItem/"
    

        
      ScheduleTemplate : scheduled_entities
        
          
    
        
        
        ScheduleTemplate --> "*" Entity : scheduled_entities
        click Entity href "../Entity/"
    

        
      ScheduleTemplate : status
        
          
    
        
        
        ScheduleTemplate --> "0..1" StatusType : status
        click StatusType href "../StatusType/"
    

        
      ScheduleTemplate : tasks
        
          
    
        
        
        ScheduleTemplate --> "*" Task : tasks
        click Task href "../Task/"
    

        
      
```





## Inheritance
* [Entity](Entity.md)
    * **ScheduleTemplate**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:ScheduleTemplate](https://schema.pragmaticbim.ch/ScheduleTemplate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [scheduled_entities](scheduled_entities.md) | * <br/> [Entity](Entity.md) | Model entities that this schedule template or schedule item applies to | direct |
| [schedule_items](schedule_items.md) | * <br/> [ScheduleItem](ScheduleItem.md) | Schedule items contained in this template; milestone instances may also appea... | direct |
| [schedule_dependencies](schedule_dependencies.md) | * <br/> [ScheduleDependency](ScheduleDependency.md) | Dependency relationships used within this schedule template | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier | [Entity](Entity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name | [Entity](Entity.md) |
| [localized_names](localized_names.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of name | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text | [Entity](Entity.md) |
| [meaning_uri](meaning_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional semantic URI for linking the entity instance to an external ontology... | [Entity](Entity.md) |
| [localized_descriptions](localized_descriptions.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of description | [Entity](Entity.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity | [Entity](Entity.md) |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes | [Entity](Entity.md) |
| [geometry_representations](geometry_representations.md) | * <br/> [GeometryRepresentation](GeometryRepresentation.md) | Geometry references associated with the entity | [Entity](Entity.md) |
| [quantity_values](quantity_values.md) | * <br/> [QuantityValue](QuantityValue.md) | Quantities associated with the entity | [Entity](Entity.md) |
| [documents](documents.md) | * <br/> [Document](Document.md) | Linked documents associated with this entity | [Entity](Entity.md) |
| [metadata](metadata.md) | * <br/> [MetadataEntry](MetadataEntry.md) | Generic metadata container for IFC attributes/properties and project-specific... | [Entity](Entity.md) |
| [performance_properties](performance_properties.md) | * <br/> [PerformanceProperty](PerformanceProperty.md) | Normalized, strongly typed domain properties (fire/acoustic/thermal/structura... | [Entity](Entity.md) |
| [decisions](decisions.md) | * <br/> [Decision](Decision.md) | Decision records associated with this entity | [Entity](Entity.md) |
| [tasks](tasks.md) | * <br/> [Task](Task.md) | Tasks associated with this entity | [Entity](Entity.md) |
| [messages](messages.md) | * <br/> [Message](Message.md) | Messages associated with this entity | [Entity](Entity.md) |
| [created_at](created_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Creation timestamp for this entity record | [Entity](Entity.md) |
| [modified_at](modified_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Last modification timestamp for this entity record | [Entity](Entity.md) |
| [revision](revision.md) | 0..1 <br/> [Integer](Integer.md) | Integer revision counter for change tracking | [Entity](Entity.md) |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ScheduleItem](ScheduleItem.md) | [schedule_template](schedule_template.md) | range | [ScheduleTemplate](ScheduleTemplate.md) |
| [Milestone](Milestone.md) | [schedule_template](schedule_template.md) | range | [ScheduleTemplate](ScheduleTemplate.md) |
| [ScheduleDependency](ScheduleDependency.md) | [schedule_template](schedule_template.md) | range | [ScheduleTemplate](ScheduleTemplate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:ScheduleTemplate |
| native | pbs:ScheduleTemplate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ScheduleTemplate
description: Reusable schedule container defining items, milestones, and dependencies
  for a scoped plan.
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
slots:
- scheduled_entities
- schedule_items
- schedule_dependencies
class_uri: pbs:ScheduleTemplate

```
</details>

### Induced

<details>
```yaml
name: ScheduleTemplate
description: Reusable schedule container defining items, milestones, and dependencies
  for a scoped plan.
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
attributes:
  scheduled_entities:
    name: scheduled_entities
    description: Model entities that this schedule template or schedule item applies
      to.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - ScheduleTemplate
    - ScheduleItem
    range: Entity
    multivalued: true
    inlined: false
  schedule_items:
    name: schedule_items
    description: Schedule items contained in this template; milestone instances may
      also appear through the ScheduleItem subtype.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - ScheduleTemplate
    range: ScheduleItem
    multivalued: true
    inlined: false
  schedule_dependencies:
    name: schedule_dependencies
    description: Dependency relationships used within this schedule template.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - ScheduleTemplate
    range: ScheduleDependency
    multivalued: true
    inlined: false
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: ScheduleTemplate
    domain_of:
    - Entity
    - Task
    - Document
    - Change
    - ChangeSet
    range: string
    required: true
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
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
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
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
    owner: ScheduleTemplate
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
    owner: ScheduleTemplate
    domain_of:
    - Entity
    - Document
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
    owner: ScheduleTemplate
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
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: QuantityValue
    multivalued: true
    inlined: true
  documents:
    name: documents
    description: Linked documents associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: Document
    multivalued: true
    inlined: true
  metadata:
    name: metadata
    description: Generic metadata container for IFC attributes/properties and project-specific
      extensions.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
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
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: PerformanceProperty
    multivalued: true
    inlined: true
  decisions:
    name: decisions
    description: Decision records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: Decision
    multivalued: true
    inlined: true
  tasks:
    name: tasks
    description: Tasks associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: Task
    multivalued: true
    inlined: true
  messages:
    name: messages
    description: Messages associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: Message
    multivalued: true
    inlined: true
  created_at:
    name: created_at
    description: Creation timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ScheduleTemplate
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:ScheduleTemplate

```
</details></div>