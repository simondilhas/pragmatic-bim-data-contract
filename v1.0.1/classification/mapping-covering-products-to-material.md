# Abstract covering products to material mapping

Source: [`abstract-covering-products-to-material.mapping.ttl`](sources/mapping-covering-products-to-material.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Boden-, Wand-, Decken-, Fassaden-, Dach- und Fundamentbekleidungsprodukte dominanten Materialklassen zu. skos:closeMatch fuer primaere Substanz; skos:relatedMatch bei Verbund oder Variabilitaet.
- **description (en):** Maps abstract floor, wall, ceiling, facade, roof, and foundation covering product concepts to dominant-substance material classes. Uses skos:closeMatch for primary substance; skos:relatedMatch where composite or variable.
- **title (de):** Mapping abstrakter Bekleidungsprodukte nach Material
- **title (en):** Abstract covering products to material mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ccp:CCP-GYPSUM-BOARD` | `closeMatch` | `mat:MAT-GYP` |
| `ccp:CCP-METAL-GRID` | `closeMatch` | `mat:MAT-MET` |
| `ccp:CCP-METAL-PANEL` | `closeMatch` | `mat:MAT-MET` |
| `ccp:CCP-METAL-SHEET` | `closeMatch` | `mat:MAT-MET` |
| `ccp:CCP-MINERAL-FIBRE` | `closeMatch` | `mat:MAT-INS-MWO` |
| `ccp:CCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `ccp:CCP-SYNTHETIC` | `closeMatch` | `mat:MAT-PLA` |
| `ccp:CCP-WOOD` | `closeMatch` | `mat:MAT-WOD` |
| `fcp:FCP-ARTIFICIAL-STONE` | `closeMatch` | `mat:MAT-CONC` |
| `fcp:FCP-ARTIFICIAL-STONE` | `relatedMatch` | `mat:MAT-CMP` |
| `fcp:FCP-CARPET` | `closeMatch` | `mat:MAT-PLA` |
| `fcp:FCP-CARPET` | `relatedMatch` | `mat:MAT-CMP` |
| `fcp:FCP-CERAMIC-TILE` | `closeMatch` | `mat:MAT-MSN-CLY` |
| `fcp:FCP-LAMINATE` | `closeMatch` | `mat:MAT-WOD` |
| `fcp:FCP-LAMINATE` | `relatedMatch` | `mat:MAT-CMP` |
| `fcp:FCP-LINOLIUM` | `closeMatch` | `mat:MAT-PLA` |
| `fcp:FCP-LVT` | `closeMatch` | `mat:MAT-PLA` |
| `fcp:FCP-NATURAL-STONE` | `closeMatch` | `mat:MAT-MSN` |
| `fcp:FCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `fcp:FCP-PARQUET` | `closeMatch` | `mat:MAT-WOD` |
| `fcp:FCP-RAISED-FLOOR` | `closeMatch` | `mat:MAT-CMP` |
| `fcp:FCP-SEAMLESS-RESIN` | `closeMatch` | `mat:MAT-PLA` |
| `fcp:FCP-SUBFLOOR` | `closeMatch` | `mat:MAT-CONC` |
| `fcp:FCP-SUBFLOOR` | `relatedMatch` | `mat:MAT-CMP` |
| `fdp:FDP-DRAINAGE` | `closeMatch` | `mat:MAT-PLA` |
| `fdp:FDP-DRAINAGE` | `relatedMatch` | `mat:MAT-CMP` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-MICRO-PILE` | `relatedMatch` | `mat:MAT-MSN` |
| `fdp:FDP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `fdp:FDP-PAD` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-PILE` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-RAFT` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-RAFT` | `relatedMatch` | `mat:MAT-INS` |
| `fdp:FDP-RAFT-INS` | `closeMatch` | `mat:MAT-PLA` |
| `fdp:FDP-RAFT-INS` | `relatedMatch` | `mat:MAT-INS` |
| `fdp:FDP-RETAINING` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-RETAINING` | `relatedMatch` | `mat:MAT-INS` |
| `fdp:FDP-RETAINING-INS` | `closeMatch` | `mat:MAT-INS-MWO` |
| `fdp:FDP-RETAINING-INS` | `relatedMatch` | `mat:MAT-PLA` |
| `fdp:FDP-STRIP` | `closeMatch` | `mat:MAT-CONC` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `mat:MAT-ASP` |
| `fdp:FDP-WATERPROOF` | `relatedMatch` | `mat:MAT-PLA` |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-BIPV-INTEGRATED` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-BIPV-INTEGRATED` | `relatedMatch` | `mat:MAT-GLS` |
| `facp:FaCP-BRICK-SLIP` | `closeMatch` | `mat:MAT-MSN` |
| `facp:FaCP-BRICK-SLIP` | `relatedMatch` | `mat:MAT-MSN-CLY` |
| `facp:FaCP-CERAMIC-VENTILATED` | `closeMatch` | `mat:MAT-MSN-CLY` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `closeMatch` | `mat:MAT-CONC` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-HPL-PANEL` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-HPL-PANEL` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-NATURAL-STONE-VENTILATED` | `closeMatch` | `mat:MAT-MSN` |
| `facp:FaCP-OTHER` | `closeMatch` | `mat:MAT-OTH` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `relatedMatch` | `mat:MAT-INS` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `closeMatch` | `mat:MAT-WOD` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `relatedMatch` | `mat:MAT-INS` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `closeMatch` | `mat:MAT-CMP` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `mat:MAT-INS` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `mat:MAT-MSN` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `relatedMatch` | `mat:MAT-PLA` |
| `facp:FaCP-RENDER-ETICS-WDVS-INS` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-RENDER-ETICS-WDVS-INS` | `relatedMatch` | `mat:MAT-INS-MWO` |
| `facp:FaCP-RENDER-ETICS-WDVS-RENDER` | `closeMatch` | `mat:MAT-MSN` |
| `facp:FaCP-RENDER-ETICS-WDVS-RENDER` | `relatedMatch` | `mat:MAT-PLA` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `closeMatch` | `mat:MAT-CMP` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `relatedMatch` | `mat:MAT-INS` |
| `facp:FaCP-SYNTHETIC-VENTILATED` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-TIMBER-VENTILATED` | `closeMatch` | `mat:MAT-WOD` |
| `rcp:RCP-FLAT-BITUMEN` | `closeMatch` | `mat:MAT-ASP` |
| `rcp:RCP-FLAT-BITUMEN` | `relatedMatch` | `mat:MAT-INS` |
| `rcp:RCP-FLAT-BITUMEN` | `relatedMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-BITUMEN-INS` | `closeMatch` | `mat:MAT-INS` |
| `rcp:RCP-FLAT-BITUMEN-INS` | `relatedMatch` | `mat:MAT-INS-MWO` |
| `rcp:RCP-FLAT-BITUMEN-INS` | `relatedMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-BITUMEN-MEM` | `closeMatch` | `mat:MAT-ASP` |
| `rcp:RCP-FLAT-BITUMEN-MEM` | `relatedMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-LIQUID` | `closeMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-LIQUID` | `relatedMatch` | `mat:MAT-ASP` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `closeMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `relatedMatch` | `mat:MAT-INS` |
| `rcp:RCP-FLAT-SINGLE-PLY-INS` | `closeMatch` | `mat:MAT-INS` |
| `rcp:RCP-FLAT-SINGLE-PLY-INS` | `relatedMatch` | `mat:MAT-INS-MWO` |
| `rcp:RCP-FLAT-SINGLE-PLY-INS` | `relatedMatch` | `mat:MAT-PLA` |
| `rcp:RCP-FLAT-SINGLE-PLY-MEM` | `closeMatch` | `mat:MAT-PLA` |
| `rcp:RCP-GREEN-EXTENSIVE` | `closeMatch` | `mat:MAT-CMP` |
| `rcp:RCP-GREEN-EXTENSIVE` | `relatedMatch` | `mat:MAT-INS` |
| `rcp:RCP-GREEN-EXTENSIVE` | `relatedMatch` | `mat:MAT-PLA` |
| `rcp:RCP-GREEN-INTENSIVE` | `closeMatch` | `mat:MAT-CMP` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `mat:MAT-CONC` |
| `rcp:RCP-GREEN-INTENSIVE` | `relatedMatch` | `mat:MAT-INS` |
| `rcp:RCP-METAL-SHEET` | `closeMatch` | `mat:MAT-MET` |
| `rcp:RCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `rcp:RCP-PV-ROOF` | `closeMatch` | `mat:MAT-MET` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `mat:MAT-GLS` |
| `rcp:RCP-SLATE` | `closeMatch` | `mat:MAT-MSN` |
| `rcp:RCP-TILE-CLAY` | `closeMatch` | `mat:MAT-MSN-CLY` |
| `rcp:RCP-TILE-CONCRETE` | `closeMatch` | `mat:MAT-CONC` |
| `rcp:RCP-TILE-CONCRETE` | `relatedMatch` | `mat:MAT-CMP` |
| `rcp:RCP-WOOD-SHINGLE` | `closeMatch` | `mat:MAT-WOD` |
| `wcp:WCP-ARTIFICIAL-STONE` | `closeMatch` | `mat:MAT-CONC` |
| `wcp:WCP-ARTIFICIAL-STONE` | `relatedMatch` | `mat:MAT-CMP` |
| `wcp:WCP-CERAMIC-TILE` | `closeMatch` | `mat:MAT-MSN-CLY` |
| `wcp:WCP-NATURAL-STONE` | `closeMatch` | `mat:MAT-MSN` |
| `wcp:WCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `wcp:WCP-PAINT` | `closeMatch` | `mat:MAT-PLA` |
| `wcp:WCP-PAINT` | `relatedMatch` | `mat:MAT-CMP` |
| `wcp:WCP-SEAMLESS-COATING` | `closeMatch` | `mat:MAT-MSN` |
| `wcp:WCP-SEAMLESS-COATING` | `relatedMatch` | `mat:MAT-CMP` |
| `wcp:WCP-SYNTHETIC-PANEL` | `closeMatch` | `mat:MAT-PLA` |
| `wcp:WCP-TEXTILE` | `closeMatch` | `mat:MAT-PLA` |
| `wcp:WCP-WALLPAPER` | `closeMatch` | `mat:MAT-PLA` |
| `wcp:WCP-WALLPAPER` | `relatedMatch` | `mat:MAT-CMP` |
| `wcp:WCP-WOOD-PANEL` | `closeMatch` | `mat:MAT-WOD` |
