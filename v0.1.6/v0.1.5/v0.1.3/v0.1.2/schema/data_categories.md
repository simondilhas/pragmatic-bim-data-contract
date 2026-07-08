---
search:
  boost: 3.0
---

# Slot: data_categories 


_Personal data categories covered by this consent or processing record._



<div data-search-exclude markdown="1">



URI: [pbs:data_categories](https://schema.pragmaticbim.ch/data_categories)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonalDataCategory](PersonalDataCategory.md) |
| Domain Of | [ConsentRecord](ConsentRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:data_categories |
| native | pbs:data_categories |




## LinkML Source

<details>
```yaml
name: data_categories
description: Personal data categories covered by this consent or processing record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConsentRecord
range: PersonalDataCategory
required: true
multivalued: true

```
</details></div>