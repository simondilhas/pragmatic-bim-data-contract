# Abstract facade covering products to KBOB ecobilans mapping

Source: [`abstract-facade-covering-products-to-kbob-ecobilans.mapping.ttl`](sources/mapping-facade-covering-products-to-kbob-ecobilans.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fassadenbekleidungsprodukte KBOB-Oekobilanz-Zeilen zu. ETICS/WDVS nutzt Schicht-narrower fuer Daemmung und Putz; andere Fassadentypen naechste Baugruppen- oder Materialzeile.
- **description (en):** Maps abstract facade covering products to KBOB ecobilans rows. ETICS/WDVS uses layer narrowers for insulation and render; other facade types map to closest assembly or material row where available.
- **title (de):** Mapping abstrakter Fassadenbekleidungsprodukte nach KBOB Oekobilanz
- **title (en):** Abstract facade covering products to KBOB ecobilans mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `kbobbm:05-008` |
| `facp:FaCP-BIPV-INTEGRATED` | `relatedMatch` | `kbobbm:05-022` |
| `facp:FaCP-BIPV-INTEGRATED` | `relatedMatch` | `kbobbm:06-001` |
| `facp:FaCP-CERAMIC-VENTILATED` | `closeMatch` | `kbobbm:03-010` |
| `facp:FaCP-CERAMIC-VENTILATED` | `relatedMatch` | `kbobbm:11-008` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `closeMatch` | `kbobbm:14-001` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `closeMatch` | `kbobbm:03-003` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `relatedMatch` | `kbobbm:05-028` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `closeMatch` | `kbobbm:05-022` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `closeMatch` | `kbobbm:06-001` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `relatedMatch` | `kbobbm:06-002` |
| `facp:FaCP-NATURAL-STONE-VENTILATED` | `closeMatch` | `kbobbm:05-025` |
| `facp:FaCP-OTHER` | `closeMatch` | `kbobbm:05-023` |
| `facp:FaCP-OTHER` | `relatedMatch` | `kbobbm:04-007` |
| `facp:FaCP-OTHER` | `relatedMatch` | `kbobbm:05-022` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `closeMatch` | `kbobbm:05-022` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `relatedMatch` | `kbobbm:06-012` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `closeMatch` | `kbobbm:07-003` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `relatedMatch` | `kbobbm:07-023` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `kbobbm:04-007` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `kbobbm:10-004` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `kbobbm:10-008` |
| `facp:FaCP-RENDER-ETICS-WDVS-INS` | `closeMatch` | `kbobbm:10-004` |
| `facp:FaCP-RENDER-ETICS-WDVS-INS` | `relatedMatch` | `kbobbm:10-008` |
| `facp:FaCP-RENDER-ETICS-WDVS-RENDER` | `closeMatch` | `kbobbm:04-007` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `relatedMatch` | `kbobbm:04-007` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `relatedMatch` | `kbobbm:05-023` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `relatedMatch` | `kbobbm:10-004` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `relatedMatch` | `kbobbm:10-008` |
| `facp:FaCP-SYNTHETIC-VENTILATED` | `closeMatch` | `kbobbm:05-023` |
| `facp:FaCP-SYNTHETIC-VENTILATED` | `relatedMatch` | `kbobbm:05-024` |
| `facp:FaCP-TIMBER-VENTILATED` | `closeMatch` | `kbobbm:07-003` |
