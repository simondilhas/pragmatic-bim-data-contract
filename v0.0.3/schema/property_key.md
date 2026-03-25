

# Slot: property_key 


_Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum._





URI: [pbs:property_key](https://example.org/pragmatic-bim-data-contract/property_key)
Alias: property_key

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ThermalProperty](ThermalProperty.md) | Normalized thermal-related property |  yes  |
| [AcousticProperty](AcousticProperty.md) | Normalized acoustic-related property |  yes  |
| [FireProperty](FireProperty.md) | Normalized fire-related property |  yes  |
| [MaterialProperty](MaterialProperty.md) | Normalized material-related property |  yes  |
| [StructuralProperty](StructuralProperty.md) | Normalized structural-related property |  yes  |
| [SecurityProperty](SecurityProperty.md) | Normalized security-related property |  yes  |
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
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:property_key |
| native | pbs:property_key |




## LinkML Source

<details>
```yaml
name: property_key
description: Canonical key inside the domain; constrained via subclass slot_usage
  to a domain-specific enum.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: property_key
domain_of:
- PerformanceProperty
range: string
required: true

```
</details>