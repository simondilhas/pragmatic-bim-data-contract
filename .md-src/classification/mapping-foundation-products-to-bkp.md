# Abstract foundation products to BKP mapping

Source: [`abstract-foundation-products-to-bkp.mapping.ttl`](sources/mapping-foundation-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fundamentprodukte BKP-Rohbau-1-Positionen zu (216 Fundamente; 211 Baumeisterarbeiten wo Beton tragend dominiert). BKP-Untercodes mit Unterstrich. Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps abstract foundation product concepts to BKP Rohbau 1 cost lines (216 Fundamente; 211 Baumeisterarbeiten where structural concrete dominates). BKP subcodes use underscore notation (e.g. bkp:216_0 for BKP 216.0). Full BKP vocabulary is external; only referenced IRIs are used.
- **title (de):** Mapping abstrakter Fundamentprodukte nach BKP
- **title (en):** Abstract foundation products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `fdp:FDP-DRAINAGE` | `closeMatch` | `bkp:216-5` |
| `fdp:FDP-DRAINAGE` | `relatedMatch` | `bkp:216-0` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `bkp:216-2` |
| `fdp:FDP-MICRO-PILE` | `relatedMatch` | `bkp:216-3` |
| `fdp:FDP-PAD` | `closeMatch` | `bkp:216-1` |
| `fdp:FDP-PAD` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-PILE` | `closeMatch` | `bkp:216-2` |
| `fdp:FDP-PILE` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-RAFT` | `closeMatch` | `bkp:216-0` |
| `fdp:FDP-RAFT` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-RETAINING` | `closeMatch` | `bkp:216-0` |
| `fdp:FDP-RETAINING` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-STRIP` | `closeMatch` | `bkp:216-1` |
| `fdp:FDP-STRIP` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `bkp:216-4` |
| `fdp:FDP-WATERPROOF` | `relatedMatch` | `bkp:216-0` |
