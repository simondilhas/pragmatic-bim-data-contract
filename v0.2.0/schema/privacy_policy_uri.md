---
search:
  boost: 5.0
---

# Slot: privacy_policy_uri 


_URI of the current or default privacy policy or notice applicable to this person record._



<div data-search-exclude markdown="1">



URI: [pbs:privacy_policy_uri](https://schema.pragmaticbim.ch/privacy_policy_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Person](Person.md), [ConsentRecord](ConsentRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:privacy_policy_uri |
| native | pbs:privacy_policy_uri |




## LinkML Source

<details>
```yaml
name: privacy_policy_uri
description: URI of the current or default privacy policy or notice applicable to
  this person record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
- ConsentRecord
range: uriorcurie

```
</details></div>