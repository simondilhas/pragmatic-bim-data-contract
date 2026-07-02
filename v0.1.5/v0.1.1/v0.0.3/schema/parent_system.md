

# Slot: parent_system 


_Parent systems that the equipment belongs to._





URI: [pbs:parent_system](https://example.org/pragmatic-bim-data-contract/parent_system)
Alias: parent_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, senso... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [System](System.md) |
| Domain Of | [Equipment](Equipment.md) |

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
| self | pbs:parent_system |
| native | pbs:parent_system |




## LinkML Source

<details>
```yaml
name: parent_system
description: Parent systems that the equipment belongs to.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: parent_system
domain_of:
- Equipment
range: System
multivalued: true

```
</details>