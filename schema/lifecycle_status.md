---
search:
  boost: 5.0
---

# Slot: lifecycle_status 


_Whether the person is active, retired, or deceased. Orthogonal to privacy processing state and workflow QA status._



<div data-search-exclude markdown="1">



URI: [pbs:lifecycle_status](https://schema.pragmaticbim.ch/lifecycle_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonLifecycleStatus](PersonLifecycleStatus.md) |
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
| self | pbs:lifecycle_status |
| native | pbs:lifecycle_status |




## LinkML Source

<details>
```yaml
name: lifecycle_status
description: Whether the person is active, retired, or deceased. Orthogonal to privacy
  processing state and workflow QA status.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: PersonLifecycleStatus

```
</details></div>