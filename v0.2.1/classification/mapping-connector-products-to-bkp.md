# Abstract connector products to BKP mapping

Source: [`abstract-connector-products-to-bkp.mapping.ttl`](sources/mapping-connector-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Tuer- und Fenster-Verbindungsprodukte BKP-Rohbau-221.x (Aussenfenster und -tueren) und Ausbau-272/273 (innere Metall- und Holz-Oeffnungen) zu. BKP-Untercodes mit Unterstrich. Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps abstract door and window connector product concepts to BKP Rohbau 221.x (exterior windows and doors) and Ausbau 272/273 (interior metal and wood openings). BKP subcodes use underscore notation (e.g. bkp:221_0 for BKP 221.0). Full BKP vocabulary is external.
- **title (de):** Mapping abstrakter Verbindungsprodukte nach BKP
- **title (en):** Abstract connector products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `dcp:DCP-GATE` | `closeMatch` | `bkp:221-6` |
| `dcp:DCP-GATE` | `relatedMatch` | `bkp:221-9` |
| `dcp:DCP-GATE` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-GLASS` | `closeMatch` | `bkp:221-6` |
| `dcp:DCP-GLASS` | `relatedMatch` | `bkp:221-8` |
| `dcp:DCP-GLASS` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-METAL` | `closeMatch` | `bkp:221-6` |
| `dcp:DCP-METAL` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-PVC` | `closeMatch` | `bkp:221-6` |
| `dcp:DCP-PVC` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-SPECIAL` | `closeMatch` | `bkp:221-8` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `bkp:221-6` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-WOOD` | `closeMatch` | `bkp:221-5` |
| `dcp:DCP-WOOD` | `relatedMatch` | `bkp:273` |
| `dcp:DCP-WOOD-METAL` | `closeMatch` | `bkp:221-5` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `bkp:272` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `bkp:273` |
| `wicp:WICP-ALUMINIUM` | `closeMatch` | `bkp:221-4` |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `bkp:272` |
| `wicp:WICP-FACADE-UNIT` | `closeMatch` | `bkp:221-8` |
| `wicp:WICP-FACADE-UNIT` | `relatedMatch` | `bkp:221-4` |
| `wicp:WICP-FACADE-UNIT` | `relatedMatch` | `bkp:221-9` |
| `wicp:WICP-PVC` | `closeMatch` | `bkp:221-2` |
| `wicp:WICP-PVC` | `relatedMatch` | `bkp:272` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `bkp:221-0` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `bkp:221-4` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `bkp:224` |
| `wicp:WICP-SPECIAL` | `closeMatch` | `bkp:221-8` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `bkp:221-4` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `bkp:272` |
| `wicp:WICP-STEEL` | `closeMatch` | `bkp:221-3` |
| `wicp:WICP-STEEL` | `relatedMatch` | `bkp:272` |
| `wicp:WICP-WOOD` | `closeMatch` | `bkp:221-0` |
| `wicp:WICP-WOOD` | `relatedMatch` | `bkp:273` |
| `wicp:WICP-WOOD-METAL` | `closeMatch` | `bkp:221-1` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `bkp:272` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `bkp:273` |
