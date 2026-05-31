<!-- schema-diagrams-preamble -->

## Schema diagrams

Generated from `schema/*.yaml`. See the [schema documentation](https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html) for interactive class pages.

### Module map

```mermaid
flowchart TB
  Root["Pragmatic BIM Data Contract"]
  Root --> core["Core"]
  Root --> performance_enums["Performance Enums"]
  Root --> requirements_enums["Requirements Enums"]
  Root --> performance["Performance"]
  Root --> requirements["Requirements"]
  Root --> elements_physical["Elements Physical"]
  Root --> elements_virtual["Elements Virtual"]
  Root --> enums["Enums"]
  Root --> changes["Changes"]
```

### Entity hierarchy (overview)

```mermaid
classDiagram
  direction TB
  Entity <|-- Agent
  Agent <|-- Company
  Agent <|-- Person
  Entity <|-- Message
  Entity <|-- PhysicalElement
  PhysicalElement <|-- Boundary
  PhysicalElement <|-- ConnectionPhysical
  PhysicalElement <|-- Equipment
  PhysicalElement <|-- Separator
  Entity <|-- ScheduleDependency
  Entity <|-- ScheduleItem
  ScheduleItem <|-- Milestone
  Entity <|-- ScheduleTemplate
  Entity <|-- VirtualEntity
  VirtualEntity <|-- AbstractCostRecord
  VirtualEntity <|-- ConnectionVirtual
  VirtualEntity <|-- Material
  VirtualEntity <|-- Space
  VirtualEntity <|-- SpatialContext
  VirtualEntity <|-- System
  PerformanceProperty <|-- AcousticProperty
  PerformanceProperty <|-- FireProperty
  PerformanceProperty <|-- MaterialProperty
  PerformanceProperty <|-- SecurityProperty
  PerformanceProperty <|-- StructuralProperty
  PerformanceProperty <|-- ThermalProperty
```

### Entity model

```mermaid
classDiagram
  direction TB
  Entity <|-- Agent
  Agent <|-- Company
  Agent <|-- Person
  Entity <|-- Message
  Entity <|-- PhysicalElement
  PhysicalElement <|-- Boundary
  PhysicalElement <|-- ConnectionPhysical
  PhysicalElement <|-- Equipment
  PhysicalElement <|-- Separator
  Separator <|-- SeparatorSlab
  Separator <|-- SeparatorWall
  Entity <|-- ScheduleDependency
  Entity <|-- ScheduleItem
  ScheduleItem <|-- Milestone
  Entity <|-- ScheduleTemplate
  Entity <|-- VirtualEntity
  VirtualEntity <|-- AbstractCostRecord
  AbstractCostRecord <|-- CostAssembly
  AbstractCostRecord <|-- CostItem
  VirtualEntity <|-- ConnectionVirtual
  VirtualEntity <|-- Material
  VirtualEntity <|-- Space
  VirtualEntity <|-- SpatialContext
  SpatialContext <|-- BuiltAssetContext
  BuiltAssetContext <|-- BuildingContext
  BuiltAssetContext <|-- CivilStructureContext
  SpatialContext <|-- LegalSiteContext
  SpatialContext <|-- LevelContext
  SpatialContext <|-- PerimeterContext
  SpatialContext <|-- ProjectContext
  SpatialContext <|-- ZoneContext
  VirtualEntity <|-- System
```

### Performance properties

```mermaid
classDiagram
  direction TB
  PerformanceProperty <|-- AcousticProperty
  PerformanceProperty <|-- FireProperty
  PerformanceProperty <|-- MaterialProperty
  PerformanceProperty <|-- SecurityProperty
  PerformanceProperty <|-- StructuralProperty
  PerformanceProperty <|-- ThermalProperty
```

