"""CLI entrypoint for converter workflows."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from alembic import command
from alembic.config import Config

from pbs_converter.config import get_default_database_url
from pbs_converter.db import build_engine, build_session_factory
from pbs_converter.exporter import export_ndjson
from pbs_converter.pipeline import run_ifc_conversion


def _repo_root_from_here() -> Path:
    # converter/src/pbs_converter/cli.py -> repo root
    return Path(__file__).resolve().parents[3]


def _converter_root_from_here() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pbs-converter", description="Pragmatic BIM IFC converter")
    sub = parser.add_subparsers(dest="command", required=True)

    init_db = sub.add_parser("init-db", help="Create or migrate DB schema")
    init_db.add_argument("--database-url", default=get_default_database_url(), help="SQLAlchemy DB URL")

    convert = sub.add_parser("convert-ifc", help="Convert one IFC file and upsert into DB")
    convert.add_argument("--ifc-file", required=True, help="Path to IFC file")
    convert.add_argument("--database-url", default=get_default_database_url(), help="SQLAlchemy DB URL")
    convert.add_argument("--strict", action="store_true", help="Fail fast on validation errors")

    export = sub.add_parser("export-ndjson", help="Export DB contents to NDJSON")
    export.add_argument("--out-dir", required=True, help="Output directory for NDJSON files")
    export.add_argument("--database-url", default=get_default_database_url(), help="SQLAlchemy DB URL")
    return parser


def _alembic_upgrade_head(database_url: str) -> None:
    converter_root = _converter_root_from_here()
    cfg = Config(str(converter_root / "alembic.ini"))
    cfg.set_main_option("script_location", str(converter_root / "alembic"))
    cfg.set_main_option("sqlalchemy.url", database_url)
    command.upgrade(cfg, "head")


def _run_init_db(args: argparse.Namespace) -> None:
    _alembic_upgrade_head(args.database_url)
    print(f"Database initialized: {args.database_url}")


def _run_convert_ifc(args: argparse.Namespace) -> None:
    _alembic_upgrade_head(args.database_url)
    engine = build_engine(args.database_url)
    session_factory = build_session_factory(engine)
    repo_root = _repo_root_from_here()
    enum_schemas = [
        repo_root / "schema" / "enums_schema.yaml",
        repo_root / "schema" / "performance_enums_schema.yaml",
        repo_root / "schema" / "requirements_enums_schema.yaml",
    ]
    ifc_file = Path(args.ifc_file).resolve()

    with session_factory() as session:
        stats = run_ifc_conversion(
            session=session,
            ifc_file=ifc_file,
            enums_schema_files=enum_schemas,
            strict=args.strict,
        )
    print(f"Entities written: {stats.entities_written}")
    print(f"Relations written: {stats.relations_written}")
    print(f"Geometries written: {stats.geometries_written}")
    if stats.warnings:
        print("Warnings:")
        for warning in stats.warnings:
            print(f"- {warning}")
    if stats.errors:
        print("Validation errors:")
        for error in stats.errors:
            print(f"- {error}")


def _run_export_ndjson(args: argparse.Namespace) -> None:
    engine = build_engine(args.database_url)
    session_factory = build_session_factory(engine)
    out_dir = Path(args.out_dir).resolve()
    with session_factory() as session:
        entities_file, relations_file = export_ndjson(session, out_dir)
    print(f"Wrote {entities_file}")
    print(f"Wrote {relations_file}")


def main() -> None:
    """Run CLI."""
    parser = _build_parser()
    args = parser.parse_args()
    # make alembic import resolution deterministic for local runs
    os.environ.setdefault("PYTHONPATH", str(_converter_root_from_here() / "src"))
    if args.command == "init-db":
        _run_init_db(args)
        return
    if args.command == "convert-ifc":
        _run_convert_ifc(args)
        return
    if args.command == "export-ndjson":
        _run_export_ndjson(args)
        return
    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
