---
search:
  boost: 2.0
---


# Enum: SeparatorSlabType 




_Classification of slab-based separator elements._



<div data-search-exclude markdown="1">

URI: [pbs:SeparatorSlabType](https://schema.pragmaticbim.ch/SeparatorSlabType)

**Enum URI:** [pbs:SeparatorSlabType](https://schema.pragmaticbim.ch/SeparatorSlabType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| floor | ifcowl:IfcSlabTypeEnum.FLOOR |  | Title: Floor<br>|
| roof | ifcowl:IfcSlabTypeEnum.ROOF |  | Title: Roof<br>|
| baseslab | ifcowl:IfcSlabTypeEnum.BASESLAB |  | Title: Base Slab<br>|
| balcony | ifcowl:IfcSlabTypeEnum.FLOOR | Balcony slab; mapped to FLOOR as the closest IFC slab type. | Title: Balcony<br>|




## Slots

| Name | Description |
| ---  | --- |
| [separator_slab_type](separator_slab_type.md) | Classification of slab-based separator element (for example floor/roof/base slab). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SeparatorSlabType
description: Classification of slab-based separator elements.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SeparatorSlabType
permissible_values:
  floor:
    text: floor
    meaning: ifcowl:IfcSlabTypeEnum.FLOOR
    alt_descriptions:
      de:
        source: de
        description: Boden
    title: Floor
  roof:
    text: roof
    meaning: ifcowl:IfcSlabTypeEnum.ROOF
    alt_descriptions:
      de:
        source: de
        description: Dach
    title: Roof
  baseslab:
    text: baseslab
    meaning: ifcowl:IfcSlabTypeEnum.BASESLAB
    alt_descriptions:
      de:
        source: de
        description: Bodenplatte
    title: Base Slab
  balcony:
    text: balcony
    description: Balcony slab; mapped to FLOOR as the closest IFC slab type.
    meaning: ifcowl:IfcSlabTypeEnum.FLOOR
    alt_descriptions:
      de:
        source: de
        description: Balkon
    title: Balcony

```
</details>

</div>