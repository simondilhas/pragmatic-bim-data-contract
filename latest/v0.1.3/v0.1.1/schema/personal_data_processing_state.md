---
search:
  boost: 5.0
---

# Slot: personal_data_processing_state 


_Privacy handling state for personal data on this person, orthogonal to workflow QA status._



<div data-search-exclude markdown="1">



URI: [pbs:personal_data_processing_state](https://schema.pragmaticbim.ch/personal_data_processing_state)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonalDataProcessingState](PersonalDataProcessingState.md) |
| Domain Of | [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:personal_data_processing_state |
| native | pbs:personal_data_processing_state |




## LinkML Source

<details>
```yaml
name: personal_data_processing_state
description: Privacy handling state for personal data on this person, orthogonal to
  workflow QA status.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: PersonalDataProcessingState

```
</details></div>