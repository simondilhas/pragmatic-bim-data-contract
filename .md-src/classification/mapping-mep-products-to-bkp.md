# Abstract MEP products to BKP mapping

Source: [`abstract-mep-products-to-bkp.mapping.ttl`](sources/mapping-mep-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Gebaeudetechnikprodukte (Erzeuger und Endgeraete) BKP-Positionen der Gebaeudetechnik zu (23 Elektroanlagen, 24 Heizungs-, Lueftungs-, Klimaanlagen, 25 Sanitaeranlagen). closeMatch ist die Leitposition; relatedMatch eine sekundaere Position je nach Systemgrenze. Erzeugung und Zentralen loesen auf 231/242/245/253 auf, Verteilung und Endgeraete auf 232/233/236/243/244/251/254. Vollstaendiges BKP-Vokabular extern. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps abstract MEP unit and terminal product concepts to BKP building services cost lines (23 Elektroanlagen, 24 Heizungs-, Lueftungs-, Klimaanlagen, 25 Sanitaeranlagen). closeMatch is the leading cost line; relatedMatch is a secondary line the product may be booked under depending on system boundary. Generation and central plant resolve to 231/242/245/253, distribution terminals to 232/233/236/243/244/251/254. Full BKP vocabulary is external; only referenced IRIs are used. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
- **title (de):** Mapping abstrakter Gebaeudetechnikprodukte nach BKP
- **title (en):** Abstract MEP products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mtp:MTP-COOL-CHILLED-CEILING` | `closeMatch` | `bkp:245` |
| `mtp:MTP-COOL-CHILLED-CEILING` | `relatedMatch` | `bkp:283-1` |
| `mtp:MTP-COOL-FAN-COIL` | `closeMatch` | `bkp:245` |
| `mtp:MTP-COOL-FAN-COIL` | `relatedMatch` | `bkp:243` |
| `mtp:MTP-DATA-DATA-OUTLET` | `closeMatch` | `bkp:236` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `closeMatch` | `bkp:236` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `relatedMatch` | `bkp:247` |
| `mtp:MTP-DATA-WIFI-AP` | `closeMatch` | `bkp:236` |
| `mtp:MTP-ELEC-LIGHT` | `closeMatch` | `bkp:233` |
| `mtp:MTP-ELEC-LIGHT` | `relatedMatch` | `bkp:232` |
| `mtp:MTP-ELEC-SOCKET` | `closeMatch` | `bkp:232` |
| `mtp:MTP-ELEC-SWITCH` | `closeMatch` | `bkp:232` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `closeMatch` | `bkp:244` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `bkp:236` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `bkp:244` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `closeMatch` | `bkp:236` |
| `mtp:MTP-FW-SHOWER` | `closeMatch` | `bkp:251` |
| `mtp:MTP-FW-TAP` | `closeMatch` | `bkp:251` |
| `mtp:MTP-FW-WC-FLUSH` | `closeMatch` | `bkp:251` |
| `mtp:MTP-HEAT-FAN-COIL` | `closeMatch` | `bkp:243` |
| `mtp:MTP-HEAT-FAN-COIL` | `relatedMatch` | `bkp:245` |
| `mtp:MTP-HEAT-RADIATOR` | `closeMatch` | `bkp:243` |
| `mtp:MTP-HEAT-UFH-MANIFOLD` | `closeMatch` | `bkp:243` |
| `mtp:MTP-SM-GAS-OUTLET` | `closeMatch` | `bkp:254` |
| `mtp:MTP-SM-GAS-OUTLET` | `relatedMatch` | `bkp:253` |
| `mtp:MTP-SM-HOSE-REEL` | `closeMatch` | `bkp:252` |
| `mtp:MTP-SM-SPRINKLER-HEAD` | `closeMatch` | `bkp:252` |
| `mtp:MTP-VENT-AIR-VALVE` | `closeMatch` | `bkp:244` |
| `mtp:MTP-VENT-GRILLE` | `closeMatch` | `bkp:244` |
| `mtp:MTP-WW-FLOOR-DRAIN` | `closeMatch` | `bkp:254` |
| `mtp:MTP-WW-FLOOR-DRAIN` | `relatedMatch` | `bkp:253` |
| `mtp:MTP-WW-SINK-DRAIN` | `closeMatch` | `bkp:254` |
| `mtp:MTP-WW-SINK-DRAIN` | `relatedMatch` | `bkp:253` |
| `mtp:MTP-WW-WC-OUTLET` | `closeMatch` | `bkp:254` |
| `mtp:MTP-WW-WC-OUTLET` | `relatedMatch` | `bkp:251` |
| `mup:MUP-COOL-CHILLER` | `closeMatch` | `bkp:245` |
| `mup:MUP-COOL-FREE-COOLER` | `closeMatch` | `bkp:245` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `closeMatch` | `bkp:236` |
| `mup:MUP-DATA-PATCH-PANEL` | `closeMatch` | `bkp:236` |
| `mup:MUP-DATA-SERVER` | `closeMatch` | `bkp:236` |
| `mup:MUP-DATA-SERVER` | `relatedMatch` | `bkp:234` |
| `mup:MUP-ELEC-GENERATOR` | `closeMatch` | `bkp:231` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `closeMatch` | `bkp:231` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `relatedMatch` | `bkp:232` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `closeMatch` | `bkp:232` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `relatedMatch` | `bkp:231` |
| `mup:MUP-ELEC-TRANSFORMER` | `closeMatch` | `bkp:231` |
| `mup:MUP-ELEC-UPS` | `closeMatch` | `bkp:231` |
| `mup:MUP-FW-PRESSURE-BOOSTER` | `closeMatch` | `bkp:253` |
| `mup:MUP-FW-PRESSURE-BOOSTER` | `relatedMatch` | `bkp:254` |
| `mup:MUP-FW-WATER-HEATER` | `closeMatch` | `bkp:242` |
| `mup:MUP-FW-WATER-HEATER` | `closeMatch` | `bkp:253` |
| `mup:MUP-HEAT-BOILER` | `closeMatch` | `bkp:242` |
| `mup:MUP-HEAT-BOILER` | `relatedMatch` | `bkp:241` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `closeMatch` | `bkp:242` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `relatedMatch` | `bkp:241` |
| `mup:MUP-HEAT-HEAT-PUMP` | `closeMatch` | `bkp:242` |
| `mup:MUP-SM-COMPRESSOR` | `closeMatch` | `bkp:247` |
| `mup:MUP-SM-COMPRESSOR` | `relatedMatch` | `bkp:247-1` |
| `mup:MUP-SM-FIRE-PUMP` | `closeMatch` | `bkp:252` |
| `mup:MUP-SM-FIRE-PUMP` | `relatedMatch` | `bkp:253` |
| `mup:MUP-SM-GAS-REGULATOR` | `closeMatch` | `bkp:253` |
| `mup:MUP-SM-GAS-REGULATOR` | `relatedMatch` | `bkp:254` |
| `mup:MUP-VENT-AHU` | `closeMatch` | `bkp:244` |
| `mup:MUP-VENT-AHU` | `relatedMatch` | `bkp:245` |
| `mup:MUP-VENT-FAN` | `closeMatch` | `bkp:244` |
| `mup:MUP-WW-GREASE-SEPARATOR` | `closeMatch` | `bkp:253` |
| `mup:MUP-WW-LIFTING-STATION` | `closeMatch` | `bkp:253` |
