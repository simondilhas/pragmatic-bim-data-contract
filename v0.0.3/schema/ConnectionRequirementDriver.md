# Enum: ConnectionRequirementDriver 




_Main requirement drivers for connection element performance._



URI: [pbs:ConnectionRequirementDriver](https://example.org/pragmatic-bim-data-contract/ConnectionRequirementDriver)

**Enum URI:** [pbs:ConnectionRequirementDriver](https://example.org/pragmatic-bim-data-contract/ConnectionRequirementDriver)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| fire | pbs:connection_requirement_driver_fire |  |
| security | pbs:connection_requirement_driver_security |  |
| accessibility | pbs:connection_requirement_driver_accessibility |  |
| acoustic | pbs:connection_requirement_driver_acoustic |  |
| thermal | pbs:connection_requirement_driver_thermal |  |
| visual | pbs:connection_requirement_driver_visual |  |
| structural | pbs:connection_requirement_driver_structural |  |




## Slots

| Name | Description |
| ---  | --- |
| [connection_physical_requirement_drivers](connection_physical_requirement_drivers.md) | Performance requirement drivers for this physical connection element |
| [connection_virtual_requirement_drivers](connection_virtual_requirement_drivers.md) | Main requirement drivers for this virtual connection |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: ConnectionRequirementDriver
description: Main requirement drivers for connection element performance.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:ConnectionRequirementDriver
permissible_values:
  fire:
    text: fire
    meaning: pbs:connection_requirement_driver_fire
  security:
    text: security
    meaning: pbs:connection_requirement_driver_security
  accessibility:
    text: accessibility
    meaning: pbs:connection_requirement_driver_accessibility
  acoustic:
    text: acoustic
    meaning: pbs:connection_requirement_driver_acoustic
  thermal:
    text: thermal
    meaning: pbs:connection_requirement_driver_thermal
  visual:
    text: visual
    meaning: pbs:connection_requirement_driver_visual
  structural:
    text: structural
    meaning: pbs:connection_requirement_driver_structural

```
</details>