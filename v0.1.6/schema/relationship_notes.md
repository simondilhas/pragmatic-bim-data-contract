---
search:
  boost: 3.0
---

# Slot: relationship_notes 


_Optional free-text context for this relationship record._



<div data-search-exclude markdown="1">



URI: [pbs:relationship_notes](https://schema.pragmaticbim.ch/relationship_notes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:relationship_notes |
| native | pbs:relationship_notes |




## LinkML Source

<details>
```yaml
name: relationship_notes
description: Optional free-text context for this relationship record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: string

```
</details></div>