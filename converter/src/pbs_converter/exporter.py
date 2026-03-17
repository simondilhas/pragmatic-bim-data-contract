"""Export DB contents to NDJSON for debugging and interchange."""

from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from pbs_converter.models import EntityModel, RelationModel


def export_ndjson(session: Session, output_dir: Path) -> tuple[Path, Path]:
    """Export entities and relations to separate NDJSON files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    entities_file = output_dir / "entities.ndjson"
    relations_file = output_dir / "relations.ndjson"

    with entities_file.open("w", encoding="utf-8") as handle:
        for entity in session.scalars(select(EntityModel).order_by(EntityModel.id)):
            row = {
                "id": entity.id,
                "type": entity.type,
                "name": entity.name,
                "ifc_global_id": entity.ifc_global_id,
                "payload": entity.payload,
            }
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")

    with relations_file.open("w", encoding="utf-8") as handle:
        for rel in session.scalars(select(RelationModel).order_by(RelationModel.id)):
            row = {
                "from_id": rel.from_id,
                "relation_type": rel.relation_type,
                "to_id": rel.to_id,
                "payload": rel.payload,
                "source": rel.source,
            }
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")

    return entities_file, relations_file
