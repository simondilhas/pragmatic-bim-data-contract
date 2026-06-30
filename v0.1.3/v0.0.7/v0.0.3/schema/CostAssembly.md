

# Class: CostAssembly 


_Aggregated unit price assembled from multiple cost items._





URI: [pbs:CostAssembly](https://example.org/pragmatic-bim-data-contract/CostAssembly)





```mermaid
 classDiagram
    class CostAssembly
    click CostAssembly href "../CostAssembly/"
      AbstractCostRecord <|-- CostAssembly
        click AbstractCostRecord href "../AbstractCostRecord/"
      
      CostAssembly : applies_to_entities
        
          
    
        
        
        CostAssembly --> "*" Entity : applies_to_entities
        click Entity href "../Entity/"
    

        
      CostAssembly : classifications
        
          
    
        
        
        CostAssembly --> "*" Classification : classifications
        click Classification href "../Classification/"
    

        
      CostAssembly : component_cost_items
        
          
    
        
        
        CostAssembly --> "*" CostItem : component_cost_items
        click CostItem href "../CostItem/"
    

        
      CostAssembly : cost_assemblies
        
          
    
        
        
        CostAssembly --> "*" CostAssembly : cost_assemblies
        click CostAssembly href "../CostAssembly/"
    

        
      CostAssembly : cost_category
        
      CostAssembly : cost_items
        
          
    
        
        
        CostAssembly --> "*" CostItem : cost_items
        click CostItem href "../CostItem/"
    

        
      CostAssembly : cost_quantity_type
        
          
    
        
        
        CostAssembly --> "0..1" QuantityType : cost_quantity_type
        click QuantityType href "../QuantityType/"
    

        
      CostAssembly : cost_quantity_unit
        
      CostAssembly : cost_quantity_value
        
      CostAssembly : created_at
        
      CostAssembly : currency
        
      CostAssembly : decisions
        
          
    
        
        
        CostAssembly --> "*" Decision : decisions
        click Decision href "../Decision/"
    

        
      CostAssembly : description
        
      CostAssembly : documents
        
          
    
        
        
        CostAssembly --> "*" Document : documents
        click Document href "../Document/"
    

        
      CostAssembly : geometry_representations
        
          
    
        
        
        CostAssembly --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "../GeometryRepresentation/"
    

        
      CostAssembly : id
        
      CostAssembly : ifc_global_id
        
      CostAssembly : localized_descriptions
        
          
    
        
        
        CostAssembly --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "../LocalizedText/"
    

        
      CostAssembly : localized_names
        
          
    
        
        
        CostAssembly --> "*" LocalizedText : localized_names
        click LocalizedText href "../LocalizedText/"
    

        
      CostAssembly : materials
        
          
    
        
        
        CostAssembly --> "*" Material : materials
        click Material href "../Material/"
    

        
      CostAssembly : meaning_uri
        
      CostAssembly : messages
        
          
    
        
        
        CostAssembly --> "*" Message : messages
        click Message href "../Message/"
    

        
      CostAssembly : metadata
        
          
    
        
        
        CostAssembly --> "*" MetadataEntry : metadata
        click MetadataEntry href "../MetadataEntry/"
    

        
      CostAssembly : modified_at
        
      CostAssembly : name
        
      CostAssembly : performance_properties
        
          
    
        
        
        CostAssembly --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "../PerformanceProperty/"
    

        
      CostAssembly : quantity_values
        
          
    
        
        
        CostAssembly --> "*" QuantityValue : quantity_values
        click QuantityValue href "../QuantityValue/"
    

        
      CostAssembly : revision
        
      CostAssembly : status
        
          
    
        
        
        CostAssembly --> "0..1" StatusType : status
        click StatusType href "../StatusType/"
    

        
      CostAssembly : tasks
        
          
    
        
        
        CostAssembly --> "*" Task : tasks
        click Task href "../Task/"
    

        
      CostAssembly : unit_cost
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * [AbstractCostRecord](AbstractCostRecord.md)
            * **CostAssembly**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:CostAssembly](https://example.org/pragmatic-bim-data-contract/CostAssembly) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [component_cost_items](component_cost_items.md) | * <br/> [CostItem](CostItem.md) | Atomic cost items that are aggregated into this cost assembly | direct |
| [cost_category](cost_category.md) | 0..1 <br/> [String](String.md) | Cost category label kept intentionally open pending classification-backed mod... | [AbstractCostRecord](AbstractCostRecord.md) |
| [unit_cost](unit_cost.md) | 1 <br/> [Double](Double.md) | Unit cost for this cost item | [AbstractCostRecord](AbstractCostRecord.md) |
| [currency](currency.md) | 1 <br/> [String](String.md) | ISO 4217 currency code (for example EUR, USD) | [AbstractCostRecord](AbstractCostRecord.md) |
| [cost_quantity_type](cost_quantity_type.md) | 0..1 <br/> [QuantityType](QuantityType.md) | Quantity type used as basis for this cost calculation | [AbstractCostRecord](AbstractCostRecord.md) |
| [cost_quantity_value](cost_quantity_value.md) | 0..1 <br/> [Double](Double.md) | Quantity magnitude used as basis for this cost calculation | [AbstractCostRecord](AbstractCostRecord.md) |
| [cost_quantity_unit](cost_quantity_unit.md) | 0..1 <br/> [String](String.md) | Unit of the cost quantity value | [AbstractCostRecord](AbstractCostRecord.md) |
| [applies_to_entities](applies_to_entities.md) | * <br/> [Entity](Entity.md) | Entities this cost item applies to | [AbstractCostRecord](AbstractCostRecord.md) |
| [cost_items](cost_items.md) | * <br/> [CostItem](CostItem.md) | Cost items associated with this entity | [VirtualEntity](VirtualEntity.md) |
| [cost_assemblies](cost_assemblies.md) | * <br/> [CostAssembly](CostAssembly.md) | Aggregated unit prices associated with this entity | [VirtualEntity](VirtualEntity.md) |
| [materials](materials.md) | * <br/> [Material](Material.md) | Material definitions associated with this entity | [VirtualEntity](VirtualEntity.md) |
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
| [VirtualEntity](VirtualEntity.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [SpatialContext](SpatialContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [ProjectContext](ProjectContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [PerimeterContext](PerimeterContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [LegalSiteContext](LegalSiteContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [BuildingContext](BuildingContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [CivilStructureContext](CivilStructureContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [LevelContext](LevelContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [ZoneContext](ZoneContext.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [Space](Space.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [System](System.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [CostItem](CostItem.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [CostAssembly](CostAssembly.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |
| [Material](Material.md) | [cost_assemblies](cost_assemblies.md) | range | [CostAssembly](CostAssembly.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:CostAssembly |
| native | pbs:CostAssembly |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CostAssembly
description: Aggregated unit price assembled from multiple cost items.
from_schema: https://example.org/pragmatic-bim-data-contract
is_a: AbstractCostRecord
slots:
- component_cost_items
class_uri: pbs:CostAssembly

```
</details>

### Induced

<details>
```yaml
name: CostAssembly
description: Aggregated unit price assembled from multiple cost items.
from_schema: https://example.org/pragmatic-bim-data-contract
is_a: AbstractCostRecord
attributes:
  component_cost_items:
    name: component_cost_items
    description: Atomic cost items that are aggregated into this cost assembly.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: component_cost_items
    owner: CostAssembly
    domain_of:
    - CostAssembly
    range: CostItem
    multivalued: true
    inlined: false
  cost_category:
    name: cost_category
    description: Cost category label kept intentionally open pending classification-backed
      modeling.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_category
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: string
  unit_cost:
    name: unit_cost
    description: Unit cost for this cost item.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: unit_cost
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: double
    required: true
    minimum_value: 0
  currency:
    name: currency
    description: ISO 4217 currency code (for example EUR, USD).
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: currency
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: string
    required: true
    pattern: ^[A-Z]{3}$
  cost_quantity_type:
    name: cost_quantity_type
    description: Quantity type used as basis for this cost calculation.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_quantity_type
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: QuantityType
  cost_quantity_value:
    name: cost_quantity_value
    description: Quantity magnitude used as basis for this cost calculation.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_quantity_value
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: double
    minimum_value: 0
  cost_quantity_unit:
    name: cost_quantity_unit
    description: Unit of the cost quantity value.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_quantity_unit
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: string
  applies_to_entities:
    name: applies_to_entities
    description: Entities this cost item applies to.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: applies_to_entities
    owner: CostAssembly
    domain_of:
    - AbstractCostRecord
    range: Entity
    multivalued: true
  cost_items:
    name: cost_items
    description: Cost items associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_items
    owner: CostAssembly
    domain_of:
    - VirtualEntity
    range: CostItem
    multivalued: true
    inlined: false
  cost_assemblies:
    name: cost_assemblies
    description: Aggregated unit prices associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_assemblies
    owner: CostAssembly
    domain_of:
    - VirtualEntity
    range: CostAssembly
    multivalued: true
    inlined: false
  materials:
    name: materials
    description: Material definitions associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: materials
    owner: CostAssembly
    domain_of:
    - VirtualEntity
    range: Material
    multivalued: true
    inlined: false
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    identifier: true
    alias: id
    owner: CostAssembly
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: Default display name.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: name
    owner: CostAssembly
    domain_of:
    - Entity
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: localized_names
    owner: CostAssembly
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  description:
    name: description
    description: Default description text.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: description
    owner: CostAssembly
    domain_of:
    - Entity
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: meaning_uri
    owner: CostAssembly
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: localized_descriptions
    owner: CostAssembly
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: ifc_global_id
    owner: CostAssembly
    domain_of:
    - Entity
    range: string
    pattern: ^[0-3][0-9A-Za-z_$]{21}$
  classifications:
    name: classifications
    description: Classification entries from IFC and other schemes.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: classifications
    owner: CostAssembly
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
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: geometry_representations
    owner: CostAssembly
    domain_of:
    - Entity
    range: GeometryRepresentation
    multivalued: true
    inlined: true
  quantity_values:
    name: quantity_values
    description: Quantities associated with the entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: quantity_values
    owner: CostAssembly
    domain_of:
    - Entity
    range: QuantityValue
    multivalued: true
    inlined: true
  documents:
    name: documents
    description: Linked documents associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: documents
    owner: CostAssembly
    domain_of:
    - Entity
    range: Document
    multivalued: true
    inlined: true
  metadata:
    name: metadata
    description: Generic metadata container for IFC attributes/properties and project-specific
      extensions.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: metadata
    owner: CostAssembly
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
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: performance_properties
    owner: CostAssembly
    domain_of:
    - Entity
    range: PerformanceProperty
    multivalued: true
    inlined: true
  decisions:
    name: decisions
    description: Decision records associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: decisions
    owner: CostAssembly
    domain_of:
    - Entity
    range: Decision
    multivalued: true
    inlined: true
  tasks:
    name: tasks
    description: Tasks associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: tasks
    owner: CostAssembly
    domain_of:
    - Entity
    range: Task
    multivalued: true
    inlined: true
  messages:
    name: messages
    description: Messages associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: messages
    owner: CostAssembly
    domain_of:
    - Entity
    range: Message
    multivalued: true
    inlined: true
  created_at:
    name: created_at
    description: Creation timestamp for this entity record.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: created_at
    owner: CostAssembly
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: modified_at
    owner: CostAssembly
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: revision
    owner: CostAssembly
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: status
    owner: CostAssembly
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:CostAssembly

```
</details>