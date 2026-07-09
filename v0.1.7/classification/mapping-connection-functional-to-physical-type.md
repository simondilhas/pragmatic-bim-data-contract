# Connection functional type to physical type mapping

Source: [`connection-functional-to-physical-type.mapping.ttl`](sources/mapping-connection-functional-to-physical-type.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet zuweisbare funktionale Verbindungstypen kompatiblen ConnectionPhysicalType-Enum-Werten (IFC-ausgerichtete physische Typen) zu. opening_other wird ueber die funktionale Zuweisung aufgeloest, nicht durch Aufteilung des physischen Enums.
- **description (en):** Maps assignable connection functional types to compatible ConnectionPhysicalType enum values (IFC-aligned physical types). opening_other disambiguation is resolved at functional-type assignment, not by splitting the physical enum.
- **title (de):** Mapping funktionaler Verbindungstypen zu physischen Typen
- **title (en):** Connection functional type to physical type mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `func:access` | `relatedMatch` | `phys:door` |
| `func:access` | `relatedMatch` | `phys:opening-other` |
| `func:cooling` | `relatedMatch` | `phys:pipe` |
| `func:data` | `relatedMatch` | `phys:cable` |
| `func:data` | `relatedMatch` | `phys:conduit` |
| `func:electrical` | `relatedMatch` | `phys:cable` |
| `func:electrical` | `relatedMatch` | `phys:conduit` |
| `func:fresh-water` | `relatedMatch` | `phys:pipe` |
| `func:heating` | `relatedMatch` | `phys:pipe` |
| `func:special-media` | `relatedMatch` | `phys:network-other` |
| `func:special-media` | `relatedMatch` | `phys:pipe` |
| `func:ventilation` | `relatedMatch` | `phys:duct` |
| `func:visual` | `relatedMatch` | `phys:opening-other` |
| `func:visual` | `relatedMatch` | `phys:window` |
| `func:waste-water` | `relatedMatch` | `phys:pipe` |
