---
search:
  boost: 2.0
---


# Enum: SeparatorRequirementDriver 




_Main requirement drivers for separator performance._



<div data-search-exclude markdown="1">

URI: [pbs:SeparatorRequirementDriver](https://schema.pragmaticbim.ch/SeparatorRequirementDriver)

**Enum URI:** [pbs:SeparatorRequirementDriver](https://schema.pragmaticbim.ch/SeparatorRequirementDriver)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| acoustic | pbs:requirement_driver_acoustic |  | Title: Acoustic<br>|
| fire | pbs:requirement_driver_fire |  | Title: Fire<br>|
| thermal | pbs:requirement_driver_thermal |  | Title: Thermal<br>|
| privacy | pbs:requirement_driver_privacy |  | Title: Privacy<br>|
| hygiene | pbs:requirement_driver_hygiene |  | Title: Hygiene<br>|
| structural | pbs:requirement_driver_structural |  | Title: Structural<br>|




## Slots

| Name | Description |
| ---  | --- |
| [separator_requirement_drivers](separator_requirement_drivers.md) | Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SeparatorRequirementDriver
description: Main requirement drivers for separator performance.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SeparatorRequirementDriver
permissible_values:
  acoustic:
    text: acoustic
    meaning: pbs:requirement_driver_acoustic
    alt_descriptions:
      de:
        source: de
        description: Akustik
    title: Acoustic
  fire:
    text: fire
    meaning: pbs:requirement_driver_fire
    alt_descriptions:
      de:
        source: de
        description: Brandschutz
    title: Fire
  thermal:
    text: thermal
    meaning: pbs:requirement_driver_thermal
    alt_descriptions:
      de:
        source: de
        description: Waerme
    title: Thermal
  privacy:
    text: privacy
    meaning: pbs:requirement_driver_privacy
    alt_descriptions:
      de:
        source: de
        description: Privatsphaere
    title: Privacy
  hygiene:
    text: hygiene
    meaning: pbs:requirement_driver_hygiene
    alt_descriptions:
      de:
        source: de
        description: Hygiene
    title: Hygiene
  structural:
    text: structural
    meaning: pbs:requirement_driver_structural
    alt_descriptions:
      de:
        source: de
        description: Tragwerk
    title: Structural

```
</details>

</div>