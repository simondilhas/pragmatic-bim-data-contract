# Abstract foundation products to BKP mapping

Source: [`abstract-foundation-products-to-bkp.mapping.ttl`](sources/mapping-foundation-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fundamentprodukte BKP-Positionen zu: 211.5 Beton- und Stahlbetonarbeiten fuer betonierte Fundamente, 17 Fundation, Sicherung, Abdichtung fuer Tiefgruendungen und Grundwasserabdichtung (171 Pfaehle, 172 Baugrubenabschluesse, 175 Grundwasserabdichtungen, 177 Baugrundverbesserungen), 211.4 Kanalisationen im Gebaeude fuer Perimeterentwaesserung und 225.2 Spezielle Daemmungen fuer Perimeterdaemmschichten. BKP-Untercodes mit Unterstrich. Vollstaendiges BKP-Vokabular extern. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps abstract foundation product concepts to BKP cost lines: 211.5 Beton- und Stahlbetonarbeiten for cast concrete foundations, 17 Fundation, Sicherung, Abdichtung for deep foundations and groundwater sealing (171 Pfaehle, 172 Baugrubenabschluesse, 175 Grundwasserabdichtungen, 177 Baugrundverbesserungen), 211.4 Kanalisationen im Gebaeude for perimeter drainage and 225.2 Spezielle Daemmungen for perimeter insulation layers. BKP subcodes use underscore notation (e.g. bkp:211_5 for BKP 211.5). Full BKP vocabulary is external; only referenced IRIs are used. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
- **title (de):** Mapping abstrakter Fundamentprodukte nach BKP
- **title (en):** Abstract foundation products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `fdp:FDP-DRAINAGE` | `closeMatch` | `bkp:211-4` |
| `fdp:FDP-DRAINAGE` | `relatedMatch` | `bkp:175` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `bkp:171` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `bkp:177` |
| `fdp:FDP-MICRO-PILE` | `relatedMatch` | `bkp:123-2` |
| `fdp:FDP-PAD` | `closeMatch` | `bkp:211-5` |
| `fdp:FDP-PAD` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-PILE` | `closeMatch` | `bkp:171` |
| `fdp:FDP-PILE` | `closeMatch` | `bkp:211-5` |
| `fdp:FDP-RAFT` | `closeMatch` | `bkp:211-5` |
| `fdp:FDP-RAFT` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-RAFT-INS` | `closeMatch` | `bkp:225-2` |
| `fdp:FDP-RAFT-INS` | `relatedMatch` | `bkp:211-5` |
| `fdp:FDP-RETAINING` | `closeMatch` | `bkp:172` |
| `fdp:FDP-RETAINING` | `closeMatch` | `bkp:211-5` |
| `fdp:FDP-RETAINING-INS` | `closeMatch` | `bkp:225-2` |
| `fdp:FDP-RETAINING-INS` | `relatedMatch` | `bkp:211-5` |
| `fdp:FDP-STRIP` | `closeMatch` | `bkp:211-5` |
| `fdp:FDP-STRIP` | `relatedMatch` | `bkp:211` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `bkp:175` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `bkp:225-3` |
