# Classification

SKOS vocabularies, mapping bridges, and reference diagrams for the data contract
`Classification` slot (`classification_scheme`, `classification_code`,
`classification_uri`, …).

- **classifications** — abstract vocabularies and crosswalks to project code lists
- **diagrams** — generated hierarchy and overview views (see [Presentation visualizations](#presentation-visualizations))

**License:** CC-BY-4.0 — sourced from [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules).

## Layout

```
classification/
├── abstract-room-classification/       # SKOS + JSON — space activity (area) vocabulary
├── abstract-room-name-classification/  # SKOS — normalized room name types
├── abstract-metric-definition/         # SKOS — building-level area, volume, count metrics
├── abstract-ratio-definition/          # SKOS — dimensionless building KPIs
├── abstract-separator-classification/  # SKOS — wall and slab separator roles
├── abstract-connector-classification/  # SKOS — physical connection types (door, window, duct, …)
├── abstract-roles/                     # SKOS + YAML
├── abstract-document-function/         # SKOS
├── abstract-material-classification/   # SKOS
├── abstract-covering-product-classification/  # SKOS — floor, wall, ceiling, facade, roof covering products
├── abstract-foundation-product-classification/  # SKOS — foundation products
├── abstract-separator-product-classification/  # SKOS — wall and slab separator products
├── abstract-connector-product-classification/  # SKOS — door and window connector products
├── abstract-mep-product-classification/  # SKOS — MEP unit and terminal products
├── abstract-usecase-classification/    # SKOS — project lifecycle use cases
├── abstract-person-relationship-classification/  # SKOS — CRM person relationship predicates
├── abstract-topic-classification/      # SKOS — general person interests for CRM/LLM extraction
├── abstract-company-sector-classification/  # SKOS — industry sectors for company classification
└── mapping/                            # bridge TTL files
```

| Path | Role |
|------|------|
| `abstract-room-classification/` | Building space and activity vocabulary |
| `abstract-room-name-classification/` | Normalized abstract room name types |
| `abstract-metric-definition/` | Building-level area, volume, and count metrics |
| `abstract-ratio-definition/` | Dimensionless building KPIs (quotients of metrics) |
| `abstract-separator-classification/` | Wall and slab separator roles |
| `abstract-connector-classification/` | Functional connection types (electrical, access, ventilation, …) |
| `abstract-roles/` | Workflow participant roles |
| `abstract-document-function/` | Document function vocabulary |
| `abstract-material-classification/` | Abstract material categories |
| `abstract-covering-product-classification/` | Floor, wall, ceiling, facade, and roof covering product types |
| `abstract-foundation-product-classification/` | Foundation product types (raft, strip, pile, slab-on-grade, …) |
| `abstract-separator-product-classification/` | Wall and slab separator product types (interior/exterior via wall role classification) |
| `abstract-connector-product-classification/` | Door and window connector product types (interior/exterior via BKP context) |
| `abstract-mep-product-classification/` | MEP unit (producer/converter) and terminal (end device) product types |
| `abstract-usecase-classification/` | Project lifecycle use cases (ordering, design, QA, construction, handover, operation, deconstruction) |
| `abstract-person-relationship-classification/` | CRM person relationship predicates (knows, works_at, key account manager, has_interest, …) |
| `abstract-topic-classification/` | General person interests (music, sport, travel, …) for CRM stories and LLM extraction |
| `abstract-company-sector-classification/` | Industry and sector taxonomy for classifying organizations in CRM |
| `mapping/` | Crosswalks from abstract concepts to external code lists (SIA, D0165, BKP, …) |

## Mapping bridges

| File | Links |
|------|-------|
| `mapping/connection-functional-to-physical-type.mapping.ttl` | Connection functional types → ConnectionPhysicalType enum values |
| `mapping/mep-product-to-connection-functional-type.mapping.ttl` | MEP unit and terminal products → ConnectionFunctionalType disciplines |
| `mapping/mep-product-to-ifc-class.mapping.ttl` | MEP unit and terminal products → IFC entity class hints |
| `mapping/separator-role-to-space-activity.mapping.ttl` | Abstract separator roles → space activity |
| `mapping/abstract-room-classification-to-d0165.mapping.ttl` | Space activity → SIA D0165 area codes |
| `mapping/d0165-to-abstract-room-classification.mapping.ttl` | D0165 → space activity (reverse) |
| `mapping/abstract-room-classification-to-sia416.mapping.ttl` | Space activity → SIA 416 area classes |
| `mapping/abstract-room-name-to-space-activity.mapping.ttl` | Room name → space activity |
| `mapping/room-name-notation-v1-to-v2.mapping.ttl` | Mnemonic v1 room name codes → numeric v2 codes |
| `mapping/armasuisse-room-name-to-abstract-room-name.mapping.ttl` | armasuisse Raumliste → abstract room names |
| `mapping/abstract-roles-to-bkp.mapping.ttl` | Workflow roles → BKP cost lines |
| `mapping/kbob-document-types-to-document-function.mapping.ttl` | KBOB/IPB document type catalogue → abstract document function classes |
| `mapping/abstract-material-to-uniclass-ma.mapping.ttl` | Abstract material → Uniclass Ma |
| `mapping/abstract-metric-to-sia416.mapping.ttl` | Abstract building metrics → SIA 416 |
| `mapping/abstract-metric-to-din277.mapping.ttl` | Abstract building metrics → DIN 277 |
| `mapping/abstract-metric-to-iso9836.mapping.ttl` | Abstract building metrics → ISO 9836 |
| `mapping/abstract-metric-to-rics-ipms.mapping.ttl` | Abstract building metrics → RICS IPMS |
| `mapping/abstract-ratio-to-sia416.mapping.ttl` | Abstract building ratios → SIA 416 quotients |
| `mapping/qto-buccaneer-to-abstract-metric.mapping.ttl` | qto_buccaneer metric keys → abstract metrics (guideline) |
| `mapping/qto-buccaneer-to-abstract-ratio.mapping.ttl` | qto_buccaneer ratio keys → abstract ratios (guideline) |
| `mapping/abstract-covering-products-to-material.mapping.ttl` | Abstract covering products → dominant material classes |
| `mapping/abstract-covering-products-to-bkp.mapping.ttl` | Abstract covering products → BKP 281/282/283 (Ausbau 2) and 215.5/226/227 (facade, Rohbau 2) |
| `mapping/abstract-foundation-products-to-bkp.mapping.ttl` | Abstract foundation products → BKP 216 / 211 (Rohbau 1) |
| `mapping/abstract-roof-covering-products-to-bkp.mapping.ttl` | Abstract roof covering products → BKP 224 (Rohbau 2) |
| `mapping/abstract-separator-products-to-material.mapping.ttl` | Abstract separator products → dominant material classes |
| `mapping/abstract-separator-products-to-bkp.mapping.ttl` | Abstract separator products → BKP 211–215 / 277 cost lines |
| `mapping/abstract-connector-products-to-material.mapping.ttl` | Abstract door and window connector products → dominant material classes |
| `mapping/abstract-connector-products-to-bkp.mapping.ttl` | Abstract door and window connector products → BKP 221.x / 272 / 273 / 224 cost lines |
| `mapping/kbob-ecobilans-baumat.skos.ttl` | KBOB ecobilans Baumaterialien vocabulary (row notations and IRIs; generated from Excel) |
| `mapping/kbob-ecobilans-layer-recipes.json` | Default layer quantity rules for composite product carbon decomposition |
| `mapping/abstract-floor-covering-products-to-kbob-ecobilans.mapping.ttl` | Abstract floor covering products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-wall-covering-products-to-kbob-ecobilans.mapping.ttl` | Abstract wall covering products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-ceiling-covering-products-to-kbob-ecobilans.mapping.ttl` | Abstract ceiling covering products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-facade-covering-products-to-kbob-ecobilans.mapping.ttl` | Abstract facade covering products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-roof-covering-products-to-kbob-ecobilans.mapping.ttl` | Abstract roof covering products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-wall-separator-products-to-kbob-ecobilans.mapping.ttl` | Abstract wall separator products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-slab-separator-products-to-kbob-ecobilans.mapping.ttl` | Abstract slab separator products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-window-connector-products-to-kbob-ecobilans.mapping.ttl` | Abstract window connector products → KBOB ecobilans Baumaterialien rows |
| `mapping/abstract-door-connector-products-to-kbob-ecobilans.mapping.ttl` | Abstract door connector products → KBOB ecobilans Baumaterialien rows |
| `mapping/person-relationship-type-to-target-kind.mapping.ttl` | Person relationship predicates → PersonRelationship target slot (related_person, related_company, related_topic) |

Bridge files reference external IRIs by code. Full proprietary KBOB vocabularies and LCA indicator values are **not** redistributed in this repository — only row notations, concept IRIs, and mapping links. Obtain indicator values from the official KBOB ecobilans dataset. Product scheme nodes declare the mapping bridge via `dcterms:references` (see covering, separator, and window connector product vocabularies).

Local authoring may use a gitignored JSON extract under `temp/` to validate mapping notations; do not commit KBOB workbook or JSON extracts.

## Subsystem product classification

Envelope products (facade `FaCP-*`, roof `RCP-*`, foundation `FDP-*`) follow a **subsystem model**: assign **one parent topConcept** per element. That code drives baseline cost as a bundled installation. Internal layer narrowers (`*-INS`, `*-SUB`, `*-FIN`, and legacy suffixes such as `*-RENDER`, `*-MEM`, `*-FRAME`) are **LCA decomposition only** — not user-assignable product classifications.

| Slot | Scheme | Required? | Drives cost? | Example |
|------|--------|-----------|--------------|---------|
| `classification_code` (primary) | Envelope product | Yes | Yes — whole subsystem | `FaCP-PREFAB-MODULAR-METAL` |
| LCA layer narrowers | Same envelope scheme | No | No — carbon only | `FaCP-RENDER-ETICS-WDVS-INS` |
| `material_category` or 2nd `classifications[]` | `abstract-material-classification` | Optional | No alone | `MAT-INS-MWO` |

**Carbon patterns:**

- **Bundled** — single KBOB row on the parent (e.g. `FaCP-PREFAB-MODULAR-METAL`, pitched roof tiles).
- **Layer recipe sum** — parent + `mapping/kbob-ecobilans-layer-recipes.json` decomposes into internal layers (e.g. `FaCP-RENDER-ETICS-WDVS`, `RCP-FLAT-BITUMEN`).

**Generic internal layer roles** (new systems): `-INS` (insulation), `-SUB` (substructure/frame), `-FIN` (finish/cladding/membrane). Legacy suffixes remain unchanged.

**`MAT-INS*` usage:** tags dominant **substance**, not envelope product type. Pair with a parent subsystem code when material is known. Use alone only as an early-design fallback when the system type is not yet known — resolve to a parent product before cost sign-off. Layer `-INS` narrowers map to `MAT-INS*` via [`abstract-covering-products-to-material.mapping.ttl`](mapping/abstract-covering-products-to-material.mapping.ttl).

**Assignment decision tree:**

```
Known subsystem type (ETICS, prefab metal, bitumen flat roof, raft foundation)?
  YES → classification_code = parent FaCP-* / RCP-* / FDP-*
        cost = parent baseline entry
        carbon = direct (bundled) OR layer_recipe_sum (composite)
        optional: material_category = MAT-INS* if substance known

Only material known, no system?
  YES → material_category = MAT-INS* (early design fallback)
        resolve to parent product before cost sign-off

BIM models separate insulation layer element?
  Prefer inherit parent subsystem from assembly/context;
  do NOT assign layer notation as primary classification_code
```

Do **not** use `MAT-INS` as primary `classification_code` on boundary elements when a subsystem parent exists. Do **not** add standalone assignable insulation topConcepts (e.g. generic roof insulation) — insulation belongs under the parent subsystem or as optional material metadata.

## MEP product classification

MEP unit (`MUP-*`) and terminal (`MTP-*`) products classify generating/converting plant and end devices on `Equipment`. They align with `SystemType.unit` and `SystemType.terminal` when elements are grouped in `IfcSystem`.

| Slot | Scheme | Required? | Example |
|------|--------|-----------|---------|
| `classifications[].classification_code` | `AbstractMepUnitProduct` or `AbstractMepTerminalProduct` | When product type is known | `MUP-VENT-AHU` |
| `equipment_type` | PBS enum | Yes (IFC-derived) | `hvac`, `electrical`, `plumbing`, `fire_safety`, `controls` |
| Parent `System.system_type` | PBS enum | When grouped in `IfcSystem` | `unit` vs `terminal` |
| Parent system functional context | Via system assignment | Validates discipline | ventilation system → `MUP-VENT-*` / `MTP-VENT-*` |

**Validation rule (documented, not enforced in schema yet):** the discipline token in `MUP-*` / `MTP-*` notation must be compatible with the parent system's `ConnectionFunctionalType` (via [`mep-product-to-connection-functional-type.mapping.ttl`](mapping/mep-product-to-connection-functional-type.mapping.ttl)). `MTP-FIRE-*` cross-cutting terminals are exempt — discipline is inherited from the inline host system.

**Notation:** `{PREFIX}-{DISC}-{PRODUCT}` where `PREFIX` is `MUP` or `MTP`, and `DISC` is `ELEC`, `DATA`, `VENT`, `HEAT`, `COOL`, `FW`, `WW`, `SM`, or `FIRE` (terminals only, cross-cutting).

IFC ingestion hints: [`mep-product-to-ifc-class.mapping.ttl`](mapping/mep-product-to-ifc-class.mapping.ttl).

## Room name notation (v2)

Building space name classification uses a three-level numeric code (similar to D0165 / Uniclass):

| Level | Pattern | Example | Assignable on `IfcSpace` |
|-------|---------|---------|--------------------------|
| Category | `RN-{CC}` | `RN-03` Circulation | No |
| Subgroup | `RN-{CC}-{GG}` | `RN-03-10` Horizontal circulation | No |
| Leaf | `RN-{CC}-{GG}-{LL}` | `RN-03-10-01` Corridor | Yes (`SpaceNameType`) |

- Source of truth: [`scripts/room_name_data.py`](../scripts/room_name_data.py)
- Regenerate SKOS, enum, and mappings: `python scripts/generate_room_name_vocabulary.py`
- v1 mnemonic codes (`RN-CIR-COR`, …) map to v2 via [`mapping/room-name-notation-v1-to-v2.mapping.ttl`](mapping/room-name-notation-v1-to-v2.mapping.ttl)
- Concept IRIs (`RN_CIR_COR`, …) are stable; only notation and enum keys changed

## Published documentation

Human-readable reference docs are generated from the SKOS and mapping TTL files:

- **Live site:** [schema.pragmaticbim.ch/classification](https://schema.pragmaticbim.ch/classification/)
- **Regenerate locally:** `python scripts/build_classification_docs.py` (or `python scripts/build_site.py` for schema + classifications)
- **Catalog:** [`catalog.yaml`](catalog.yaml) lists vocabularies and mappings included in the docs

Abstract product **unit prices** are a separate cost enrichment layer: [`contract/cost/`](../contract/cost/) (JSON in `baseline-unit-prices/` at repo root; see [`contract/cost/README.md`](../contract/cost/README.md)), keyed by SKOS product notation from the vocabularies above.

CI validates that committed `site/.md-src/classification/` matches the TTL sources (`schema-generation.yml`).

## Presentation visualizations

Generate interactive and static views from the repo root:

```bash
python classification/scripts/visualize.py
```

Outputs land in `classification/out/`:

| File | Use |
|------|-----|
| `room-hierarchy.html` | Full-screen sunburst (offline, no CDN); best for live presentation |
| `room-tree.svg` | Static tree for PowerPoint / Keynote / PDF |
| `room-hierarchy.mmd` | Mermaid source for Markdown-based slides |
| `classification-overview.html` | Room + separator vocabs + role→space mapping table |

Room-only (no separator/mapping pages):

```bash
python classification/scripts/visualize.py --room-only
```

## Related

- [`contract/README.md`](../contract/README.md) — data contract schema and `Classification` slot definition
- [`contract/mapping/README.md`](../contract/mapping/README.md) — IFC ingestion populates `classifications[]` from `IfcRelAssociatesClassification`
