---
search:
  boost: 2.0
---


# Enum: ConnectionFunctionalType 




_Functional classification of physical connections between spaces by transported medium or passage role._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionFunctionalType](https://schema.pragmaticbim.ch/ConnectionFunctionalType)

**Enum URI:** [pbs:ConnectionFunctionalType](https://schema.pragmaticbim.ch/ConnectionFunctionalType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| electrical | https://example.org/abstract/connection-functional-type/electrical | Power distribution connection. | Title: Electrical<br>|
| data | https://example.org/abstract/connection-functional-type/data | Data, telecom, or building-automation connection. | Title: Data / ICT<br>|
| ventilation | https://example.org/abstract/connection-functional-type/ventilation | Air supply, extract, or transfer connection. | Title: Ventilation<br>|
| heating | https://example.org/abstract/connection-functional-type/heating | Heating-medium supply or return connection. | Title: Heating<br>|
| cooling | https://example.org/abstract/connection-functional-type/cooling | Cooling-medium supply or return connection. | Title: Cooling<br>|
| fresh_water | https://example.org/abstract/connection-functional-type/fresh_water | Potable or domestic water supply connection. | Title: Fresh Water<br>|
| waste_water | https://example.org/abstract/connection-functional-type/waste_water | Drainage, sewage, or rainwater connection. | Title: Waste Water<br>|
| special_media | https://example.org/abstract/connection-functional-type/special_media | Gas, compressed air, fire suppression, vacuum, or other process-media connection. | Title: Special Media<br>|
| access | https://example.org/abstract/connection-functional-type/access | Physical passage of people or goods between spaces. | Title: Access / Circulation<br>|
| visual | https://example.org/abstract/connection-functional-type/visual | Sightline or daylight connection without physical passage. | Title: Visual / Daylight<br>|




## Slots

| Name | Description |
| ---  | --- |
| [connection_functional_types](connection_functional_types.md) | Functional connection role(s) between spaces (for example access, visual, ventilation, heating). Multiple values allowed (for example glazed door as access plus visual). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionFunctionalType
description: Functional classification of physical connections between spaces by transported
  medium or passage role.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionFunctionalType
permissible_values:
  electrical:
    text: electrical
    description: Power distribution connection.
    meaning: https://example.org/abstract/connection-functional-type/electrical
    alt_descriptions:
      de:
        source: de
        description: Elektro
    title: Electrical
  data:
    text: data
    description: Data, telecom, or building-automation connection.
    meaning: https://example.org/abstract/connection-functional-type/data
    alt_descriptions:
      de:
        source: de
        description: Daten / ICT
    title: Data / ICT
  ventilation:
    text: ventilation
    description: Air supply, extract, or transfer connection.
    meaning: https://example.org/abstract/connection-functional-type/ventilation
    alt_descriptions:
      de:
        source: de
        description: Lueftung
    title: Ventilation
  heating:
    text: heating
    description: Heating-medium supply or return connection.
    meaning: https://example.org/abstract/connection-functional-type/heating
    alt_descriptions:
      de:
        source: de
        description: Heizung
    title: Heating
  cooling:
    text: cooling
    description: Cooling-medium supply or return connection.
    meaning: https://example.org/abstract/connection-functional-type/cooling
    alt_descriptions:
      de:
        source: de
        description: Kuehlung
    title: Cooling
  fresh_water:
    text: fresh_water
    description: Potable or domestic water supply connection.
    meaning: https://example.org/abstract/connection-functional-type/fresh_water
    alt_descriptions:
      de:
        source: de
        description: Frischwasser
    title: Fresh Water
  waste_water:
    text: waste_water
    description: Drainage, sewage, or rainwater connection.
    meaning: https://example.org/abstract/connection-functional-type/waste_water
    alt_descriptions:
      de:
        source: de
        description: Abwasser
    title: Waste Water
  special_media:
    text: special_media
    description: Gas, compressed air, fire suppression, vacuum, or other process-media
      connection.
    meaning: https://example.org/abstract/connection-functional-type/special_media
    alt_descriptions:
      de:
        source: de
        description: Sondermedien
    title: Special Media
  access:
    text: access
    description: Physical passage of people or goods between spaces.
    meaning: https://example.org/abstract/connection-functional-type/access
    alt_descriptions:
      de:
        source: de
        description: Erschliessung
    title: Access / Circulation
  visual:
    text: visual
    description: Sightline or daylight connection without physical passage.
    meaning: https://example.org/abstract/connection-functional-type/visual
    alt_descriptions:
      de:
        source: de
        description: Sicht / Tageslicht
    title: Visual / Daylight

```
</details>

</div>