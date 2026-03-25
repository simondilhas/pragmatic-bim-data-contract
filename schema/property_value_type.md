

# Slot: property_value_type 


_Value type discriminator for normalized storage (for example string, number, boolean)._





URI: [pbs:property_value_type](https://example.org/pragmatic-bim-data-contract/property_value_type)
Alias: property_value_type

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
| Range | [PerformancePropertyValueType](PerformancePropertyValueType.md) |
| Domain Of | [PerformanceProperty](PerformanceProperty.md) |

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
| self | pbs:property_value_type |
| native | pbs:property_value_type |




## LinkML Source

<details>
```yaml
name: property_value_type
description: Value type discriminator for normalized storage (for example string,
  number, boolean).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: property_value_type
domain_of:
- PerformanceProperty
range: PerformancePropertyValueType
required: true

```
</details>