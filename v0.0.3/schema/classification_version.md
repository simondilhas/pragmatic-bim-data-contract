

# Slot: classification_version 


_Optional scheme/version identifier._





URI: [pbs:classification_version](https://example.org/pragmatic-bim-data-contract/classification_version)
Alias: classification_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Classification](Classification.md) | Generic classification entry from any scheme (for example IFC, Uniclass, Omni... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:classification_version |
| native | pbs:classification_version |




## LinkML Source

<details>
```yaml
name: classification_version
description: Optional scheme/version identifier.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_version
domain_of:
- Classification
range: string

```
</details>