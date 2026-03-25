

# Slot: contact_channel_type 


_Communication channel type such as email, phone, website, linkedin, whatsapp, signal, slack, teams, or telegram._





URI: [pbs:contact_channel_type](https://example.org/pragmatic-bim-data-contract/contact_channel_type)
Alias: contact_channel_type

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
| self | pbs:contact_channel_type |
| native | pbs:contact_channel_type |




## LinkML Source

<details>
```yaml
name: contact_channel_type
description: Communication channel type such as email, phone, website, linkedin, whatsapp,
  signal, slack, teams, or telegram.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: contact_channel_type
domain_of:
- ContactPoint
range: string

```
</details>