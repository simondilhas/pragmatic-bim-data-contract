# qto_buccaneer to abstract building metrics mapping

Source: [`qto-buccaneer-to-abstract-metric.mapping.ttl`](sources/mapping-qto-buccaneer-to-metric.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (en):** Optional guideline bridge from qto_buccaneer V0.1.3 metric keys to abstract metric concepts. Not a port of calculation logic.
- **title (en):** qto_buccaneer metric keys to abstract building metrics mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `qto:construction-area` | `closeMatch` | `met:total-construction-floor-area` |
| `qto:construction-area-above-ground` | `closeMatch` | `met:total-construction-floor-area-above-ground` |
| `qto:construction-area-below-ground` | `closeMatch` | `met:total-construction-floor-area-below-ground` |
| `qto:doors-exterior-area` | `closeMatch` | `met:total-exterior-door-area` |
| `qto:doors-exterior-area-above-ground` | `closeMatch` | `met:total-exterior-door-area-above-ground` |
| `qto:doors-exterior-area-below-ground` | `closeMatch` | `met:total-exterior-door-area-below-ground` |
| `qto:facade-vertical-area` | `closeMatch` | `met:total-vertical-facade-area` |
| `qto:facade-vertical-area-above-ground` | `closeMatch` | `met:total-vertical-facade-area-above-ground` |
| `qto:facade-vertical-area-below-ground` | `closeMatch` | `met:total-vertical-facade-area-below-ground` |
| `qto:gross-floor-area` | `closeMatch` | `met:total-gross-floor-area` |
| `qto:gross-floor-area-above-ground` | `closeMatch` | `met:total-gross-floor-area-above-ground` |
| `qto:gross-floor-area-below-ground` | `closeMatch` | `met:total-gross-floor-area-below-ground` |
| `qto:gross-volume` | `closeMatch` | `met:total-gross-building-volume` |
| `qto:gross-volume-above-ground` | `closeMatch` | `met:total-gross-building-volume-above-ground` |
| `qto:gross-volume-below-ground` | `closeMatch` | `met:total-gross-building-volume-below-ground` |
| `qto:roof-area` | `closeMatch` | `met:total-roof-area` |
| `qto:roof-area-above-ground` | `closeMatch` | `met:total-roof-area-above-ground` |
| `qto:roof-area-below-ground` | `closeMatch` | `met:total-roof-area-below-ground` |
| `qto:soffit-area` | `closeMatch` | `met:total-soffit-area` |
| `qto:soffit-area-above-ground` | `closeMatch` | `met:total-soffit-area-above-ground` |
| `qto:soffit-area-below-ground` | `closeMatch` | `met:total-soffit-area-below-ground` |
| `qto:space-exterior-area` | `closeMatch` | `met:total-exterior-floor-area` |
| `qto:space-interior-floor-area` | `closeMatch` | `met:total-net-floor-area` |
| `qto:space-interior-floor-area-above-ground` | `closeMatch` | `met:total-net-floor-area-above-ground` |
| `qto:space-interior-floor-area-below-ground` | `closeMatch` | `met:total-net-floor-area-below-ground` |
| `qto:space-interior-volume` | `closeMatch` | `met:total-net-building-volume` |
| `qto:space-interior-volume-above-ground` | `closeMatch` | `met:total-net-building-volume-above-ground` |
| `qto:space-interior-volume-below-ground` | `closeMatch` | `met:total-net-building-volume-below-ground` |
| `qto:storeys-count-including-roof` | `closeMatch` | `met:total-storey-count` |
| `qto:storeys-count-including-roof-above-ground` | `closeMatch` | `met:total-storey-count-above-ground` |
| `qto:storeys-count-including-roof-below-ground` | `closeMatch` | `met:total-storey-count-below-ground` |
| `qto:total-envelope-area` | `closeMatch` | `met:total-envelope-area` |
| `qto:windows-exterior-area` | `closeMatch` | `met:total-exterior-window-area` |
| `qto:windows-exterior-area-above-ground` | `closeMatch` | `met:total-exterior-window-area-above-ground` |
| `qto:windows-exterior-area-below-ground` | `closeMatch` | `met:total-exterior-window-area-below-ground` |
