---
search:
  boost: 2.0
---


# Enum: EquipmentType 



<div data-search-exclude markdown="1">

URI: [pbs:EquipmentType](https://schema.pragmaticbim.ch/EquipmentType)

**Enum URI:** [pbs:EquipmentType](https://schema.pragmaticbim.ch/EquipmentType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| hvac | ifcowl:IfcDistributionElement | HVAC endpoint/device such as terminal units or packaged devices. | Title: HVAC<br>|
| electrical | ifcowl:IfcElectricalElement | Electrical endpoint/device such as appliances, outlets, or fixtures. | Title: Electrical<br>|
| plumbing | ifcowl:IfcFlowTerminal | Plumbing endpoint/device such as sanitary terminals and fixtures. | Title: Plumbing<br>|
| fire_safety | ifcowl:IfcFireSuppressionTerminal | Fire safety endpoint/device such as suppression terminals and alarms. | Title: Fire Safety<br>|
| controls | ifcowl:IfcDistributionControlElement | Monitoring/control device such as sensors, actuators, and controllers. | Title: Controls<br>|
| furniture | ifcowl:IfcFurniture | Furniture/device objects treated as endpoint assets. | Title: Furniture<br>|
| other | ifcowl:IfcElement | Other endpoint/device element not covered by controlled values. | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [equipment_type](equipment_type.md) | Classification of equipment (for example HVAC, electrical, plumbing). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: EquipmentType
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:EquipmentType
permissible_values:
  hvac:
    text: hvac
    description: HVAC endpoint/device such as terminal units or packaged devices.
    meaning: ifcowl:IfcDistributionElement
    alt_descriptions:
      de:
        source: de
        description: HLK
    title: HVAC
  electrical:
    text: electrical
    description: Electrical endpoint/device such as appliances, outlets, or fixtures.
    meaning: ifcowl:IfcElectricalElement
    alt_descriptions:
      de:
        source: de
        description: Elektro
    title: Electrical
  plumbing:
    text: plumbing
    description: Plumbing endpoint/device such as sanitary terminals and fixtures.
    meaning: ifcowl:IfcFlowTerminal
    alt_descriptions:
      de:
        source: de
        description: Sanitaer
    title: Plumbing
  fire_safety:
    text: fire_safety
    description: Fire safety endpoint/device such as suppression terminals and alarms.
    meaning: ifcowl:IfcFireSuppressionTerminal
    alt_descriptions:
      de:
        source: de
        description: Brandschutz
    title: Fire Safety
  controls:
    text: controls
    description: Monitoring/control device such as sensors, actuators, and controllers.
    meaning: ifcowl:IfcDistributionControlElement
    alt_descriptions:
      de:
        source: de
        description: Regelung
    title: Controls
  furniture:
    text: furniture
    description: Furniture/device objects treated as endpoint assets.
    meaning: ifcowl:IfcFurniture
    alt_descriptions:
      de:
        source: de
        description: Mobiliar
    title: Furniture
  other:
    text: other
    description: Other endpoint/device element not covered by controlled values.
    meaning: ifcowl:IfcElement
    alt_descriptions:
      de:
        source: de
        description: Sonstiges
    title: Other

```
</details>

</div>