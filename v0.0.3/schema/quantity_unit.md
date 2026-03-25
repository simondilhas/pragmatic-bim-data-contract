

# Slot: quantity_unit 


_Unit of the quantity value._





URI: [pbs:quantity_unit](https://example.org/pragmatic-bim-data-contract/quantity_unit)
Alias: quantity_unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [QuantityValue](QuantityValue.md) |

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
| self | pbs:quantity_unit |
| native | pbs:quantity_unit |




## LinkML Source

<details>
```yaml
name: quantity_unit
description: Unit of the quantity value.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: quantity_unit
domain_of:
- QuantityValue
range: string
required: true

```
</details>