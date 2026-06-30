

# Class: BuildingContext 


_Spatial context node constrained to building semantics._





URI: [pbs:BuildingContext](https://example.org/pragmatic-bim-data-contract/BuildingContext)





```mermaid
 classDiagram
    class BuildingContext
    click BuildingContext href "../BuildingContext/"
      BuiltAssetContext <|-- BuildingContext
        click BuiltAssetContext href "../BuiltAssetContext/"
      
      BuildingContext : classifications
        
          
    
        
        
        BuildingContext --> "*" Classification : classifications
        click Classification href "../Classification/"
    

        
      BuildingContext : context_type
        
          
    
        
        
        BuildingContext --> "1" ContextType : context_type
        click ContextType href "../ContextType/"
    

        
      BuildingContext : cost_assemblies
        
          
    
        
        
        BuildingContext --> "*" CostAssembly : cost_assemblies
        click CostAssembly href "../CostAssembly/"
    

        
      BuildingContext : cost_items
        
          
    
        
        
        BuildingContext --> "*" CostItem : cost_items
        click CostItem href "../CostItem/"
    

        
      BuildingContext : created_at
        
      BuildingContext : decisions
        
          
    
        
        
        BuildingContext --> "*" Decision : decisions
        click Decision href "../Decision/"
    

        
      BuildingContext : description
        
      BuildingContext : documents
        
          
    
        
        
        BuildingContext --> "*" Document : documents
        click Document href "../Document/"
    

        
      BuildingContext : geometry_representations
        
          
    
        
        
        BuildingContext --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "../GeometryRepresentation/"
    

        
      BuildingContext : group_members
        
          
    
        
        
        BuildingContext --> "*" Entity : group_members
        click Entity href "../Entity/"
    

        
      BuildingContext : id
        
      BuildingContext : ifc_global_id
        
      BuildingContext : localized_descriptions
        
          
    
        
        
        BuildingContext --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "../LocalizedText/"
    

        
      BuildingContext : localized_names
        
          
    
        
        
        BuildingContext --> "*" LocalizedText : localized_names
        click LocalizedText href "../LocalizedText/"
    

        
      BuildingContext : materials
        
          
    
        
        
        BuildingContext --> "*" Material : materials
        click Material href "../Material/"
    

        
      BuildingContext : meaning_uri
        
      BuildingContext : messages
        
          
    
        
        
        BuildingContext --> "*" Message : messages
        click Message href "../Message/"
    

        
      BuildingContext : metadata
        
          
    
        
        
        BuildingContext --> "*" MetadataEntry : metadata
        click MetadataEntry href "../MetadataEntry/"
    

        
      BuildingContext : modified_at
        
      BuildingContext : name
        
      BuildingContext : parent_building
        
          
    
        
        
        BuildingContext --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "../BuiltAssetContext/"
    

        
      BuildingContext : parent_legal_site
        
          
    
        
        
        BuildingContext --> "0..1" LegalSiteContext : parent_legal_site
        click LegalSiteContext href "../LegalSiteContext/"
    

        
      BuildingContext : parent_level
        
          
    
        
        
        BuildingContext --> "0..1" LevelContext : parent_level
        click LevelContext href "../LevelContext/"
    

        
      BuildingContext : parent_perimeter
        
          
    
        
        
        BuildingContext --> "0..1" PerimeterContext : parent_perimeter
        click PerimeterContext href "../PerimeterContext/"
    

        
      BuildingContext : parent_project
        
          
    
        
        
        BuildingContext --> "0..1" ProjectContext : parent_project
        click ProjectContext href "../ProjectContext/"
    

        
      BuildingContext : parent_zone
        
          
    
        
        
        BuildingContext --> "0..1" ZoneContext : parent_zone
        click ZoneContext href "../ZoneContext/"
    

        
      BuildingContext : performance_properties
        
          
    
        
        
        BuildingContext --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "../PerformanceProperty/"
    

        
      BuildingContext : quantity_values
        
          
    
        
        
        BuildingContext --> "*" QuantityValue : quantity_values
        click QuantityValue href "../QuantityValue/"
    

        
      BuildingContext : revision
        
      BuildingContext : status
        
          
    
        
        
        BuildingContext --> "0..1" StatusType : status
        click StatusType href "../StatusType/"
    

        
      BuildingContext : tasks
        
          
    
        
        
        BuildingContext --> "*" Task : tasks
        click Task href "../Task/"
    

        
      BuildingContext : zone_type
        
          
    
        
        
        BuildingContext --> "0..1" ZoneType : zone_type
        click ZoneType href "../ZoneType/"
    

        
      
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * [SpatialContext](SpatialContext.md)
            * [BuiltAssetContext](BuiltAssetContext.md)
                * **BuildingContext**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:BuildingContext](https://example.org/pragmatic-bim-data-contract/BuildingContext) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [context_type](context_type.md) | 1 <br/> [ContextType](ContextType.md) | Classification of context entity (project, perimeter, legal_site, building, c... | [SpatialContext](SpatialContext.md) |
| [zone_type](zone_type.md) | 0..1 <br/> [ZoneType](ZoneType.md) | Optional zone classification; intended for SpatialContext nodes where context... | [SpatialContext](SpatialContext.md) |
| [parent_project](parent_project.md) | 0..1 <br/> [ProjectContext](ProjectContext.md) | Parent project context reference | [SpatialContext](SpatialContext.md) |
| [parent_perimeter](parent_perimeter.md) | 0..1 <br/> [PerimeterContext](PerimeterContext.md) | Parent perimeter context reference | [SpatialContext](SpatialContext.md) |
| [parent_legal_site](parent_legal_site.md) | 0..1 <br/> [LegalSiteContext](LegalSiteContext.md) | Parent legal site context reference | [SpatialContext](SpatialContext.md) |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference | [SpatialContext](SpatialContext.md) |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference | [SpatialContext](SpatialContext.md) |
| [parent_zone](parent_zone.md) | 0..1 <br/> [ZoneContext](ZoneContext.md) | Parent zone context reference | [SpatialContext](SpatialContext.md) |
| [group_members](group_members.md) | * <br/> [Entity](Entity.md) | Zone members; may include spaces, separations, systems, etc | [SpatialContext](SpatialContext.md) |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:BuildingContext |
| native | pbs:BuildingContext |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BuildingContext
description: Spatial context node constrained to building semantics.
from_schema: https://example.org/pragmatic-bim-data-contract
is_a: BuiltAssetContext
class_uri: pbs:BuildingContext

```
</details>

### Induced

<details>
```yaml
name: BuildingContext
description: Spatial context node constrained to building semantics.
from_schema: https://example.org/pragmatic-bim-data-contract
is_a: BuiltAssetContext
attributes:
  context_type:
    name: context_type
    description: Classification of context entity (project, perimeter, legal_site,
      building, civil_structure, level, zone).
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: context_type
    owner: BuildingContext
    domain_of:
    - SpatialContext
    range: ContextType
    required: true
  zone_type:
    name: zone_type
    description: Optional zone classification; intended for SpatialContext nodes where
      context_type is zone.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: zone_type
    owner: BuildingContext
    domain_of:
    - SpatialContext
    range: ZoneType
  parent_project:
    name: parent_project
    description: Parent project context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_project
    owner: BuildingContext
    domain_of:
    - SpatialContext
    - System
    range: ProjectContext
  parent_perimeter:
    name: parent_perimeter
    description: Parent perimeter context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_perimeter
    owner: BuildingContext
    domain_of:
    - SpatialContext
    range: PerimeterContext
  parent_legal_site:
    name: parent_legal_site
    description: Parent legal site context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_legal_site
    owner: BuildingContext
    domain_of:
    - SpatialContext
    range: LegalSiteContext
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_building
    owner: BuildingContext
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    - System
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    description: Parent level/storey context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_level
    owner: BuildingContext
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  parent_zone:
    name: parent_zone
    description: Parent zone context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_zone
    owner: BuildingContext
    domain_of:
    - SpatialContext
    - Space
    range: ZoneContext
  group_members:
    name: group_members
    description: Zone members; may include spaces, separations, systems, etc.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: group_members
    owner: BuildingContext
    domain_of:
    - SpatialContext
    range: Entity
    multivalued: true
  cost_items:
    name: cost_items
    description: Cost items associated with this entity.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: cost_items
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: localized_descriptions
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
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
    owner: BuildingContext
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: modified_at
    owner: BuildingContext
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: revision
    owner: BuildingContext
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
    owner: BuildingContext
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:BuildingContext

```
</details>