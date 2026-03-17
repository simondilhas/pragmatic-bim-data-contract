# pragmatic-bim-schema

An open-source project for defining and using a pragmatic BIM schema.

## Why

After creating many data models, the same design questions keep coming up.
This project exists to capture those recurring decisions in one practical schema
that can be reused and evolved instead of reinvented each time.

## Project Structure

- `schema/00_pragmatic_bim_schema.yaml`: Root schema entrypoint importing all modules.
- `schema/core_schema.yaml`: Core entities and reusable base slots.
- `schema/performance_enums_schema.yaml`: Enums for normalized performance properties.
- `schema/requirements_enums_schema.yaml`: Enums for requirement drivers and assessment status.
- `schema/performance_schema.yaml`: Domain-specific normalized performance property classes.
- `schema/requirements_schema.yaml`: Requirement-driver slots and assessment structures.
- `schema/elements_physical_schema.yaml`: Physical element hierarchy and element-related slots.
- `schema/elements_virtual_schema.yaml`: Virtual entities (`SpatialContext`, `Space`, `System`, `ConnectionVirtual`, `CostItem`, `CostAssembly`, `Material`) and their slots.
- `schema/enums_schema.yaml`: All controlled vocabularies.
- `schema/enum_localizations.yaml`: Enum label/localization metadata.
- `converter/`: Converter module for transforming data to and from the schema. Setup, tests, and DB import/export commands are documented in `converter/README.md`.

## Schema Overview

The Pragmatic BIM Schema is a streamlined, graph-oriented data model designed
for BIM integration. It bridges the gap between complex IFC (Industry
Foundation Classes) data and practical analysis workflows such as costing and
querying.

The schema is structured into five core modules:

1. Core Schema (`core_schema.yaml`)

   The foundation of the model. It defines the abstract `Entity` base and
   shared metadata for all entity types.

   - Identification: local identifiers and IFC `ifc_global_id` mapping.
   - Localization: multilingual names/descriptions via `LocalizedText`.
   - Semantic hooks: optional `meaning_uri` for external ontology linking.
   - Quantities and geometry: one entity can link to multiple geometry
     representations and quantity records for different downstream intents.
   - Metadata and lifecycle: generic `metadata` entries plus `created_at`,
     `modified_at`, `revision`, and `status` support IFC property capture and
     QA/change tracking.

2. Physical Elements (`elements_physical_schema.yaml`)

   This module captures tangible building components.

   - Separators: abstract `Separator` base with concrete `SeparatorWall` and
     `SeparatorSlab`.
   - Requirement drivers: performance-oriented drivers (fire, acoustic,
     structural, etc.) for separators and physical connections.
   - Physical connections: opening elements (`ConnectionPhysical`) such as doors
     and windows.
   - Equipment: HVAC/electrical/plumbing elements linked to parent spaces and
     systems.

3. Virtual Entities (`elements_virtual_schema.yaml`)

   This module captures non-physical building logic.

   - Spatial context: a hierarchy (`project > perimeter > building > level >
     zone`) represented with `SpatialContext` using parent references as the
     single source of truth.
   - Spaces: occupancy/circulation/service/analysis containers.
   - Systems: service groupings serving spaces and zones.
   - Virtual connections: logical/topological connections between spaces and/or
     physical elements.
   - Costing and materials: `CostItem` and `CostAssembly` can be attached to
     entities; material specifications are modeled as first-class virtual
     entities.
   - Entry and traversal: `SpatialContext` is the root entry point
     (`tree_root: true`); `Space` is intentionally non-root and traversed via
     references/relationships in graph workflows.

4. Controlled Vocabularies (`enums_schema.yaml`)

   Ensures consistency through controlled enumerations.

   - IFC-aware mappings: many values map to `ifcowl` or `bot`.
   - Discipline logic: system/equipment categories for MEP domains.

5. Localizations (`enum_localizations.yaml`)

   Provides human-readable enum translations for UI/UX, without changing the
   underlying canonical values.

## Modeling Conventions

- Graph edges are modeled as ID references (`inlined: false`) for
  entity-to-entity relationships.
- Embedded (`inlined: true`) structures are reserved for value objects that are
  part of an entity record.
- `cost_category` and `material_category` are intentionally open text for now;
  they are planned to be replaced or complemented by classification-backed
  modeling in a later iteration.

## Goals

- Keep schema definitions clear and easy to evolve.
- Enable conversion workflows around a single source of truth schema.
- Stay simple and practical for real-world usage.

## Getting Started

1. Clone the repository.
2. Explore the schema files in `schema/`.
3. Use or implement converter logic in `converter/` as needed by your workflow.
4. For converter quickstart and command usage, follow `converter/README.md`.

## Private Extensions (SKOS/SPARQL)

Copyright-restricted norm translations and derived SPARQL rules should live in
a separate private repository and be consumed as a submodule.

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
