---
search:
  boost: 2.0
---


# Enum: PersonLifecycleStatus 




_Life stage of a person in CRM context, orthogonal to privacy processing state and workflow QA status._



<div data-search-exclude markdown="1">

URI: [pbs:PersonLifecycleStatus](https://schema.pragmaticbim.ch/PersonLifecycleStatus)

**Enum URI:** [pbs:PersonLifecycleStatus](https://schema.pragmaticbim.ch/PersonLifecycleStatus)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| active | pbs:person_lifecycle_status_active | Person is living and considered active in CRM context. | Title: Active<br>|
| retired | pbs:person_lifecycle_status_retired | Person has retired from professional or public life. | Title: Retired<br>|
| deceased | pbs:person_lifecycle_status_deceased | Person has died. | Title: Deceased<br>|




## Slots

| Name | Description |
| ---  | --- |
| [lifecycle_status](lifecycle_status.md) | Whether the person is active, retired, or deceased. Orthogonal to privacy processing state and workflow QA status. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: PersonLifecycleStatus
description: Life stage of a person in CRM context, orthogonal to privacy processing
  state and workflow QA status.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:PersonLifecycleStatus
permissible_values:
  active:
    text: active
    description: Person is living and considered active in CRM context.
    meaning: pbs:person_lifecycle_status_active
    alt_descriptions:
      de:
        source: de
        description: Aktiv
    title: Active
  retired:
    text: retired
    description: Person has retired from professional or public life.
    meaning: pbs:person_lifecycle_status_retired
    alt_descriptions:
      de:
        source: de
        description: Im Ruhestand
    title: Retired
  deceased:
    text: deceased
    description: Person has died.
    meaning: pbs:person_lifecycle_status_deceased
    alt_descriptions:
      de:
        source: de
        description: Verstorben
    title: Deceased

```
</details>

</div>