# Pragmatic BIM Data Contract

A pragmatic, graph-first LinkML data contract for BIM integration, querying, costing, and analysis workflows.

<div class="pbs-doc-meta" markdown="1">

| | |
|---|---|
| **Schema URI** | [schema.pragmaticbim.ch](https://schema.pragmaticbim.ch/) |
| **Version** | [v0.1.7](https://github.com/simondilhas/pragmatic-bim-data-contract/releases/tag/v0.1.7) |
| **Source** | [github.com/simondilhas/pragmatic-bim-data-contract](https://github.com/simondilhas/pragmatic-bim-data-contract) |

</div>

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

Only data required for real decision workflows is included.

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

## How it fits in a workflow

1. Ingest BIM/IFC data with project-specific extraction logic.
2. Map extracted entities to this schema.
3. Store/query as graph or relational projections.
4. Enrich with requirements, performance metrics, schedules, and cost/material metadata.
5. Export, analyze, or feed application APIs.

## Products that use it

- [iterthink](https://www.iterthink.com/)
- [abstractBIM](https://www.abstractbim.com/)
- [{yourcompany}os](https://yourcompanyos.io/)

## Getting started

1. Browse the [Schema](schema/pragmatic-bim.docs.md) reference and download artifacts (JSON Schema, SHACL, CSV, Pydantic).
2. Read [Mappings to IFC](mapping/index.md) for declarative ingestion from IFC.
3. Explore [Classifications](classification/index.md) for SKOS vocabularies and mapping bridges.

## Governance

This contract is maintained by the Pragmatic BIM team. It is not governed by a formal standards body.

| | |
|---|---|
| **Maintainer** | Pragmatic BIM maintainers ([GitHub](https://github.com/simondilhas/pragmatic-bim-data-contract)) |
| **Change process** | [GitHub issues](https://github.com/simondilhas/pragmatic-bim-data-contract/issues) for proposals; focused pull requests for changes |
| **Release cadence** | Semantic version tags (`v*`) publish schema releases to [schema.pragmaticbim.ch](https://schema.pragmaticbim.ch/) |

**How to participate**

- **Proposals:** Open a [GitHub issue](https://github.com/simondilhas/pragmatic-bim-data-contract/issues) — bugs, gaps, new entities, classification requests.
- **Contributions:** Pull requests welcome; keep changes focused and include documentation updates.
- **Classifications:** Abstract vocabularies live in [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules); project-specific schemes live in this repository.

**Versioning**

- Releases are tagged `vMAJOR.MINOR.PATCH` on GitHub.
- Each tag publishes versioned snapshots at `schema.pragmaticbim.ch/<version>/` (for example `/v0.0.7/`).
- Breaking schema changes bump the major or minor version; patch releases are fixes and non-breaking additions.

There is no separate steering committee or public RFC process at this stage. Input via GitHub issues is the primary channel for community feedback.
