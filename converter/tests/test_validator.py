from pathlib import Path

from pbs_converter.schema_records import EntityRecord, RelationRecord
from pbs_converter.validator import RecordValidator


def test_validator_accepts_valid_minimal_records() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    validator = RecordValidator(repo_root / "schema" / "enums_schema.yaml")
    entities = [
        EntityRecord(id="3H7gK7S6v3A8mM2f1ABC12", type="Space", name="Room 101", ifc_global_id="3H7gK7S6v3A8mM2f1ABC12", payload={"space_type": "usable"}),
        EntityRecord(
            id="1H7gK7S6v3A8mM2f1ABC12",
            type="BuildingContext",
            name="Building A",
            ifc_global_id="1H7gK7S6v3A8mM2f1ABC12",
            payload={"context_type": "building"},
        ),
    ]
    relations = [RelationRecord(from_id="1H7gK7S6v3A8mM2f1ABC12", relation_type="contained_entities", to_id="3H7gK7S6v3A8mM2f1ABC12")]
    result = validator.validate(entities, relations)
    assert result.errors == []
    assert len(result.entities) == 2
    assert len(result.relations) == 1


def test_validator_rejects_invalid_enum_value() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    validator = RecordValidator(repo_root / "schema" / "enums_schema.yaml")
    entities = [
        EntityRecord(
            id="3H7gK7S6v3A8mM2f1ABC12",
            type="Space",
            name="Room 102",
            ifc_global_id="3H7gK7S6v3A8mM2f1ABC12",
            payload={"space_type": "NOT_VALID"},
        )
    ]
    result = validator.validate(entities, [])
    assert any("space_type" in e for e in result.errors)
