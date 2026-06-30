

# Slot: address_country_code 


_Optional ISO 3166-1 alpha-2 or alpha-3 country code._





URI: [pbs:address_country_code](https://example.org/pragmatic-bim-data-contract/address_country_code)
Alias: address_country_code

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

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:address_country_code |
| native | pbs:address_country_code |




## LinkML Source

<details>
```yaml
name: address_country_code
description: Optional ISO 3166-1 alpha-2 or alpha-3 country code.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: address_country_code
domain_of:
- PostalAddress
range: string

```
</details>