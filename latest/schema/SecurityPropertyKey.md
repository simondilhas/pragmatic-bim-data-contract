# Enum: SecurityPropertyKey 




_Canonical security-related keys derived from IFC PropertySets._



URI: [pbs:SecurityPropertyKey](https://example.org/pragmatic-bim-data-contract/SecurityPropertyKey)

**Enum URI:** [pbs:SecurityPropertyKey](https://example.org/pragmatic-bim-data-contract/SecurityPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| access_control_class | pbs:security_property_access_control_class |  |
| intrusion_resistance_class | pbs:security_property_intrusion_resistance_class |  |
| surveillance_coverage | pbs:security_property_surveillance_coverage |  |




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
name: SecurityPropertyKey
description: Canonical security-related keys derived from IFC PropertySets.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:SecurityPropertyKey
permissible_values:
  access_control_class:
    text: access_control_class
    meaning: pbs:security_property_access_control_class
  intrusion_resistance_class:
    text: intrusion_resistance_class
    meaning: pbs:security_property_intrusion_resistance_class
  surveillance_coverage:
    text: surveillance_coverage
    meaning: pbs:security_property_surveillance_coverage

```
</details>