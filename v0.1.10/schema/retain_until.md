---
search:
  boost: 5.0
---

# Slot: retain_until 


_Storage-limit deadline after which personal data should be deleted or redacted._



<div data-search-exclude markdown="1">



URI: [pbs:retain_until](https://schema.pragmaticbim.ch/retain_until)
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
| self | pbs:retain_until |
| native | pbs:retain_until |




## LinkML Source

<details>
```yaml
name: retain_until
description: Storage-limit deadline after which personal data should be deleted or
  redacted.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: datetime

```
</details></div>