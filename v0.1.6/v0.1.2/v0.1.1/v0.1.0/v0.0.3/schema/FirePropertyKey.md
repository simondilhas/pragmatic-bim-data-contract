# Enum: FirePropertyKey 




_Canonical fire-related keys derived from IFC PropertySets._



URI: [pbs:FirePropertyKey](https://example.org/pragmatic-bim-data-contract/FirePropertyKey)

**Enum URI:** [pbs:FirePropertyKey](https://example.org/pragmatic-bim-data-contract/FirePropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| resistance_rating | pbs:fire_property_resistance_rating |  |
| smoke_rating | pbs:fire_property_smoke_rating |  |
| reaction_to_fire | pbs:fire_property_reaction_to_fire |  |




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
name: FirePropertyKey
description: Canonical fire-related keys derived from IFC PropertySets.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:FirePropertyKey
permissible_values:
  resistance_rating:
    text: resistance_rating
    meaning: pbs:fire_property_resistance_rating
  smoke_rating:
    text: smoke_rating
    meaning: pbs:fire_property_smoke_rating
  reaction_to_fire:
    text: reaction_to_fire
    meaning: pbs:fire_property_reaction_to_fire

```
</details>