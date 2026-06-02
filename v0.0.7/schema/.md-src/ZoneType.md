---
search:
  boost: 2.0
---


# Enum: ZoneType 




_Classification of zone purpose and organizational intent._



<div data-search-exclude markdown="1">

URI: [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)

**Enum URI:** [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| occupancy_unit | ifcowl:IfcSpatialZone | Occupancy unit zone (for example apartment, office suite, or retail unit). | Title: Occupancy Unit<br>|
| tenant | ifcowl:IfcSpatialZone | Tenant area zone used for leasing and occupancy boundaries. | Title: Tenant<br>|
| functional | ifcowl:IfcSpatialZone | Functional grouping zone (for example clinical, retail, office support). | Title: Functional<br>|
| cost | ifcowl:IfcGroup | Cost grouping zone for estimation and controlling. | Title: Cost<br>|
| fire | ifcowl:IfcSpatialZone | Fire compartment or fire strategy grouping zone. | Title: Fire<br>|
| security | ifcowl:IfcSpatialZone | Security management zone for access control and surveillance planning. | Title: Security<br>|




## Slots

| Name | Description |
| ---  | --- |
| [zone_type](zone_type.md) | Optional zone classification; intended for SpatialContext nodes where context_type is zone. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ZoneType
description: Classification of zone purpose and organizational intent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ZoneType
permissible_values:
  occupancy_unit:
    text: occupancy_unit
    description: Occupancy unit zone (for example apartment, office suite, or retail
      unit).
    meaning: ifcowl:IfcSpatialZone
    alt_descriptions:
      de:
        source: de
        description: Nutzungseinheit
    title: Occupancy Unit
  tenant:
    text: tenant
    description: Tenant area zone used for leasing and occupancy boundaries.
    meaning: ifcowl:IfcSpatialZone
    alt_descriptions:
      de:
        source: de
        description: Mieter
    title: Tenant
  functional:
    text: functional
    description: Functional grouping zone (for example clinical, retail, office support).
    meaning: ifcowl:IfcSpatialZone
    alt_descriptions:
      de:
        source: de
        description: Funktional
    title: Functional
  cost:
    text: cost
    description: Cost grouping zone for estimation and controlling.
    meaning: ifcowl:IfcGroup
    alt_descriptions:
      de:
        source: de
        description: Kosten
    title: Cost
  fire:
    text: fire
    description: Fire compartment or fire strategy grouping zone.
    meaning: ifcowl:IfcSpatialZone
    alt_descriptions:
      de:
        source: de
        description: Brandschutz
    title: Fire
  security:
    text: security
    description: Security management zone for access control and surveillance planning.
    meaning: ifcowl:IfcSpatialZone
    alt_descriptions:
      de:
        source: de
        description: Sicherheit
    title: Security

```
</details>

</div>