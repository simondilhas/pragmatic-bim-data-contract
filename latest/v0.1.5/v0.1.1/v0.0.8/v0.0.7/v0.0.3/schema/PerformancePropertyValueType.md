# Enum: PerformancePropertyValueType 




_Type discriminator for normalized performance property values._



URI: [pbs:PerformancePropertyValueType](https://example.org/pragmatic-bim-data-contract/PerformancePropertyValueType)

**Enum URI:** [pbs:PerformancePropertyValueType](https://example.org/pragmatic-bim-data-contract/PerformancePropertyValueType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| string | pbs:performance_property_value_type_string |  |
| number | pbs:performance_property_value_type_number |  |
| boolean | pbs:performance_property_value_type_boolean |  |




## Slots

| Name | Description |
| ---  | --- |
| [property_value_type](property_value_type.md) | Value type discriminator for normalized storage (for example string, number, ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: PerformancePropertyValueType
description: Type discriminator for normalized performance property values.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:PerformancePropertyValueType
permissible_values:
  string:
    text: string
    meaning: pbs:performance_property_value_type_string
  number:
    text: number
    meaning: pbs:performance_property_value_type_number
  boolean:
    text: boolean
    meaning: pbs:performance_property_value_type_boolean

```
</details>