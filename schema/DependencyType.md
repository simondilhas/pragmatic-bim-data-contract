---
search:
  boost: 2.0
---


# Enum: DependencyType 




_Precedence logic between two time records (FS finish-to-start, SS start-to-start, FF finish-to-finish, SF start-to-finish)._



<div data-search-exclude markdown="1">

URI: [pbs:DependencyType](https://schema.pragmaticbim.ch/DependencyType)

**Enum URI:** [pbs:DependencyType](https://schema.pragmaticbim.ch/DependencyType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| FS | pbs:dependency_type_finish_to_start | Successor starts when the predecessor finishes. | Title: Finish to Start<br>|
| SS | pbs:dependency_type_start_to_start | Successor starts when the predecessor starts. | Title: Start to Start<br>|
| FF | pbs:dependency_type_finish_to_finish | Successor finishes when the predecessor finishes. | Title: Finish to Finish<br>|
| SF | pbs:dependency_type_start_to_finish | Successor finishes when the predecessor starts. | Title: Start to Finish<br>|




## Slots

| Name | Description |
| ---  | --- |
| [dependency_type](dependency_type.md) | FS | SS | FF | SF |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: DependencyType
description: Precedence logic between two time records (FS finish-to-start, SS start-to-start,
  FF finish-to-finish, SF start-to-finish).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:DependencyType
permissible_values:
  FS:
    text: FS
    description: Successor starts when the predecessor finishes.
    meaning: pbs:dependency_type_finish_to_start
    alt_descriptions:
      de:
        source: de
        description: Ende zu Start
    title: Finish to Start
  SS:
    text: SS
    description: Successor starts when the predecessor starts.
    meaning: pbs:dependency_type_start_to_start
    alt_descriptions:
      de:
        source: de
        description: Start zu Start
    title: Start to Start
  FF:
    text: FF
    description: Successor finishes when the predecessor finishes.
    meaning: pbs:dependency_type_finish_to_finish
    alt_descriptions:
      de:
        source: de
        description: Ende zu Ende
    title: Finish to Finish
  SF:
    text: SF
    description: Successor finishes when the predecessor starts.
    meaning: pbs:dependency_type_start_to_finish
    alt_descriptions:
      de:
        source: de
        description: Start zu Ende
    title: Start to Finish

```
</details>

</div>