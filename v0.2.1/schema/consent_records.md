---
search:
  boost: 5.0
---

# Slot: consent_records 


_Audit trail of lawful basis and consent for processing personal data. When lawful_basis is consent and state is active, at least one non-withdrawn record should be present._

__



<div data-search-exclude markdown="1">



URI: [pbs:consent_records](https://schema.pragmaticbim.ch/consent_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConsentRecord](ConsentRecord.md) |
| Domain Of | [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:consent_records |
| native | pbs:consent_records |




## LinkML Source

<details>
```yaml
name: consent_records
description: 'Audit trail of lawful basis and consent for processing personal data.
  When lawful_basis is consent and state is active, at least one non-withdrawn record
  should be present.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: ConsentRecord
multivalued: true
inlined: true

```
</details></div>