---
search:
  boost: 10.0
---

# Class: SeparatorSlab 


_Slab-based separating element (for example floor/roof/base slab separators)._



<div data-search-exclude markdown="1">



URI: [pbs:SeparatorSlab](https://schema.pragmaticbim.ch/SeparatorSlab)





```mermaid
classDiagram
direction TB
class SeparatorSlab
click SeparatorSlab href "./SeparatorSlab.html" _blank
Separator <|-- SeparatorSlab
click Separator href "./Separator.html" _blank
click Entity href "./Entity.html" _blank
click Classification href "./Classification.html" _blank
click GeometryRepresentation href "./GeometryRepresentation.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click LocalizedText href "./LocalizedText.html" _blank
click MetadataEntry href "./MetadataEntry.html" _blank
click BuiltAssetContext href "./BuiltAssetContext.html" _blank
click LevelContext href "./LevelContext.html" _blank
click PerformanceProperty href "./PerformanceProperty.html" _blank
click QuantityValue href "./QuantityValue.html" _blank
click LevelContext href "./LevelContext.html" _blank
click SeparatorRequirementDriver href "./SeparatorRequirementDriver.html" _blank
click SeparatorSlabType href "./SeparatorSlabType.html" _blank
click StatusType href "./StatusType.html" _blank
```





## Inheritance
* [Entity](Entity.md)
    * [PhysicalElement](PhysicalElement.md)
        * [Separator](Separator.md)
            * **SeparatorSlab**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:SeparatorSlab](https://schema.pragmaticbim.ch/SeparatorSlab) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [separator_slab_type](separator_slab_type.md) | 1 <br/> [SeparatorSlabType](SeparatorSlabType.md) | Classification of slab-based separator element (for example floor/roof/base slab). | direct |
| [separates_levels](separates_levels.md) | * <br/> [LevelContext](LevelContext.md) | Level context nodes separated by this slab separator. | direct |
| [separator_requirement_drivers](separator_requirement_drivers.md) | * <br/> [SeparatorRequirementDriver](SeparatorRequirementDriver.md) | Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements. | [Separator](Separator.md) |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | [PhysicalElement](PhysicalElement.md) |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | [PhysicalElement](PhysicalElement.md) |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:SeparatorSlab |
| native | pbs:SeparatorSlab |
| exact | ifcowl:IfcSlab |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeparatorSlab
description: Slab-based separating element (for example floor/roof/base slab separators).
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcSlab
is_a: Separator
slots:
- separator_slab_type
- separates_levels
class_uri: pbs:SeparatorSlab

```
</details>

### Induced

<details>
```yaml
name: SeparatorSlab
description: Slab-based separating element (for example floor/roof/base slab separators).
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcSlab
is_a: Separator
attributes:
  separator_slab_type:
    name: separator_slab_type
    description: Classification of slab-based separator element (for example floor/roof/base
      slab).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - SeparatorSlab
    range: SeparatorSlabType
    required: true
  separates_levels:
    name: separates_levels
    description: Level context nodes separated by this slab separator.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - SeparatorSlab
    range: LevelContext
    multivalued: true
  separator_requirement_drivers:
    name: separator_requirement_drivers
    description: 'Performance requirement drivers for this separator. Multiple values
      are allowed because one separator may need to satisfy several requirements.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Separator
    range: SeparatorRequirementDriver
    multivalued: true
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
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
    owner: SeparatorSlab
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: SeparatorSlab
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
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: physical
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
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
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
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
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorSlab
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:SeparatorSlab

```
</details></div>