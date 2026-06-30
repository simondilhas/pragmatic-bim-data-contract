

# Slot: transport_medium 


_Primary transport medium carried or enabled by the connector (for example human_access, air, liquid, electricity)._





URI: [pbs:transport_medium](https://example.org/pragmatic-bim-data-contract/transport_medium)
Alias: transport_medium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for exampl... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TransportMedium](TransportMedium.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

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
| self | pbs:transport_medium |
| native | pbs:transport_medium |




## LinkML Source

<details>
```yaml
name: transport_medium
description: Primary transport medium carried or enabled by the connector (for example
  human_access, air, liquid, electricity).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: transport_medium
domain_of:
- ConnectionPhysical
range: TransportMedium
required: true

```
</details>