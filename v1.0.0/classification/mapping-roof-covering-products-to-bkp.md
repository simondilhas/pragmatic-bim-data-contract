# Abstract roof covering products to BKP mapping

Source: [`abstract-roof-covering-products-to-bkp.mapping.ttl`](sources/mapping-roof-covering-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Dachbekleidungsprodukte BKP-Rohbau-2-Positionen zu: 224.0 Deckungen (Steildaecher) fuer Steildacheindeckungen, 224.1 Plastische und elastische Dichtungsbelaege fuer Flachdachabdichtungen und Gruendachaufbauten, 222 Spenglerarbeiten fuer Metallblechdaecher. Sekundaere Positionen sind 214 Montagebau in Holz, 421 Gaertnerarbeiten (Bepflanzung) und 231 Zentrale Starkstromanlagen (Dach-Photovoltaik). BKP-Untercodes mit Unterstrich. Vollstaendiges BKP-Vokabular extern. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps abstract roof covering product concepts to BKP Rohbau 2 cost lines: 224.0 Deckungen (Steildaecher) for pitched coverings, 224.1 Plastische und elastische Dichtungsbelaege for flat roof membranes and green roof build-ups, 222 Spenglerarbeiten for sheet metal roofs. Secondary lines are 214 Montagebau in Holz, 421 Gaertnerarbeiten (planting) and 231 Zentrale Starkstromanlagen (roof photovoltaics). BKP subcodes use underscore notation (e.g. bkp:224_0 for BKP 224.0). Full BKP vocabulary is external; only referenced IRIs are used. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
- **title (de):** Mapping abstrakter Dachbekleidungsprodukte nach BKP
- **title (en):** Abstract roof covering products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rcp:RCP-FLAT-BITUMEN` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-FLAT-LIQUID` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-GREEN-EXTENSIVE` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-GREEN-EXTENSIVE` | `closeMatch` | `bkp:421` |
| `rcp:RCP-GREEN-INTENSIVE` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-GREEN-INTENSIVE` | `closeMatch` | `bkp:421` |
| `rcp:RCP-METAL-SHEET` | `closeMatch` | `bkp:222` |
| `rcp:RCP-METAL-SHEET` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-PV-ROOF` | `closeMatch` | `bkp:224-1` |
| `rcp:RCP-PV-ROOF` | `closeMatch` | `bkp:231` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `bkp:232` |
| `rcp:RCP-SLATE` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-TILE-CLAY` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-TILE-CONCRETE` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-WOOD-SHINGLE` | `closeMatch` | `bkp:224-0` |
| `rcp:RCP-WOOD-SHINGLE` | `relatedMatch` | `bkp:214` |
