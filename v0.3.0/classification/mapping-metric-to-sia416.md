# Abstract building metrics to SIA 416 mapping

Source: [`abstract-metric-to-sia416.mapping.ttl`](sources/mapping-metric-to-sia416.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (en):** Close match between abstract building-level metrics and SIA 416 area/volume codes. Above/below ground scope variants have no SIA 416 equivalent.
- **title (en):** Abstract building metrics to SIA 416 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `met:total-construction-floor-area` | `closeMatch` | `sia416:KF` |
| `met:total-exterior-floor-area` | `closeMatch` | `sia416:AGF` |
| `met:total-gross-building-volume` | `closeMatch` | `sia416:GV` |
| `met:total-gross-floor-area` | `closeMatch` | `sia416:GF` |
| `met:total-net-floor-area` | `closeMatch` | `sia416:NGF` |
