---
search:
  boost: 5.0
---

# Slot: client 


_Owning client organization._



<div data-search-exclude markdown="1">



URI: [pbs:client](https://schema.pragmaticbim.ch/client)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Project](Project.md) | Business delivery scope for spatial context, systems, and workflow entities. |  no  |
| [Program](Program.md) | Portfolio or capital program scope grouping related projects. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
| Domain Of | [Project](Project.md), [Program](Program.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:client |
| native | pbs:client |




## LinkML Source

<details>
```yaml
name: client
description: Owning client organization.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Project
- Program
range: Company
inlined: false

```
</details></div>