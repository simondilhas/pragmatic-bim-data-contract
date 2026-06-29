---
search:
  boost: 2.0
---


# Enum: ChangeKind 




_Severity or category of change detected between two revisions._



<div data-search-exclude markdown="1">

URI: [pbs:ChangeKind](https://schema.pragmaticbim.ch/ChangeKind)

**Enum URI:** [pbs:ChangeKind](https://schema.pragmaticbim.ch/ChangeKind)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| unchanged | pbs:change_kind_unchanged | No material difference (typically omitted from persisted Change records) |
| minor | pbs:change_kind_minor | Small attribute, metadata, or wording adjustment |
| major | pbs:change_kind_major | Significant attribute, geometry, relationship, or structural content change |
| rewritten | pbs:change_kind_rewritten | Subject substantially replaced while retaining the same identity |
| new | pbs:change_kind_new | Subject introduced in to_revision (absent in from_revision) |
| deleted | pbs:change_kind_deleted | Subject removed in to_revision (present in from_revision) |




## Slots

| Name | Description |
| ---  | --- |
| [change_kind](change_kind.md) | Severity or category of change detected between two revisions |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ChangeKind
description: Severity or category of change detected between two revisions.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ChangeKind
permissible_values:
  unchanged:
    text: unchanged
    description: No material difference (typically omitted from persisted Change records).
    meaning: pbs:change_kind_unchanged
  minor:
    text: minor
    description: Small attribute, metadata, or wording adjustment.
    meaning: pbs:change_kind_minor
  major:
    text: major
    description: Significant attribute, geometry, relationship, or structural content
      change.
    meaning: pbs:change_kind_major
  rewritten:
    text: rewritten
    description: Subject substantially replaced while retaining the same identity.
    meaning: pbs:change_kind_rewritten
  new:
    text: new
    description: Subject introduced in to_revision (absent in from_revision).
    meaning: pbs:change_kind_new
  deleted:
    text: deleted
    description: Subject removed in to_revision (present in from_revision).
    meaning: pbs:change_kind_deleted

```
</details>

</div>