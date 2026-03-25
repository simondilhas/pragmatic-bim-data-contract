

# Slot: classification_scheme 


_Name of the classification scheme (for example ifc, uniclass, omniclass, custom)._





URI: [pbs:classification_scheme](https://example.org/pragmatic-bim-data-contract/classification_scheme)
Alias: classification_scheme

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
| self | pbs:classification_scheme |
| native | pbs:classification_scheme |




## LinkML Source

<details>
```yaml
name: classification_scheme
description: Name of the classification scheme (for example ifc, uniclass, omniclass,
  custom).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: classification_scheme
domain_of:
- Classification
range: string
required: true

```
</details>