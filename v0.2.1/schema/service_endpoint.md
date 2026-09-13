---
search:
  boost: 5.0
---

# Slot: service_endpoint 


_Optional URI of the running service or integration endpoint._



<div data-search-exclude markdown="1">



URI: [pbs:service_endpoint](https://schema.pragmaticbim.ch/service_endpoint)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoftwareAgent](SoftwareAgent.md) | Automated actor (integration, bot, or pipeline) acting in workflow roles. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:service_endpoint |
| native | pbs:service_endpoint |




## LinkML Source

<details>
```yaml
name: service_endpoint
description: Optional URI of the running service or integration endpoint.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SoftwareAgent
range: uriorcurie

```
</details></div>