# Enum: MaterialPropertyKey 




_Canonical material-related keys derived from IFC PropertySets and material metadata._



URI: [pbs:MaterialPropertyKey](https://example.org/pragmatic-bim-data-contract/MaterialPropertyKey)

**Enum URI:** [pbs:MaterialPropertyKey](https://example.org/pragmatic-bim-data-contract/MaterialPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| material_name | pbs:material_property_name |  |
| material_class | pbs:material_property_class |  |
| density | pbs:material_property_density |  |
| thermal_conductivity | pbs:material_property_thermal_conductivity |  |




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
name: MaterialPropertyKey
description: Canonical material-related keys derived from IFC PropertySets and material
  metadata.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:MaterialPropertyKey
permissible_values:
  material_name:
    text: material_name
    meaning: pbs:material_property_name
  material_class:
    text: material_class
    meaning: pbs:material_property_class
  density:
    text: density
    meaning: pbs:material_property_density
  thermal_conductivity:
    text: thermal_conductivity
    meaning: pbs:material_property_thermal_conductivity

```
</details>