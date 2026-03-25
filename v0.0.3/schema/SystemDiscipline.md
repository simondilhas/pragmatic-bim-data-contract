# Enum: SystemDiscipline 




_Discipline of a building service system._



URI: [pbs:SystemDiscipline](https://example.org/pragmatic-bim-data-contract/SystemDiscipline)

**Enum URI:** [pbs:SystemDiscipline](https://example.org/pragmatic-bim-data-contract/SystemDiscipline)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| electrical | ifcowl:IfcDistributionSystemEnum.ELECTRICAL | Electrical power, lighting, and related electrical services |
| sanitary | ifcowl:IfcDistributionSystemEnum.PLUMBING | Water supply, drainage, and sanitary plumbing services |
| ventilation | ifcowl:IfcDistributionSystemEnum.VENTILATION | Air movement and ventilation services |
| heating | ifcowl:IfcDistributionSystemEnum.HEATING | Heat generation and heat distribution services |




## Slots

| Name | Description |
| ---  | --- |
| [system_discipline](system_discipline.md) | Classification of system discipline (electrical, sanitary, ventilation, heati... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: SystemDiscipline
description: Discipline of a building service system.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:SystemDiscipline
permissible_values:
  electrical:
    text: electrical
    description: Electrical power, lighting, and related electrical services.
    meaning: ifcowl:IfcDistributionSystemEnum.ELECTRICAL
  sanitary:
    text: sanitary
    description: Water supply, drainage, and sanitary plumbing services.
    meaning: ifcowl:IfcDistributionSystemEnum.PLUMBING
  ventilation:
    text: ventilation
    description: Air movement and ventilation services.
    meaning: ifcowl:IfcDistributionSystemEnum.VENTILATION
  heating:
    text: heating
    description: Heat generation and heat distribution services.
    meaning: ifcowl:IfcDistributionSystemEnum.HEATING

```
</details>