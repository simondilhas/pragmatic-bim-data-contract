

# Class: SeparatorWall 


_Wall-based separating element._





URI: [pbs:SeparatorWall](https://example.org/pragmatic-bim-data-contract/SeparatorWall)





```mermaid
 classDiagram
    class SeparatorWall
    click SeparatorWall href "../SeparatorWall/"
      Separator <|-- SeparatorWall
        click Separator href "../Separator/"
      
      SeparatorWall : classifications
        
          
    
        
        
        SeparatorWall --> "*" Classification : classifications
        click Classification href "../Classification/"
    

        
      SeparatorWall : created_at
        
      SeparatorWall : decisions
        
          
    
        
        
        SeparatorWall --> "*" Decision : decisions
        click Decision href "../Decision/"
    

        
      SeparatorWall : description
        
      SeparatorWall : documents
        
          
    
        
        
        SeparatorWall --> "*" Document : documents
        click Document href "../Document/"
    

        
      SeparatorWall : geometry_representations
        
          
    
        
        
        SeparatorWall --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "../GeometryRepresentation/"
    

        
      SeparatorWall : id
        
      SeparatorWall : ifc_global_id
        
      SeparatorWall : localized_descriptions
        
          
    
        
        
        SeparatorWall --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "../LocalizedText/"
    

        
      SeparatorWall : localized_names
        
          
    
        
        
        SeparatorWall --> "*" LocalizedText : localized_names
        click LocalizedText href "../LocalizedText/"
    

        
      SeparatorWall : meaning_uri
        
      SeparatorWall : messages
        
          
    
        
        
        SeparatorWall --> "*" Message : messages
        click Message href "../Message/"
    

        
      SeparatorWall : metadata
        
          
    
        
        
        SeparatorWall --> "*" MetadataEntry : metadata
        click MetadataEntry href "../MetadataEntry/"
    

        
      SeparatorWall : modified_at
        
      SeparatorWall : name
        
      SeparatorWall : parent_building
        
          
    
        
        
        SeparatorWall --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "../BuiltAssetContext/"
    

        
      SeparatorWall : parent_level
        
          
    
        
        
        SeparatorWall --> "0..1" LevelContext : parent_level
        click LevelContext href "../LevelContext/"
    

        
      SeparatorWall : performance_properties
        
          
    
        
        
        SeparatorWall --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "../PerformanceProperty/"
    

        
      SeparatorWall : quantity_values
        
          
    
        
        
        SeparatorWall --> "*" QuantityValue : quantity_values
        click QuantityValue href "../QuantityValue/"
    

        
      SeparatorWall : revision
        
      SeparatorWall : separates_spaces
        
          
    
        
        
        SeparatorWall --> "*" Space : separates_spaces
        click Space href "../Space/"
    

        
      SeparatorWall : separator_requirement_drivers
        
          
    
        
        
        SeparatorWall --> "*" SeparatorRequirementDriver : separator_requirement_drivers
        click SeparatorRequirementDriver href "../SeparatorRequirementDriver/"
    

        
      SeparatorWall : separator_wall_type
        
          
    
        
        
        SeparatorWall --> "1" SeparatorWallType : separator_wall_type
        click SeparatorWallType href "../SeparatorWallType/"
    

        
      SeparatorWall : status
        
          
    
        
        
        SeparatorWall --> "0..1" StatusType : status
        click StatusType href "../StatusType/"
    

        
      SeparatorWall : tasks
        
          
    
        
        
        SeparatorWall --> "*" Task : tasks
        click Task href "../Task/"
    

        
      
```





## Inheritance
* [Entity](Entity.md)
    * [PhysicalElement](PhysicalElement.md)
        * [Separator](Separator.md)
            * **SeparatorWall**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:SeparatorWall](https://example.org/pragmatic-bim-data-contract/SeparatorWall) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [separator_wall_type](separator_wall_type.md) | 1 <br/> [SeparatorWallType](SeparatorWallType.md) | Classification of wall-based separator element | direct |
| [separates_spaces](separates_spaces.md) | * <br/> [Space](Space.md) | Spaces separated by this separator element | direct |
| [separator_requirement_drivers](separator_requirement_drivers.md) | * <br/> [SeparatorRequirementDriver](SeparatorRequirementDriver.md) | Performance requirement drivers for this separator | [Separator](Separator.md) |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference | [PhysicalElement](PhysicalElement.md) |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference | [PhysicalElement](PhysicalElement.md) |
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
from_schema: https://example.org/pragmatic-bim-data-contract
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
from_schema: https://example.org/pragmatic-bim-data-contract
exact_mappings:
- ifcowl:IfcWall
is_a: Separator
attributes:
  separator_wall_type:
    name: separator_wall_type
    description: Classification of wall-based separator element.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: separator_wall_type
    owner: SeparatorWall
    domain_of:
    - SeparatorWall
    range: SeparatorWallType
    required: true
  separates_spaces:
    name: separates_spaces
    description: Spaces separated by this separator element.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: separates_spaces
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
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: separator_requirement_drivers
    owner: SeparatorWall
    domain_of:
    - Separator
    range: SeparatorRequirementDriver
    multivalued: true
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_building
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
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: parent_level
    owner: SeparatorWall
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    identifier: true
    alias: id
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: localized_descriptions
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: performance_properties
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: modified_at
    owner: SeparatorWall
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: revision
    owner: SeparatorWall
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
    owner: SeparatorWall
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:SeparatorWall

```
</details>