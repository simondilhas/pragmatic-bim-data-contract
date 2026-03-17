"""Validation and normalization for mapped records."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from pbs_converter.mapping import ENUM_NAMES_BY_SLOT, EnumCatalog, REQUIRED_SLOTS_BY_CLASS
from pbs_converter.schema_records import EntityRecord, RelationRecord

IFC_GLOBAL_ID_PATTERN = re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")


@dataclass(slots=True)
class ValidationResult:
    """Validation output with normalized records and diagnostics."""

    entities: list[EntityRecord]
    relations: list[RelationRecord]
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


class RecordValidator:
    """Validate and normalize records against schema constraints."""

    def __init__(self, enums_schema_file: Path) -> None:
        self.enums = EnumCatalog.from_schema(enums_schema_file)

    def validate(self, entities: list[EntityRecord], relations: list[RelationRecord], strict: bool = False) -> ValidationResult:
        """Validate records and return normalized output."""
        warnings: list[str] = []
        errors: list[str] = []
        seen_ids: set[str] = set()
        filtered_entities: list[EntityRecord] = []

        for entity in entities:
            if entity.id in seen_ids:
                warnings.append(f"Duplicate entity id encountered and skipped: {entity.id}")
                continue
            seen_ids.add(entity.id)

            if entity.ifc_global_id and not IFC_GLOBAL_ID_PATTERN.match(entity.ifc_global_id):
                errors.append(f"Invalid IFC GlobalId format for entity {entity.id}: {entity.ifc_global_id}")
                continue

            required_slots = REQUIRED_SLOTS_BY_CLASS.get(entity.type, {"id", "name"})
            missing = [slot for slot in required_slots if not self._has_value(entity, slot)]
            if missing:
                errors.append(f"Missing required slot(s) for {entity.type}({entity.id}): {', '.join(sorted(missing))}")
                continue

            enum_errors = self._validate_entity_enums(entity)
            if enum_errors:
                errors.extend(enum_errors)
                continue
            filtered_entities.append(entity)

        entity_ids = {e.id for e in filtered_entities}
        filtered_relations: list[RelationRecord] = []
        for rel in relations:
            if rel.from_id not in entity_ids or rel.to_id not in entity_ids:
                warnings.append(
                    f"Dropping dangling relation {rel.relation_type}: {rel.from_id} -> {rel.to_id} (missing endpoint entity)"
                )
                continue
            filtered_relations.append(rel)

        if strict and errors:
            raise ValueError("Validation failed:\n" + "\n".join(errors))
        return ValidationResult(entities=filtered_entities, relations=filtered_relations, warnings=warnings, errors=errors)

    def _has_value(self, entity: EntityRecord, slot: str) -> bool:
        if slot == "id":
            return bool(entity.id)
        if slot == "name":
            return bool(entity.name)
        if slot == "ifc_global_id":
            return bool(entity.ifc_global_id)
        return bool(entity.payload.get(slot))

    def _validate_entity_enums(self, entity: EntityRecord) -> list[str]:
        errors: list[str] = []
        for slot, enum_name in ENUM_NAMES_BY_SLOT.items():
            value = entity.payload.get(slot)
            if value is None:
                continue
            enum_values = self.enums.values.get(enum_name, set())
            if isinstance(value, list):
                invalid = [item for item in value if item not in enum_values]
                if invalid:
                    errors.append(f"Invalid enum value(s) for {entity.id}.{slot}: {invalid} not in {enum_name}")
                continue
            if value not in enum_values:
                errors.append(f"Invalid enum value for {entity.id}.{slot}: {value} not in {enum_name}")
        return errors
