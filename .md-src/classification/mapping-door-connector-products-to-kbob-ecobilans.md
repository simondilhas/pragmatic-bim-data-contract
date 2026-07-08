# Abstract door connector products to KBOB ecobilans mapping

Source: [`abstract-door-connector-products-to-kbob-ecobilans.mapping.ttl`](sources/mapping-door-connector-products-to-kbob-ecobilans.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Tuer-Verbindungsprodukte KBOB-Oekobilanz-Gruppe-12-Tuerbaugruppen (m2-Bezugseinheit) zu. DCP-PVC ohne Gruppe-12-Zeile; closeMatch PVC-Material 13.004 (kg) mit Flaechenertrag. DCP-GATE ohne Industrietor-Zeile; 12.006 als naechste Grossformat-Tuer-Naeherung. pcs-bewertete Tueren nutzen Standard-Tuerblattflaeche in kbob-ecobilans-price-unit-defaults.json.
- **description (en):** Maps abstract door connector products to KBOB ecobilans group 12 door assembly rows (m2 reference unit). DCP-PVC has no group-12 row; closeMatch uses PVC material 13.004 (kg) with area yield defaults. DCP-GATE has no industrial-gate row; 12.006 used as closest large-format door proxy. pcs-priced doors use default door leaf area in kbob-ecobilans-price-unit-defaults.json.
- **title (de):** Mapping abstrakter Tuer-Verbindungsprodukte nach KBOB Oekobilanz
- **title (en):** Abstract door connector products to KBOB ecobilans mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `dcp:DCP-GATE` | `closeMatch` | `kbobbm:12-006` |
| `dcp:DCP-GATE` | `relatedMatch` | `kbobbm:06-012` |
| `dcp:DCP-GATE` | `relatedMatch` | `kbobbm:12-009` |
| `dcp:DCP-GLASS` | `closeMatch` | `kbobbm:12-002` |
| `dcp:DCP-GLASS` | `relatedMatch` | `kbobbm:05-001` |
| `dcp:DCP-GLASS` | `relatedMatch` | `kbobbm:12-007` |
| `dcp:DCP-METAL` | `closeMatch` | `kbobbm:12-012` |
| `dcp:DCP-METAL` | `relatedMatch` | `kbobbm:12-007` |
| `dcp:DCP-METAL` | `relatedMatch` | `kbobbm:12-009` |
| `dcp:DCP-OTH` | `closeMatch` | `kbobbm:12-003` |
| `dcp:DCP-OTH` | `relatedMatch` | `kbobbm:12-010` |
| `dcp:DCP-PVC` | `closeMatch` | `kbobbm:13-004` |
| `dcp:DCP-PVC` | `relatedMatch` | `kbobbm:12-003` |
| `dcp:DCP-SPECIAL` | `closeMatch` | `kbobbm:12-009` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `kbobbm:05-016` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `kbobbm:12-005` |
| `dcp:DCP-WOOD` | `closeMatch` | `kbobbm:12-003` |
| `dcp:DCP-WOOD` | `relatedMatch` | `kbobbm:12-008` |
| `dcp:DCP-WOOD` | `relatedMatch` | `kbobbm:12-010` |
| `dcp:DCP-WOOD-METAL` | `closeMatch` | `kbobbm:12-001` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `kbobbm:12-002` |
