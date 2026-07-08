---
search:
  boost: 3.0
---

# Slot: related_person 


_Target person for social and professional predicates such as knows, was_colleague_of, reports_to, or has_key_account_manager._



<div data-search-exclude markdown="1">



URI: [pbs:related_person](https://schema.pragmaticbim.ch/related_person)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [PersonRelationship](PersonRelationship.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_person |
| native | pbs:related_person |




## LinkML Source

<details>
```yaml
name: related_person
description: Target person for social and professional predicates such as knows, was_colleague_of,
  reports_to, or has_key_account_manager.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: Person
inlined: false

```
</details></div>