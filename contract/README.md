# Data contract

LinkML schema modules and declarative IFC → schema mapping for the pragmatic BIM data contract.

**License:** MIT (see repository root `LICENSE`).

## Layout

```
contract/
├── 00_pragmatic_bim_data_contract.yaml   # root entrypoint (imports all modules)
├── entity_core_schema.yaml
├── entity_physical_schema.yaml
├── entity_virtual_schema.yaml
├── entity_performance_schema.yaml
├── entity_schema_enums.yaml
├── entity_requirements_schema.yaml
├── changes_schema.yaml
├── changes_schema_enums.yaml
└── mappings/                             # IFC ingestion — see mappings/README.md
    ├── ifc_mapping.yaml
    ├── ifc_mapping.merged.yaml           # generated
    └── entities/
```

| File | Role |
|------|------|
| `00_pragmatic_bim_data_contract.yaml` | Root entrypoint importing all modules |
| `entity_core_schema.yaml` | `Entity` base, agents, documents, decisions, tasks, messages |
| `entity_physical_schema.yaml` | Physical element hierarchy |
| `entity_virtual_schema.yaml` | Virtual entities (`Space`, `System`, `TimeRecord`, …) |
| `entity_performance_schema.yaml` | Performance property classes on `Entity.performance_properties` |
| `entity_schema_enums.yaml` | Entity-graph enums with EN/DE labels |
| `entity_requirements_schema.yaml` | Requirement subclasses and requirement-driver slots |
| `changes_schema.yaml` | Typed change records |
| `changes_schema_enums.yaml` | Change enums (EN/DE labels) |
| `mappings/` | Declarative IFC → contract mapping |

Cross-cutting enums such as `ContentKind` and `StatusType` live in `entity_schema_enums.yaml`.

## Schema overview

The contract has two top-level concerns:

1. **Entity graph** — everything modeled, specified, or managed in the project. All graph nodes are `Entity` subclasses with uniform `id`, `content_kind`, `status`, `created_at`, and `applies_to_entities`. The `content_kind` slot discriminates branches: physical, virtual, context, requirement, document, decision, task, agent, and message. Normalized IFC performance values stay on `Entity.performance_properties` (not requirements).
2. **Change audit** — revision diff records as `Change` subclasses (`PropertyChange`, `GeometryChange`, `RequirementChange`, `MatchChange`, `AdditionChange`, `DeletionChange`). Change observes the graph between revisions; it is not an Entity and has no `content_kind`.

Full class hierarchy and reference tables: [schema documentation](https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html).

### Breaking change (major version)

Documents, decisions, tasks, and messages are now top-level entity records linked via `applies_to_entities` instead of being embedded on other entities. `ContentKind.change` is removed. Change records use typed references (`affected_subject`, `affected_requirement`, `related_requirement`, `triggered_task`) instead of bare string IDs where applicable.

## Modeling conventions

- Entity-to-entity relationships are modeled as ID references (`inlined: false`).
- Value objects that belong inside a record are embedded (`inlined: true`).
- `cost_category` and `material_category` are intentionally open text for now and can later be aligned with stronger classification systems.
- Units can be carried as plain strings for operational compatibility and optionally accompanied by unit URIs (for example QUDT) for stronger semantic alignment.

## IFC mapping

[`mappings/README.md`](mappings/README.md) documents the split YAML sources, merge workflow, database projection, and entity mapping rules. After editing mapping sources:

```bash
python scripts/merge_ifc_mapping.py
```

## Hosted URIs

Generated schema artifacts are published via GitHub Pages from stable release tags (`v*`).

- Stable landing page: `https://schema.pragmaticbim.ch/` (redirects to the docs index)
- Stable docs (HTML): `https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html`
- Stable JSON Schema: `https://schema.pragmaticbim.ch/schema/pragmatic-bim.schema.json`
- Stable SHACL: `https://schema.pragmaticbim.ch/schema/pragmatic-bim.shacl.ttl`
- Stable CSV: `https://schema.pragmaticbim.ch/schema/pragmatic-bim.csv`
- Stable Pydantic: `https://schema.pragmaticbim.ch/schema/pragmatic-bim.pydantic.py`
- Stable docs (Markdown, raw): `https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.md`
- Latest stable alias: `https://schema.pragmaticbim.ch/latest/`
- Version-pinned snapshot: `https://schema.pragmaticbim.ch/vX.Y.Z/`

### URI resolution

Human-readable documentation lives on one page: [`/schema/pragmatic-bim.docs.html`](https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html).

| Purpose | URL pattern | Example |
|---|---|---|
| Documentation index | `https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html` | main entry point |
| Module metadata (JSON) | `https://schema.pragmaticbim.ch/{slug}/descriptor.json` | [`/entity/virtual/descriptor.json`](https://schema.pragmaticbim.ch/entity/virtual/descriptor.json) |
| Class documentation | `https://schema.pragmaticbim.ch/schema/{ClassName}.html` | [`/schema/VirtualEntity.html`](https://schema.pragmaticbim.ch/schema/VirtualEntity.html) |
| Validation / codegen | `https://schema.pragmaticbim.ch/schema/pragmatic-bim.schema.json` | merged schema (all modules) |

Module slug → primary class doc:

| Module slug | Primary class docs |
|---|---|
| `entity/core` | `Entity.html` |
| `entity/virtual` | `VirtualEntity.html` |
| `entity/physical` | `PhysicalElement.html` |
| `entity/performance` | `FireProperty.html` |
| `entity/enums` | `ContentKind.html`, `RequirementTargetOperator.html`, `FirePropertyKey.html` |
| `entity/requirements` | `Requirement.html` |
| `changes` | `PropertyChange.html`, `Change.html` |
| `changes/enums` | `ChangeType.html` |

Module descriptors are generated by [`scripts/generate_module_pages.py`](../scripts/generate_module_pages.py) during the stable Pages release workflow.

## Local documentation build

Install tooling once, then build the full site from `contract/*.yaml`:

```bash
pip install -r requirements-docs.txt
python scripts/build_site.py
```

| Folder | Role |
|--------|------|
| `contract/` | LinkML source of truth (edit YAML here) |
| `site/` | Generated publish output (do not edit by hand) |

Main entry point: `site/schema/pragmatic-bim.docs.html`.

Optional live preview:

```bash
python scripts/build_site.py serve
```

Development and pull request validation remain in CI (`schema-generation.yml`) and are not deployed to the stable Pages root.

Classification vocabulary docs are published at [schema.pragmaticbim.ch/classification](https://schema.pragmaticbim.ch/classification/).

## Related

- [`classification/README.md`](../classification/README.md) — SKOS vocabularies and mapping bridges for the `Classification` slot
- [Classification docs (published)](../site/classification/index.html) — generated reference pages
