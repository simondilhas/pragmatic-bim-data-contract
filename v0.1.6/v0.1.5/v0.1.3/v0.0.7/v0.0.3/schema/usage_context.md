

# Slot: usage_context 


_Optional usage context such as work, personal, support, billing, or emergency._





URI: [pbs:usage_context](https://example.org/pragmatic-bim-data-contract/usage_context)
Alias: usage_context

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
| self | pbs:usage_context |
| native | pbs:usage_context |




## LinkML Source

<details>
```yaml
name: usage_context
description: Optional usage context such as work, personal, support, billing, or emergency.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: usage_context
domain_of:
- ContactPoint
range: string

```
</details>