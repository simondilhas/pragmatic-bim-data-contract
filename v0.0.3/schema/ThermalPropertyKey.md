# Enum: ThermalPropertyKey 




_Canonical thermal-related keys derived from IFC PropertySets._



URI: [pbs:ThermalPropertyKey](https://example.org/pragmatic-bim-data-contract/ThermalPropertyKey)

**Enum URI:** [pbs:ThermalPropertyKey](https://example.org/pragmatic-bim-data-contract/ThermalPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| u_value | pbs:thermal_property_u_value |  |
| r_value | pbs:thermal_property_r_value |  |
| thermal_transmittance | pbs:thermal_property_thermal_transmittance |  |




## Slots

| Name | Description |
| ---  | --- |
| [property_key](property_key.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: ThermalPropertyKey
description: Canonical thermal-related keys derived from IFC PropertySets.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:ThermalPropertyKey
permissible_values:
  u_value:
    text: u_value
    meaning: pbs:thermal_property_u_value
  r_value:
    text: r_value
    meaning: pbs:thermal_property_r_value
  thermal_transmittance:
    text: thermal_transmittance
    meaning: pbs:thermal_property_thermal_transmittance

```
</details>