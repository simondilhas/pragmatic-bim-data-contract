# Enum: BoundaryType 



URI: [pbs:BoundaryType](https://example.org/pragmatic-bim-data-contract/BoundaryType)

**Enum URI:** [pbs:BoundaryType](https://example.org/pragmatic-bim-data-contract/BoundaryType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| flooring | ifcowl:IfcCoveringTypeEnum.FLOORING |  |
| ceiling | ifcowl:IfcCoveringTypeEnum.CEILING |  |
| cladding | ifcowl:IfcCoveringTypeEnum.CLADDING |  |




## Slots

| Name | Description |
| ---  | --- |
| [boundary_type](boundary_type.md) | Classification of boundary element (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: BoundaryType
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:BoundaryType
permissible_values:
  flooring:
    text: flooring
    meaning: ifcowl:IfcCoveringTypeEnum.FLOORING
  ceiling:
    text: ceiling
    meaning: ifcowl:IfcCoveringTypeEnum.CEILING
  cladding:
    text: cladding
    meaning: ifcowl:IfcCoveringTypeEnum.CLADDING

```
</details>