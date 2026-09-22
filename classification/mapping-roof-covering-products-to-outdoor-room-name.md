# Roof covering products to outdoor room name mapping

Source: [`roof-covering-products-to-outdoor-room-name.mapping.ttl`](sources/mapping-roof-covering-products-to-outdoor-room-name.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Kompatibilitaetsverknuepfungen von Dachbekleidungsprodukten (RCP) zu Aussenraumnamen auf Flachdaechern und Dachplattformen (RN-OUT-*). skos:relatedMatch: ein Dachprodukt nennt typische Aussenraumtypen fuer diesen Aufbau. Raumnutzung bleibt ueber Raumnamen, Dachsystem ueber RCP. Schicht-narrower sind nicht gemappt. Nicht bijektiv — Disambiguierung in PBS-Regeln.
- **description (en):** Compatibility links from roof covering products (RCP) to outdoor room names on flat roofs and roof platforms (RN-OUT-*). Uses skos:relatedMatch: a roof product suggests typical outdoor space types where that build-up is commonly used. Space use remains assigned via room name; roof system remains assigned via RCP. Layer narrowers are not mapped. Not bijective — PBS rules disambiguate.
- **title (de):** Mapping Dachbekleidungsprodukte zu Aussenraumnamen
- **title (en):** Roof covering products to outdoor room name mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rcp:RCP-FLAT-BITUMEN` | `relatedMatch` | `rn:RN-OUT-RTR` |
| `rcp:RCP-FLAT-BITUMEN` | `relatedMatch` | `rn:RN-OUT-RWM` |
| `rcp:RCP-FLAT-BITUMEN` | `relatedMatch` | `rn:RN-OUT-TEQ` |
| `rcp:RCP-FLAT-LIQUID` | `relatedMatch` | `rn:RN-OUT-RTR` |
| `rcp:RCP-FLAT-LIQUID` | `relatedMatch` | `rn:RN-OUT-RWM` |
| `rcp:RCP-FLAT-LIQUID` | `relatedMatch` | `rn:RN-OUT-TEQ` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `relatedMatch` | `rn:RN-OUT-RTR` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `relatedMatch` | `rn:RN-OUT-RWM` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `relatedMatch` | `rn:RN-OUT-TEQ` |
| `rcp:RCP-GREEN-EXTENSIVE` | `relatedMatch` | `rn:RN-OUT-GRN` |
| `rcp:RCP-GREEN-EXTENSIVE` | `relatedMatch` | `rn:RN-OUT-RWM` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `rn:RN-OUT-GDN` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `rn:RN-OUT-GRN` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `rn:RN-OUT-RTR` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `rn:RN-OUT-RWM` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `rn:RN-OUT-TEQ` |
