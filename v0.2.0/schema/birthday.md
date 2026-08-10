---
search:
  boost: 5.0
---

# Slot: birthday 


_Date of birth. Personal data; governed by personal_data_processing_state, consent_records, and retain_until._



<div data-search-exclude markdown="1">



URI: [schema:birthDate](https://schema.org/birthDate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [schema:birthDate](https://schema.org/birthDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:birthDate |
| native | pbs:birthday |




## LinkML Source

<details>
```yaml
name: birthday
description: Date of birth. Personal data; governed by personal_data_processing_state,
  consent_records, and retain_until.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:birthDate
domain_of:
- Person
range: date

```
</details></div>