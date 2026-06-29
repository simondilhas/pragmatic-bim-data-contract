---
search:
  boost: 3.0
---

# Slot: granted_at 


_Timestamp when consent was given. Required when lawful_basis is consent._



<div data-search-exclude markdown="1">



URI: [pbs:granted_at](https://schema.pragmaticbim.ch/granted_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:granted_at |
| native | pbs:granted_at |




## LinkML Source

<details>
```yaml
name: granted_at
description: Timestamp when consent was given. Required when lawful_basis is consent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConsentRecord
range: datetime

```
</details></div>