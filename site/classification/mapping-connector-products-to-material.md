# Abstract connector products to material mapping

Source: [`abstract-connector-products-to-material.mapping.ttl`](sources/mapping-connector-products-to-material.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Tuer- und Fenster-Verbindungsprodukte dominanten Materialklassen fuer Rahmen und Fuellung zu. skos:closeMatch fuer primaere Rahmensubstanz; skos:relatedMatch fuer Verglasung, Verbund oder variable Fuellung.
- **description (en):** Maps abstract door and window connector product concepts to dominant-substance material classes for frame and infill. Uses skos:closeMatch for primary frame substance; skos:relatedMatch for glazing, composite, or variable infill.
- **title (de):** Mapping abstrakter Verbindungsprodukte nach Material
- **title (en):** Abstract connector products to material mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `dcp:DCP-GATE` | `closeMatch` | `mat:MAT-MET-STL` |
| `dcp:DCP-GATE` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `dcp:DCP-GATE` | `relatedMatch` | `mat:MAT-PLA` |
| `dcp:DCP-GATE` | `relatedMatch` | `mat:MAT-WOD` |
| `dcp:DCP-GLASS` | `closeMatch` | `mat:MAT-GLS` |
| `dcp:DCP-GLASS` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `dcp:DCP-GLASS` | `relatedMatch` | `mat:MAT-MET-STL` |
| `dcp:DCP-METAL` | `closeMatch` | `mat:MAT-MET-STL` |
| `dcp:DCP-METAL` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `dcp:DCP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `dcp:DCP-PVC` | `closeMatch` | `mat:MAT-PLA` |
| `dcp:DCP-SPECIAL` | `closeMatch` | `mat:MAT-CMP` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `mat:MAT-GLS` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `mat:MAT-MET-STL` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `mat:MAT-WOD` |
| `dcp:DCP-WOOD` | `closeMatch` | `mat:MAT-WOD` |
| `dcp:DCP-WOOD-METAL` | `closeMatch` | `mat:MAT-WOD` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `mat:MAT-CMP` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `wicp:WICP-ALUMINIUM` | `closeMatch` | `mat:MAT-MET-ALU` |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `mat:MAT-GLS` |
| `wicp:WICP-FACADE-UNIT` | `closeMatch` | `mat:MAT-GLS` |
| `wicp:WICP-FACADE-UNIT` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `wicp:WICP-FACADE-UNIT` | `relatedMatch` | `mat:MAT-MET-STL` |
| `wicp:WICP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `wicp:WICP-PVC` | `closeMatch` | `mat:MAT-PLA` |
| `wicp:WICP-PVC` | `relatedMatch` | `mat:MAT-GLS` |
| `wicp:WICP-SKYLIGHT` | `closeMatch` | `mat:MAT-GLS` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `mat:MAT-PLA` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `mat:MAT-WOD` |
| `wicp:WICP-SPECIAL` | `closeMatch` | `mat:MAT-GLS` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `mat:MAT-CMP` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `mat:MAT-MET-ALU` |
| `wicp:WICP-STEEL` | `closeMatch` | `mat:MAT-MET-STL` |
| `wicp:WICP-STEEL` | `relatedMatch` | `mat:MAT-GLS` |
| `wicp:WICP-WOOD` | `closeMatch` | `mat:MAT-WOD` |
| `wicp:WICP-WOOD` | `relatedMatch` | `mat:MAT-GLS` |
| `wicp:WICP-WOOD-METAL` | `closeMatch` | `mat:MAT-WOD` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `mat:MAT-GLS` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `mat:MAT-MET-ALU` |
