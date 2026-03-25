# Enum: EquipmentType 



URI: [pbs:EquipmentType](https://example.org/pragmatic-bim-data-contract/EquipmentType)

**Enum URI:** [pbs:EquipmentType](https://example.org/pragmatic-bim-data-contract/EquipmentType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| hvac | ifcowl:IfcDistributionElement | HVAC endpoint/device such as terminal units or packaged devices |
| electrical | ifcowl:IfcElectricalElement | Electrical endpoint/device such as appliances, outlets, or fixtures |
| plumbing | ifcowl:IfcFlowTerminal | Plumbing endpoint/device such as sanitary terminals and fixtures |
| fire_safety | ifcowl:IfcFireSuppressionTerminal | Fire safety endpoint/device such as suppression terminals and alarms |
| controls | ifcowl:IfcDistributionControlElement | Monitoring/control device such as sensors, actuators, and controllers |
| furniture | ifcowl:IfcFurniture | Furniture/device objects treated as endpoint assets |
| other | ifcowl:IfcElement | Other endpoint/device element not covered by controlled values |




## Slots

| Name | Description |
| ---  | --- |
| [equipment_type](equipment_type.md) | Classification of equipment (for example HVAC, electrical, plumbing) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: EquipmentType
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:EquipmentType
permissible_values:
  hvac:
    text: hvac
    description: HVAC endpoint/device such as terminal units or packaged devices.
    meaning: ifcowl:IfcDistributionElement
  electrical:
    text: electrical
    description: Electrical endpoint/device such as appliances, outlets, or fixtures.
    meaning: ifcowl:IfcElectricalElement
  plumbing:
    text: plumbing
    description: Plumbing endpoint/device such as sanitary terminals and fixtures.
    meaning: ifcowl:IfcFlowTerminal
  fire_safety:
    text: fire_safety
    description: Fire safety endpoint/device such as suppression terminals and alarms.
    meaning: ifcowl:IfcFireSuppressionTerminal
  controls:
    text: controls
    description: Monitoring/control device such as sensors, actuators, and controllers.
    meaning: ifcowl:IfcDistributionControlElement
  furniture:
    text: furniture
    description: Furniture/device objects treated as endpoint assets.
    meaning: ifcowl:IfcFurniture
  other:
    text: other
    description: Other endpoint/device element not covered by controlled values.
    meaning: ifcowl:IfcElement

```
</details>