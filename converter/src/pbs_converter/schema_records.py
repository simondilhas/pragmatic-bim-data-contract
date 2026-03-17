"""Typed records used across reader, mapper, validator, and DB writer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EntityRecord:
    """In-memory representation of one mapped entity."""

    id: str
    type: str
    name: str
    ifc_global_id: str | None = None
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RelationRecord:
    """In-memory representation of one mapped relation."""

    from_id: str
    relation_type: str
    to_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    source: str | None = None


@dataclass(slots=True)
class GeometryRecord:
    """In-memory representation of one geometry representation row."""

    entity_id: str
    geometry_representation: str
    geometry_format: str
    geometry_reference: str
    payload: dict[str, Any] = field(default_factory=dict)
    source: str | None = None
