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
├── abstract-separator-classification/  # SKOS
├── abstract-roles/                     # SKOS + YAML
├── abstract-document-function/         # SKOS
├── abstract-material-classification/   # SKOS
├── abstract-covering-product-classification/  # SKOS — floor, wall, ceiling covering products
├── abstract-separator-product-classification/  # SKOS — wall and slab separator products
├── abstract-usecase-classification/    # SKOS — project lifecycle use cases
└── mapping/                            # bridge TTL files
```

| Path | Role |
|------|------|
| `abstract-room-classification/` | Building space and activity vocabulary |
| `abstract-room-name-classification/` | Normalized abstract room name types |
| `abstract-metric-definition/` | Building-level area, volume, and count metrics |
| `abstract-ratio-definition/` | Dimensionless building KPIs (quotients of metrics) |
| `abstract-separator-classification/` | Wall/slab separator roles and connection types |
| `abstract-roles/` | Workflow participant roles |
| `abstract-document-function/` | Document function vocabulary |
| `abstract-material-classification/` | Abstract material categories |
| `abstract-covering-product-classification/` | Floor, wall, and ceiling covering product types |
| `abstract-separator-product-classification/` | Wall and slab separator product types (interior/exterior via wall role classification) |
| `abstract-usecase-classification/` | Project lifecycle use cases (ordering, design, QA, construction, handover, operation, deconstruction) |
| `mapping/` | Crosswalks from abstract concepts to external code lists (SIA, D0165, BKP, …) |

## Mapping bridges

| File | Links |
|------|-------|
| `mapping/separator-role-to-space-activity.mapping.ttl` | Abstract separator roles → space activity |
| `mapping/abstract-room-classification-to-d0165.mapping.ttl` | Space activity → SIA D0165 area codes |
| `mapping/d0165-to-abstract-room-classification.mapping.ttl` | D0165 → space activity (reverse) |
| `mapping/abstract-room-classification-to-sia416.mapping.ttl` | Space activity → SIA 416 area classes |
| `mapping/abstract-room-name-to-space-activity.mapping.ttl` | Room name → space activity |
| `mapping/armasuisse-room-name-to-abstract-room-name.mapping.ttl` | armasuisse Raumliste → abstract room names |
| `mapping/abstract-roles-to-bkp.mapping.ttl` | Workflow roles → BKP cost lines |
| `mapping/abstract-material-to-uniclass-ma.mapping.ttl` | Abstract material → Uniclass Ma |
| `mapping/abstract-metric-to-sia416.mapping.ttl` | Abstract building metrics → SIA 416 |
| `mapping/abstract-metric-to-din277.mapping.ttl` | Abstract building metrics → DIN 277 |
| `mapping/abstract-metric-to-iso9836.mapping.ttl` | Abstract building metrics → ISO 9836 |
| `mapping/abstract-metric-to-rics-ipms.mapping.ttl` | Abstract building metrics → RICS IPMS |
| `mapping/abstract-ratio-to-sia416.mapping.ttl` | Abstract building ratios → SIA 416 quotients |
| `mapping/qto-buccaneer-to-abstract-metric.mapping.ttl` | qto_buccaneer metric keys → abstract metrics (guideline) |
| `mapping/qto-buccaneer-to-abstract-ratio.mapping.ttl` | qto_buccaneer ratio keys → abstract ratios (guideline) |
| `mapping/abstract-covering-products-to-material.mapping.ttl` | Abstract covering products → dominant material classes |
| `mapping/abstract-covering-products-to-bkp.mapping.ttl` | Abstract covering products → BKP 281/282/283 cost lines |
| `mapping/abstract-separator-products-to-material.mapping.ttl` | Abstract separator products → dominant material classes |
| `mapping/abstract-separator-products-to-bkp.mapping.ttl` | Abstract separator products → BKP 211–215 / 277 cost lines |

Bridge files reference external IRIs by code. Full proprietary vocabularies are not shipped in this repository.

## Published documentation

Human-readable reference docs are generated from the SKOS and mapping TTL files:

- **Live site:** [schema.pragmaticbim.ch/classification](https://schema.pragmaticbim.ch/classification/)
- **Regenerate locally:** `python scripts/build_classification_docs.py` (or `python scripts/build_site.py` for schema + classifications)
- **Catalog:** [`catalog.yaml`](catalog.yaml) lists vocabularies and mappings included in the docs

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
