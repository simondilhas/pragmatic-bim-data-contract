---
search:
  boost: 2.0
---


# Enum: SystemDiscipline 




_Discipline of a building service system._



<div data-search-exclude markdown="1">

URI: [pbs:SystemDiscipline](https://schema.pragmaticbim.ch/SystemDiscipline)

**Enum URI:** [pbs:SystemDiscipline](https://schema.pragmaticbim.ch/SystemDiscipline)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| electrical | ifcowl:IfcDistributionSystemEnum.ELECTRICAL | Electrical power, lighting, and related electrical services. | Title: Electrical<br>|
| sanitary | ifcowl:IfcDistributionSystemEnum.PLUMBING | Water supply, drainage, and sanitary plumbing services. | Title: Sanitary<br>|
| ventilation | ifcowl:IfcDistributionSystemEnum.VENTILATION | Air movement and ventilation services. | Title: Ventilation<br>|
| heating | ifcowl:IfcDistributionSystemEnum.HEATING | Heat generation and heat distribution services. | Title: Heating<br>|




## Slots

| Name | Description |
| ---  | --- |
| [system_discipline](system_discipline.md) | Classification of system discipline (electrical, sanitary, ventilation, heating). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SystemDiscipline
description: Discipline of a building service system.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SystemDiscipline
permissible_values:
  electrical:
    text: electrical
    description: Electrical power, lighting, and related electrical services.
    meaning: ifcowl:IfcDistributionSystemEnum.ELECTRICAL
    alt_descriptions:
      de:
        source: de
        description: Elektro
    title: Electrical
  sanitary:
    text: sanitary
    description: Water supply, drainage, and sanitary plumbing services.
    meaning: ifcowl:IfcDistributionSystemEnum.PLUMBING
    alt_descriptions:
      de:
        source: de
        description: Sanitaer
    title: Sanitary
  ventilation:
    text: ventilation
    description: Air movement and ventilation services.
    meaning: ifcowl:IfcDistributionSystemEnum.VENTILATION
    alt_descriptions:
      de:
        source: de
        description: Lueftung
    title: Ventilation
  heating:
    text: heating
    description: Heat generation and heat distribution services.
    meaning: ifcowl:IfcDistributionSystemEnum.HEATING
    alt_descriptions:
      de:
        source: de
        description: Heizung
    title: Heating

```
</details>

</div>