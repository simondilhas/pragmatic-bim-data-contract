

# Slot: property_value_boolean 


_Boolean value when property_value_type is boolean._





URI: [pbs:property_value_boolean](https://example.org/pragmatic-bim-data-contract/property_value_boolean)
Alias: property_value_boolean

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
| Range | [Boolean](Boolean.md) |
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
| self | pbs:property_value_boolean |
| native | pbs:property_value_boolean |




## LinkML Source

<details>
```yaml
name: property_value_boolean
description: Boolean value when property_value_type is boolean.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: property_value_boolean
domain_of:
- PerformanceProperty
range: boolean

```
</details>