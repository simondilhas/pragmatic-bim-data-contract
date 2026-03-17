"""IFC-to-Pragmatic BIM mapping constants and mapping helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from pbs_converter.schema_records import EntityRecord, RelationRecord

IFC_CLASS_TO_PBS_TYPE: dict[str, str] = {
    "IfcProject": "ProjectContext",
    "IfcSite": "PerimeterContext",
    "IfcBuilding": "BuildingContext",
    "IfcBuildingStorey": "LevelContext",
    "IfcZone": "ZoneContext",
    "IfcSpace": "Space",
    "IfcSystem": "System",
    "IfcWall": "SeparatorWall",
    "IfcSlab": "SeparatorSlab",
    "IfcDoor": "ConnectionPhysical",
    "IfcWindow": "ConnectionPhysical",
    "IfcDuctSegment": "ConnectionPhysical",
    "IfcPipeSegment": "ConnectionPhysical",
    "IfcCableSegment": "ConnectionPhysical",
    "IfcCableCarrierSegment": "ConnectionPhysical",
    "IfcConduitSegment": "ConnectionPhysical",
    "IfcCovering": "Boundary",
    "IfcFlowTerminal": "Equipment",
    "IfcDistributionControlElement": "Equipment",
    "IfcUnitaryEquipment": "Equipment",
    "IfcElectricAppliance": "Equipment",
    "IfcSanitaryTerminal": "Equipment",
}

CLASS_DEFAULT_SLOT_VALUES: dict[str, dict[str, Any]] = {
    "ProjectContext": {"context_type": "project"},
    "PerimeterContext": {"context_type": "perimeter"},
    "BuildingContext": {"context_type": "building"},
    "LevelContext": {"context_type": "level"},
    "ZoneContext": {"context_type": "zone"},
    "Space": {"space_type": "usable"},
    "System": {"system_type": "network", "system_discipline": "ventilation"},
    "SeparatorWall": {"separator_wall_type": "unit_boundary"},
    "SeparatorSlab": {"separator_slab_type": "floor"},
    "ConnectionPhysical": {"connection_physical_type": "opening_other", "transport_medium": "human_access"},
    "Boundary": {"boundary_type": "cladding"},
    "Equipment": {"equipment_type": "other"},
}

IFC_CLASS_DEFAULT_SLOT_VALUES: dict[str, dict[str, Any]] = {
    "IfcDoor": {"connection_physical_type": "door", "transport_medium": "human_access"},
    "IfcWindow": {"connection_physical_type": "window", "transport_medium": "daylight_view"},
    "IfcDuctSegment": {"connection_physical_type": "duct", "transport_medium": "air"},
    "IfcPipeSegment": {"connection_physical_type": "pipe", "transport_medium": "liquid"},
    "IfcCableSegment": {"connection_physical_type": "cable", "transport_medium": "electricity"},
    "IfcCableCarrierSegment": {"connection_physical_type": "cable", "transport_medium": "electricity"},
    "IfcConduitSegment": {"connection_physical_type": "conduit", "transport_medium": "electricity"},
}

IFC_REL_CLASS_TO_RELATION_TYPE: dict[str, str] = {
    "IfcRelContainedInSpatialStructure": "contained_entities",
    "IfcRelAssignsToGroup": "group_members",
    "IfcRelAssignsToGroup:System": "contained_entities",
    "IfcRelSpaceBoundary": "bounded_by",
    "IfcRelConnectsElements": "connects_physical_elements",
}

IFC_SPATIAL_PARENT_SLOT: dict[str, str] = {
    "IfcProject": "",
    "IfcSite": "parent_project",
    "IfcBuilding": "parent_perimeter",
    "IfcBuildingStorey": "parent_building",
    "IfcSpace": "parent_level",
}

REQUIRED_SLOTS_BY_CLASS: dict[str, set[str]] = {
    "ProjectContext": {"id", "name", "context_type"},
    "PerimeterContext": {"id", "name", "context_type"},
    "BuildingContext": {"id", "name", "context_type"},
    "LevelContext": {"id", "name", "context_type"},
    "ZoneContext": {"id", "name", "context_type"},
    "Space": {"id", "name", "space_type"},
    "System": {"id", "name", "system_type", "system_discipline"},
    "SeparatorWall": {"id", "name", "separator_wall_type"},
    "SeparatorSlab": {"id", "name", "separator_slab_type"},
    "ConnectionPhysical": {"id", "name", "connection_physical_type", "transport_medium"},
    "Boundary": {"id", "name", "boundary_type"},
    "Equipment": {"id", "name", "equipment_type"},
}

ENUM_NAMES_BY_SLOT: dict[str, str] = {
    "context_type": "ContextType",
    "zone_type": "ZoneType",
    "space_type": "SpaceType",
    "system_type": "SystemType",
    "system_discipline": "SystemDiscipline",
    "equipment_type": "EquipmentType",
    "connection_physical_type": "ConnectionPhysicalType",
    "transport_medium": "TransportMedium",
    "connection_virtual_type": "ConnectionVirtualType",
    "connection_virtual_requirement_drivers": "ConnectionRequirementDriver",
    "connection_physical_requirement_drivers": "ConnectionRequirementDriver",
    "separator_wall_type": "SeparatorWallType",
    "separator_slab_type": "SeparatorSlabType",
    "separator_requirement_drivers": "SeparatorRequirementDriver",
    "boundary_type": "BoundaryType",
    "quantity_type": "QuantityType",
    "status": "StatusType",
}


@dataclass(slots=True)
class EnumCatalog:
    """Resolved enum values indexed by enum name."""

    values: dict[str, set[str]]

    @classmethod
    def from_schemas(cls, enums_schema_files: list[Path]) -> "EnumCatalog":
        """Load permissible enum values from one or more LinkML enums schema files."""
        values: dict[str, set[str]] = {}
        for enums_schema_file in enums_schema_files:
            with enums_schema_file.open("r", encoding="utf-8") as handle:
                parsed = yaml.safe_load(handle)
            for enum_name, enum_payload in (parsed.get("enums") or {}).items():
                permissible = enum_payload.get("permissible_values") or {}
                values[enum_name] = set(permissible.keys())
        return cls(values=values)


def map_ifc_product_to_entity(
    *,
    ifc_class_name: str,
    global_id: str,
    name: str | None,
    extra_payload: dict[str, Any] | None = None,
) -> EntityRecord | None:
    """Map one IFC class instance to Pragmatic BIM entity record."""
    pbs_type = IFC_CLASS_TO_PBS_TYPE.get(ifc_class_name)
    if pbs_type is None:
        return None
    payload: dict[str, Any] = {}
    payload.update(CLASS_DEFAULT_SLOT_VALUES.get(pbs_type, {}))
    payload.update(IFC_CLASS_DEFAULT_SLOT_VALUES.get(ifc_class_name, {}))
    if extra_payload:
        payload.update(extra_payload)
    entity_name = name or f"{ifc_class_name}-{global_id}"
    return EntityRecord(
        id=global_id,
        type=pbs_type,
        name=entity_name,
        ifc_global_id=global_id,
        payload=payload,
    )


def relation(from_id: str, relation_type: str, to_id: str, source: str | None = None) -> RelationRecord:
    """Create relation record with lightweight defaults."""
    return RelationRecord(from_id=from_id, relation_type=relation_type, to_id=to_id, payload={}, source=source)
