

# Class: MetadataEntry 


_Generic metadata entry for storing IFC attributes, PropertySet fields, or project-specific key-value data._





URI: [pbs:MetadataEntry](https://example.org/pragmatic-bim-data-contract/MetadataEntry)





```mermaid
 classDiagram
    class MetadataEntry
    click MetadataEntry href "../MetadataEntry/"
      MetadataEntry : metadata_key
        
      MetadataEntry : metadata_value
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:MetadataEntry](https://example.org/pragmatic-bim-data-contract/MetadataEntry) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [metadata_key](metadata_key.md) | 1 <br/> [String](String.md) | Metadata key, for example IfcWall | direct |
| [metadata_value](metadata_value.md) | 0..1 <br/> [String](String.md) | Metadata value serialized as text | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Entity](Entity.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Agent](Agent.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Person](Person.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Company](Company.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Message](Message.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [PhysicalElement](PhysicalElement.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Separator](Separator.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [SeparatorWall](SeparatorWall.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [SeparatorSlab](SeparatorSlab.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [ConnectionPhysical](ConnectionPhysical.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Boundary](Boundary.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Equipment](Equipment.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [VirtualEntity](VirtualEntity.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [SpatialContext](SpatialContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [ProjectContext](ProjectContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [PerimeterContext](PerimeterContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [LegalSiteContext](LegalSiteContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [BuildingContext](BuildingContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [CivilStructureContext](CivilStructureContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [LevelContext](LevelContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [ZoneContext](ZoneContext.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Space](Space.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [System](System.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [CostItem](CostItem.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [CostAssembly](CostAssembly.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |
| [Material](Material.md) | [metadata](metadata.md) | range | [MetadataEntry](MetadataEntry.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:MetadataEntry |
| native | pbs:MetadataEntry |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetadataEntry
description: Generic metadata entry for storing IFC attributes, PropertySet fields,
  or project-specific key-value data.
from_schema: https://example.org/pragmatic-bim-data-contract
slots:
- metadata_key
- metadata_value
class_uri: pbs:MetadataEntry

```
</details>

### Induced

<details>
```yaml
name: MetadataEntry
description: Generic metadata entry for storing IFC attributes, PropertySet fields,
  or project-specific key-value data.
from_schema: https://example.org/pragmatic-bim-data-contract
attributes:
  metadata_key:
    name: metadata_key
    description: Metadata key, for example IfcWall.FireRating or Pset_WallCommon.Reference.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: metadata_key
    owner: MetadataEntry
    domain_of:
    - MetadataEntry
    range: string
    required: true
  metadata_value:
    name: metadata_value
    description: Metadata value serialized as text.
    from_schema: https://example.org/pragmatic-bim-data-contract
    rank: 1000
    alias: metadata_value
    owner: MetadataEntry
    domain_of:
    - MetadataEntry
    range: string
class_uri: pbs:MetadataEntry

```
</details>