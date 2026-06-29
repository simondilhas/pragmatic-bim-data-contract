

# Slot: classification_code 


_Classification code inside the scheme._





URI: [pbs:classification_code](https://example.org/pragmatic-bim-data-contract/classification_code)
Alias: classification_code

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
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:classification_code |
| native | pbs:classification_code |




## LinkML Source

<details>
```yaml
name: classification_code
description: Classification code inside the scheme.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_code
domain_of:
- Classification
range: string
required: true

```
</details>