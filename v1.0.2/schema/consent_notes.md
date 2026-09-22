---
search:
  boost: 3.0
---

# Slot: consent_notes 


_Optional notes about how or where consent was captured._



<div data-search-exclude markdown="1">



URI: [pbs:consent_notes](https://schema.pragmaticbim.ch/consent_notes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ConsentRecord](ConsentRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:consent_notes |
| native | pbs:consent_notes |




## LinkML Source

<details>
```yaml
name: consent_notes
description: Optional notes about how or where consent was captured.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConsentRecord
range: string

```
</details></div>