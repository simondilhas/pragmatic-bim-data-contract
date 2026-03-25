

# Slot: postal_code 


_Postal or ZIP code._





URI: [schema:postalCode](https://schema.org/postalCode)
Alias: postal_code

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
| Slot URI | [schema:postalCode](https://schema.org/postalCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:postalCode |
| native | pbs:postal_code |




## LinkML Source

<details>
```yaml
name: postal_code
description: Postal or ZIP code.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:postalCode
alias: postal_code
domain_of:
- PostalAddress
range: string

```
</details>