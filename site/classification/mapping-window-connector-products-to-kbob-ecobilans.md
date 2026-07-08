# Abstract window connector products to KBOB ecobilans mapping

Source: [`abstract-window-connector-products-to-kbob-ecobilans.mapping.ttl`](sources/mapping-window-connector-products-to-kbob-ecobilans.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fenster-Verbindungsprodukte KBOB-Oekobilanz-Zeilen zu. Rahmen- und Verglasungsschichten per skos:closeMatch auf narrower-Konzepte; Eltern-Fenstertypen skos:relatedMatch fuer Standard-2-fach-Rezept. WICP-STEEL-FRAME ohne KBOB-Stahl-Fensterrahmen-Zeile; 05.004 Aluminiumrahmen als strukturelle Naeherung mit 06.012 Stahlprofil als Material-Fallback.
- **description (en):** Maps abstract window connector products to KBOB ecobilans rows. Frame and glazing layers use skos:closeMatch on narrower concepts; parent window types use skos:relatedMatch for the default 2-pane recipe. Facade glazing units map to the full curtain-wall assembly row. WICP-STEEL-FRAME has no KBOB steel window-frame row; 05.004 aluminium frame used as structural proxy with 06.012 steel profile as material fallback.
- **title (de):** Mapping abstrakter Fenster-Verbindungsprodukte nach KBOB Oekobilanz
- **title (en):** Abstract window connector products to KBOB ecobilans mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `kbobbm:05-004` |
| `wicp:WICP-ALUMINIUM-FRAME` | `closeMatch` | `kbobbm:05-004` |
| `wicp:WICP-ALUMINIUM-GLZ-2P` | `closeMatch` | `kbobbm:05-001` |
| `wicp:WICP-ALUMINIUM-GLZ-2P` | `relatedMatch` | `kbobbm:05-003` |
| `wicp:WICP-ALUMINIUM-GLZ-2P` | `relatedMatch` | `kbobbm:05-012` |
| `wicp:WICP-FACADE-UNIT` | `closeMatch` | `kbobbm:05-008` |
| `wicp:WICP-OTH` | `closeMatch` | `kbobbm:05-005` |
| `wicp:WICP-OTH` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-PVC` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-PVC` | `relatedMatch` | `kbobbm:05-007` |
| `wicp:WICP-PVC-FRAME` | `closeMatch` | `kbobbm:05-007` |
| `wicp:WICP-PVC-GLZ-2P` | `closeMatch` | `kbobbm:05-001` |
| `wicp:WICP-SKYLIGHT` | `closeMatch` | `kbobbm:05-005` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `kbobbm:05-012` |
| `wicp:WICP-SPECIAL` | `closeMatch` | `kbobbm:05-012` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `kbobbm:05-008` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `kbobbm:05-016` |
| `wicp:WICP-STEEL` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-STEEL` | `relatedMatch` | `kbobbm:05-004` |
| `wicp:WICP-STEEL-FRAME` | `closeMatch` | `kbobbm:05-004` |
| `wicp:WICP-STEEL-FRAME` | `relatedMatch` | `kbobbm:06-012` |
| `wicp:WICP-STEEL-GLZ-2P` | `closeMatch` | `kbobbm:05-001` |
| `wicp:WICP-WOOD` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-WOOD` | `relatedMatch` | `kbobbm:05-005` |
| `wicp:WICP-WOOD-FRAME` | `closeMatch` | `kbobbm:05-005` |
| `wicp:WICP-WOOD-GLZ-2P` | `closeMatch` | `kbobbm:05-001` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `kbobbm:05-001` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `kbobbm:05-006` |
| `wicp:WICP-WOOD-METAL-FRAME` | `closeMatch` | `kbobbm:05-006` |
| `wicp:WICP-WOOD-METAL-GLZ-2P` | `closeMatch` | `kbobbm:05-001` |
