---
search:
  boost: 5.0
---

# Slot: person_relationships 


_Typed social, professional, commercial, and interest relationships to other agents or topic concepts. May be populated manually or extracted from CRM stories via LLM; use relationship_source for provenance (for example a Message id). May constitute personal data; governed by personal_data_processing_state, consent_records, retain_until, and related privacy slots on this Person._

__



<div data-search-exclude markdown="1">



URI: [pbs:person_relationships](https://schema.pragmaticbim.ch/person_relationships)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonRelationship](PersonRelationship.md) |
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
| self | pbs:person_relationships |
| native | pbs:person_relationships |




## LinkML Source

<details>
```yaml
name: person_relationships
description: 'Typed social, professional, commercial, and interest relationships to
  other agents or topic concepts. May be populated manually or extracted from CRM
  stories via LLM; use relationship_source for provenance (for example a Message id).
  May constitute personal data; governed by personal_data_processing_state, consent_records,
  retain_until, and related privacy slots on this Person.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: PersonRelationship
multivalued: true
inlined: true

```
</details></div>