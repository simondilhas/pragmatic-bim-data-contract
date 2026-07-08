

# Slot: classification_label 


_Optional human-readable classification label._





URI: [pbs:classification_label](https://example.org/pragmatic-bim-data-contract/classification_label)
Alias: classification_label

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
| self | pbs:classification_label |
| native | pbs:classification_label |




## LinkML Source

<details>
```yaml
name: classification_label
description: Optional human-readable classification label.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_label
domain_of:
- Classification
range: string

```
</details>