

# Slot: property_value_string 


_String value when property_value_type is string._





URI: [pbs:property_value_string](https://example.org/pragmatic-bim-data-contract/property_value_string)
Alias: property_value_string

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
| self | pbs:property_value_string |
| native | pbs:property_value_string |




## LinkML Source

<details>
```yaml
name: property_value_string
description: String value when property_value_type is string.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: property_value_string
domain_of:
- PerformanceProperty
range: string

```
</details>