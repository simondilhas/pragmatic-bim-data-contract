#!/usr/bin/env python3
"""Build the published documentation site from contract/*.yaml and classification TTL."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA_ROOT = REPO_ROOT / "contract" / "00_pragmatic_bim_data_contract.yaml"
DEFAULT_SITE_DIR = REPO_ROOT / "site"
DEFAULT_MD_SRC = DEFAULT_SITE_DIR / ".md-src"
DEFAULT_HTML_BUILD = DEFAULT_SITE_DIR / ".html-build"
MAPPING_README = REPO_ROOT / "contract" / "mapping" / "README.md"
MKDOCS_CONFIG = REPO_ROOT / "mkdocs.yml"

BRAND_STYLESHEET = (
    REPO_ROOT / "docs-assets" / "material" / "assets" / "stylesheets" / "pragmatic-bim-brand.css"
)
BRAND_JAVASCRIPT = (
    REPO_ROOT
    / "docs-assets"
    / "material"
    / "assets"
    / "javascripts"
    / "classification-lang-switch.js"
)

SITE_ROOT_PRESERVE = {
    ".md-src",
    ".html-build",
    "entity",
    "modules.json",
    "versions.json",
}
SCHEMA_ARTIFACTS = {
    "pragmatic-bim.shacl.ttl",
    "pragmatic-bim.schema.json",
    "pragmatic-bim.csv",
    "pragmatic-bim.pydantic.py",
    "pragmatic-bim.docs.md",
}
CLASSIFICATION_PRESERVE = {"sources", "classifications.json"}
MKDOCS_OUTPUT_NAMES = {
    "assets",
    "search",
    "stylesheets",
    "javascripts",
    "404.html",
    "sitemap.xml",
    "sitemap.xml.gz",
}


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


def render_root_index_markdown() -> str:
    return """# Pragmatic BIM Data Contract

A pragmatic, graph-first LinkML data contract for BIM integration, querying, costing, and analysis workflows.

URI: https://schema.pragmaticbim.ch

## Sections

| Section | Description |
| --- | --- |
| [Schema](schema/pragmatic-bim.docs.md) | LinkML schema reference, classes, slots, and downloadable artifacts |
| [Mappings to IFC](mapping/index.md) | Declarative IFC ingestion mapping specification |
| [Classifications](classification/index.md) | SKOS vocabularies and mapping bridges for the `Classification` slot |

## Repository layout

