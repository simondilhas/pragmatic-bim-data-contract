# Abstract wall separator products to KBOB ecobilans mapping

Source: [`abstract-wall-separator-products-to-kbob-ecobilans.mapping.ttl`](sources/mapping-wall-separator-products-to-kbob-ecobilans.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Wand-Trennelementprodukte KBOB-Oekobilanz-Zeilen zu. m2-bewertete Waende auf kg-Zeilen nutzen Standard-Flaechenertraege in kbob-ecobilans-price-unit-defaults.json. m3-Beton nutzt Dichtekonversion von 01.002.
- **description (en):** Maps abstract wall separator products to KBOB ecobilans rows. m2-priced walls mapped to kg rows use default area yields in kbob-ecobilans-price-unit-defaults.json. m3 concrete uses density conversion from 01.002.
- **title (de):** Mapping abstrakter Wand-Trennelementprodukte nach KBOB Oekobilanz
- **title (en):** Abstract wall separator products to KBOB ecobilans mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `swp:SWP-BLT` | `closeMatch` | `kbobbm:02-006` |
| `swp:SWP-BLT` | `relatedMatch` | `kbobbm:01-041` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `kbobbm:05-008` |
| `swp:SWP-ELEMENT-WALL` | `closeMatch` | `kbobbm:05-021` |
| `swp:SWP-ELEMENT-WALL` | `relatedMatch` | `kbobbm:03-008` |
| `swp:SWP-ELEMENT-WALL` | `relatedMatch` | `kbobbm:07-014` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `kbobbm:07-005` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `kbobbm:07-004` |
| `swp:SWP-MASONRY` | `closeMatch` | `kbobbm:02-001` |
| `swp:SWP-MASONRY` | `relatedMatch` | `kbobbm:02-002` |
| `swp:SWP-MASONRY` | `relatedMatch` | `kbobbm:02-006` |
| `swp:SWP-ORTBETON` | `closeMatch` | `kbobbm:01-002` |
| `swp:SWP-OTH` | `closeMatch` | `kbobbm:01-002` |
| `swp:SWP-OTH` | `relatedMatch` | `kbobbm:02-001` |
| `swp:SWP-OTH` | `relatedMatch` | `kbobbm:07-005` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `kbobbm:01-042` |
| `swp:SWP-PREFAB-CONC` | `relatedMatch` | `kbobbm:01-041` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `kbobbm:03-020` |
| `swp:SWP-RAMMED-EARTH` | `relatedMatch` | `kbobbm:10-015` |
| `swp:SWP-STEEL` | `closeMatch` | `kbobbm:06-012` |
| `swp:SWP-STEEL` | `relatedMatch` | `kbobbm:06-001` |
| `swp:SWP-TIMBER` | `closeMatch` | `kbobbm:07-003` |
| `swp:SWP-TIMBER` | `relatedMatch` | `kbobbm:07-023` |
