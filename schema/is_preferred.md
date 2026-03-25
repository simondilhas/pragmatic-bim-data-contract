

# Slot: is_preferred 


_Indicates whether this is the preferred contact point._





URI: [pbs:is_preferred](https://example.org/pragmatic-bim-data-contract/is_preferred)
Alias: is_preferred

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
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
| self | pbs:is_preferred |
| native | pbs:is_preferred |




## LinkML Source

<details>
```yaml
name: is_preferred
description: Indicates whether this is the preferred contact point.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: is_preferred
domain_of:
- ContactPoint
range: boolean

```
</details>