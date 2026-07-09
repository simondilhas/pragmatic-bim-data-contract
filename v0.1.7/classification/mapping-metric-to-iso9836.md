# Abstract building metrics to ISO 9836 mapping

Source: [`abstract-metric-to-iso9836.mapping.ttl`](sources/mapping-metric-to-iso9836.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (en):** Close match between abstract building metrics and ISO 9836:2017 area and volume definitions.
- **title (en):** Abstract building metrics to ISO 9836:2017 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `met:total-construction-floor-area` | `closeMatch` | `iso9836:StructuralElementsArea` |
| `met:total-gross-building-volume` | `closeMatch` | `iso9836:GrossVolume` |
| `met:total-gross-floor-area` | `closeMatch` | `iso9836:TotalFloorArea` |
| `met:total-net-building-volume` | `closeMatch` | `iso9836:NetVolume` |
| `met:total-net-floor-area` | `closeMatch` | `iso9836:NetFloorArea` |
