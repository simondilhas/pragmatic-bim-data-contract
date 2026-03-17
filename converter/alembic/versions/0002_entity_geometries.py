"""Add entity geometries table.

Revision ID: 0002_entity_geometries
Revises: 0001_initial
Create Date: 2026-03-17
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

revision = "0002_entity_geometries"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create table for geometry representations by entity."""
    op.create_table(
        "entity_geometries",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("entity_id", sa.String(length=128), nullable=False),
        sa.Column("geometry_representation", sa.String(length=64), nullable=False),
        sa.Column("geometry_format", sa.String(length=64), nullable=False),
        sa.Column("geometry_reference", sa.Text(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("source", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["entity_id"], ["entities.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "entity_id",
            "geometry_representation",
            "geometry_format",
            name="uq_entity_geometry_variant",
        ),
    )
    op.create_index("ix_entity_geometries_entity_id", "entity_geometries", ["entity_id"], unique=False)
    op.create_index("ix_entity_geometries_representation", "entity_geometries", ["geometry_representation"], unique=False)


def downgrade() -> None:
    """Drop geometry table."""
    op.drop_index("ix_entity_geometries_representation", table_name="entity_geometries")
    op.drop_index("ix_entity_geometries_entity_id", table_name="entity_geometries")
    op.drop_table("entity_geometries")
