#!/usr/bin/env python3
"""Build the published schema site from schema/*.yaml (LinkML-first)."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA_ROOT = REPO_ROOT / "schema" / "00_pragmatic_bim_data_contract.yaml"
DEFAULT_SITE_SCHEMA = REPO_ROOT / "site" / "schema"
MAIN_ENTRY = DEFAULT_SITE_SCHEMA / "pragmatic-bim.docs.html"


def find_cmd(*names: str) -> str:
    for name in names:
        if shutil.which(name):
            return name
    raise SystemExit(f"No command found (tried: {', '.join(names)})")


def run_linkml_artifacts(schema_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_cmd = find_cmd("gen-csv", "csvgen")
    pydantic_cmd = find_cmd("gen-pydantic", "pydanticgen")

    def write_cmd_output(filename: str, cmd: list[str]) -> None:
        result = subprocess.run(cmd, check=True, cwd=REPO_ROOT, capture_output=True, text=True)
        (out_dir / filename).write_text(result.stdout, encoding="utf-8")

    write_cmd_output("pragmatic-bim.shacl.ttl", ["gen-shacl", str(schema_root)])
    write_cmd_output("pragmatic-bim.schema.json", ["gen-json-schema", str(schema_root)])
    write_cmd_output("pragmatic-bim.csv", [csv_cmd, str(schema_root)])
    write_cmd_output("pragmatic-bim.pydantic.py", [pydantic_cmd, str(schema_root)])


def build_site(*, schema_root: Path, site_dir: Path, base_url: str) -> None:
    schema_out = site_dir / "schema"
    run_linkml_artifacts(schema_root, schema_out)

    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--schema-root",
            str(schema_root),
            "--md-src",
            str(schema_out / ".md-src"),
            "--site-dir",
            str(schema_out),
        ],
        check=True,
        cwd=REPO_ROOT,
    )

    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "generate_module_pages.py"),
            "--site-dir",
            str(site_dir),
            "--schema-dir",
            str(schema_root.parent),
            "--base-url",
            base_url,
            "--write-root-index",
        ],
        check=True,
        cwd=REPO_ROOT,
    )


def check_site(*, schema_root: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--check",
            "--schema-root",
            str(schema_root),
        ],
        check=True,
        cwd=REPO_ROOT,
    )


def serve_site(*, schema_root: Path, site_dir: Path, base_url: str) -> None:
    build_site(schema_root=schema_root, site_dir=site_dir, base_url=base_url)
    subprocess.run(["mkdocs", "serve", "-f", str(REPO_ROOT / "mkdocs.yml")], check=True, cwd=REPO_ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        nargs="?",
        default="build",
        choices=("build", "check", "serve"),
        help="build (default), check, or serve",
    )
    parser.add_argument("--site-dir", type=Path, default=REPO_ROOT / "site")
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=Path(os.environ.get("SCHEMA_ROOT", DEFAULT_SCHEMA_ROOT)),
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("SCHEMA_BASE_URL", "https://schema.pragmaticbim.ch"),
    )
    args = parser.parse_args()

    if args.command == "check":
        check_site(schema_root=args.schema_root)
        return

    if args.command == "serve":
        serve_site(schema_root=args.schema_root, site_dir=args.site_dir, base_url=args.base_url)
        return

    build_site(schema_root=args.schema_root, site_dir=args.site_dir, base_url=args.base_url)
    print(f"Built site in {args.site_dir}")
    print(f"Main entry point: {MAIN_ENTRY}")


if __name__ == "__main__":
    main()
