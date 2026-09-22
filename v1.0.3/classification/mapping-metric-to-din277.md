# Abstract building metrics to DIN 277 mapping

Source: [`abstract-metric-to-din277.mapping.ttl`](sources/mapping-metric-to-din277.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (en):** Close match between abstract building metrics and DIN 277 floor area and volume codes.
- **title (en):** Abstract building metrics to DIN 277 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `met:total-construction-floor-area` | `closeMatch` | `din277:KGF` |
| `met:total-gross-building-volume` | `closeMatch` | `din277:BRI` |
| `met:total-gross-floor-area` | `closeMatch` | `din277:BGF` |
| `met:total-net-building-volume` | `closeMatch` | `din277:NRI` |
| `met:total-net-floor-area` | `closeMatch` | `din277:NRF` |
