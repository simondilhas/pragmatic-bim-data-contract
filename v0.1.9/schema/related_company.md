---
search:
  boost: 3.0
---

# Slot: related_company 


_Target organization for org and commercial predicates such as works_at, worked_at, is_key_account_manager_for, client_of, or vendor_of._



<div data-search-exclude markdown="1">



URI: [pbs:related_company](https://schema.pragmaticbim.ch/related_company)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonRelationship](PersonRelationship.md) | Typed link from a person to another agent or to a topic concept. The predicate is expressed as a Classification referencing AbstractPersonRelationshipType. Exactly one of related_person, related_company, or related_topic must be set; see the target-kind mapping for predicate-to-slot rules. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
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
| self | pbs:related_company |
| native | pbs:related_company |




## LinkML Source

<details>
```yaml
name: related_company
description: Target organization for org and commercial predicates such as works_at,
  worked_at, is_key_account_manager_for, client_of, or vendor_of.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PersonRelationship
range: Company
inlined: false

```
</details></div>