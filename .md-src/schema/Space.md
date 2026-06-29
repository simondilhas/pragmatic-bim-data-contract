---
search:
  boost: 10.0
---

# Class: Space 


_Spatial container used for occupancy, circulation, service, or analysis._



<div data-search-exclude markdown="1">



URI: [pbs:Space](https://schema.pragmaticbim.ch/Space)





```mermaid
classDiagram
direction TB
class Space
click Space href "./Space.html" _blank
VirtualEntity <|-- Space
click VirtualEntity href "./VirtualEntity.html" _blank
click Entity href "./Entity.html" _blank
click PhysicalElement href "./PhysicalElement.html" _blank
click Classification href "./Classification.html" _blank
click Entity href "./Entity.html" _blank
click CostRecord href "./CostRecord.html" _blank
click GeometryRepresentation href "./GeometryRepresentation.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click Material href "./Material.html" _blank
click MetadataEntry href "./MetadataEntry.html" _blank
click BuiltAssetContext href "./BuiltAssetContext.html" _blank
click LevelContext href "./LevelContext.html" _blank
click ZoneContext href "./ZoneContext.html" _blank
click PerformanceProperty href "./PerformanceProperty.html" _blank
click QuantityValue href "./QuantityValue.html" _blank
click SpaceNameType href "./SpaceNameType.html" _blank
click SpaceType href "./SpaceType.html" _blank
click StatusType href "./StatusType.html" _blank
click TimeRecord href "./TimeRecord.html" _blank
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * **Space**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Space](https://schema.pragmaticbim.ch/Space) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [space_type](space_type.md) | 1 <br/> [SpaceType](SpaceType.md) | Classification of space (void, circulation, usable, service). | direct |
| [space_name_type](space_name_type.md) | 0..1 <br/> [SpaceNameType](SpaceNameType.md) | Normalized abstract room name type (for example office, kitchen, corridor). Project-specific labels remain on name. When set, adapters may derive a BuildingSpaceActivityClassification entry in classifications[] via the room-name-to-activity mapping bridge. | direct |
| [is_heated](is_heated.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the space is designed to receive heating. | direct |
| [is_cooled](is_cooled.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the space is designed to receive cooling (air conditioning). | direct |
| [is_above_ground](is_above_ground.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the space is above ground level. When unset, consumers may derive from parent_level elevation relative to project datum. | direct |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | direct |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | direct |
| [parent_zone](parent_zone.md) | 0..1 <br/> [ZoneContext](ZoneContext.md) | Parent zone context reference. | direct |
| [bounded_by](bounded_by.md) | * <br/> [PhysicalElement](PhysicalElement.md) | Physical elements that bound a space. | direct |
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
| [SeparatorWall](SeparatorWall.md) | [separates_spaces](separates_spaces.md) | range | [Space](Space.md) |
| [Boundary](Boundary.md) | [bounded_space](bounded_space.md) | range | [Space](Space.md) |
| [Equipment](Equipment.md) | [parent_space](parent_space.md) | range | [Space](Space.md) |
| [System](System.md) | [serves_spaces](serves_spaces.md) | range | [Space](Space.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [connects_spaces](connects_spaces.md) | range | [Space](Space.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Space |
| native | pbs:Space |
| exact | bot:Space, ifcowl:IfcSpace |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Space
description: Spatial container used for occupancy, circulation, service, or analysis.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Space
- ifcowl:IfcSpace
is_a: VirtualEntity
slots:
- space_type
- space_name_type
- is_heated
- is_cooled
- is_above_ground
- parent_building
- parent_level
- parent_zone
- bounded_by
- contained_entities
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
class_uri: pbs:Space

```
</details>

### Induced

<details>
```yaml
name: Space
description: Spatial container used for occupancy, circulation, service, or analysis.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Space
- ifcowl:IfcSpace
is_a: VirtualEntity
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
attributes:
  space_type:
    name: space_type
    description: Classification of space (void, circulation, usable, service).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: SpaceType
    required: true
  space_name_type:
    name: space_name_type
    description: Normalized abstract room name type (for example office, kitchen,
      corridor). Project-specific labels remain on name. When set, adapters may derive
      a BuildingSpaceActivityClassification entry in classifications[] via the room-name-to-activity
      mapping bridge.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: SpaceNameType
  is_heated:
    name: is_heated
    description: Whether the space is designed to receive heating.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: boolean
  is_cooled:
    name: is_cooled
    description: Whether the space is designed to receive cooling (air conditioning).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: boolean
  is_above_ground:
    name: is_above_ground
    description: Whether the space is above ground level. When unset, consumers may
      derive from parent_level elevation relative to project datum.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: boolean
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    - System
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    description: Parent level/storey context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  parent_zone:
    name: parent_zone
    description: Parent zone context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - SpatialContext
    - Space
    range: ZoneContext
  bounded_by:
    name: bounded_by
    description: Physical elements that bound a space.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    inverse: bounded_space
    range: PhysicalElement
    multivalued: true
  contained_entities:
    name: contained_entities
    description: Generic containment for associated entities.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
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
    owner: Space
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:Space

```
</details></div>