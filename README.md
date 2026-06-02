
# Pragmatic BIM Data Contract 

## Why this exists

BIM data is hard to use.

Not because the data is missing, but because it is buried in complexity:

- IFC (Industry Foundation Classes) is powerful but:
  - too complex (hundreds of entities and deep relationships)
  - inconsistent across tools and projects
  - difficult to query for real workflows
  - mixes **performance** (what a product or assembly actually delivers) with
    **requirements** (what a project or regulation demands) in the same property
    sets and attributes, so compliance checks and product data stay entangled
  - treats **change** as an afterthought: revisions are file swaps, not structured
    diff records you can query, aggregate, or feed into workflows
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
- separates performance properties from requirement drivers so each can be queried,
  validated, and updated independently
- models change as first-class data (`Change` and its subclasses) rather
  than relying on opaque file diffs

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

```
pragmatic-bim-data-contract/
├── contract/           LinkML schema + IFC mapping (MIT)
├── classification/     SKOS vocabularies + mapping bridges (CC-BY-4.0)
├── scripts/            Build, merge, and publish tooling
└── site/               Generated schema docs and artifacts (do not edit)
```

| Path | Role |
|------|------|
| [`contract/`](contract/README.md) | LinkML schema YAML at folder root; IFC mapping in `contract/mapping/`. MIT. |
| [`classification/`](classification/README.md) | Abstract SKOS vocabularies and `mapping/` bridge files. CC-BY-4.0. |
| `scripts/` | Schema site build, IFC mapping merge, module page generation |
| `site/` | Generated schema documentation and artifacts (do not edit by hand) |

## How it fits in a workflow

1. Ingest BIM/IFC data with project-specific extraction logic.
2. Map extracted entities to this schema.
3. Store/query as graph or relational projections.
4. Enrich with requirements, performance metrics, schedules, and cost/material metadata.
5. Export, analyze, or feed application APIs.

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/simondilhas/pragmatic-bim-data-contract.git
   ```

2. Read [`contract/README.md`](contract/README.md) — schema modules, IFC mapping, hosted URIs, local docs build.
3. Read [`classification/README.md`](classification/README.md) — vocabularies and mapping bridges.
4. Browse the [hosted documentation](https://schema.pragmaticbim.ch/).

## Contributing

Contributions are welcome.

- Open an issue for bugs or feature proposals.
- Keep pull requests focused and small where possible.
- Add or update documentation when behavior changes.

## License

- **Contract (schema + IFC mapping) and repository code:** MIT — see [`LICENSE`](LICENSE).
- **Classification assets:** CC-BY-4.0 — see [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules).
t