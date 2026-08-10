---
search:
  boost: 3.0
---

# Slot: valid_to 


_Optional end of the relationship period (for example employment end for worked_at)._



<div data-search-exclude markdown="1">



URI: [pbs:valid_to](https://schema.pragmaticbim.ch/valid_to)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:valid_to |
| native | pbs:valid_to |




## LinkML Source

<details>
```yaml
name: valid_to
description: Optional end of the relationship period (for example employment end for
  worked_at).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: datetime

```
</details></div>