

# Class: Agent 


_Abstract base class for people or organizations acting in workflow and communication roles._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [pbs:Agent](https://example.org/pragmatic-bim-data-contract/Agent)





```mermaid
 classDiagram
    class Agent
    click Agent href "../Agent/"
      Entity <|-- Agent
        click Entity href "../Entity/"
      

      Agent <|-- Person
        click Person href "../Person/"
      Agent <|-- Company
        click Company href "../Company/"
      

      Agent : classifications
        
          
    
        
        
        Agent --> "*" Classification : classifications
        click Classification href "../Classification/"
    

        
      Agent : contact_points
        
          
    
        
        
        Agent --> "*" ContactPoint : contact_points
        click ContactPoint href "../ContactPoint/"
    

        
      Agent : created_at
        
      Agent : decisions
        
          
    
        
        
        Agent --> "*" Decision : decisions
        click Decision href "../Decision/"
    

        
      Agent : description
        
      Agent : documents
        
          
    
        
        
        Agent --> "*" Document : documents
        click Document href "../Document/"
    

        
      Agent : geometry_representations
        
          
    
        
        
        Agent --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "../GeometryRepresentation/"
    

        
      Agent : id
        
      Agent : ifc_global_id
        
      Agent : localized_descriptions
        
          
    
        
        
        Agent --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "../LocalizedText/"
    

        
      Agent : localized_names
        
          
    
        
        
        Agent --> "*" LocalizedText : localized_names
        click LocalizedText href "../LocalizedText/"
    

        
      Agent : meaning_uri
        
      Agent : messages
        
          
    
        
        
        Agent --> "*" Message : messages
        click Message href "../Message/"
    

        
      Agent : metadata
        
          
    
        
        
        Agent --> "*" MetadataEntry : metadata
        click MetadataEntry href "../MetadataEntry/"
    

        
      Agent : modified_at
        
      Agent : name
        
      Agent : performance_properties
        
          
    
        
        
        Agent --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "../PerformanceProperty/"
    

        
      Agent : postal_addresses
        
          
    
        
        
        Agent --> "*" PostalAddress : postal_addresses
        click PostalAddress href "../PostalAddress/"
    

        
      Agent : quantity_values
        
          
    
        
        
        Agent --> "*" QuantityValue : quantity_values
        click QuantityValue href "../QuantityValue/"
    

        
      Agent : revision
        
      Agent : status
        
          
    
        
        
        Agent --> "0..1" StatusType : status
        click StatusType href "../StatusType/"
    

        
      Agent : tasks
        
          
    
        
        
        Agent --> "*" Task : tasks
        click Task href "../Task/"
    

        
      
```





## Inheritance
* [Entity](Entity.md)
    * **Agent**
        * [Person](Person.md)
        * [Company](Company.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Agent](https://example.org/pragmatic-bim-data-contract/Agent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [postal_addresses](postal_addresses.md) | * <br/> [PostalAddress](PostalAddress.md) | Structured postal or physical addresses associated with this agent | direct |
| [contact_points](contact_points.md) | * <br/> [ContactPoint](ContactPoint.md) | Structured communication channels and profiles associated with this agent | direct |
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
| [Decision](Decision.md) | [decided_by](decided_by.md) | range | [Agent](Agent.md) |
| [Task](Task.md) | [assignee](assignee.md) | range | [Agent](Agent.md) |
| [Message](Message.md) | [sender](sender.md) | range | [Agent](Agent.md) |
| [Message](Message.md) | [recipients](recipients.md) | range | [Agent](Agent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Agent |
| native | pbs:Agent |
| exact | prov:Agent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Agent
description: Abstract base class for people or organizations acting in workflow and
  communication roles.
from_schema: https://example.org/pragmatic-bim-data-contract
exact_mappings:
- prov:Agent
is_a: Entity
abstract: true
slots:
- postal_addresses
- contact_points
class_uri: pbs:Agent

```
</details>

### Induced

<details>
```yaml
name: Agent
description: Abstract base class for people or organizations acting in workflow and
  communication roles.
from_schema: https://example.org/pragmatic-bim-data-contract
exact_mappings:
- prov:Agent
is_a: Entity
abstract: true
attributes:
  postal_addresses:
    name: postal_addresses
    description: Structured postal or physical addresses associated with this agent.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: postal_addresses
    owner: Agent
    domain_of:
    - Agent
    range: PostalAddress
    multivalued: true
    inlined: true
  contact_points:
    name: contact_points
    description: Structured communication channels and profiles associated with this
      agent.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: contact_points
    owner: Agent
    domain_of:
    - Agent
    range: ContactPoint
    multivalued: true
    inlined: true
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    identifier: true
    alias: id
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: localized_descriptions
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
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
    owner: Agent
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: modified_at
    owner: Agent
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: revision
    owner: Agent
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
    owner: Agent
    domain_of:
    - Entity
    range: StatusType
class_uri: pbs:Agent

```
</details>