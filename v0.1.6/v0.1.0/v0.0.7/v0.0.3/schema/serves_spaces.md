

# Slot: serves_spaces 


_Spaces served by this system._





URI: [pbs:serves_spaces](https://example.org/pragmatic-bim-data-contract/serves_spaces)
Alias: serves_spaces

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [System](System.md) |

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
| self | pbs:serves_spaces |
| native | pbs:serves_spaces |




## LinkML Source

<details>
```yaml
name: serves_spaces
description: Spaces served by this system.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: serves_spaces
domain_of:
- System
range: Space
multivalued: true

```
</details>