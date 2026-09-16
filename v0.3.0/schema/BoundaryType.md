---
search:
  boost: 2.0
---


# Enum: BoundaryType 



<div data-search-exclude markdown="1">

URI: [pbs:BoundaryType](https://schema.pragmaticbim.ch/BoundaryType)

**Enum URI:** [pbs:BoundaryType](https://schema.pragmaticbim.ch/BoundaryType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| flooring | ifcowl:IfcCoveringTypeEnum.FLOORING |  | Title: Flooring<br>|
| ceiling | ifcowl:IfcCoveringTypeEnum.CEILING |  | Title: Ceiling<br>|
| cladding | ifcowl:IfcCoveringTypeEnum.CLADDING |  | Title: Cladding<br>|
| roofing | ifcowl:IfcCoveringTypeEnum.ROOFING |  | Title: Roofing<br>|




## Slots

| Name | Description |
| ---  | --- |
| [boundary_type](boundary_type.md) | Classification of boundary element (e.g., covering). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: BoundaryType
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:BoundaryType
permissible_values:
  flooring:
    text: flooring
    meaning: ifcowl:IfcCoveringTypeEnum.FLOORING
    alt_descriptions:
      de:
        source: de
        description: Bodenbelag
    title: Flooring
  ceiling:
    text: ceiling
    meaning: ifcowl:IfcCoveringTypeEnum.CEILING
    alt_descriptions:
      de:
        source: de
        description: Decke
    title: Ceiling
  cladding:
    text: cladding
    meaning: ifcowl:IfcCoveringTypeEnum.CLADDING
    alt_descriptions:
      de:
        source: de
        description: Verkleidung
    title: Cladding
  roofing:
    text: roofing
    meaning: ifcowl:IfcCoveringTypeEnum.ROOFING
    alt_descriptions:
      de:
        source: de
        description: Dachbekleidung
    title: Roofing

```
</details>

</div>