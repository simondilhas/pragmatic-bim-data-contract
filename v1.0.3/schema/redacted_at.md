---
search:
  boost: 5.0
---

# Slot: redacted_at 


_Timestamp when identifying personal data was redacted on this record._



<div data-search-exclude markdown="1">



URI: [pbs:redacted_at](https://schema.pragmaticbim.ch/redacted_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:redacted_at |
| native | pbs:redacted_at |




## LinkML Source

<details>
```yaml
name: redacted_at
description: Timestamp when identifying personal data was redacted on this record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: datetime

```
</details></div>