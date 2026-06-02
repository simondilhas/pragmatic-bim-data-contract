---
search:
  boost: 5.0
---

# Slot: document_storage_link 


_Document location when the subject is a yamlDocument entity or document field diff._



<div data-search-exclude markdown="1">



URI: [pbs:document_storage_link](https://schema.pragmaticbim.ch/document_storage_link)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Audit record observing the project graph moving between revisions. Not an Entity and not a graph node — it watches the graph. Use change_type together with the concrete subclass for interpretation. |  no  |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  no  |
| [GeometryChange](GeometryChange.md) | Geometry or representation change for a subject. |  no  |
| [RequirementChange](RequirementChange.md) | Change to a requirement entity or its fields. |  no  |
| [MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |  no  |
| [AdditionChange](AdditionChange.md) | New entity introduced in to_revision. |  no  |
| [DeletionChange](DeletionChange.md) | Entity removed in to_revision. |  no  |






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
description: Document location when the subject is a yamlDocument entity or document
  field diff.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: uriorcurie

```
</details></div>