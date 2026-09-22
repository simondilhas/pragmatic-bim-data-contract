---
search:
  boost: 5.0
---

# Slot: software_version 


_Optional deployed version label for the software agent._



<div data-search-exclude markdown="1">



URI: [pbs:software_version](https://schema.pragmaticbim.ch/software_version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoftwareAgent](SoftwareAgent.md) | Automated actor (integration, bot, or pipeline) acting in workflow roles. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:software_version |
| native | pbs:software_version |




## LinkML Source

<details>
```yaml
name: software_version
description: Optional deployed version label for the software agent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SoftwareAgent
range: string

```
</details></div>