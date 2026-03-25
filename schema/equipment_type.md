

# Slot: equipment_type 


_Classification of equipment (for example HVAC, electrical, plumbing)._





URI: [pbs:equipment_type](https://example.org/pragmatic-bim-data-contract/equipment_type)
Alias: equipment_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EquipmentType](EquipmentType.md) |
| Domain Of | [Equipment](Equipment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:equipment_type |
| native | pbs:equipment_type |




## LinkML Source

<details>
```yaml
name: equipment_type
description: Classification of equipment (for example HVAC, electrical, plumbing).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: equipment_type
domain_of:
- Equipment
range: EquipmentType
required: true

```
</details>