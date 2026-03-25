

# Slot: contact_value 


_Human-readable contact value such as an email address, phone number, handle, or username._





URI: [pbs:contact_value](https://example.org/pragmatic-bim-data-contract/contact_value)
Alias: contact_value

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
| self | pbs:contact_value |
| native | pbs:contact_value |




## LinkML Source

<details>
```yaml
name: contact_value
description: Human-readable contact value such as an email address, phone number,
  handle, or username.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: contact_value
domain_of:
- ContactPoint
range: string

```
</details>