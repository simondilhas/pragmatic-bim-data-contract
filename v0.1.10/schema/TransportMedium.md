---
search:
  boost: 2.0
---


# Enum: TransportMedium 




_Primary medium transported through or enabled by a physical connector._



<div data-search-exclude markdown="1">

URI: [pbs:TransportMedium](https://schema.pragmaticbim.ch/TransportMedium)

**Enum URI:** [pbs:TransportMedium](https://schema.pragmaticbim.ch/TransportMedium)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| human_access | pbs:transport_medium_human_access | Human movement/access medium. | Title: Human Access<br>|
| daylight_view | pbs:transport_medium_daylight_view | Daylight/view medium. | Title: Daylight/View<br>|
| air | pbs:transport_medium_air | Air medium. | Title: Air<br>|
| liquid | pbs:transport_medium_liquid | Liquid medium. | Title: Liquid<br>|
| gas | pbs:transport_medium_gas | Gas medium. | Title: Gas<br>|
| electricity | pbs:transport_medium_electricity | Electrical energy medium. | Title: Electricity<br>|
| data | pbs:transport_medium_data | Data/signal medium. | Title: Data<br>|




## Slots

| Name | Description |
| ---  | --- |
| [transport_medium](transport_medium.md) | Primary transport medium carried or enabled by the connector (for example human_access, air, liquid, electricity). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: TransportMedium
description: Primary medium transported through or enabled by a physical connector.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:TransportMedium
permissible_values:
  human_access:
    text: human_access
    description: Human movement/access medium.
    meaning: pbs:transport_medium_human_access
    alt_descriptions:
      de:
        source: de
        description: Personenverkehr
    title: Human Access
  daylight_view:
    text: daylight_view
    description: Daylight/view medium.
    meaning: pbs:transport_medium_daylight_view
    alt_descriptions:
      de:
        source: de
        description: Tageslicht/Sicht
    title: Daylight/View
  air:
    text: air
    description: Air medium.
    meaning: pbs:transport_medium_air
    alt_descriptions:
      de:
        source: de
        description: Luft
    title: Air
  liquid:
    text: liquid
    description: Liquid medium.
    meaning: pbs:transport_medium_liquid
    alt_descriptions:
      de:
        source: de
        description: Fluessigkeit
    title: Liquid
  gas:
    text: gas
    description: Gas medium.
    meaning: pbs:transport_medium_gas
    alt_descriptions:
      de:
        source: de
        description: Gas
    title: Gas
  electricity:
    text: electricity
    description: Electrical energy medium.
    meaning: pbs:transport_medium_electricity
    alt_descriptions:
      de:
        source: de
        description: Elektrizitaet
    title: Electricity
  data:
    text: data
    description: Data/signal medium.
    meaning: pbs:transport_medium_data
    alt_descriptions:
      de:
        source: de
        description: Daten
    title: Data

```
</details>

</div>