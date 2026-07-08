

# Slot: quantity_type 


_Controlled quantity type._





URI: [pbs:quantity_type](https://example.org/pragmatic-bim-data-contract/quantity_type)
Alias: quantity_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuantityType](QuantityType.md) |
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
| self | pbs:quantity_type |
| native | pbs:quantity_type |




## LinkML Source

<details>
```yaml
name: quantity_type
description: Controlled quantity type.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: quantity_type
domain_of:
- QuantityValue
range: QuantityType
required: true

```
</details>