

# Slot: address_region 


_Region, state, canton, or province._





URI: [schema:addressRegion](https://schema.org/addressRegion)
Alias: address_region

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
| Slot URI | [schema:addressRegion](https://schema.org/addressRegion) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:addressRegion |
| native | pbs:address_region |




## LinkML Source

<details>
```yaml
name: address_region
description: Region, state, canton, or province.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: schema:addressRegion
alias: address_region
domain_of:
- PostalAddress
range: string

```
</details>