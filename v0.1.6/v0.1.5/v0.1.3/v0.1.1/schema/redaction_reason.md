---
search:
  boost: 5.0
---

# Slot: redaction_reason 


_Reason for redaction (for example external model export, erasure request, retention expired)._



<div data-search-exclude markdown="1">



URI: [pbs:redaction_reason](https://schema.pragmaticbim.ch/redaction_reason)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:redaction_reason |
| native | pbs:redaction_reason |




## LinkML Source

<details>
```yaml
name: redaction_reason
description: Reason for redaction (for example external model export, erasure request,
  retention expired).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: string

```
</details></div>