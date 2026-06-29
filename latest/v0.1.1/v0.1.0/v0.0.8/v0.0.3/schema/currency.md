

# Slot: currency 


_ISO 4217 currency code (for example EUR, USD)._





URI: [pbs:currency](https://example.org/pragmatic-bim-data-contract/currency)
Alias: currency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantit... |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated... |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Z]{3}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:currency |
| native | pbs:currency |




## LinkML Source

<details>
```yaml
name: currency
description: ISO 4217 currency code (for example EUR, USD).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: currency
domain_of:
- AbstractCostRecord
range: string
required: true
pattern: ^[A-Z]{3}$

```
</details>