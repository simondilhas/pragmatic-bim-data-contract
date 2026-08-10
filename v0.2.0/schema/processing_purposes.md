---
search:
  boost: 5.0
---

# Slot: processing_purposes 


_High-level purposes for processing personal data (for example project coordination, contract administration)._



<div data-search-exclude markdown="1">



URI: [pbs:processing_purposes](https://schema.pragmaticbim.ch/processing_purposes)
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
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:processing_purposes |
| native | pbs:processing_purposes |




## LinkML Source

<details>
```yaml
name: processing_purposes
description: High-level purposes for processing personal data (for example project
  coordination, contract administration).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: string
multivalued: true

```
</details></div>