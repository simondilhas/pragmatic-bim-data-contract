# Enum: ZoneType 




_Classification of zone purpose and organizational intent._



URI: [pbs:ZoneType](https://example.org/pragmatic-bim-data-contract/ZoneType)

**Enum URI:** [pbs:ZoneType](https://example.org/pragmatic-bim-data-contract/ZoneType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| occupancy_unit | ifcowl:IfcSpatialZone | Occupancy unit zone (for example apartment, office suite, or retail unit) |
| tenant | ifcowl:IfcSpatialZone | Tenant area zone used for leasing and occupancy boundaries |
| functional | ifcowl:IfcSpatialZone | Functional grouping zone (for example clinical, retail, office support) |
| cost | ifcowl:IfcGroup | Cost grouping zone for estimation and controlling |
| fire | ifcowl:IfcSpatialZone | Fire compartment or fire strategy grouping zone |
| security | ifcowl:IfcSpatialZone | Security management zone for access control and surveillance planning |




## Slots

| Name | Description |
| ---  | --- |
| [zone_type](zone_type.md) | Optional zone classification; intended for SpatialContext nodes where context... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract






## LinkML Source

<details>
```yaml
name: ZoneType
description: Classification of zone purpose and organizational intent.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
enum_uri: pbs:ZoneType
permissible_values:
  occupancy_unit:
    text: occupancy_unit
    description: Occupancy unit zone (for example apartment, office suite, or retail
      unit).
    meaning: ifcowl:IfcSpatialZone
  tenant:
    text: tenant
    description: Tenant area zone used for leasing and occupancy boundaries.
    meaning: ifcowl:IfcSpatialZone
  functional:
    text: functional
    description: Functional grouping zone (for example clinical, retail, office support).
    meaning: ifcowl:IfcSpatialZone
  cost:
    text: cost
    description: Cost grouping zone for estimation and controlling.
    meaning: ifcowl:IfcGroup
  fire:
    text: fire
    description: Fire compartment or fire strategy grouping zone.
    meaning: ifcowl:IfcSpatialZone
  security:
    text: security
    description: Security management zone for access control and surveillance planning.
    meaning: ifcowl:IfcSpatialZone

```
</details>