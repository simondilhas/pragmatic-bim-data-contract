#!/usr/bin/env python3
"""Build the published documentation site from contract/*.yaml and classification TTL."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA_ROOT = REPO_ROOT / "contract" / "00_pragmatic_bim_data_contract.yaml"
DEFAULT_COST_SCHEMA_ROOT = REPO_ROOT / "contract" / "cost" / "baseline_cost_schema.yaml"
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
MERMAID_INIT_JAVASCRIPT = (
    REPO_ROOT
    / "docs-assets"
    / "material"
    / "assets"
    / "javascripts"
    / "mermaid-init.js"
)
VERSION_SELECTOR_JAVASCRIPT = (
    REPO_ROOT
    / "docs-assets"
    / "material"
    / "assets"
    / "javascripts"
    / "version-selector.js"
)
GITHUB_REPO = "https://github.com/simondilhas/pragmatic-bim-data-contract"

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
COST_SCHEMA_ARTIFACTS = {
    "baseline-cost.shacl.ttl",
    "baseline-cost.schema.json",
    "baseline-cost.csv",
    "baseline-cost.pydantic.py",
    "baseline-cost.docs.md",
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


def resolve_repo_path(path: Path) -> Path:
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def run_linkml_artifacts(schema_root: Path, out_dir: Path, *, prefix: str = "pragmatic-bim") -> None:
    schema_root = resolve_repo_path(schema_root)
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_cmd = find_cmd("gen-csv", "csvgen")
    pydantic_cmd = find_cmd("gen-pydantic", "pydanticgen")

    def write_cmd_output(filename: str, cmd: list[str]) -> None:
        result = subprocess.run(cmd, check=True, cwd=REPO_ROOT, capture_output=True, text=True)
        (out_dir / filename).write_text(result.stdout, encoding="utf-8")

    schema_arg = schema_root.relative_to(REPO_ROOT).as_posix()
    write_cmd_output(f"{prefix}.shacl.ttl", ["gen-shacl", schema_arg])
    write_cmd_output(f"{prefix}.schema.json", ["gen-json-schema", schema_arg])
    write_cmd_output(f"{prefix}.csv", [csv_cmd, schema_arg])
    write_cmd_output(f"{prefix}.pydantic.py", [pydantic_cmd, schema_arg])


def resolve_release_version(site_dir: Path) -> str:
    env_version = os.environ.get("RELEASE_VERSION")
    if env_version:
        return env_version

    versions_file = site_dir / "versions.json"
    if versions_file.is_file():
        try:
            data = json.loads(versions_file.read_text(encoding="utf-8"))
            latest = data.get("latest")
            if isinstance(latest, str) and latest:
                return latest
        except (json.JSONDecodeError, OSError):
            pass

    result = subprocess.run(
        ["git", "tag", "-l", "v*", "--sort=-v:refname"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode == 0:
        tags = [tag for tag in result.stdout.splitlines() if tag.strip()]
        if tags:
            return tags[0]
    return "dev"


def render_root_index_markdown(version: str) -> str:
    version_label = version if version != "dev" else "development"
    version_href = (
        f"{GITHUB_REPO}/releases/tag/{version}"
        if version != "dev"
        else GITHUB_REPO
    )
    return f"""# Pragmatic BIM Data Contract

A pragmatic, graph-first LinkML data contract for BIM integration, querying, costing, and analysis workflows.

<div class="pbs-doc-meta" markdown="1">

