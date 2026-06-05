---
search:
  boost: 10.0
---

# Class: System 


_Building service system grouping that serves spaces or zones._



<div data-search-exclude markdown="1">



URI: [pbs:System](https://schema.pragmaticbim.ch/System)





```mermaid
classDiagram
direction TB
class System
click System href "./System.html" _blank
VirtualEntity <|-- System
click VirtualEntity href "./VirtualEntity.html" _blank
click Entity href "./Entity.html" _blank
click Classification href "./Classification.html" _blank
click Entity href "./Entity.html" _blank
click CostRecord href "./CostRecord.html" _blank
click GeometryRepresentation href "./GeometryRepresentation.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click Material href "./Material.html" _blank
click MetadataEntry href "./MetadataEntry.html" _blank
click BuiltAssetContext href "./BuiltAssetContext.html" _blank
click Project href "./Project.html" _blank
click PerformanceProperty href "./PerformanceProperty.html" _blank
click QuantityValue href "./QuantityValue.html" _blank
click Space href "./Space.html" _blank
click ZoneContext href "./ZoneContext.html" _blank
click StatusType href "./StatusType.html" _blank
click SystemDiscipline href "./SystemDiscipline.html" _blank
click SystemType href "./SystemType.html" _blank
click TimeRecord href "./TimeRecord.html" _blank
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * **System**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:System](https://schema.pragmaticbim.ch/System) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [system_type](system_type.md) | 1 <br/> [SystemType](SystemType.md) | Classification of system role (unit, network, terminal). | direct |
| [system_discipline](system_discipline.md) | 1 <br/> [SystemDiscipline](SystemDiscipline.md) | Classification of system discipline (electrical, sanitary, ventilation, heating). | direct |
| [parent_project](parent_project.md) | 0..1 <br/> [Project](Project.md) | Parent project reference. | direct |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | direct |
| [serves_spaces](serves_spaces.md) | * <br/> [Space](Space.md) | Spaces served by this system. | direct |
| [serves_zones](serves_zones.md) | * <br/> [ZoneContext](ZoneContext.md) | Zone context nodes served by this system. | direct |
| [contained_entities](contained_entities.md) | * <br/> [Entity](Entity.md) | Generic containment for associated entities. | direct |
| [cost_records](cost_records.md) | * <br/> [CostRecord](CostRecord.md) | Cost records associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [time_records](time_records.md) | * <br/> [TimeRecord](TimeRecord.md) | Time records associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [materials](materials.md) | * <br/> [Material](Material.md) | Material definitions associated with this entity. | [VirtualEntity](VirtualEntity.md) |
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
| [Equipment](Equipment.md) | [parent_system](parent_system.md) | range | [System](System.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:System |
| native | pbs:System |
| exact | ifcowl:IfcSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: System
description: Building service system grouping that serves spaces or zones.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcSystem
is_a: VirtualEntity
slots:
- system_type
- system_discipline
- parent_project
- parent_building
- serves_spaces
- serves_zones
- contained_entities
slot_usage:
  parent_project:
    name: parent_project
    range: Project
  parent_building:
    name: parent_building
    range: BuiltAssetContext
class_uri: pbs:System

```
</details>

### Induced

<details>
```yaml
name: System
description: Building service system grouping that serves spaces or zones.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcSystem
is_a: VirtualEntity
slot_usage:
  parent_project:
    name: parent_project
    range: Project
  parent_building:
    name: parent_building
    range: BuiltAssetContext
attributes:
  system_type:
    name: system_type
    description: Classification of system role (unit, network, terminal).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - System
    range: SystemType
    required: true
  system_discipline:
    name: system_discipline
    description: Classification of system discipline (electrical, sanitary, ventilation,
      heating).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - System
    range: SystemDiscipline
    required: true
  parent_project:
    name: parent_project
    description: Parent project reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Deliverable
    - SpatialContext
    - System
    range: Project
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    - System
    range: BuiltAssetContext
  serves_spaces:
    name: serves_spaces
    description: Spaces served by this system.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - System
    range: Space
    multivalued: true
  serves_zones:
    name: serves_zones
    description: Zone context nodes served by this system.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - System
    range: ZoneContext
    multivalued: true
  contained_entities:
    name: contained_entities
    description: Generic containment for associated entities.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Space
    - System
    range: Entity
    multivalued: true
  cost_records:
    name: cost_records
    description: Cost records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - VirtualEntity
    range: CostRecord
    multivalued: true
    inlined: false
  time_records:
    name: time_records
    description: Time records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - VirtualEntity
    range: TimeRecord
    multivalued: true
    inlined: false
  materials:
    name: materials
    description: Material definitions associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - VirtualEntity
    range: Material
    multivalued: true
    inlined: false
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: System
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
    owner: System
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: virtual
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
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
    owner: System
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
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
    owner: System
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: System
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:System

```
</details></div>