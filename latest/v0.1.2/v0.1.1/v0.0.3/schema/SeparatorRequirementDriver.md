# Enum: SeparatorRequirementDriver 




_Main requirement drivers for separator performance._



URI: [pbs:SeparatorRequirementDriver](https://example.org/pragmatic-bim-data-contract/SeparatorRequirementDriver)

**Enum URI:** [pbs:SeparatorRequirementDriver](https://example.org/pragmatic-bim-data-contract/SeparatorRequirementDriver)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| acoustic | pbs:requirement_driver_acoustic |  |
| fire | pbs:requirement_driver_fire |  |
| thermal | pbs:requirement_driver_thermal |  |
| privacy | pbs:requirement_driver_privacy |  |
| hygiene | pbs:requirement_driver_hygiene |  |
| structural | pbs:requirement_driver_structural |  |




## Slots

| Name | Description |
| ---  | --- |
| [separator_requirement_drivers](separator_requirement_drivers.md) | Performance requirement drivers for this separator |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: SeparatorRequirementDriver
description: Main requirement drivers for separator performance.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:SeparatorRequirementDriver
permissible_values:
  acoustic:
    text: acoustic
    meaning: pbs:requirement_driver_acoustic
  fire:
    text: fire
    meaning: pbs:requirement_driver_fire
  thermal:
    text: thermal
    meaning: pbs:requirement_driver_thermal
  privacy:
    text: privacy
    meaning: pbs:requirement_driver_privacy
  hygiene:
    text: hygiene
    meaning: pbs:requirement_driver_hygiene
  structural:
    text: structural
    meaning: pbs:requirement_driver_structural

```
</details>