---
search:
  boost: 10.0
---

# Class: Artifact 


_External project artifact (text document, model, or plan) at storage_link. Used for provenance (Requirement.source_artifact). Not a modeled building element._

__



<div data-search-exclude markdown="1">



URI: [pbs:Artifact](https://schema.pragmaticbim.ch/Artifact)





```mermaid
 classDiagram
    class Artifact
    click Artifact href "./Artifact.html"
      Entity <|-- Artifact
        click Entity href "./Entity.html"
      Artifact : applies_to_entities
        Artifact --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      Artifact : artifact_kind
        Artifact --> "1" ArtifactKind : artifact_kind
        click ArtifactKind href "./ArtifactKind.html"
      Artifact : classifications
        Artifact --> "*" Classification : classifications
        click Classification href "./Classification.html"
      Artifact : content_kind
      Artifact : created_at
      Artifact : description
      Artifact : geometry_representations
        Artifact --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      Artifact : id
      Artifact : ifc_global_id
      Artifact : localized_descriptions
        Artifact --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      Artifact : localized_names
        Artifact --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      Artifact : meaning_uri
      Artifact : media_format
      Artifact : metadata
        Artifact --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      Artifact : modified_at
      Artifact : name
      Artifact : performance_properties
        Artifact --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      Artifact : quantity_values
        Artifact --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      Artifact : revision
      Artifact : status
        Artifact --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      Artifact : storage_link
```





## Inheritance
* [Entity](Entity.md)
    * **Artifact**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Artifact](https://schema.pragmaticbim.ch/Artifact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes. | direct |
| [storage_link](storage_link.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI/URL/path to the stored artifact location. | direct |
| [artifact_kind](artifact_kind.md) | 1 <br/> [ArtifactKind](ArtifactKind.md) | Kind of external artifact (text document, model, or plan). | direct |
| [media_format](media_format.md) | 0..1 <br/> [String](String.md) | Encoding or format label (for example IFC4, PDF, DWG). | direct |
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
| [Requirement](Requirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [PerformanceRequirement](PerformanceRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [SpatialRequirement](SpatialRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [RegulatoryRequirement](RegulatoryRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [BriefRequirement](BriefRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [DeliverableRequirement](DeliverableRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [ScheduleRequirement](ScheduleRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [CostRequirement](CostRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |
| [MaterialRequirement](MaterialRequirement.md) | [source_artifact](source_artifact.md) | range | [Artifact](Artifact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Artifact |
| native | pbs:Artifact |
| exact | schema:CreativeWork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Artifact
description: 'External project artifact (text document, model, or plan) at storage_link.
  Used for provenance (Requirement.source_artifact). Not a modeled building element.

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- schema:CreativeWork
is_a: Entity
slots:
- classifications
- storage_link
- artifact_kind
- media_format
slot_usage:
  content_kind:
    name: content_kind
    equals_string: artifact
  id:
    name: id
    required: true
  artifact_kind:
    name: artifact_kind
    required: true
class_uri: pbs:Artifact

```
</details>

### Induced

<details>
```yaml
name: Artifact
description: 'External project artifact (text document, model, or plan) at storage_link.
  Used for provenance (Requirement.source_artifact). Not a modeled building element.

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- schema:CreativeWork
is_a: Entity
slot_usage:
  content_kind:
    name: content_kind
    equals_string: artifact
  id:
    name: id
    required: true
  artifact_kind:
    name: artifact_kind
    required: true
attributes:
  classifications:
    name: classifications
    description: Classification entries from IFC and other schemes.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    - Artifact
    range: Classification
    multivalued: true
    inlined: true
  storage_link:
    name: storage_link
    description: URI/URL/path to the stored artifact location.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Artifact
    range: uriorcurie
    required: true
  artifact_kind:
    name: artifact_kind
    description: Kind of external artifact (text document, model, or plan).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Artifact
    range: ArtifactKind
    required: true
  media_format:
    name: media_format
    description: Encoding or format label (for example IFC4, PDF, DWG).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Artifact
    range: string
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: Artifact
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
    owner: Artifact
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: artifact
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
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
    owner: Artifact
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
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
    owner: Artifact
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Artifact
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:Artifact

```
</details></div>