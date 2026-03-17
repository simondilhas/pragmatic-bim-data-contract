"""Initial converter schema.

Revision ID: 0001_initial
Revises:
Create Date: 2026-03-17
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create base tables for entities and relations."""
    op.create_table(
        "entities",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("type", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=512), nullable=False),
        sa.Column("ifc_global_id", sa.String(length=22), nullable=True),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_entities_type", "entities", ["type"], unique=False)
    op.create_index("ix_entities_ifc_global_id", "entities", ["ifc_global_id"], unique=False)

    op.create_table(
        "relations",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("from_id", sa.String(length=128), nullable=False),
        sa.Column("relation_type", sa.String(length=128), nullable=False),
        sa.Column("to_id", sa.String(length=128), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("source", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["from_id"], ["entities.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["to_id"], ["entities.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("from_id", "relation_type", "to_id", name="uq_relation_triplet"),
    )
    op.create_index("ix_relations_relation_type", "relations", ["relation_type"], unique=False)
    op.create_index("ix_relations_from_id", "relations", ["from_id"], unique=False)
    op.create_index("ix_relations_to_id", "relations", ["to_id"], unique=False)


def downgrade() -> None:
    """Drop converter tables."""
    op.drop_index("ix_relations_to_id", table_name="relations")
    op.drop_index("ix_relations_from_id", table_name="relations")
    op.drop_index("ix_relations_relation_type", table_name="relations")
    op.drop_table("relations")
    op.drop_index("ix_entities_ifc_global_id", table_name="entities")
    op.drop_index("ix_entities_type", table_name="entities")
    op.drop_table("entities")
