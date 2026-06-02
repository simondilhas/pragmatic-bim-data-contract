#!/usr/bin/env python3
"""Build classification HTML documentation from SKOS TTL via MkDocs Material."""

from __future__ import annotations

import argparse
import difflib
import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from skos_doc_model import (  # noqa: E402
    load_catalog,
    parse_mapping,
    parse_vocabulary,
    render_mapping_markdown,
    render_vocabulary_markdown,
)

CLASSIFICATION_ROOT = REPO_ROOT / "classification"
CATALOG_PATH = CLASSIFICATION_ROOT / "catalog.yaml"
DEFAULT_MD_SRC = REPO_ROOT / "site" / "classification" / ".md-src"
DEFAULT_SITE_DIR = REPO_ROOT / "site" / "classification"
DEFAULT_HTML_BUILD = DEFAULT_SITE_DIR / ".html-build"
MKDOCS_CONFIG = REPO_ROOT / "mkdocs-classification.yml"
BASE_URL = os.environ.get("CLASSIFICATION_BASE_URL", "https://schema.pragmaticbim.ch/classification")
PRESERVE_SITE_ENTRIES = {
    ".md-src",
    ".html-build",
    "sources",
    "classifications.json",
}
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


def stage_brand_assets(md_src: Path) -> None:
    stylesheet_dir = md_src / "stylesheets"
    stylesheet_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_STYLESHEET, stylesheet_dir / "pragmatic-bim-brand.css")

    javascript_dir = md_src / "javascripts"
    javascript_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_JAVASCRIPT, javascript_dir / "classification-lang-switch.js")


def clear_markdown_source(md_src: Path) -> None:
    if md_src.exists():
        shutil.rmtree(md_src)
    md_src.mkdir(parents=True, exist_ok=True)


def clear_published_doc_outputs(site_dir: Path) -> None:
    if not site_dir.exists():
        site_dir.mkdir(parents=True, exist_ok=True)
        return
    for item in site_dir.iterdir():
        if item.name in PRESERVE_SITE_ENTRIES:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def build_nav(vocab_entries: list[dict[str, Any]], mapping_entries: list[dict[str, Any]]) -> list[Any]:
    nav: list[Any] = [{"Overview": "index.md"}]
    vocab_nav = [{entry["title"]: f"{entry['slug']}.md"} for entry in vocab_entries]
    if vocab_nav:
        nav.append({"Vocabularies": vocab_nav})
    mapping_nav = [{entry["title"]: f"mapping-{entry['slug']}.md"} for entry in mapping_entries]
    if mapping_nav:
        nav.append({"Mappings": mapping_nav})
    return nav


def write_mkdocs_config(nav: list[Any]) -> None:
    config = {
        "site_name": "Pragmatic BIM Classifications",
        "site_url": f"{BASE_URL.rstrip('/')}/",
        "use_directory_urls": False,
        "docs_dir": "site/classification/.md-src",
        "site_dir": "site/classification/.html-build",
        "extra_css": ["stylesheets/pragmatic-bim-brand.css"],
        "extra_javascript": ["javascripts/classification-lang-switch.js"],
        "theme": {
            "name": "material",
            "palette": [{"scheme": "default", "primary": "custom", "accent": "custom"}],
            "features": [
                "search.suggest",
                "search.highlight",
                "content.code.copy",
                "navigation.top",
            ],
        },
        "nav": nav,
        "plugins": ["search"],
        "validation": {"unrecognized_links": "ignore"},
        "markdown_extensions": [
            "tables",
            {"toc": {"permalink": True}},
            {
                "pymdownx.superfences": {
                    "custom_fences": [
                        {
                            "name": "mermaid",
                            "class": "mermaid",
                            "format": "!!python/name:pymdownx.superfences.fence_code_format",
                        }
                    ]
                }
            },
            "attr_list",
            "md_in_html",
        ],
    }
    config_text = yaml.safe_dump(config, sort_keys=False)
    config_text = config_text.replace(
        "format: '!!python/name:pymdownx.superfences.fence_code_format'",
        "format: !!python/name:pymdownx.superfences.fence_code_format",
    )
    MKDOCS_CONFIG.write_text(config_text, encoding="utf-8")


