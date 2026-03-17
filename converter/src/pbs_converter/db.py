"""Database helpers for SQLAlchemy engine, sessions, and upserts."""

from __future__ import annotations

from collections.abc import Iterable

from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from pbs_converter.models import Base, EntityModel, GeometryModel, RelationModel
from pbs_converter.schema_records import EntityRecord, GeometryRecord, RelationRecord


def build_engine(database_url: str) -> Engine:
    """Build SQLAlchemy engine from URL."""
    return create_engine(database_url, future=True)


def build_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Build configured session factory."""
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, future=True)


def create_schema(engine: Engine) -> None:
    """Create all tables without running alembic (used as fallback/dev helper)."""
    Base.metadata.create_all(engine)


def upsert_entities(session: Session, entities: Iterable[EntityRecord]) -> int:
    """Upsert entity records by ID."""
    count = 0
    for record in entities:
        existing = session.get(EntityModel, record.id)
        if existing is None:
            existing = EntityModel(
                id=record.id,
                type=record.type,
                name=record.name,
                ifc_global_id=record.ifc_global_id,
                payload=record.payload,
            )
            session.add(existing)
        else:
            existing.type = record.type
            existing.name = record.name
            existing.ifc_global_id = record.ifc_global_id
            existing.payload = record.payload
        count += 1
    return count


def replace_relations(session: Session, relations: Iterable[RelationRecord]) -> int:
    """Replace relation set by deleting existing same triplets first."""
    count = 0
    for record in relations:
        existing = session.execute(
            select(RelationModel).where(
                RelationModel.from_id == record.from_id,
                RelationModel.relation_type == record.relation_type,
                RelationModel.to_id == record.to_id,
            )
        ).scalar_one_or_none()
        if existing is None:
            existing = RelationModel(
                from_id=record.from_id,
                relation_type=record.relation_type,
                to_id=record.to_id,
                payload=record.payload,
                source=record.source,
            )
            session.add(existing)
        else:
            existing.payload = record.payload
            existing.source = record.source
        count += 1
    return count


def replace_geometries(session: Session, geometries: Iterable[GeometryRecord]) -> int:
    """Upsert geometry rows by entity+representation+format variant."""
    # Ensure pending geometry inserts from earlier operations are visible to lookups.
    session.flush()
    count = 0
    for record in geometries:
        existing = session.execute(
            select(GeometryModel).where(
                GeometryModel.entity_id == record.entity_id,
                GeometryModel.geometry_representation == record.geometry_representation,
                GeometryModel.geometry_format == record.geometry_format,
            )
        ).scalar_one_or_none()
        if existing is None:
            existing = GeometryModel(
                entity_id=record.entity_id,
                geometry_representation=record.geometry_representation,
                geometry_format=record.geometry_format,
                geometry_reference=record.geometry_reference,
                payload=record.payload,
                source=record.source,
            )
            session.add(existing)
        else:
            existing.geometry_reference = record.geometry_reference
            existing.payload = record.payload
            existing.source = record.source
        count += 1
    return count