| | |
|---|---|
| **Schema URI** | [schema.pragmaticbim.ch](https://schema.pragmaticbim.ch/) |
| **Version** | [{version_label}]({version_href}) |
| **Source** | [github.com/simondilhas/pragmatic-bim-data-contract]({GITHUB_REPO}) |

</div>

## Why this exists

BIM data is hard to use.

Not because the data is missing, but because it is buried in complexity:

- IFC (Industry Foundation Classes) is powerful but:
  - too complex (hundreds of entities and deep relationships)
  - inconsistent across tools and projects
  - difficult to query for real workflows
  - mixes **performance** (what a product or assembly actually delivers) with
    **requirements** (what a project or regulation demands) in the same property
    sets and attributes, so compliance checks and product data stay entangled
  - treats **change** as an afterthought: revisions are file swaps, not structured
    diff records you can query, aggregate, or feed into workflows
- IDS (Information Delivery Specification) focuses on data validation, but not on
  complex conditional validation logic (for example: if a building is below 25 m,
  staircase walls must be EI90).
- bSDD (buildingSMART Data Dictionary) focuses on classification, not workflows.

Result: teams cannot reliably build automation, dashboards, or simulations on top
of BIM data without heavy preprocessing.

## What this is

This project defines a pragmatic BIM data contract: a minimal, opinionated
structure for BIM data designed for workflows, not modeling.

It acts as a layer between:

- complex source data (for example IFC)
- and real applications (QTO, simulations, dashboards, quality checks)

## Core idea

Instead of trying to standardize everything, this contract:

- reduces complexity
- enforces consistency
- focuses on what is actually needed
- separates performance properties from requirement drivers so each can be queried,
  validated, and updated independently
- models change as first-class data (`Change` and its subclasses) rather
  than relying on opaque file diffs

It is intentionally limited.

## Principles

### 1) Not a replacement for IFC

This contract does not compete with IFC.

IFC remains:

- the exchange format
- the source of truth

This contract exists to make IFC usable in day-to-day workflows.

### 2) Designed for workflows, not modeling

This contract is built for:

- querying data
- running calculations
- feeding simulations
- building applications

Not for:

- authoring models
- preserving full semantic richness

### 3) Opinionated by design

Flexibility is often the enemy of automation. This contract intentionally:

- limits structure
- enforces naming
- reduces ambiguity

If your use case requires full flexibility, use IFC directly.

### 4) Abstraction over completeness

This project intentionally ignores large parts of IFC.

Only data required for real decision workflows is included.

### 5) Consistency over universality

This is not a universal standard.

It is a consistent contract that enables:

- repeatable queries
- predictable pipelines
- reliable automation

## What this enables

Using this contract, you can build:

- quantity takeoff pipelines
- room and space analysis
- simulation input models
- project dashboards
- validation workflows

Without having to:

- traverse complex IFC relationships
- handle inconsistent structures
- rebuild logic for every project

## How it fits in a workflow

1. Ingest BIM/IFC data with project-specific extraction logic.
2. Map extracted entities to this schema.
3. Store/query as graph or relational projections.
4. Enrich with requirements, performance metrics, schedules, and cost/material metadata.
5. Export, analyze, or feed application APIs.

## Products that use it

- [iterthink](https://www.iterthink.com/)
- [abstractBIM](https://www.abstractbim.com/)
- [{{yourcompany}}os](https://yourcompanyos.io/)

## Getting started

1. Browse the [Schema](schema/pragmatic-bim.docs.md) reference and download artifacts (JSON Schema, SHACL, CSV, Pydantic).
2. Read [Mappings to IFC](mapping/index.md) for declarative ingestion from IFC.
3. Explore [Classifications](classification/index.md) for SKOS vocabularies and mapping bridges.

## Governance

This contract is maintained by the Pragmatic BIM team. It is not governed by a formal standards body.

| | |
|---|---|
| **Maintainer** | Pragmatic BIM maintainers ([GitHub]({GITHUB_REPO})) |
| **Change process** | [GitHub issues]({GITHUB_REPO}/issues) for proposals; focused pull requests for changes |
| **Release cadence** | Semantic version tags (`v*`) publish schema releases to [schema.pragmaticbim.ch](https://schema.pragmaticbim.ch/) |

**How to participate**

- **Proposals:** Open a [GitHub issue]({GITHUB_REPO}/issues) — bugs, gaps, new entities, classification requests.
- **Contributions:** Pull requests welcome; keep changes focused and include documentation updates.
- **Classifications:** Abstract vocabularies live in [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules); project-specific schemes live in this repository.

**Versioning**

- Releases are tagged `vMAJOR.MINOR.PATCH` on GitHub.
- Each tag publishes versioned snapshots at `schema.pragmaticbim.ch/<version>/` (for example `/v0.0.7/`).
- Breaking schema changes bump the major or minor version; patch releases are fixes and non-breaking additions.

There is no separate steering committee or public RFC process at this stage. Input via GitHub issues is the primary channel for community feedback.
"""


def write_mapping_index(md_src: Path) -> None:
    mapping_dir = md_src / "mapping"
    mapping_dir.mkdir(parents=True, exist_ok=True)
    if not MAPPING_README.is_file():
        raise SystemExit(f"IFC mapping README not found: {MAPPING_README}")
    shutil.copy2(MAPPING_README, mapping_dir / "index.md")


def write_root_index(md_src: Path, *, version: str) -> None:
    (md_src / "index.md").write_text(render_root_index_markdown(version), encoding="utf-8")


def stage_brand_assets(md_src: Path) -> None:
    stylesheet_dir = md_src / "stylesheets"
    stylesheet_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_STYLESHEET, stylesheet_dir / "pragmatic-bim-brand.css")

    javascript_dir = md_src / "javascripts"
    javascript_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_JAVASCRIPT, javascript_dir / "classification-lang-switch.js")
    shutil.copy2(MERMAID_INIT_JAVASCRIPT, javascript_dir / "mermaid-init.js")
    shutil.copy2(VERSION_SELECTOR_JAVASCRIPT, javascript_dir / "version-selector.js")


def publish_schema_markdown(md_src: Path, site_schema_dir: Path) -> None:
    site_schema_dir.mkdir(parents=True, exist_ok=True)
    for md_file in md_src.rglob("*.md"):
        target = site_schema_dir / md_file.relative_to(md_src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, target)


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
    if section_dir.name == "cost":
        preserve = COST_SCHEMA_ARTIFACTS
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
        elif item.is_dir() and item.name in {"schema", "classification", "mapping", "cost"}:
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
    cost_schema_root = REPO_ROOT / "contract" / "cost" / "baseline_cost_schema.yaml"
    cost_out = site_dir / "cost"

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
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--schema-root",
            str(cost_schema_root),
            "--md-src",
            str(md_src / "cost"),
            "--index-name",
            "baseline-cost.docs",
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

    write_root_index(md_src, version=resolve_release_version(site_dir))
    write_mapping_index(md_src)
    stage_brand_assets(md_src)
    run_mkdocs_build(html_build=html_build)
    merge_html_build(html_build, site_dir)
    run_linkml_artifacts(schema_root, schema_out)
    run_linkml_artifacts(cost_schema_root, cost_out, prefix="baseline-cost")
    publish_schema_markdown(md_src / "schema", schema_out)
    publish_schema_markdown(md_src / "cost", cost_out)
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
    cost_schema_root = REPO_ROOT / "contract" / "cost" / "baseline_cost_schema.yaml"
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
            str(REPO_ROOT / "scripts" / "build_schema_docs.py"),
            "--check",
            "--schema-root",
            str(cost_schema_root),
            "--md-src",
            str(DEFAULT_MD_SRC / "cost"),
            "--index-name",
            "baseline-cost.docs",
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
    args.schema_root = resolve_repo_path(args.schema_root)

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
