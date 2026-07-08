

# Slot: system_discipline 


_Classification of system discipline (electrical, sanitary, ventilation, heating)._





URI: [pbs:system_discipline](https://example.org/pragmatic-bim-data-contract/system_discipline)
Alias: system_discipline

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SystemDiscipline](SystemDiscipline.md) |
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
| self | pbs:system_discipline |
| native | pbs:system_discipline |




## LinkML Source

<details>
```yaml
name: system_discipline
description: Classification of system discipline (electrical, sanitary, ventilation,
  heating).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: system_discipline
domain_of:
- System
range: SystemDiscipline
required: true

```
</details>