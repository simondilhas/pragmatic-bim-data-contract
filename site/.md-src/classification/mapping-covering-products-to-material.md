# Abstract covering products to material mapping

Source: [`abstract-covering-products-to-material.mapping.ttl`](sources/mapping-covering-products-to-material.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Boden-, Wand-, Decken- und Fassadenbekleidungsprodukte dominanten Materialklassen zu. skos:closeMatch fuer primaere Substanz; skos:relatedMatch bei Verbund oder Variabilitaet.
- **description (en):** Maps abstract floor, wall, ceiling, and facade covering product concepts to dominant-substance material classes. Uses skos:closeMatch for primary substance; skos:relatedMatch where composite or variable.
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
| `facp:FaCP-CERAMIC-TILE` | `closeMatch` | `mat:MAT-MSN-CLY` |
| `facp:FaCP-EXTERIOR-PAINT` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-EXTERIOR-PAINT` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-FIBRE-CEMENT` | `closeMatch` | `mat:MAT-CONC` |
| `facp:FaCP-FIBRE-CEMENT` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-METAL-PANEL` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-METAL-PANEL` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-METAL-SHEET` | `closeMatch` | `mat:MAT-MET` |
| `facp:FaCP-NATURAL-STONE` | `closeMatch` | `mat:MAT-MSN` |
| `facp:FaCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `facp:FaCP-RENDER` | `closeMatch` | `mat:MAT-MSN` |
| `facp:FaCP-RENDER` | `relatedMatch` | `mat:MAT-CMP` |
| `facp:FaCP-RENDER` | `relatedMatch` | `mat:MAT-INS-MWO` |
| `facp:FaCP-SYNTHETIC` | `closeMatch` | `mat:MAT-PLA` |
| `facp:FaCP-WOOD` | `closeMatch` | `mat:MAT-WOD` |
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
