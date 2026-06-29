---
search:
  boost: 3.0
---

# Slot: lawful_basis 


_Lawful basis for processing the scoped personal data categories._



<div data-search-exclude markdown="1">



URI: [pbs:lawful_basis](https://schema.pragmaticbim.ch/lawful_basis)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LawfulBasis](LawfulBasis.md) |
| Domain Of | [ConsentRecord](ConsentRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:lawful_basis |
| native | pbs:lawful_basis |




## LinkML Source

<details>
```yaml
name: lawful_basis
description: Lawful basis for processing the scoped personal data categories.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConsentRecord
range: LawfulBasis
required: true

```
</details></div>