---
search:
  boost: 5.0
---

# Slot: effective_until 


_End of contractual validity when applicable._



<div data-search-exclude markdown="1">



URI: [pbs:effective_until](https://schema.pragmaticbim.ch/effective_until)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Contract](Contract.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:effective_until |
| native | pbs:effective_until |




## LinkML Source

<details>
```yaml
name: effective_until
description: End of contractual validity when applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Contract
range: datetime

```
</details></div>