def render_index_markdown(
    vocab_entries: list[dict[str, Any]],
    mapping_entries: list[dict[str, Any]],
) -> str:
    lines = [
        "# Pragmatic BIM Classifications",
        "",
        "SKOS vocabularies and mapping bridges for the data contract `Classification` slot.",
        "",
        "License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — sourced from "
        "[pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules).",
        "",
        "## Vocabularies",
        "",
        "| Vocabulary | Description |",
        "| --- | --- |",
    ]
    for entry in vocab_entries:
        lines.append(f"| [{entry['title']}]({entry['slug']}.md) | `{entry['path']}` |")
    lines.extend(["", "## Mappings", "", "| Mapping | Description |", "| --- | --- |"])
    for entry in mapping_entries:
        lines.append(f"| [{entry['title']}](mapping-{entry['slug']}.md) | `{entry['path']}` |")
    lines.append("")
    return "\n".join(lines)


def write_sources(site_dir: Path, vocab_docs: list, mapping_docs: list) -> None:
    sources_dir = site_dir / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    for vocab in vocab_docs:
        dest = sources_dir / f"{vocab.slug}.ttl"
        shutil.copy2(vocab.source_path, dest)
    for mapping in mapping_docs:
        dest = sources_dir / f"mapping-{mapping.slug}.ttl"
        shutil.copy2(mapping.source_path, dest)


