

# Slot: address_locality 


_Locality, city, or town._





URI: [schema:addressLocality](https://schema.org/addressLocality)
Alias: address_locality

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
| Slot URI | [schema:addressLocality](https://schema.org/addressLocality) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:addressLocality |
| native | pbs:address_locality |




## LinkML Source

<details>
```yaml
name: address_locality
description: Locality, city, or town.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:addressLocality
alias: address_locality
domain_of:
- PostalAddress
range: string

```
</details>