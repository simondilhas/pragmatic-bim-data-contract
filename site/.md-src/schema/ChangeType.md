---
search:
  boost: 2.0
---


# Enum: ChangeType 




_Category of change detected between two revisions._



<div data-search-exclude markdown="1">

URI: [pbs:ChangeType](https://schema.pragmaticbim.ch/ChangeType)

**Enum URI:** [pbs:ChangeType](https://schema.pragmaticbim.ch/ChangeType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| geometry_change | pbs:change_type_geometry_change | Geometry or representation changed. | Title: Geometry Change<br>|
| property_change | pbs:change_type_property_change | Attribute, PropertySet, or schema slot changed. | Title: Property Change<br>|
| requirement_change | pbs:change_type_requirement_change | Requirement record or field changed. | Title: Requirement Change<br>|
| match_change | pbs:change_type_match_change | Entity match status against a requirement changed (met / unmet). | Title: Match Change<br>|
| addition | pbs:change_type_addition | New entity or requirement introduced. | Title: Addition<br>|
| deletion | pbs:change_type_deletion | Entity or requirement removed. | Title: Deletion<br>|




## Slots

| Name | Description |
| ---  | --- |
| [change_type](change_type.md) | Category of change detected between two revisions. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ChangeType
description: Category of change detected between two revisions.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ChangeType
permissible_values:
  geometry_change:
    text: geometry_change
    description: Geometry or representation changed.
    meaning: pbs:change_type_geometry_change
    alt_descriptions:
      de:
        source: de
        description: Geometrieaenderung
    title: Geometry Change
  property_change:
    text: property_change
    description: Attribute, PropertySet, or schema slot changed.
    meaning: pbs:change_type_property_change
    alt_descriptions:
      de:
        source: de
        description: Eigenschaftsaenderung
    title: Property Change
  requirement_change:
    text: requirement_change
    description: Requirement record or field changed.
    meaning: pbs:change_type_requirement_change
    alt_descriptions:
      de:
        source: de
        description: Anforderungsaenderung
    title: Requirement Change
  match_change:
    text: match_change
    description: Entity match status against a requirement changed (met / unmet).
    meaning: pbs:change_type_match_change
    alt_descriptions:
      de:
        source: de
        description: Erfuellungsaenderung
    title: Match Change
  addition:
    text: addition
    description: New entity or requirement introduced.
    meaning: pbs:change_type_addition
    alt_descriptions:
      de:
        source: de
        description: Hinzufuegung
    title: Addition
  deletion:
    text: deletion
    description: Entity or requirement removed.
    meaning: pbs:change_type_deletion
    alt_descriptions:
      de:
        source: de
        description: Loeschung
    title: Deletion

```
</details>

</div>