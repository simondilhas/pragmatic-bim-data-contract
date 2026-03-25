

# Slot: separates_levels 


_Level context nodes separated by this slab separator._





URI: [pbs:separates_levels](https://example.org/pragmatic-bim-data-contract/separates_levels)
Alias: separates_levels

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LevelContext](LevelContext.md) |
| Domain Of | [SeparatorSlab](SeparatorSlab.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:separates_levels |
| native | pbs:separates_levels |




## LinkML Source

<details>
```yaml
name: separates_levels
description: Level context nodes separated by this slab separator.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: separates_levels
domain_of:
- SeparatorSlab
range: LevelContext
multivalued: true

```
</details>