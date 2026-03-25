

# Slot: system_type 


_Classification of system role (unit, network, terminal)._





URI: [pbs:system_type](https://example.org/pragmatic-bim-data-contract/system_type)
Alias: system_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SystemType](SystemType.md) |
| Domain Of | [System](System.md) |

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
| self | pbs:system_type |
| native | pbs:system_type |




## LinkML Source

<details>
```yaml
name: system_type
description: Classification of system role (unit, network, terminal).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: system_type
domain_of:
- System
range: SystemType
required: true

```
</details>