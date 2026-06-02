---
search:
  boost: 10.0
---

# Class: CostRequirement 


_Cost or budget requirement (unit-cost cap, total budget limit, etc.)._



<div data-search-exclude markdown="1">



URI: [pbs:CostRequirement](https://schema.pragmaticbim.ch/CostRequirement)





```mermaid
 classDiagram
    class CostRequirement
    click CostRequirement href "./CostRequirement.html"
      Requirement <|-- CostRequirement
        click Requirement href "./Requirement.html"
      CostRequirement : applies_to_entities
        CostRequirement --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      CostRequirement : classifications
        CostRequirement --> "*" Classification : classifications
        click Classification href "./Classification.html"
      CostRequirement : content_kind
      CostRequirement : cost_category
      CostRequirement : cost_quantity_type
        CostRequirement --> "0..1" QuantityType : cost_quantity_type
        click QuantityType href "./QuantityType.html"
      CostRequirement : created_at
      CostRequirement : currency
      CostRequirement : description
      CostRequirement : geometry_representations
        CostRequirement --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      CostRequirement : id
      CostRequirement : ifc_global_id
      CostRequirement : localized_descriptions
        CostRequirement --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      CostRequirement : localized_names
        CostRequirement --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      CostRequirement : meaning_uri
      CostRequirement : metadata
        CostRequirement --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      CostRequirement : modified_at
      CostRequirement : name
      CostRequirement : performance_properties
        CostRequirement --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      CostRequirement : quantity_values
        CostRequirement --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      CostRequirement : revision
      CostRequirement : source_artifact
        CostRequirement --> "0..1" Artifact : source_artifact
        click Artifact href "./Artifact.html"
      CostRequirement : status
        CostRequirement --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      CostRequirement : target_operator
        CostRequirement --> "0..1" RequirementTargetOperator : target_operator
        click RequirementTargetOperator href "./RequirementTargetOperator.html"
      CostRequirement : target_value_number
```





## Inheritance
* [Entity](Entity.md)
    * [Requirement](Requirement.md)
        * **CostRequirement**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:CostRequirement](https://schema.pragmaticbim.ch/CostRequirement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cost_category](cost_category.md) | 0..1 <br/> [String](String.md) | Cost category label kept intentionally open pending classification-backed modeling. | direct |
| [target_operator](target_operator.md) | 0..1 <br/> [RequirementTargetOperator](RequirementTargetOperator.md) | Comparison operator for the requirement target. | direct |
| [target_value_number](target_value_number.md) | 0..1 <br/> [Double](Double.md) | Numeric target value when applicable. | direct |
| [currency](currency.md) | 1 <br/> [String](String.md) | ISO 4217 currency code (for example EUR, USD). | direct |
| [cost_quantity_type](cost_quantity_type.md) | 0..1 <br/> [QuantityType](QuantityType.md) | Quantity type used as basis for this cost calculation. | direct |
| [source_artifact](source_artifact.md) | 0..1 <br/> [Artifact](Artifact.md) | Optional source artifact backing this requirement. | [Requirement](Requirement.md) |
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
| self | pbs:CostRequirement |
| native | pbs:CostRequirement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CostRequirement
description: Cost or budget requirement (unit-cost cap, total budget limit, etc.).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
slots:
- cost_category
- target_operator
- target_value_number
- currency
- cost_quantity_type
class_uri: pbs:CostRequirement

```
</details>

### Induced

<details>
```yaml
name: CostRequirement
description: Cost or budget requirement (unit-cost cap, total budget limit, etc.).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
attributes:
  cost_category:
    name: cost_category
    description: Cost category label kept intentionally open pending classification-backed
      modeling.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - CostRequirement
    - CostRecord
    range: string
  target_operator:
    name: target_operator
    description: Comparison operator for the requirement target.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - PerformanceRequirement
    - CostRequirement
    range: RequirementTargetOperator
  target_value_number:
    name: target_value_number
    description: Numeric target value when applicable.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - PerformanceRequirement
    - CostRequirement
    range: double
  currency:
    name: currency
    description: ISO 4217 currency code (for example EUR, USD).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - CostRequirement
    - CostRecord
    range: string
    required: true
    pattern: ^[A-Z]{3}$
  cost_quantity_type:
    name: cost_quantity_type
    description: Quantity type used as basis for this cost calculation.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - CostRequirement
    - CostRecord
    range: QuantityType
  source_artifact:
    name: source_artifact
    description: Optional source artifact backing this requirement.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Requirement
    range: Artifact
    inlined: false
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: CostRequirement
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
    owner: CostRequirement
    domain_of:
    - Entity
    range: string
    required: true
    equals_string: requirement
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
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
    owner: CostRequirement
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
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
    owner: CostRequirement
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: CostRequirement
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:CostRequirement

```
</details></div>