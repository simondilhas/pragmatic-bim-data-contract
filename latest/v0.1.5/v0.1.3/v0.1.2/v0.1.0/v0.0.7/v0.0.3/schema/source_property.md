

# Slot: source_property 


_Original property name inside the source PropertySet (for example FireRating)._





URI: [pbs:source_property](https://example.org/pragmatic-bim-data-contract/source_property)
Alias: source_property

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
| self | pbs:source_property |
| native | pbs:source_property |




## LinkML Source

<details>
```yaml
name: source_property
description: Original property name inside the source PropertySet (for example FireRating).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: source_property
domain_of:
- PerformanceProperty
range: string

```
</details>