---
search:
  boost: 10.0
---

# Class: SeparatorWall 


_Wall-based separating element._



<div data-search-exclude markdown="1">



URI: [pbs:SeparatorWall](https://schema.pragmaticbim.ch/SeparatorWall)





```mermaid
classDiagram
direction TB
class SeparatorWall
click SeparatorWall href "./SeparatorWall.html" _blank
Separator <|-- SeparatorWall
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
click Space href "./Space.html" _blank
click SeparatorRequirementDriver href "./SeparatorRequirementDriver.html" _blank
click SeparatorWallType href "./SeparatorWallType.html" _blank
click StatusType href "./StatusType.html" _blank
```





## Inheritance
* [Entity](Entity.md)
    * [PhysicalElement](PhysicalElement.md)
        * [Separator](Separator.md)
            * **SeparatorWall**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:SeparatorWall](https://schema.pragmaticbim.ch/SeparatorWall) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [separator_wall_type](separator_wall_type.md) | 1 <br/> [SeparatorWallType](SeparatorWallType.md) | Classification of wall-based separator element. | direct |
| [separates_spaces](separates_spaces.md) | * <br/> [Space](Space.md) | Spaces separated by this separator element. | direct |
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
| self | pbs:SeparatorWall |
| native | pbs:SeparatorWall |
| exact | ifcowl:IfcWall |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeparatorWall
description: Wall-based separating element.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcWall
is_a: Separator
slots:
- separator_wall_type
- separates_spaces
class_uri: pbs:SeparatorWall

```
</details>

### Induced

<details>
```yaml
name: SeparatorWall
description: Wall-based separating element.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcWall
is_a: Separator
attributes:
  separator_wall_type:
    name: separator_wall_type
    description: Classification of wall-based separator element.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - SeparatorWall
    range: SeparatorWallType
    required: true
  separates_spaces:
    name: separates_spaces
    description: Spaces separated by this separator element.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - SeparatorWall
    range: Space
    multivalued: true
  separator_requirement_drivers:
    name: separator_requirement_drivers
    description: 'Performance requirement drivers for this separator. Multiple values
      are allowed because one separator may need to satisfy several requirements.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - Separator
    range: SeparatorRequirementDriver
    multivalued: true
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SeparatorWall
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:SeparatorWall

```
</details></div>