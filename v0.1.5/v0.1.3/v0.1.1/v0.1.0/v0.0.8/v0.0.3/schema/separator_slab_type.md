

# Slot: separator_slab_type 


_Classification of slab-based separator element (for example floor/roof/base slab)._





URI: [pbs:separator_slab_type](https://example.org/pragmatic-bim-data-contract/separator_slab_type)
Alias: separator_slab_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SeparatorSlabType](SeparatorSlabType.md) |
| Domain Of | [SeparatorSlab](SeparatorSlab.md) |

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
| self | pbs:separator_slab_type |
| native | pbs:separator_slab_type |




## LinkML Source

<details>
```yaml
name: separator_slab_type
description: Classification of slab-based separator element (for example floor/roof/base
  slab).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: separator_slab_type
domain_of:
- SeparatorSlab
range: SeparatorSlabType
required: true

```
</details>