---
search:
  boost: 2.0
---


# Enum: SpaceType 




_Classification of space semantics used by modeling and downstream conversion._



<div data-search-exclude markdown="1">

URI: [pbs:SpaceType](https://schema.pragmaticbim.ch/SpaceType)

**Enum URI:** [pbs:SpaceType](https://schema.pragmaticbim.ch/SpaceType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| void | ifcowl:IfcSpace | Non-occupiable or intentionally empty space in the model. | Title: Void<br>|
| circulation | ifcowl:IfcSpace | Space primarily intended for movement and access. | Title: Circulation<br>|
| usable | ifcowl:IfcSpace | Space intended for regular occupancy or primary use. | Title: Usable<br>|
| service | ifcowl:IfcSpace | Space primarily intended for technical/service functions. | Title: Service<br>|
| modeled_gross_floor_area | ifcowl:IfcSpace | Space classification used when representing gross floor area as modeled space. | Title: Modeled Gross Floor Area<br>|
| modeled_gross_volume | ifcowl:IfcSpace | Space classification used when representing gross volume as modeled space. | Title: Modeled Gross Volume<br>|




## Slots

| Name | Description |
| ---  | --- |
| [space_type](space_type.md) | Classification of space (void, circulation, usable, service). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SpaceType
description: Classification of space semantics used by modeling and downstream conversion.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SpaceType
permissible_values:
  void:
    text: void
    description: Non-occupiable or intentionally empty space in the model.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Leerraum
    title: Void
  circulation:
    text: circulation
    description: Space primarily intended for movement and access.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Erschliessung
    title: Circulation
  usable:
    text: usable
    description: Space intended for regular occupancy or primary use.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Nutzflaeche
    title: Usable
  service:
    text: service
    description: Space primarily intended for technical/service functions.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Technikflaeche
    title: Service
  modeled_gross_floor_area:
    text: modeled_gross_floor_area
    description: Space classification used when representing gross floor area as modeled
      space.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Modellierte Brutto-Grundflaeche
    title: Modeled Gross Floor Area
  modeled_gross_volume:
    text: modeled_gross_volume
    description: Space classification used when representing gross volume as modeled
      space.
    meaning: ifcowl:IfcSpace
    alt_descriptions:
      de:
        source: de
        description: Modelliertes Brutto-Volumen
    title: Modeled Gross Volume

```
</details>

</div>