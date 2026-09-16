# Abstract building elements to products mapping

Source: [`abstract-elements-to-products.mapping.ttl`](sources/mapping-elements-to-products.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Verknüpft jedes kostenrelevante Bauteil mit dem Produkt-SKOS-Schema, dessen Konzepte es für die Bepreisung differenzieren (pbs:productScheme), sowie mit dem Sammelprodukt als Rückfallwert, wenn ein Modell keine Produktklassifikation trägt (skos:closeMatch). Jedes Konzept des referenzierten Schemas ist ein gültiges Produkt für das Bauteil; alle teilen Referenzmenge und Verrechnungseinheit des Bauteils. Bauteile ohne pbs:productScheme haben noch kein Produktvokabular. Regenerieren mit scripts/generate_element_vocabulary.py.
- **description (en):** Links each cost-relevant building element to the product SKOS scheme whose concepts differentiate it for pricing (pbs:productScheme), plus the catch-all product used as fallback when a model carries no product classification (skos:closeMatch). Any concept of the referenced scheme is a valid product for the element; all of them share the element reference quantity and price unit. Elements without a pbs:productScheme have no product vocabulary yet. Regenerate with scripts/generate_element_vocabulary.py.
- **title (de):** Mapping abstrakter Bauteile zu Produkten
- **title (en):** Abstract building elements to products mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `el:ARC-BEAM` | `closeMatch` | `bmp:BMP-OTH` |
| `el:ARC-BEAM` | `productScheme` | `bmp:scheme` |
| `el:ARC-CEILING` | `closeMatch` | `ccp:CCP-OTH` |
| `el:ARC-CEILING` | `productScheme` | `ccp:scheme` |
| `el:ARC-COLUMN` | `closeMatch` | `clp:CLP-OTH` |
| `el:ARC-COLUMN` | `productScheme` | `clp:scheme` |
| `el:ARC-FLOOR-COV` | `closeMatch` | `fcp:FCP-OTH` |
| `el:ARC-FLOOR-COV` | `productScheme` | `fcp:scheme` |
| `el:ARC-FOOTING` | `closeMatch` | `fdp:FDP-OTH` |
| `el:ARC-FOOTING` | `productScheme` | `fdp:scheme` |
| `el:ARC-RAILING` | `closeMatch` | `rap:RAP-OTH` |
| `el:ARC-RAILING` | `productScheme` | `rap:scheme` |
| `el:ARC-ROOF-FLAT` | `closeMatch` | `rcp:RCP-OTH` |
| `el:ARC-ROOF-FLAT` | `productScheme` | `rcp:scheme` |
| `el:ARC-ROOF-PITCH` | `closeMatch` | `rcp:RCP-OTH` |
| `el:ARC-ROOF-PITCH` | `productScheme` | `rcp:scheme` |
| `el:ARC-SLAB-BALCONY` | `closeMatch` | `ssp:SSP-OTH` |
| `el:ARC-SLAB-BALCONY` | `productScheme` | `ssp:scheme` |
| `el:ARC-SLAB-BASE` | `closeMatch` | `fdp:FDP-OTH` |
| `el:ARC-SLAB-BASE` | `productScheme` | `fdp:scheme` |
| `el:ARC-SLAB-FLOOR` | `closeMatch` | `ssp:SSP-OTH` |
| `el:ARC-SLAB-FLOOR` | `productScheme` | `ssp:scheme` |
| `el:ARC-STAIR` | `closeMatch` | `srp:SRP-OTH` |
| `el:ARC-STAIR` | `productScheme` | `srp:scheme` |
| `el:ARC-WALL-CLAD` | `closeMatch` | `wcp:WCP-OTH` |
| `el:ARC-WALL-CLAD` | `productScheme` | `wcp:scheme` |
| `el:ARC-WALL-CLAD-EXT` | `closeMatch` | `facp:FaCP-OTHER` |
| `el:ARC-WALL-CLAD-EXT` | `productScheme` | `facp:scheme` |
| `el:ARC-WALL-EXT` | `closeMatch` | `swp:SWP-OTH` |
| `el:ARC-WALL-EXT` | `productScheme` | `swp:scheme` |
| `el:ARC-WALL-INT` | `closeMatch` | `swp:SWP-OTH` |
| `el:ARC-WALL-INT` | `productScheme` | `swp:scheme` |
| `el:ARC-WALL-INT-LB` | `closeMatch` | `swp:SWP-OTH` |
| `el:ARC-WALL-INT-LB` | `productScheme` | `swp:scheme` |
| `el:DOOR` | `closeMatch` | `dcp:DCP-OTH` |
| `el:DOOR` | `productScheme` | `dcp:scheme` |
| `el:WINDOW` | `closeMatch` | `wicp:WICP-OTH` |
| `el:WINDOW` | `productScheme` | `wicp:scheme` |
