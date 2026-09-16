---
search:
  boost: 3.0
---

# Slot: relationship_type 


_Relationship predicate. classification_scheme must be AbstractPersonRelationshipType; classification_code and classification_uri reference the SKOS concept._

__



<div data-search-exclude markdown="1">



URI: [pbs:relationship_type](https://schema.pragmaticbim.ch/relationship_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Classification](Classification.md) |
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
| self | pbs:relationship_type |
| native | pbs:relationship_type |




## LinkML Source

<details>
```yaml
name: relationship_type
description: 'Relationship predicate. classification_scheme must be AbstractPersonRelationshipType;
  classification_code and classification_uri reference the SKOS concept.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: Classification
inlined: true

```
</details></div>