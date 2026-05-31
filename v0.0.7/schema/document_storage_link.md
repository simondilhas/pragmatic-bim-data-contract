---
search:
  boost: 5.0
---

# Slot: document_storage_link 


_Document location when the subject is or embeds a Document._



<div data-search-exclude markdown="1">



URI: [pbs:document_storage_link](https://schema.pragmaticbim.ch/document_storage_link)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Change](Change.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:document_storage_link |
| native | pbs:document_storage_link |




## LinkML Source

<details>
```yaml
name: document_storage_link
description: Document location when the subject is or embeds a Document.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: uriorcurie

```
</details></div>