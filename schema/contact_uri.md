

# Slot: contact_uri 


_URI for the contact endpoint or profile where applicable._





URI: [pbs:contact_uri](https://example.org/pragmatic-bim-data-contract/contact_uri)
Alias: contact_uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:contact_uri |
| native | pbs:contact_uri |




## LinkML Source

<details>
```yaml
name: contact_uri
description: URI for the contact endpoint or profile where applicable.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: contact_uri
domain_of:
- ContactPoint
range: uriorcurie

```
</details>