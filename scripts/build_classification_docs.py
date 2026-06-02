#!/usr/bin/env python3
"""Generate classification markdown documentation from SKOS TTL."""

from __future__ import annotations

import argparse
import difflib
import filecmp
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

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
DEFAULT_MD_SRC = REPO_ROOT / "site" / ".md-src" / "classification"
DEFAULT_SITE_DIR = REPO_ROOT / "site" / "classification"
DEFAULT_BASE_URL = os.environ.get("SCHEMA_BASE_URL", "https://schema.pragmaticbim.ch")


def clear_markdown_source(md_src: Path) -> None:
    if md_src.exists():
        shutil.rmtree(md_src)
    md_src.mkdir(parents=True, exist_ok=True)


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
    *,
    base_url: str,
) -> None:
    base = base_url.rstrip("/")
    payload = {
        "base_url": base,
        "docs_index": f"{base}/classification/index.html",
        "vocabularies": [
            {
                "slug": vocab.slug,
                "title": vocab.title,
                "source_ttl": f"{base}/classification/sources/{vocab.slug}.ttl",
                "docs_html": f"{base}/classification/{vocab.slug}.html",
                "scheme_iri": vocab.scheme_iri,
            }
            for vocab in vocab_docs
        ],
        "mappings": [
            {
                "slug": mapping.slug,
                "title": mapping.title,
                "source_ttl": f"{base}/classification/sources/mapping-{mapping.slug}.ttl",
                "docs_html": f"{base}/classification/mapping-{mapping.slug}.html",
                "dataset_iri": mapping.dataset_iri,
            }
            for mapping in mapping_docs
        ],
    }
    (site_dir / "classifications.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


def generate_classification_markdown(
    *,
    md_src: Path,
    site_dir: Path,
    catalog_path: Path = CATALOG_PATH,
    base_url: str = DEFAULT_BASE_URL,
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

    write_sources(site_dir, vocab_docs, mapping_docs)
    write_classifications_json(site_dir, vocab_docs, mapping_docs, base_url=base_url)


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
    catalog_path: Path = CATALOG_PATH,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        tmp_md_src = tmp_root / "classification"
        generate_classification_markdown(
            md_src=tmp_md_src,
            site_dir=tmp_root / "site",
            catalog_path=catalog_path,
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
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="Published site base URL for classifications.json.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed classification docs match a fresh build.",
    )
    args = parser.parse_args()

    if args.check:
        verify_classification_docs(md_src=args.md_src, catalog_path=args.catalog)
        return

    generate_classification_markdown(
        md_src=args.md_src,
        site_dir=args.site_dir,
        catalog_path=args.catalog,
        base_url=args.base_url,
    )
    print(f"Generated classification markdown in {args.md_src}")


if __name__ == "__main__":
    main()
