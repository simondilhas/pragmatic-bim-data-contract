---
search:
  boost: 2.0
---


# Enum: MatchStatus 




_Whether an entity satisfies a related requirement at the target revision._



<div data-search-exclude markdown="1">

URI: [pbs:MatchStatus](https://schema.pragmaticbim.ch/MatchStatus)

**Enum URI:** [pbs:MatchStatus](https://schema.pragmaticbim.ch/MatchStatus)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| met | pbs:match_status_met | Subject satisfies the requirement. | Title: Met<br>|
| unmet | pbs:match_status_unmet | Subject no longer satisfies the requirement. | Title: Unmet<br>|
| unknown | pbs:match_status_unknown | Match could not be determined. | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [match_status](match_status.md) | Whether the subject met the requirement at the target revision. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: MatchStatus
description: Whether an entity satisfies a related requirement at the target revision.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:MatchStatus
permissible_values:
  met:
    text: met
    description: Subject satisfies the requirement.
    meaning: pbs:match_status_met
    alt_descriptions:
      de:
        source: de
        description: Erfuellt
    title: Met
  unmet:
    text: unmet
    description: Subject no longer satisfies the requirement.
    meaning: pbs:match_status_unmet
    alt_descriptions:
      de:
        source: de
        description: Nicht erfuellt
    title: Unmet
  unknown:
    text: unknown
    description: Match could not be determined.
    meaning: pbs:match_status_unknown
    alt_descriptions:
      de:
        source: de
        description: Unbekannt
    title: Unknown

```
</details>

</div>