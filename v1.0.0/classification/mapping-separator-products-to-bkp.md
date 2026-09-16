# Abstract separator products to BKP mapping

Source: [`abstract-separator-products-to-bkp.mapping.ttl`](sources/mapping-separator-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Trennelementprodukte BKP-Rohbau-1-Positionen zu (211 Baumeisterarbeiten bis 215 Leichtkonstruktionen; 277 Elementwaende fuer Trockenbau-Trennwaende). Vollstaendiges BKP-Vokabular extern. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps abstract separator product concepts to BKP Rohbau 1 cost lines (211 Baumeisterarbeiten through 215 Leichtkonstruktionen; 277 Elementwaende for drywall partitions). Full BKP vocabulary is external; only referenced IRIs are used. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
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
