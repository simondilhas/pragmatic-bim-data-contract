from pathlib import Path

from pbs_converter.db import build_engine, build_session_factory, create_schema, replace_relations, upsert_entities
from pbs_converter.exporter import export_ndjson
from pbs_converter.schema_records import EntityRecord, RelationRecord


def test_sqlite_create_write_export(tmp_path: Path) -> None:
    db_path = tmp_path / "test.db"
    database_url = f"sqlite:///{db_path}"
    engine = build_engine(database_url)
    create_schema(engine)
    session_factory = build_session_factory(engine)

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

    with session_factory() as session:
        upsert_entities(session, entities)
        replace_relations(session, relations)
        session.commit()
        out_dir = tmp_path / "out"
        entities_file, relations_file = export_ndjson(session, out_dir)

    assert entities_file.exists()
    assert relations_file.exists()
