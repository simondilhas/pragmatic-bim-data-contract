"""SQLAlchemy ORM models for converter persistence."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.sqlite import JSON as SQLiteJSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import JSON


class Base(DeclarativeBase):
    """Declarative base for all models."""


class EntityModel(Base):
    """Canonical entity table."""

    __tablename__ = "entities"

    id: Mapped[str] = mapped_column(String(128), primary_key=True)
    type: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    ifc_global_id: Mapped[str | None] = mapped_column(String(22), nullable=True, index=True)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON().with_variant(SQLiteJSON, "sqlite"), default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    outgoing_relations: Mapped[list["RelationModel"]] = relationship(
        back_populates="from_entity",
        cascade="all, delete-orphan",
        foreign_keys="RelationModel.from_id",
    )
    incoming_relations: Mapped[list["RelationModel"]] = relationship(
        back_populates="to_entity",
        cascade="all, delete-orphan",
        foreign_keys="RelationModel.to_id",
    )
    geometries: Mapped[list["GeometryModel"]] = relationship(
        back_populates="entity",
        cascade="all, delete-orphan",
    )


class RelationModel(Base):
    """Canonical relation/edge table."""

    __tablename__ = "relations"
    __table_args__ = (
        UniqueConstraint("from_id", "relation_type", "to_id", name="uq_relation_triplet"),
        Index("ix_relations_relation_type", "relation_type"),
        Index("ix_relations_from_id", "from_id"),
        Index("ix_relations_to_id", "to_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_id: Mapped[str] = mapped_column(String(128), ForeignKey("entities.id", ondelete="CASCADE"), nullable=False)
    relation_type: Mapped[str] = mapped_column(String(128), nullable=False)
    to_id: Mapped[str] = mapped_column(String(128), ForeignKey("entities.id", ondelete="CASCADE"), nullable=False)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON().with_variant(SQLiteJSON, "sqlite"), default=dict)
    source: Mapped[str | None] = mapped_column(Text, nullable=True)

    from_entity: Mapped[EntityModel] = relationship(back_populates="outgoing_relations", foreign_keys=[from_id])
    to_entity: Mapped[EntityModel] = relationship(back_populates="incoming_relations", foreign_keys=[to_id])


class GeometryModel(Base):
    """Geometry representations attached to canonical entities."""

    __tablename__ = "entity_geometries"
    __table_args__ = (
        UniqueConstraint(
            "entity_id",
            "geometry_representation",
            "geometry_format",
            name="uq_entity_geometry_variant",
        ),
        Index("ix_entity_geometries_entity_id", "entity_id"),
        Index("ix_entity_geometries_representation", "geometry_representation"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    entity_id: Mapped[str] = mapped_column(String(128), ForeignKey("entities.id", ondelete="CASCADE"), nullable=False)
    geometry_representation: Mapped[str] = mapped_column(String(64), nullable=False)
    geometry_format: Mapped[str] = mapped_column(String(64), nullable=False)
    geometry_reference: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON().with_variant(SQLiteJSON, "sqlite"), default=dict)
    source: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    entity: Mapped[EntityModel] = relationship(back_populates="geometries")
