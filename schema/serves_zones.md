

# Slot: serves_zones 


_Zone context nodes served by this system._





URI: [pbs:serves_zones](https://example.org/pragmatic-bim-data-contract/serves_zones)
Alias: serves_zones

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ZoneContext](ZoneContext.md) |
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
| self | pbs:serves_zones |
| native | pbs:serves_zones |




## LinkML Source

<details>
```yaml
name: serves_zones
description: Zone context nodes served by this system.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: serves_zones
domain_of:
- System
range: ZoneContext
multivalued: true

```
</details>