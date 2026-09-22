# Abstract building metrics to RICS IPMS mapping

Source: [`abstract-metric-to-rics-ipms.mapping.ttl`](sources/mapping-metric-to-rics-ipms.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (en):** Close match between abstract building metrics and RICS IPMS area concepts.
- **title (en):** Abstract building metrics to RICS IPMS mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `met:total-gross-building-volume` | `closeMatch` | `rics:GIFA` |
| `met:total-gross-floor-area` | `closeMatch` | `rics:GEA` |
| `met:total-gross-floor-area` | `closeMatch` | `rics:IPMS1` |
| `met:total-net-floor-area` | `closeMatch` | `rics:GIA` |
| `met:total-net-floor-area` | `closeMatch` | `rics:IPMS2` |
