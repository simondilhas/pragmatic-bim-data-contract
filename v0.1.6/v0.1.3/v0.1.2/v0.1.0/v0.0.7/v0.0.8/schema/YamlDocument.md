---
search:
  boost: 10.0
---

# Class: YamlDocument 


_Document entity referencing external storage. Links to related entities via applies_to_entities._



<div data-search-exclude markdown="1">



URI: [pbs:YamlDocument](https://schema.pragmaticbim.ch/YamlDocument)





```mermaid
 classDiagram
    class YamlDocument
    click YamlDocument href "./YamlDocument.html"
      Entity <|-- YamlDocument
        click Entity href "./Entity.html"
      YamlDocument : applies_to_entities
        YamlDocument --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      YamlDocument : classifications
        YamlDocument --> "*" Classification : classifications
        click Classification href "./Classification.html"
      YamlDocument : content_kind
      YamlDocument : created_at
      YamlDocument : description
      YamlDocument : geometry_representations
        YamlDocument --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      YamlDocument : id
      YamlDocument : ifc_global_id
      YamlDocument : localized_descriptions
        YamlDocument --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      YamlDocument : localized_names
        YamlDocument --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      YamlDocument : meaning_uri
      YamlDocument : metadata
        YamlDocument --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      YamlDocument : modified_at
      YamlDocument : name
      YamlDocument : performance_properties
        YamlDocument --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      YamlDocument : quantity_values
        YamlDocument --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      YamlDocument : revision
      YamlDocument : status
        YamlDocument --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      YamlDocument : storage_link
```





## Inheritance
* [Entity](Entity.md)
    * **YamlDocument**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:YamlDocument](https://schema.pragmaticbim.ch/YamlDocument) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes. | direct |
| [storage_link](storage_link.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI/URL/path to the stored document location. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Entity](Entity.md) |
| [content_kind](content_kind.md) | 1 <br/> [String](String.md) | Entity type discriminator for adapter projection and querying. Must be a ContentKind value. | [Entity](Entity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | [Entity](Entity.md) |
| [localized_names](localized_names.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of name. | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | [Entity](Entity.md) |
| [meaning_uri](meaning_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional semantic URI for linking the entity instance to an external ontology concept. | [Entity](Entity.md) |
| [localized_descriptions](localized_descriptions.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of description. | [Entity](Entity.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | [Entity](Entity.md) |
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
| [Requirement](Requirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [PerformanceRequirement](PerformanceRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [SpatialRequirement](SpatialRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [RegulatoryRequirement](RegulatoryRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [BriefRequirement](BriefRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [DeliverableRequirement](DeliverableRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [ScheduleRequirement](ScheduleRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [CostRequirement](CostRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |
| [MaterialRequirement](MaterialRequirement.md) | [source_document](source_document.md) | range | [YamlDocument](YamlDocument.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:YamlDocument |
| native | pbs:YamlDocument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: yamlDocument
description: Document entity referencing external storage. Links to related entities
  via applies_to_entities.
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
slots:
- classifications
- storage_link
slot_usage:
  content_kind:
    name: content_kind
    equals_string: document
  id:
    name: id
    required: true
class_uri: pbs:YamlDocument

```
</details>

### Induced

<details>
```yaml
name: yamlDocument
description: Document entity referencing external storage. Links to related entities
  via applies_to_entities.
from_schema: https://schema.pragmaticbim.ch
is_a: Entity
slot_usage:
  content_kind:
    name: content_kind
    equals_string: document
  id:
    name: id
    required: true
attributes:
  classifications:
    name: classifications
    description: Classification entries from IFC and other schemes.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    - yamlDocument
    range: Classification
    multivalued: true
    inlined: true
  storage_link:
    name: storage_link
    description: URI/URL/path to the stored document location.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - yamlDocument
    range: uriorcurie
    required: true
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: yamlDocument
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
    owner: yamlDocument
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: document
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
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
    owner: yamlDocument
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
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
    owner: yamlDocument
    domain_of:
    - Entity
    - Change
    range: string
    pattern: ^[0-3][0-9A-Za-z_$]{21}$
  geometry_representations:
    name: geometry_representations
    description: 'Geometry references associated with the entity. A single element
      may link to multiple geometry representations to serve different intents (authoring,
      coordination, analysis, visualization) without duplicating the element itself.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
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
    owner: yamlDocument
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
    owner: yamlDocument
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
    owner: yamlDocument
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
    owner: yamlDocument
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
    owner: yamlDocument
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: yamlDocument
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:YamlDocument

```
</details></div>