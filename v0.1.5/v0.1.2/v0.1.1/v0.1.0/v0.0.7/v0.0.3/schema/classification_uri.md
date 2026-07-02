

# Slot: classification_uri 


_Optional URI/CURIE that identifies the classification concept in an external registry._





URI: [pbs:classification_uri](https://example.org/pragmatic-bim-data-contract/classification_uri)
Alias: classification_uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Classification](Classification.md) | Generic classification entry from any scheme (for example IFC, Uniclass, Omni... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Classification](Classification.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:classification_uri |
| native | pbs:classification_uri |




## LinkML Source

<details>
```yaml
name: classification_uri
description: Optional URI/CURIE that identifies the classification concept in an external
  registry.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_uri
domain_of:
- Classification
range: uriorcurie

```
</details>