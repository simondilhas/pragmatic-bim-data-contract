# Classification

SKOS vocabularies and mapping bridges for the data contract `Classification` slot
(`classification_scheme`, `classification_code`, `classification_uri`, …).

**License:** CC-BY-4.0 — sourced from [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules).

## Layout

```
classification/
├── abstract-room-classification/       # SKOS + JSON
├── abstract-separator-classification/  # SKOS
├── abstract-roles/                     # SKOS + YAML
├── abstract-document-function/         # SKOS
├── abstract-material-classification/   # SKOS
├── abstract-usecase-classification/    # SKOS — project lifecycle use cases
└── mapping/                            # bridge TTL files
```

| Path | Role |
|------|------|
| `abstract-room-classification/` | Building space and activity vocabulary |
| `abstract-separator-classification/` | Wall/slab separator roles and connection types |
| `abstract-roles/` | Workflow participant roles |
| `abstract-document-function/` | Document function vocabulary |
| `abstract-material-classification/` | Abstract material categories |
| `abstract-usecase-classification/` | Project lifecycle use cases (ordering, design, QA, construction, handover, operation, deconstruction) |
| `mapping/` | Crosswalks from abstract concepts to external code lists (SIA, D0165, BKP, …) |

## Mapping bridges

| File | Links |
|------|-------|
| `mapping/separator-role-to-space-activity.mapping.ttl` | Abstract separator roles → space activity |
| `mapping/abstract-room-classification-to-d0165.mapping.ttl` | Space activity → SIA D0165 area codes |
| `mapping/d0165-to-abstract-room-classification.mapping.ttl` | D0165 → space activity (reverse) |
| `mapping/abstract-room-classification-to-sia416.mapping.ttl` | Space activity → SIA 416 area classes |
| `mapping/abstract-roles-to-bkp.mapping.ttl` | Workflow roles → BKP cost lines |
| `mapping/abstract-material-to-uniclass-ma.mapping.ttl` | Abstract material → Uniclass Ma |

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
