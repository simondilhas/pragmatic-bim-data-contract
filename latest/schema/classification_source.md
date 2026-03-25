

# Slot: classification_source 


_Source authority or dataset for this classification._





URI: [pbs:classification_source](https://example.org/pragmatic-bim-data-contract/classification_source)
Alias: classification_source

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
| self | pbs:classification_source |
| native | pbs:classification_source |




## LinkML Source

<details>
```yaml
name: classification_source
description: Source authority or dataset for this classification.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_source
domain_of:
- Classification
range: string

```
</details>