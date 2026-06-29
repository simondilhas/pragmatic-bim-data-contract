---
search:
  boost: 2.0
---


# Enum: PersonalDataProcessingState 




_Privacy handling state for personal data on a Person record, orthogonal to workflow QA status._



<div data-search-exclude markdown="1">

URI: [pbs:PersonalDataProcessingState](https://schema.pragmaticbim.ch/PersonalDataProcessingState)

**Enum URI:** [pbs:PersonalDataProcessingState](https://schema.pragmaticbim.ch/PersonalDataProcessingState)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| active | pbs:personal_data_processing_state_active | Identifiable personal data is present and actively processed. | Title: Active<br>|
| redacted | pbs:personal_data_processing_state_redacted | Identifying values removed or replaced; record kept for referential integrity. | Title: Redacted<br>|
| pseudonymized | pbs:personal_data_processing_state_pseudonymized | Only indirect identifiers remain, such as a role label without direct contact details. | Title: Pseudonymized<br>|
| anonymized | pbs:personal_data_processing_state_anonymized | Data is no longer relatable to an identifiable individual. | Title: Anonymized<br>|
| erasure_pending | pbs:personal_data_processing_state_erasure_pending | Erasure requested; personal data scheduled for removal after a grace period. | Title: Erasure pending<br>|
| erased | pbs:personal_data_processing_state_erased | Personal data removed; a minimal stub may remain for referential integrity. | Title: Erased<br>|




## Slots

| Name | Description |
| ---  | --- |
| [personal_data_processing_state](personal_data_processing_state.md) | Privacy handling state for personal data on this person, orthogonal to workflow QA status. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: PersonalDataProcessingState
description: Privacy handling state for personal data on a Person record, orthogonal
  to workflow QA status.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:PersonalDataProcessingState
permissible_values:
  active:
    text: active
    description: Identifiable personal data is present and actively processed.
    meaning: pbs:personal_data_processing_state_active
    alt_descriptions:
      de:
        source: de
        description: Aktiv
    title: Active
  redacted:
    text: redacted
    description: Identifying values removed or replaced; record kept for referential
      integrity.
    meaning: pbs:personal_data_processing_state_redacted
    alt_descriptions:
      de:
        source: de
        description: Redigiert
    title: Redacted
  pseudonymized:
    text: pseudonymized
    description: Only indirect identifiers remain, such as a role label without direct
      contact details.
    meaning: pbs:personal_data_processing_state_pseudonymized
    alt_descriptions:
      de:
        source: de
        description: Pseudonymisiert
    title: Pseudonymized
  anonymized:
    text: anonymized
    description: Data is no longer relatable to an identifiable individual.
    meaning: pbs:personal_data_processing_state_anonymized
    alt_descriptions:
      de:
        source: de
        description: Anonymisiert
    title: Anonymized
  erasure_pending:
    text: erasure_pending
    description: Erasure requested; personal data scheduled for removal after a grace
      period.
    meaning: pbs:personal_data_processing_state_erasure_pending
    alt_descriptions:
      de:
        source: de
        description: Löschung ausstehend
    title: Erasure pending
  erased:
    text: erased
    description: Personal data removed; a minimal stub may remain for referential
      integrity.
    meaning: pbs:personal_data_processing_state_erased
    alt_descriptions:
      de:
        source: de
        description: Gelöscht
    title: Erased

```
</details>

</div>