from pathlib import Path

from sqlalchemy import select

from pbs_converter.db import build_engine, build_session_factory, create_schema, replace_geometries, replace_relations, upsert_entities
from pbs_converter.exporter import export_ndjson
from pbs_converter.models import GeometryModel
from pbs_converter.schema_records import EntityRecord, GeometryRecord, RelationRecord


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
    geometries = [
        GeometryRecord(
            entity_id="3H7gK7S6v3A8mM2f1ABC12",
            geometry_representation="point",
            geometry_format="json",
            geometry_reference="inline://3H7gK7S6v3A8mM2f1ABC12/point",
            payload={"x": 1.0, "y": 2.0, "z": 3.0},
        ),
        GeometryRecord(
            entity_id="3H7gK7S6v3A8mM2f1ABC12",
            geometry_representation="body_3d",
            geometry_format="placeholder",
            geometry_reference="placeholder://3H7gK7S6v3A8mM2f1ABC12/body_3d",
            payload={},
        ),
    ]

    with session_factory() as session:
        upsert_entities(session, entities)
        replace_relations(session, relations)
        replace_geometries(session, geometries)
        session.commit()
        out_dir = tmp_path / "out"
        entities_file, relations_file = export_ndjson(session, out_dir)

    assert entities_file.exists()
    assert relations_file.exists()


def test_replace_geometries_updates_same_variant(tmp_path: Path) -> None:
    db_path = tmp_path / "test_variants.db"
    database_url = f"sqlite:///{db_path}"
    engine = build_engine(database_url)
    create_schema(engine)
    session_factory = build_session_factory(engine)

    entities = [
        EntityRecord(
            id="3H7gK7S6v3A8mM2f1ABC12",
            type="Space",
            name="Room 101",
            ifc_global_id="3H7gK7S6v3A8mM2f1ABC12",
            payload={"space_type": "usable"},
        )
    ]

    with session_factory() as session:
        upsert_entities(session, entities)
        replace_geometries(
            session,
            [
                GeometryRecord(
                    entity_id="3H7gK7S6v3A8mM2f1ABC12",
                    geometry_representation="point",
                    geometry_format="json",
                    geometry_reference="inline://3H7gK7S6v3A8mM2f1ABC12/point",
                    payload={"x": 0.0, "y": 0.0, "z": 0.0},
                )
            ],
        )
        replace_geometries(
            session,
            [
                GeometryRecord(
                    entity_id="3H7gK7S6v3A8mM2f1ABC12",
                    geometry_representation="point",
                    geometry_format="json",
                    geometry_reference="inline://3H7gK7S6v3A8mM2f1ABC12/point",
                    payload={"x": 4.0, "y": 5.0, "z": 6.0},
                )
            ],
        )
        session.commit()

        rows = session.execute(select(GeometryModel)).scalars().all()
        assert len(rows) == 1
        assert rows[0].payload == {"x": 4.0, "y": 5.0, "z": 6.0}