| Path | Role |
| --- | --- |
| `contract/` | LinkML schema and IFC mapping (MIT) |
| `classification/` | SKOS vocabularies and mapping bridges (CC-BY-4.0) |
| `site/` | Generated documentation and schema artifacts |
"""


def write_mapping_index(md_src: Path) -> None:
    mapping_dir = md_src / "mapping"
    mapping_dir.mkdir(parents=True, exist_ok=True)
    if not MAPPING_README.is_file():
        raise SystemExit(f"IFC mapping README not found: {MAPPING_README}")
    shutil.copy2(MAPPING_README, mapping_dir / "index.md")


def write_root_index(md_src: Path) -> None:
    (md_src / "index.md").write_text(render_root_index_markdown(), encoding="utf-8")


def stage_brand_assets(md_src: Path) -> None:
    stylesheet_dir = md_src / "stylesheets"
    stylesheet_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_STYLESHEET, stylesheet_dir / "pragmatic-bim-brand.css")

    javascript_dir = md_src / "javascripts"
    javascript_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_JAVASCRIPT, javascript_dir / "classification-lang-switch.js")


def publish_schema_markdown(md_src: Path, site_schema_dir: Path) -> None:
    site_schema_dir.mkdir(parents=True, exist_ok=True)
    for md_file in md_src.glob("*.md"):
        shutil.copy2(md_file, site_schema_dir / md_file.name)


def publish_classification_markdown(md_src: Path, site_classification_dir: Path) -> None:
    site_classification_dir.mkdir(parents=True, exist_ok=True)
    for md_file in md_src.glob("*.md"):
        shutil.copy2(md_file, site_classification_dir / md_file.name)


def _remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def clear_section_html(section_dir: Path) -> None:
    if not section_dir.is_dir():
        return
    preserve = SCHEMA_ARTIFACTS if section_dir.name == "schema" else CLASSIFICATION_PRESERVE
    for item in section_dir.iterdir():
        if item.name in preserve:
            continue
        if item.name in MKDOCS_OUTPUT_NAMES or item.suffix in {".html", ".md"}:
            _remove_path(item)
        elif item.is_dir() and item.name in {"assets", "search", "stylesheets", "javascripts"}:
            _remove_path(item)


def clear_mkdocs_outputs(site_dir: Path) -> None:
    for item in site_dir.iterdir():
        if item.name in SITE_ROOT_PRESERVE:
            continue
        if item.name in MKDOCS_OUTPUT_NAMES or item.suffix == ".html":
            _remove_path(item)
        elif item.is_dir() and item.name in {"schema", "classification", "mapping"}:
            clear_section_html(item)


def merge_html_build(html_build: Path, site_dir: Path) -> None:
    if not html_build.is_dir():
        raise SystemExit(f"MkDocs output directory not found: {html_build}")
    clear_mkdocs_outputs(site_dir)
    for item in html_build.iterdir():
        dest = site_dir / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def run_mkdocs_build(*, html_build: Path) -> None:
    if html_build.exists():
        shutil.rmtree(html_build)
    subprocess.run(
        ["mkdocs", "build", "-f", str(MKDOCS_CONFIG), "-d", str(html_build)],
        check=True,
        cwd=REPO_ROOT,
    )


def build_site(*, schema_root: Path, site_dir: Path, base_url: str) -> None:
    md_src = site_dir / ".md-src"
    html_build = site_dir / ".html-build"
    schema_out = site_dir / "schema"
    classification_out = site_dir / "classification"

    run_linkml_artifacts(schema_root, schema_out)

    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--schema-root",
            str(schema_root),
            "--md-src",
            str(md_src / "schema"),
        ],
        check=True,
        cwd=REPO_ROOT,
    )

    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_classification_docs.py"),
            "--md-src",
            str(md_src / "classification"),
            "--site-dir",
            str(classification_out),
            "--base-url",
            base_url,
        ],
        check=True,
        cwd=REPO_ROOT,
    )

    write_root_index(md_src)
    write_mapping_index(md_src)
    stage_brand_assets(md_src)
    run_mkdocs_build(html_build=html_build)
    merge_html_build(html_build, site_dir)
    publish_schema_markdown(md_src / "schema", schema_out)
    publish_classification_markdown(md_src / "classification", classification_out)

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
        ],
        check=True,
        cwd=REPO_ROOT,
    )

    if html_build.exists():
        shutil.rmtree(html_build)


def check_site(*, schema_root: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--check",
            "--schema-root",
            str(schema_root),
            "--md-src",
            str(DEFAULT_MD_SRC / "schema"),
        ],
        check=True,
        cwd=REPO_ROOT,
    )
    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_classification_docs.py"),
            "--check",
            "--md-src",
            str(DEFAULT_MD_SRC / "classification"),
        ],
        check=True,
        cwd=REPO_ROOT,
    )


def serve_site(*, schema_root: Path, site_dir: Path, base_url: str) -> None:
    build_site(schema_root=schema_root, site_dir=site_dir, base_url=base_url)
    subprocess.run(["mkdocs", "serve", "-f", str(MKDOCS_CONFIG)], check=True, cwd=REPO_ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        nargs="?",
        default="build",
        choices=("build", "check", "serve"),
        help="build (default), check, or serve",
    )
    parser.add_argument("--site-dir", type=Path, default=DEFAULT_SITE_DIR)
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
    print(f"Main entry point: {args.site_dir / 'index.html'}")


if __name__ == "__main__":
    main()
