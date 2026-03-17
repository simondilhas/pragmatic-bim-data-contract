"""End-to-end pipeline for IFC conversion into the target database."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from pbs_converter.db import replace_relations, upsert_entities
from pbs_converter.ifc_reader import read_ifc
from pbs_converter.validator import RecordValidator


@dataclass(slots=True)
class PipelineStats:
    """Simple conversion stats for CLI output."""

    entities_written: int
    relations_written: int
    warnings: list[str]
    errors: list[str]


def run_ifc_conversion(
    *,
    session: Session,
    ifc_file: Path,
    enums_schema_file: Path,
    strict: bool = False,
) -> PipelineStats:
    """Read IFC, validate mapped records, and persist to DB."""
    read_result = read_ifc(ifc_file)
    validator = RecordValidator(enums_schema_file=enums_schema_file)
    validation = validator.validate(read_result.entities, read_result.relations, strict=strict)

    entities_written = upsert_entities(session, validation.entities)
    relations_written = replace_relations(session, validation.relations)
    session.commit()

    warnings = [*read_result.warnings, *validation.warnings]
    return PipelineStats(
        entities_written=entities_written,
        relations_written=relations_written,
        warnings=warnings,
        errors=validation.errors,
    )
