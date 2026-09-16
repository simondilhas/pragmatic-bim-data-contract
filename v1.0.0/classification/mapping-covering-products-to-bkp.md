# Abstract covering products to BKP mapping

Source: [`abstract-covering-products-to-bkp.mapping.ttl`](sources/mapping-covering-products-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Bekleidungsprodukte BKP-Positionen zu: Ausbau 2 (281 Bodenbelaege, 282 Wandbelaege, 283 Deckenverkleidungen) und Rohbau 2 Fassadenbekleidungen (215.5 Aeuessere Verkleidungen, 226 Fassadenputze, 227 Aeuessere Oberflaechenbehandlungen). BKP-Untercodes mit Unterstrich (z. B. bkp:281_7 fuer BKP 281.7). Vollstaendiges BKP-Vokabular extern. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps abstract covering product concepts to BKP cost lines: Ausbau 2 (281 Bodenbelaege, 282 Wandbelaege, 283 Deckenverkleidungen) and Rohbau 2 facade cladding (215.5 Aeuessere Verkleidungen, 226 Fassadenputze, 227 Aeuessere Oberflaechenbehandlungen). BKP subcodes use underscore notation (e.g. bkp:281_7 for BKP 281.7). Full BKP vocabulary is external; only referenced IRIs are used. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
- **title (de):** Mapping abstrakter Bekleidungsprodukte nach BKP
- **title (en):** Abstract covering products to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ccp:CCP-GYPSUM-BOARD` | `closeMatch` | `bkp:283-2` |
| `ccp:CCP-METAL-GRID` | `closeMatch` | `bkp:283-7` |
| `ccp:CCP-METAL-PANEL` | `closeMatch` | `bkp:283-6` |
| `ccp:CCP-METAL-SHEET` | `closeMatch` | `bkp:283-1` |
| `ccp:CCP-MINERAL-FIBRE` | `closeMatch` | `bkp:283-3` |
| `ccp:CCP-SYNTHETIC` | `closeMatch` | `bkp:283-5` |
| `ccp:CCP-WOOD` | `closeMatch` | `bkp:283-4` |
| `fcp:FCP-ARTIFICIAL-STONE` | `closeMatch` | `bkp:281-5` |
| `fcp:FCP-CARPET` | `closeMatch` | `bkp:281-2` |
| `fcp:FCP-CERAMIC-TILE` | `closeMatch` | `bkp:281-6` |
| `fcp:FCP-LAMINATE` | `closeMatch` | `bkp:281-7` |
| `fcp:FCP-LINOLIUM` | `closeMatch` | `bkp:281-2` |
| `fcp:FCP-LVT` | `closeMatch` | `bkp:281-2` |
| `fcp:FCP-NATURAL-STONE` | `closeMatch` | `bkp:281-4` |
| `fcp:FCP-PARQUET` | `closeMatch` | `bkp:281-7` |
| `fcp:FCP-RAISED-FLOOR` | `closeMatch` | `bkp:281-8` |
| `fcp:FCP-SEAMLESS-RESIN` | `closeMatch` | `bkp:281-1` |
| `fcp:FCP-SUBFLOOR` | `closeMatch` | `bkp:281-0` |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `bkp:231` |
| `facp:FaCP-BIPV-INTEGRATED` | `relatedMatch` | `bkp:232` |
| `facp:FaCP-BRICK-SLIP` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-BRICK-SLIP` | `relatedMatch` | `bkp:211-6` |
| `facp:FaCP-CERAMIC-VENTILATED` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `closeMatch` | `bkp:227-1` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-HPL-PANEL` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-HPL-PANEL` | `relatedMatch` | `bkp:215-2` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `closeMatch` | `bkp:215-2` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `closeMatch` | `bkp:222` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `relatedMatch` | `bkp:215-2` |
| `facp:FaCP-NATURAL-STONE-VENTILATED` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-NATURAL-STONE-VENTILATED` | `relatedMatch` | `bkp:216-0` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `closeMatch` | `bkp:213-5` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `relatedMatch` | `bkp:215-2` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `closeMatch` | `bkp:214-4` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `closeMatch` | `bkp:226-2` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `bkp:226-1` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `closeMatch` | `bkp:226-2` |
| `facp:FaCP-SYNTHETIC-VENTILATED` | `closeMatch` | `bkp:215-5` |
| `facp:FaCP-TIMBER-VENTILATED` | `closeMatch` | `bkp:214-4` |
| `facp:FaCP-TIMBER-VENTILATED` | `closeMatch` | `bkp:215-5` |
| `wcp:WCP-ARTIFICIAL-STONE` | `closeMatch` | `bkp:282-3` |
| `wcp:WCP-CERAMIC-TILE` | `closeMatch` | `bkp:282-4` |
| `wcp:WCP-NATURAL-STONE` | `closeMatch` | `bkp:282-2` |
| `wcp:WCP-PAINT` | `relatedMatch` | `bkp:285` |
| `wcp:WCP-SEAMLESS-COATING` | `closeMatch` | `bkp:282-0` |
| `wcp:WCP-SYNTHETIC-PANEL` | `closeMatch` | `bkp:282-6` |
| `wcp:WCP-TEXTILE` | `closeMatch` | `bkp:282-6` |
| `wcp:WCP-WALLPAPER` | `closeMatch` | `bkp:282-1` |
| `wcp:WCP-WOOD-PANEL` | `closeMatch` | `bkp:282-5` |
