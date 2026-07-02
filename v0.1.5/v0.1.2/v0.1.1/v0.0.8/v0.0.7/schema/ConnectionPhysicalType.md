---
search:
  boost: 2.0
---


# Enum: ConnectionPhysicalType 




_Classification of physical connector elements that connect spaces._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionPhysicalType](https://schema.pragmaticbim.ch/ConnectionPhysicalType)

**Enum URI:** [pbs:ConnectionPhysicalType](https://schema.pragmaticbim.ch/ConnectionPhysicalType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| door | ifcowl:IfcDoor | Human access connector via a door element. | Title: Door<br>|
| window | ifcowl:IfcWindow | Visual/daylight connector via a window element. | Title: Window<br>|
| duct | ifcowl:IfcDuctSegment | Air distribution connector segment. | Title: Duct<br>|
| pipe | ifcowl:IfcPipeSegment | Fluid/gas distribution connector segment. | Title: Pipe<br>|
| cable | ifcowl:IfcCableSegment | Electrical/data cable connector segment. | Title: Cable<br>|
| conduit | ifcowl:IfcConduitSegment | Electrical/data conduit connector segment. | Title: Conduit<br>|
| opening_other | ifcowl:IfcOpeningElement | Other opening-style connector not covered by door/window. | Title: Opening Other<br>|
| network_other | ifcowl:IfcFlowSegment | Other network connector segment not covered by controlled values. | Title: Network Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [connection_physical_type](connection_physical_type.md) | Classification of physical connector type (for example door, window, duct, pipe, cable). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionPhysicalType
description: Classification of physical connector elements that connect spaces.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionPhysicalType
permissible_values:
  door:
    text: door
    description: Human access connector via a door element.
    meaning: ifcowl:IfcDoor
    alt_descriptions:
      de:
        source: de
        description: Tuer
    title: Door
  window:
    text: window
    description: Visual/daylight connector via a window element.
    meaning: ifcowl:IfcWindow
    alt_descriptions:
      de:
        source: de
        description: Fenster
    title: Window
  duct:
    text: duct
    description: Air distribution connector segment.
    meaning: ifcowl:IfcDuctSegment
    alt_descriptions:
      de:
        source: de
        description: Luftkanal
    title: Duct
  pipe:
    text: pipe
    description: Fluid/gas distribution connector segment.
    meaning: ifcowl:IfcPipeSegment
    alt_descriptions:
      de:
        source: de
        description: Rohr
    title: Pipe
  cable:
    text: cable
    description: Electrical/data cable connector segment.
    meaning: ifcowl:IfcCableSegment
    alt_descriptions:
      de:
        source: de
        description: Kabel
    title: Cable
  conduit:
    text: conduit
    description: Electrical/data conduit connector segment.
    meaning: ifcowl:IfcConduitSegment
    alt_descriptions:
      de:
        source: de
        description: Leerrohr
    title: Conduit
  opening_other:
    text: opening_other
    description: Other opening-style connector not covered by door/window.
    meaning: ifcowl:IfcOpeningElement
    alt_descriptions:
      de:
        source: de
        description: Sonstige Oeffnung
    title: Opening Other
  network_other:
    text: network_other
    description: Other network connector segment not covered by controlled values.
    meaning: ifcowl:IfcFlowSegment
    alt_descriptions:
      de:
        source: de
        description: Sonstiges Netz
    title: Network Other

```
</details>

</div>