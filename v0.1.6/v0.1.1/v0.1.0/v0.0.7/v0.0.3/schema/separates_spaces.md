

# Slot: separates_spaces 


_Spaces separated by this separator element._





URI: [pbs:separates_spaces](https://example.org/pragmatic-bim-data-contract/separates_spaces)
Alias: separates_spaces

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [SeparatorWall](SeparatorWall.md) |

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
| self | pbs:separates_spaces |
| native | pbs:separates_spaces |




## LinkML Source

<details>
```yaml
name: separates_spaces
description: Spaces separated by this separator element.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: separates_spaces
domain_of:
- SeparatorWall
range: Space
multivalued: true

```
</details>