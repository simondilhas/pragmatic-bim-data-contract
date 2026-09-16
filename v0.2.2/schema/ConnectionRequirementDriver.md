---
search:
  boost: 2.0
---


# Enum: ConnectionRequirementDriver 




_Main requirement drivers for connection element performance._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionRequirementDriver](https://schema.pragmaticbim.ch/ConnectionRequirementDriver)

**Enum URI:** [pbs:ConnectionRequirementDriver](https://schema.pragmaticbim.ch/ConnectionRequirementDriver)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| fire | pbs:connection_requirement_driver_fire |  | Title: Fire<br>|
| security | pbs:connection_requirement_driver_security |  | Title: Security<br>|
| accessibility | pbs:connection_requirement_driver_accessibility |  | Title: Accessibility<br>|
| acoustic | pbs:connection_requirement_driver_acoustic |  | Title: Acoustic<br>|
| thermal | pbs:connection_requirement_driver_thermal |  | Title: Thermal<br>|
| visual | pbs:connection_requirement_driver_visual |  | Title: Visual<br>|
| structural | pbs:connection_requirement_driver_structural |  | Title: Structural<br>|




## Slots

| Name | Description |
| ---  | --- |
| [connection_physical_requirement_drivers](connection_physical_requirement_drivers.md) | Performance requirement drivers for this physical connection element. Multiple values are allowed because one connection may need to satisfy several requirements. |
| [connection_virtual_requirement_drivers](connection_virtual_requirement_drivers.md) | Main requirement drivers for this virtual connection. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionRequirementDriver
description: Main requirement drivers for connection element performance.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionRequirementDriver
permissible_values:
  fire:
    text: fire
    meaning: pbs:connection_requirement_driver_fire
    alt_descriptions:
      de:
        source: de
        description: Brandschutz
    title: Fire
  security:
    text: security
    meaning: pbs:connection_requirement_driver_security
    alt_descriptions:
      de:
        source: de
        description: Sicherheit
    title: Security
  accessibility:
    text: accessibility
    meaning: pbs:connection_requirement_driver_accessibility
    alt_descriptions:
      de:
        source: de
        description: Barrierefreiheit
    title: Accessibility
  acoustic:
    text: acoustic
    meaning: pbs:connection_requirement_driver_acoustic
    alt_descriptions:
      de:
        source: de
        description: Akustik
    title: Acoustic
  thermal:
    text: thermal
    meaning: pbs:connection_requirement_driver_thermal
    alt_descriptions:
      de:
        source: de
        description: Waerme
    title: Thermal
  visual:
    text: visual
    meaning: pbs:connection_requirement_driver_visual
    alt_descriptions:
      de:
        source: de
        description: Visuell
    title: Visual
  structural:
    text: structural
    meaning: pbs:connection_requirement_driver_structural
    alt_descriptions:
      de:
        source: de
        description: Tragwerk
    title: Structural

```
</details>

</div>