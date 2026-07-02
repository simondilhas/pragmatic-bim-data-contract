# Abstract slab separator products to KBOB ecobilans mapping

Source: [`abstract-slab-separator-products-to-kbob-ecobilans.mapping.ttl`](sources/mapping-slab-separator-products-to-kbob-ecobilans.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Deckenplatten-Trennelementprodukte KBOB-Oekobilanz-Baumaterialien-Zeilen fuer geschaetzte graue Emissionen zu. Verbundprodukte nutzen skos:narrower-Schichtkonzepte mit skos:closeMatch; Elternprodukte skos:relatedMatch fuer das volle LCA-Rezept. Einfache Produkte direkt per skos:closeMatch. LCA-Faktoren in kbob-ecobilans-lca-factors.json; Standard-Schichtmengen in kbob-ecobilans-layer-recipes.json.
- **description (en):** Maps abstract slab separator product concepts to KBOB ecobilans Baumaterialien rows for estimated embodied carbon. Composite products use skos:narrower layer concepts mapped with skos:closeMatch; parent products use skos:relatedMatch to document the full LCA recipe. Simple products map directly with skos:closeMatch. LCA factors in kbob-ecobilans-lca-factors.json; default layer quantities in kbob-ecobilans-layer-recipes.json. Regenerate KBOB vocabulary with scripts/generate_kbob_ecobilans_vocabulary.py.
- **title (de):** Mapping abstrakter Deckenplatten-Trennelementprodukte nach KBOB Oekobilanz
- **title (en):** Abstract slab separator products to KBOB ecobilans mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ssp:SSP-HBV` | `relatedMatch` | `kbobbm:01-002` |
| `ssp:SSP-HBV` | `relatedMatch` | `kbobbm:07-003` |
| `ssp:SSP-HBV-CONC` | `closeMatch` | `kbobbm:01-002` |
| `ssp:SSP-HBV-WOD` | `closeMatch` | `kbobbm:07-003` |
| `ssp:SSP-HOLZ-LEHM` | `relatedMatch` | `kbobbm:03-020` |
| `ssp:SSP-HOLZ-LEHM` | `relatedMatch` | `kbobbm:07-003` |
| `ssp:SSP-HOLZ-LEHM-MSN` | `closeMatch` | `kbobbm:03-020` |
| `ssp:SSP-HOLZ-LEHM-WOD` | `closeMatch` | `kbobbm:07-003` |
| `ssp:SSP-INSITU` | `closeMatch` | `kbobbm:01-002` |
| `ssp:SSP-LIGHTWEIGHT` | `closeMatch` | `kbobbm:07-005` |
| `ssp:SSP-LIGHTWEIGHT` | `relatedMatch` | `kbobbm:10-008` |
| `ssp:SSP-OTH` | `closeMatch` | `kbobbm:01-002` |
| `ssp:SSP-OTH` | `relatedMatch` | `kbobbm:07-005` |
| `ssp:SSP-PREFAB-CONC` | `closeMatch` | `kbobbm:01-042` |
| `ssp:SSP-STEEL-COMPOSITE` | `relatedMatch` | `kbobbm:01-002` |
| `ssp:SSP-STEEL-COMPOSITE` | `relatedMatch` | `kbobbm:06-012` |
| `ssp:SSP-STEEL-COMPOSITE-CONC` | `closeMatch` | `kbobbm:01-002` |
| `ssp:SSP-STEEL-COMPOSITE-STL` | `closeMatch` | `kbobbm:06-012` |
| `ssp:SSP-TIMBER` | `closeMatch` | `kbobbm:07-023` |
| `ssp:SSP-TIMBER` | `relatedMatch` | `kbobbm:07-003` |
