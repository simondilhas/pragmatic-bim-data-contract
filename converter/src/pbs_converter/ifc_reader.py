"""IFC reading utilities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pbs_converter.geometry_ingester import build_geometry_records
from pbs_converter.mapping import (
    IFC_SPATIAL_PARENT_SLOT,
    map_ifc_product_to_entity,
    relation,
)
from pbs_converter.schema_records import EntityRecord, GeometryRecord, RelationRecord

try:
    import ifcopenshell
except ImportError:  # pragma: no cover - handled at runtime
    ifcopenshell = None


@dataclass(slots=True)
class ReadResult:
    """Parsed and mapped records extracted from IFC."""

    entities: list[EntityRecord]
    relations: list[RelationRecord]
    geometries: list[GeometryRecord]
    warnings: list[str]


def _getattr_safe(obj: Any, attr: str, default: Any = None) -> Any:
    return getattr(obj, attr, default)


def _iter_ifc_objects(model: Any) -> list[Any]:
    classes = [
        "IfcProject",
        "IfcSite",
        "IfcBuilding",
        "IfcBuildingStorey",
        "IfcZone",
        "IfcSpace",
        "IfcSystem",
        "IfcWall",
        "IfcSlab",
        "IfcDoor",
        "IfcWindow",
        "IfcDuctSegment",
        "IfcPipeSegment",
        "IfcCableSegment",
        "IfcCableCarrierSegment",
        "IfcConduitSegment",
        "IfcCovering",
        "IfcFlowTerminal",
        "IfcDistributionControlElement",
        "IfcUnitaryEquipment",
        "IfcElectricAppliance",
        "IfcSanitaryTerminal",
    ]
    objects: list[Any] = []
    for cls in classes:
        objects.extend(model.by_type(cls))
    return objects


def read_ifc(ifc_path: Path) -> ReadResult:
    """Read IFC file and produce mapped entity/relation records."""
    if ifcopenshell is None:
        raise RuntimeError("ifcopenshell is required to parse IFC input. Install converter dependencies first.")
    model = ifcopenshell.open(str(ifc_path))
    entities: list[EntityRecord] = []
    relations: list[RelationRecord] = []
    geometries: list[GeometryRecord] = []
    warnings: list[str] = []

    for obj in _iter_ifc_objects(model):
        global_id = _getattr_safe(obj, "GlobalId")
        if not global_id:
            warnings.append(f"Skipping {obj.is_a()} without GlobalId")
            continue
        entity = map_ifc_product_to_entity(
            ifc_class_name=obj.is_a(),
            global_id=global_id,
            name=_getattr_safe(obj, "Name"),
        )
        if entity:
            entities.append(entity)
            geometry_records, geometry_warnings = build_geometry_records(obj, entity.id)
            geometries.extend(geometry_records)
            warnings.extend(geometry_warnings)

    # Spatial parent references from decomposition/containment heuristics.
    for rel in model.by_type("IfcRelAggregates"):
        parent = _getattr_safe(rel, "RelatingObject")
        parent_global = _getattr_safe(parent, "GlobalId")
        for child in _getattr_safe(rel, "RelatedObjects", []) or []:
            child_global = _getattr_safe(child, "GlobalId")
            if not parent_global or not child_global:
                continue
            slot = IFC_SPATIAL_PARENT_SLOT.get(child.is_a())
            if slot:
                relations.append(relation(child_global, slot, parent_global, source="IfcRelAggregates"))

    for rel in model.by_type("IfcRelContainedInSpatialStructure"):
        struct = _getattr_safe(rel, "RelatingStructure")
        struct_global = _getattr_safe(struct, "GlobalId")
        for child in _getattr_safe(rel, "RelatedElements", []) or []:
            child_global = _getattr_safe(child, "GlobalId")
            if child_global and struct_global:
                relations.append(relation(struct_global, "contained_entities", child_global, source="IfcRelContainedInSpatialStructure"))

    for rel in model.by_type("IfcRelAssignsToGroup"):
        group = _getattr_safe(rel, "RelatingGroup")
        group_global = _getattr_safe(group, "GlobalId")
        rel_type = "contained_entities" if _getattr_safe(group, "is_a", lambda: "")() == "IfcSystem" else "group_members"
        for child in _getattr_safe(rel, "RelatedObjects", []) or []:
            child_global = _getattr_safe(child, "GlobalId")
            if child_global and group_global:
                relations.append(relation(group_global, rel_type, child_global, source="IfcRelAssignsToGroup"))

    for rel in model.by_type("IfcRelSpaceBoundary"):
        space = _getattr_safe(rel, "RelatingSpace")
        element = _getattr_safe(rel, "RelatedBuildingElement")
        space_global = _getattr_safe(space, "GlobalId")
        element_global = _getattr_safe(element, "GlobalId")
        if space_global and element_global:
            relations.append(relation(space_global, "bounded_by", element_global, source="IfcRelSpaceBoundary"))

    for rel in model.by_type("IfcRelConnectsElements"):
        first = _getattr_safe(rel, "RelatingElement")
        second = _getattr_safe(rel, "RelatedElement")
        first_global = _getattr_safe(first, "GlobalId")
        second_global = _getattr_safe(second, "GlobalId")
        if first_global and second_global:
            relations.append(relation(first_global, "connects_physical_elements", second_global, source="IfcRelConnectsElements"))

    return ReadResult(entities=entities, relations=relations, geometries=geometries, warnings=warnings)
