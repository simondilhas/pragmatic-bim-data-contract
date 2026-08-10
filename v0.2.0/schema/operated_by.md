---
search:
  boost: 5.0
---

# Slot: operated_by 


_Organization accountable for this software agent._



<div data-search-exclude markdown="1">



URI: [pbs:operated_by](https://schema.pragmaticbim.ch/operated_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoftwareAgent](SoftwareAgent.md) | Automated actor (integration, bot, or pipeline) acting in workflow roles. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
| Domain Of | [SoftwareAgent](SoftwareAgent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:operated_by |
| native | pbs:operated_by |




## LinkML Source

<details>
```yaml
name: operated_by
description: Organization accountable for this software agent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SoftwareAgent
range: Company
inlined: false

```
</details></div>