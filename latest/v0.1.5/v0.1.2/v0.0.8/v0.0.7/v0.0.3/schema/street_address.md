

# Slot: street_address 


_Street name and house number or equivalent address line._





URI: [schema:streetAddress](https://schema.org/streetAddress)
Alias: street_address

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PostalAddress](PostalAddress.md) | Structured postal or physical address for an agent |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PostalAddress](PostalAddress.md) |
| Slot URI | [schema:streetAddress](https://schema.org/streetAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:streetAddress |
| native | pbs:street_address |




## LinkML Source

<details>
```yaml
name: street_address
description: Street name and house number or equivalent address line.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:streetAddress
alias: street_address
domain_of:
- PostalAddress
range: string

```
</details>