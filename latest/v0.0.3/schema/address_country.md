

# Slot: address_country 


_Country name._





URI: [schema:addressCountry](https://schema.org/addressCountry)
Alias: address_country

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
| Slot URI | [schema:addressCountry](https://schema.org/addressCountry) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:addressCountry |
| native | pbs:address_country |




## LinkML Source

<details>
```yaml
name: address_country
description: Country name.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:addressCountry
alias: address_country
domain_of:
- PostalAddress
range: string

```
</details>