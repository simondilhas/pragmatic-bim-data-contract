---
search:
  boost: 3.0
---

# Slot: processing_purpose 


_Human-readable purpose for which the personal data categories are processed._



<div data-search-exclude markdown="1">



URI: [pbs:processing_purpose](https://schema.pragmaticbim.ch/processing_purpose)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:processing_purpose |
| native | pbs:processing_purpose |




## LinkML Source

<details>
```yaml
name: processing_purpose
description: Human-readable purpose for which the personal data categories are processed.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConsentRecord
range: string
required: true

```
</details></div>