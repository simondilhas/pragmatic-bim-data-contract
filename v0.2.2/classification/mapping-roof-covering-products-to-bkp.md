# Abstract roof covering products to BKP mapping

Source: [`abstract-roof-covering-products-to-bkp.mapping.ttl`](sources/mapping-roof-covering-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Dachbekleidungsprodukte BKP-Rohbau-2-Positionen zu (224 Bedachungsarbeiten). BKP-Untercodes mit Unterstrich. Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps abstract roof covering product concepts to BKP Rohbau 2 cost lines (224 Bedachungsarbeiten). BKP subcodes use underscore notation (e.g. bkp:224_0 for BKP 224.0). Full BKP vocabulary is external; only referenced IRIs are used.
- **title (de):** Mapping abstrakter Dachbekleidungsprodukte nach BKP
- **title (en):** Abstract roof covering products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rcp:RCP-FLAT-BITUMEN` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-FLAT-LIQUID` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-FLAT-LIQUID` | `relatedMatch` | `bkp:224-1` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-GREEN-EXTENSIVE` | `closeMatch` | `bkp:224-6` |
| `rcp:RCP-GREEN-INTENSIVE` | `closeMatch` | `bkp:224-6` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `bkp:224-0` |
| `rcp:RCP-METAL-SHEET` | `closeMatch` | `bkp:224-2` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `bkp:224-7` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `bkp:244` |
| `rcp:RCP-SLATE` | `closeMatch` | `bkp:224-3` |
| `rcp:RCP-TILE-CLAY` | `closeMatch` | `bkp:224-3` |
| `rcp:RCP-TILE-CLAY` | `relatedMatch` | `bkp:224-4` |
| `rcp:RCP-TILE-CONCRETE` | `closeMatch` | `bkp:224-4` |
| `rcp:RCP-TILE-CONCRETE` | `relatedMatch` | `bkp:224-3` |
| `rcp:RCP-WOOD-SHINGLE` | `closeMatch` | `bkp:224-5` |
| `rcp:RCP-WOOD-SHINGLE` | `relatedMatch` | `bkp:214` |
