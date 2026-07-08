

# Slot: property_unit 


_Normalized unit where applicable (for example min, dB, W/m2K)._





URI: [pbs:property_unit](https://example.org/pragmatic-bim-data-contract/property_unit)
Alias: property_unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ThermalProperty](ThermalProperty.md) | Normalized thermal-related property |  no  |
| [AcousticProperty](AcousticProperty.md) | Normalized acoustic-related property |  no  |
| [FireProperty](FireProperty.md) | Normalized fire-related property |  no  |
| [MaterialProperty](MaterialProperty.md) | Normalized material-related property |  no  |
| [StructuralProperty](StructuralProperty.md) | Normalized structural-related property |  no  |
| [SecurityProperty](SecurityProperty.md) | Normalized security-related property |  no  |
| [PerformanceProperty](PerformanceProperty.md) | Normalized performance/property record derived from raw IFC PropertySet value... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PerformanceProperty](PerformanceProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:property_unit |
| native | pbs:property_unit |




## LinkML Source

<details>
```yaml
name: property_unit
description: Normalized unit where applicable (for example min, dB, W/m2K).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: property_unit
domain_of:
- PerformanceProperty
range: string

```
</details>