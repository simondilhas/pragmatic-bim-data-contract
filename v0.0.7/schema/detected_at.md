---
search:
  boost: 5.0
---

# Slot: detected_at 


_Timestamp when this change was detected._



<div data-search-exclude markdown="1">



URI: [dcterms:created](http://purl.org/dc/terms/created)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Change](Change.md) |
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:created |
| native | pbs:detected_at |




## LinkML Source

<details>
```yaml
name: detected_at
description: Timestamp when this change was detected.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:created
domain_of:
- Change
range: datetime

```
</details></div>