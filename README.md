# pragmatic-bim-schema

An open-source project for defining and using a pragmatic BIM schema.

## Why

After creating many data models, the same design questions keep coming up.
This project exists to capture those recurring decisions in one practical schema
that can be reused and evolved instead of reinvented each time.

## Project Structure

- `schema/00_pragmatic_bim_schema.yaml`: Root schema entrypoint importing all modules.
- `schema/core_schema.yaml`: Core entities and reusable base slots.
- `schema/elements_physical_schema.yaml`: Physical element hierarchy and element-related slots.
- `schema/elements_virtual_schema.yaml`: Virtual entities (`SpatialContext`, `Space`, `System`, `ConnectionVirtual`, `CostItem`, `CostAssembly`, `Material`) and their slots.
- `schema/enums_schema.yaml`: All controlled vocabularies.
- `schema/enum_localizations.yaml`: Enum label/localization metadata.
- `converter/`: Converter module for transforming data to and from the schema.

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

4. Controlled Vocabularies (`enums_schema.yaml`)

   Ensures consistency through controlled enumerations.

   - IFC-aware mappings: many values map to `ifcowl` or `bot`.
   - Discipline logic: system/equipment categories for MEP domains.

5. Localizations (`enum_localizations.yaml`)

   Provides human-readable enum translations for UI/UX, without changing the
   underlying canonical values.

## Goals

- Keep schema definitions clear and easy to evolve.
- Enable conversion workflows around a single source of truth schema.
- Stay simple and practical for real-world usage.

## Getting Started

1. Clone the repository.
2. Explore the schema files in `schema/`.
3. Use or implement converter logic in `converter/` as needed by your workflow.

## Contributing

Contributions are welcome.

- Open an issue for bugs or feature proposals.
- Keep pull requests focused and small where possible.
- Add or update documentation when behavior changes.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
