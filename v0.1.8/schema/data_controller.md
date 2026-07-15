---
search:
  boost: 5.0
---

# Slot: data_controller 


_Organization accountable as data controller for this person record._



<div data-search-exclude markdown="1">



URI: [pbs:data_controller](https://schema.pragmaticbim.ch/data_controller)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
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
| self | pbs:data_controller |
| native | pbs:data_controller |




## LinkML Source

<details>
```yaml
name: data_controller
description: Organization accountable as data controller for this person record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: Company
inlined: false

```
</details></div>