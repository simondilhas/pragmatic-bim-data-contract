---
search:
  boost: 2.0
---


# Enum: RequirementTargetOperator 




_Comparison operator for numeric or textual requirement targets._



<div data-search-exclude markdown="1">

URI: [pbs:RequirementTargetOperator](https://schema.pragmaticbim.ch/RequirementTargetOperator)

**Enum URI:** [pbs:RequirementTargetOperator](https://schema.pragmaticbim.ch/RequirementTargetOperator)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| equals | pbs:requirement_target_operator_equals |  | Title: Equals<br>|
| minimum | pbs:requirement_target_operator_minimum |  | Title: Minimum<br>|
| maximum | pbs:requirement_target_operator_maximum |  | Title: Maximum<br>|
| range | pbs:requirement_target_operator_range |  | Title: Range<br>|




## Slots

| Name | Description |
| ---  | --- |
| [target_operator](target_operator.md) | Comparison operator for the requirement target. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: RequirementTargetOperator
description: Comparison operator for numeric or textual requirement targets.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:RequirementTargetOperator
permissible_values:
  equals:
    text: equals
    meaning: pbs:requirement_target_operator_equals
    alt_descriptions:
      de:
        source: de
        description: Gleich
    title: Equals
  minimum:
    text: minimum
    meaning: pbs:requirement_target_operator_minimum
    alt_descriptions:
      de:
        source: de
        description: Minimum
    title: Minimum
  maximum:
    text: maximum
    meaning: pbs:requirement_target_operator_maximum
    alt_descriptions:
      de:
        source: de
        description: Maximum
    title: Maximum
  range:
    text: range
    meaning: pbs:requirement_target_operator_range
    alt_descriptions:
      de:
        source: de
        description: Bereich
    title: Range

```
</details>

</div>