# Abstract separator products to BKP mapping

Source: [`abstract-separator-products-to-bkp.mapping.ttl`](sources/mapping-separator-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Trennelementprodukte BKP-Rohbau-1-Positionen zu (211 Baumeisterarbeiten bis 215 Leichtkonstruktionen; 277 Elementwaende fuer Trockenbau-Trennwaende). Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps abstract separator product concepts to BKP Rohbau 1 cost lines (211 Baumeisterarbeiten through 215 Leichtkonstruktionen; 277 Elementwaende for drywall partitions). Full BKP vocabulary is external; only referenced IRIs are used.
- **title (de):** Mapping abstrakter Trennelementprodukte nach BKP
- **title (en):** Abstract separator products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ssp:SSP-CLT` | `closeMatch` | `bkp:214` |
| `ssp:SSP-HBV` | `closeMatch` | `bkp:214` |
| `ssp:SSP-HBV` | `relatedMatch` | `bkp:211` |
| `ssp:SSP-HOLZ-LEHM` | `closeMatch` | `bkp:214` |
| `ssp:SSP-INSITU` | `closeMatch` | `bkp:211` |
| `ssp:SSP-LIGHTWEIGHT` | `closeMatch` | `bkp:215` |
| `ssp:SSP-PREFAB-CONC` | `closeMatch` | `bkp:212` |
| `ssp:SSP-STEEL-COMPOSITE` | `closeMatch` | `bkp:213` |
| `ssp:SSP-TIMBER` | `closeMatch` | `bkp:214` |
| `swp:SWP-BLT` | `closeMatch` | `bkp:212` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `bkp:215` |
| `swp:SWP-ELEMENT-WALL` | `closeMatch` | `bkp:277` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `bkp:215` |
| `swp:SWP-MASONRY` | `closeMatch` | `bkp:211` |
| `swp:SWP-ORTBETON` | `closeMatch` | `bkp:211` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `bkp:212` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `bkp:211` |
| `swp:SWP-STEEL` | `closeMatch` | `bkp:213` |
| `swp:SWP-TIMBER` | `closeMatch` | `bkp:214` |
