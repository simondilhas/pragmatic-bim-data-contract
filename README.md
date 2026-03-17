# pragmatic-bim-schema

Pragmatic BIM Data Contract

## Why this exists

BIM data is hard to use.

Not because the data is missing, but because it is buried in complexity:

- IFC (Industry Foundation Classes) is powerful but:
  - too complex (hundreds of entities and deep relationships)
  - inconsistent across tools and projects
  - difficult to query for real workflows
- IDS (Information Delivery Specification) focuses on data validation, but not on
  complex conditional validation logic (for example: if a building is below 25 m,
  staircase walls must be EI90).
- bSDD (buildingSMART Data Dictionary) focuses on classification, not workflows.

Result: teams cannot reliably build automation, dashboards, or simulations on top
of BIM data without heavy preprocessing.

## What this is

This project defines a pragmatic BIM data contract: a minimal, opinionated
structure for BIM data designed for workflows, not modeling.

It acts as a layer between:

- complex source data (for example IFC)
- and real applications (QTO, simulations, dashboards, quality checks)

## Core idea

Instead of trying to standardize everything, this contract:

- reduces complexity
- enforces consistency
- focuses on what is actually needed

It is intentionally limited.

## Principles

### 1) Not a replacement for IFC

This contract does not compete with IFC.

IFC remains:

- the exchange format
- the source of truth

This contract exists to make IFC usable in day-to-day workflows.

### 2) Designed for workflows, not modeling

This contract is built for:

- querying data
- running calculations
- feeding simulations
- building applications

Not for:

- authoring models
- preserving full semantic richness

### 3) Opinionated by design

Flexibility is often the enemy of automation. This contract intentionally:

- limits structure
- enforces naming
- reduces ambiguity

If your use case requires full flexibility, use IFC directly.

### 4) Abstraction over completeness

This project intentionally ignores large parts of IFC.

Only data required for real workflows is included.

### 5) Consistency over universality

This is not a universal standard.

It is a consistent contract that enables:

- repeatable queries
- predictable pipelines
- reliable automation

## What this enables

Using this contract, you can build:

- quantity takeoff pipelines
- room and space analysis
- simulation input models
- project dashboards
- validation workflows

Without having to:

- traverse complex IFC relationships
- handle inconsistent structures
- rebuild logic for every project

## Project structure

- `schema/00_pragmatic_bim_schema.yaml`: root schema entrypoint importing all modules.
- `schema/core_schema.yaml`: core entities and reusable base slots.
- `schema/performance_enums_schema.yaml`: enums for normalized performance properties.
- `schema/requirements_enums_schema.yaml`: enums for requirement drivers and assessment status.
- `schema/performance_schema.yaml`: domain-specific normalized performance property classes.
- `schema/requirements_schema.yaml`: requirement-driver slots and assessment structures.
- `schema/elements_physical_schema.yaml`: physical element hierarchy and element-related slots.
- `schema/elements_virtual_schema.yaml`: virtual entities (`SpatialContext`, `Space`, `System`, `ConnectionVirtual`, `CostItem`, `CostAssembly`, `Material`) and their slots.
- `schema/enums_schema.yaml`: controlled vocabularies.
- `schema/enum_localizations.yaml`: enum label/localization metadata.
- `converter/`: converter module for transforming data to and from the schema (see `converter/README.md`).

## Schema overview

The schema is organized into five core modules:

1. **Core schema** (`core_schema.yaml`)
   - shared base entity model (`Entity`), identifiers, lifecycle metadata, localization, geometry links, quantities, and extensible metadata.

2. **Physical elements** (`elements_physical_schema.yaml`)
   - tangible building components such as separators (walls/slabs), physical connections (e.g., doors/windows), and equipment.

3. **Virtual entities** (`elements_virtual_schema.yaml`)
   - non-physical structure and logic: spatial context hierarchy, spaces, systems, virtual connections, costs, and materials.

4. **Controlled vocabularies** (`enums_schema.yaml`)
   - canonical enums for consistent exchange and downstream logic.

5. **Localizations** (`enum_localizations.yaml`)
   - user-facing labels/translations for enums while preserving canonical values.

## Modeling conventions

- Entity-to-entity relationships are modeled as ID references (`inlined: false`).
- Value objects that belong inside a record are embedded (`inlined: true`).
- `cost_category` and `material_category` are intentionally open text for now and can later be aligned with stronger classification systems.

## How it fits in a workflow

1. Ingest BIM/IFC data with project-specific extraction logic.
2. Map extracted entities to this schema.
3. Store/query as graph or relational projections.
4. Enrich with requirements, performance metrics, and cost/material metadata.
5. Export, analyze, or feed application APIs.

## Getting started

1. Clone this repository.
2. Start with `schema/00_pragmatic_bim_schema.yaml` to understand module composition.
3. Inspect module definitions in `schema/`.
4. Use or extend the converter in `converter/`.
5. Follow `converter/README.md` for converter setup and commands.

## Hosted schema URIs (GitHub Pages)

Generated schema artifacts are published via GitHub Pages from CI.

- Landing page: `https://simondilhas.github.io/pragmatic-bim-schema/`
- Docs (HTML): `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.docs.html`
- JSON Schema: `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.schema.json`
- SHACL: `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.shacl.ttl`
- CSV: `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.csv`
- Pydantic: `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.pydantic.py`
- Docs (Markdown, raw): `https://simondilhas.github.io/pragmatic-bim-schema/schema/pragmatic-bim.docs.md`

Enable Pages once in repository settings:

1. Go to `Settings` -> `Pages`.
2. Under Build and deployment, set Source to `GitHub Actions`.

## Private extensions (SKOS/SPARQL)

Copyright-restricted norm translations and derived SPARQL rules should live in
an external private repository and be consumed as a submodule.

Recommended sibling checkout layout:

- `../pragmatic-bim-schema` (this repository)
- `../pragmatic-bim-classifications` (private repository)

Recommended submodule path in this repository:

- `external/classifications`

Submodule setup (run locally, outside this sandbox):

```bash
git submodule add git@github.com:simondilhas/pragmatic-bim-classifications.git external/classifications
git submodule update --init --recursive
```

Pinning to a tag/commit:

```bash
cd external/classifications
git fetch --tags
git checkout v2026.03
cd ../..
git add external/classifications .gitmodules
git commit -m "Pin classifications submodule to v2026.03"
```

## Contributing

Contributions are welcome.

- Open an issue for bugs or feature proposals.
- Keep pull requests focused and small where possible.
- Add or update documentation when behavior changes.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
