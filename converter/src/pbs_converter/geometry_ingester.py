"""Geometry ingestion helpers for IFC products."""

from __future__ import annotations

from typing import Any

from pbs_converter.schema_records import GeometryRecord

PLACEHOLDER_REPRESENTATIONS: tuple[str, ...] = ("axis", "body_3d", "footprint_2d")


def _coerce_float(value: Any) -> float | None:
    wrapped = getattr(value, "wrappedValue", value)
    try:
        return float(wrapped)
    except (TypeError, ValueError):
        return None


def _extract_placement_point(product: Any) -> tuple[float, float, float] | None:
    """Extract xyz from IFC local placement chain."""
    placement = getattr(product, "ObjectPlacement", None)
    visited: set[int] = set()
    while placement is not None and id(placement) not in visited:
        visited.add(id(placement))
        relative = getattr(placement, "RelativePlacement", None)
        location = getattr(relative, "Location", None) if relative is not None else None
        coordinates = getattr(location, "Coordinates", None) if location is not None else None
        if coordinates:
            x = _coerce_float(coordinates[0]) if len(coordinates) > 0 else None
            y = _coerce_float(coordinates[1]) if len(coordinates) > 1 else None
            z = _coerce_float(coordinates[2]) if len(coordinates) > 2 else 0.0
            if x is not None and y is not None and z is not None:
                return (x, y, z)
        placement = getattr(placement, "PlacementRelTo", None)
    return None


def build_geometry_records(product: Any, entity_id: str) -> tuple[list[GeometryRecord], list[str]]:
    """Build centroid and placeholder geometry records for one IFC product."""
    warnings: list[str] = []
    centroid = _extract_placement_point(product)
    if centroid is None:
        centroid = (0.0, 0.0, 0.0)
        warnings.append(f"Centroid fallback to origin for entity {entity_id}: placement not available")

    centroid_record = GeometryRecord(
        entity_id=entity_id,
        geometry_representation="point",
        geometry_format="json",
        geometry_reference=f"inline://{entity_id}/point",
        payload={"x": centroid[0], "y": centroid[1], "z": centroid[2]},
        source="ObjectPlacement",
    )

    placeholder_records = [
        GeometryRecord(
            entity_id=entity_id,
            geometry_representation=representation,
            geometry_format="placeholder",
            geometry_reference=f"placeholder://{entity_id}/{representation}",
            payload={},
            source="placeholder",
        )
        for representation in PLACEHOLDER_REPRESENTATIONS
    ]
    return ([centroid_record, *placeholder_records], warnings)