def write_classifications_json(
    site_dir: Path,
    vocab_docs: list,
    mapping_docs: list,
) -> None:
    base = BASE_URL.rstrip("/")
    payload = {
        "base_url": base,
        "docs_index": f"{base}/index.html",
        "vocabularies": [
            {
                "slug": vocab.slug,
                "title": vocab.title,
                "source_ttl": f"{base}/sources/{vocab.slug}.ttl",
                "docs_html": f"{base}/{vocab.slug}.html",
                "scheme_iri": vocab.scheme_iri,
            }
            for vocab in vocab_docs
        ],
        "mappings": [
            {
                "slug": mapping.slug,
                "title": mapping.title,
                "source_ttl": f"{base}/sources/mapping-{mapping.slug}.ttl",
                "docs_html": f"{base}/mapping-{mapping.slug}.html",
                "dataset_iri": mapping.dataset_iri,
            }
            for mapping in mapping_docs
        ],
    }
    (site_dir / "classifications.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


def merge_html_build(html_build: Path, site_dir: Path) -> None:
    if not html_build.is_dir():
        raise SystemExit(f"MkDocs output directory not found: {html_build}")
    site_dir.mkdir(parents=True, exist_ok=True)
    for item in html_build.iterdir():
        dest = site_dir / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def publish_markdown_artifacts(md_src: Path, site_dir: Path) -> None:
    for md_file in md_src.glob("*.md"):
        shutil.copy2(md_file, site_dir / md_file.name)


def build_classification_docs(
    *,
    md_src: Path,
    site_dir: Path,
    html_build: Path,
    catalog_path: Path = CATALOG_PATH,
    skip_mkdocs: bool = False,
) -> None:
    vocab_entries, mapping_entries = load_catalog(catalog_path)
    clear_markdown_source(md_src)

    vocab_docs = []
    for entry in vocab_entries:
        path = CLASSIFICATION_ROOT / entry["path"]
        vocab = parse_vocabulary(path, slug=entry["slug"], title=entry["title"])
        vocab_docs.append(vocab)
        (md_src / f"{entry['slug']}.md").write_text(render_vocabulary_markdown(vocab), encoding="utf-8")

    mapping_docs = []
    for entry in mapping_entries:
        path = CLASSIFICATION_ROOT / entry["path"]
        mapping = parse_mapping(path, slug=entry["slug"], title=entry["title"])
        mapping_docs.append(mapping)
        (md_src / f"mapping-{entry['slug']}.md").write_text(
            render_mapping_markdown(mapping),
            encoding="utf-8",
        )

    (md_src / "index.md").write_text(
        render_index_markdown(vocab_entries, mapping_entries),
        encoding="utf-8",
    )

    write_mkdocs_config(build_nav(vocab_entries, mapping_entries))
    stage_brand_assets(md_src)

    if skip_mkdocs:
        return

    write_sources(site_dir, vocab_docs, mapping_docs)
    write_classifications_json(site_dir, vocab_docs, mapping_docs)

    if html_build.exists():
        shutil.rmtree(html_build)

    subprocess.run(
        ["mkdocs", "build", "-f", str(MKDOCS_CONFIG), "-d", str(html_build)],
        check=True,
        cwd=REPO_ROOT,
    )

    clear_published_doc_outputs(site_dir)
    merge_html_build(html_build, site_dir)
    publish_markdown_artifacts(md_src, site_dir)
    write_sources(site_dir, vocab_docs, mapping_docs)
    write_classifications_json(site_dir, vocab_docs, mapping_docs)

    if html_build.exists():
        shutil.rmtree(html_build)


def collect_doc_tree(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(p for p in root.rglob("*") if p.is_file())


def compare_doc_trees(expected_dir: Path, actual_dir: Path) -> list[str]:
    errors: list[str] = []
    expected_files = collect_doc_tree(expected_dir)
    actual_files = collect_doc_tree(actual_dir)
    expected_rel = [path.relative_to(expected_dir) for path in expected_files]
    actual_rel = [path.relative_to(actual_dir) for path in actual_files]
    if expected_rel != actual_rel:
        errors.append(
            "Classification doc file set mismatch:\n"
            f"  expected: {[str(path) for path in expected_rel]}\n"
            f"  actual:   {[str(path) for path in actual_rel]}"
        )
    for rel_path in expected_rel:
        expected = expected_dir / rel_path
        actual = actual_dir / rel_path
        if filecmp.cmp(expected, actual, shallow=False):
            continue
        diff = difflib.unified_diff(
            expected.read_text(encoding="utf-8").splitlines(keepends=True),
            actual.read_text(encoding="utf-8").splitlines(keepends=True),
            fromfile=str(rel_path),
            tofile=f"{rel_path} (generated)",
        )
        errors.append("".join(diff))
    return errors


def verify_classification_docs(
    *,
    md_src: Path,
    site_dir: Path,
    html_build: Path,
    catalog_path: Path = CATALOG_PATH,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        tmp_md_src = tmp_root / ".md-src"
        build_classification_docs(
            md_src=tmp_md_src,
            site_dir=tmp_root / "site",
            html_build=tmp_root / ".html-build",
            catalog_path=catalog_path,
            skip_mkdocs=True,
        )
        errors = compare_doc_trees(md_src, tmp_md_src)
        if errors:
            print(
                "Classification docs are out of date relative to classification/*.ttl. "
                "Run: python scripts/build_site.py",
                file=sys.stderr,
            )
            for error in errors:
                print(error, file=sys.stderr)
            raise SystemExit(1)
    print("Classification docs are up to date with classification/*.ttl.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--md-src", type=Path, default=DEFAULT_MD_SRC)
    parser.add_argument("--site-dir", type=Path, default=DEFAULT_SITE_DIR)
    parser.add_argument("--html-build", type=Path, default=DEFAULT_HTML_BUILD)
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    parser.add_argument(
        "--skip-mkdocs",
        action="store_true",
        help="Only regenerate markdown.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed classification docs match a fresh build.",
    )
    args = parser.parse_args()

    if args.check:
        verify_classification_docs(
            md_src=args.md_src,
            site_dir=args.site_dir,
            html_build=args.html_build,
            catalog_path=args.catalog,
        )
        return

    build_classification_docs(
        md_src=args.md_src,
        site_dir=args.site_dir,
        html_build=args.html_build,
        catalog_path=args.catalog,
        skip_mkdocs=args.skip_mkdocs,
    )
    entry = args.site_dir / "index.html"
    print(f"Built classification docs in {args.site_dir}")
    print(f"Main entry point: {entry}")


if __name__ == "__main__":
    main()
