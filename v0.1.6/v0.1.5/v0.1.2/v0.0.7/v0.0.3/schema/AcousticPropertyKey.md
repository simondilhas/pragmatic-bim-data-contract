# Enum: AcousticPropertyKey 




_Canonical acoustic-related keys derived from IFC PropertySets._



URI: [pbs:AcousticPropertyKey](https://example.org/pragmatic-bim-data-contract/AcousticPropertyKey)

**Enum URI:** [pbs:AcousticPropertyKey](https://example.org/pragmatic-bim-data-contract/AcousticPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| rating_db | pbs:acoustic_property_rating_db |  |
| impact_sound_rating_db | pbs:acoustic_property_impact_sound_rating_db |  |
| airborne_sound_rating_db | pbs:acoustic_property_airborne_sound_rating_db |  |




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
name: AcousticPropertyKey
description: Canonical acoustic-related keys derived from IFC PropertySets.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:AcousticPropertyKey
permissible_values:
  rating_db:
    text: rating_db
    meaning: pbs:acoustic_property_rating_db
  impact_sound_rating_db:
    text: impact_sound_rating_db
    meaning: pbs:acoustic_property_impact_sound_rating_db
  airborne_sound_rating_db:
    text: airborne_sound_rating_db
    meaning: pbs:acoustic_property_airborne_sound_rating_db

```
</details>