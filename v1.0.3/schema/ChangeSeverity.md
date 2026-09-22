---
search:
  boost: 2.0
---


# Enum: ChangeSeverity 




_Optional severity of a change independent of change type._



<div data-search-exclude markdown="1">

URI: [pbs:ChangeSeverity](https://schema.pragmaticbim.ch/ChangeSeverity)

**Enum URI:** [pbs:ChangeSeverity](https://schema.pragmaticbim.ch/ChangeSeverity)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| unchanged | pbs:change_severity_unchanged | No material difference (typically omitted from persisted Change records). | Title: Unchanged<br>|
| minor | pbs:change_severity_minor | Small attribute, metadata, or wording adjustment. | Title: Minor<br>|
| major | pbs:change_severity_major | Significant attribute, geometry, relationship, or structural content change. | Title: Major<br>|
| rewritten | pbs:change_severity_rewritten | Subject substantially replaced while retaining the same identity. | Title: Rewritten<br>|




## Slots

| Name | Description |
| ---  | --- |
| [change_severity](change_severity.md) | Optional severity independent of change type. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ChangeSeverity
description: Optional severity of a change independent of change type.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ChangeSeverity
permissible_values:
  unchanged:
    text: unchanged
    description: No material difference (typically omitted from persisted Change records).
    meaning: pbs:change_severity_unchanged
    alt_descriptions:
      de:
        source: de
        description: Unveraendert
    title: Unchanged
  minor:
    text: minor
    description: Small attribute, metadata, or wording adjustment.
    meaning: pbs:change_severity_minor
    alt_descriptions:
      de:
        source: de
        description: Geringfuegig
    title: Minor
  major:
    text: major
    description: Significant attribute, geometry, relationship, or structural content
      change.
    meaning: pbs:change_severity_major
    alt_descriptions:
      de:
        source: de
        description: Erheblich
    title: Major
  rewritten:
    text: rewritten
    description: Subject substantially replaced while retaining the same identity.
    meaning: pbs:change_severity_rewritten
    alt_descriptions:
      de:
        source: de
        description: Neu geschrieben
    title: Rewritten

```
</details>

</div>