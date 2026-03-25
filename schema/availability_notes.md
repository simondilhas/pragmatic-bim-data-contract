

# Slot: availability_notes 


_Optional notes about availability, office hours, or response expectations._





URI: [pbs:availability_notes](https://example.org/pragmatic-bim-data-contract/availability_notes)
Alias: availability_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContactPoint](ContactPoint.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:availability_notes |
| native | pbs:availability_notes |




## LinkML Source

<details>
```yaml
name: availability_notes
description: Optional notes about availability, office hours, or response expectations.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: availability_notes
domain_of:
- ContactPoint
range: string

```
</details>