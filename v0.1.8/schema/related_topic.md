---
search:
  boost: 3.0
---

# Slot: related_topic 


_Topic of interest. classification_scheme must be AbstractTopicClassification; classification_uri references the SKOS topic concept._

__



<div data-search-exclude markdown="1">



URI: [pbs:related_topic](https://schema.pragmaticbim.ch/related_topic)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  no  |






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
| self | pbs:related_topic |
| native | pbs:related_topic |




## LinkML Source

<details>
```yaml
name: related_topic
description: 'Topic of interest. classification_scheme must be AbstractTopicClassification;
  classification_uri references the SKOS topic concept.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: Classification
inlined: true

```
</details></div>