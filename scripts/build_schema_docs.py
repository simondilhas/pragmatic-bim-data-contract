#!/usr/bin/env python3
"""Build schema HTML documentation from live LinkML YAML via MkDocs Material."""

from __future__ import annotations

import argparse
import difflib
import filecmp
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from postprocess_schema_docs import postprocess_md_dir  # noqa: E402

DEFAULT_SCHEMA_ROOT = REPO_ROOT / "contract" / "00_pragmatic_bim_data_contract.yaml"
DEFAULT_MD_SRC = REPO_ROOT / "site" / "schema" / ".md-src"
DEFAULT_SITE_DIR = REPO_ROOT / "site" / "schema"
DEFAULT_HTML_BUILD = DEFAULT_SITE_DIR / ".html-build"
INDEX_NAME = "pragmatic-bim.docs.md"
MAIN_ENTRY = DEFAULT_SITE_DIR / "pragmatic-bim.docs.html"
PRESERVE_SITE_ENTRIES = {
    ".md-src",
    ".html-build",
    "pragmatic-bim.shacl.ttl",
    "pragmatic-bim.schema.json",
    "pragmatic-bim.csv",
    "pragmatic-bim.pydantic.py",
}
BRAND_STYLESHEET = (
    REPO_ROOT / "docs-assets" / "material" / "assets" / "stylesheets" / "pragmatic-bim-brand.css"
)


def stage_brand_stylesheet(md_src: Path) -> None:
    dest_dir = md_src / "stylesheets"
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BRAND_STYLESHEET, dest_dir / "pragmatic-bim-brand.css")


def find_gen_doc() -> str:
    for cmd in ("gen-doc", "gen-docs", "gen-markdown"):
        if shutil.which(cmd):
            return cmd
    raise SystemExit("No gen-doc command found; install linkml from requirements-docs.txt")


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


def run_gen_doc(md_src: Path, schema_root: Path) -> None:
    clear_markdown_source(md_src)
    cmd = find_gen_doc()
    args = [
        cmd,
        "--index-name",
        "pragmatic-bim.docs",
        "--hierarchical-class-view",
        "--truncate-descriptions",
        "false",
        "--diagram-type",
        "mermaid_class_diagram",
        "-d",
        str(md_src),
        str(schema_root),
    ]
    subprocess.run(args, check=True, cwd=REPO_ROOT)


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
    index_src = md_src / INDEX_NAME
    if not index_src.is_file():
        raise SystemExit(f"Expected index markdown not found: {index_src}")
    shutil.copy2(index_src, site_dir / INDEX_NAME)
    for md_file in md_src.glob("*.md"):
        if md_file.name == INDEX_NAME:
            continue
        shutil.copy2(md_file, site_dir / md_file.name)


def build_schema_docs(
    *,
    md_src: Path,
    site_dir: Path,
    html_build: Path,
    schema_root: Path,
    skip_mkdocs: bool = False,
) -> None:
    run_gen_doc(md_src, schema_root)
    postprocess_md_dir(md_src, schema_root=schema_root)
    stage_brand_stylesheet(md_src)

    if skip_mkdocs:
        return

    if html_build.exists():
        shutil.rmtree(html_build)

    subprocess.run(
        ["mkdocs", "build", "-f", str(REPO_ROOT / "mkdocs.yml"), "-d", str(html_build)],
        check=True,
        cwd=REPO_ROOT,
    )

    clear_published_doc_outputs(site_dir)
    merge_html_build(html_build, site_dir)
    publish_markdown_artifacts(md_src, site_dir)

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
            "Schema doc file set mismatch:\n"
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


def verify_schema_docs(
    *,
    md_src: Path,
    site_dir: Path,
    html_build: Path,
    schema_root: Path,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        tmp_md_src = tmp_root / ".md-src"
        build_schema_docs(
            md_src=tmp_md_src,
            site_dir=tmp_root / "site",
            html_build=tmp_root / ".html-build",
            schema_root=schema_root,
            skip_mkdocs=True,
        )
        errors = compare_doc_trees(md_src, tmp_md_src)
        if errors:
            print(
                "Schema docs are out of date relative to contract/*.yaml. "
                "Run: python scripts/build_site.py",
                file=sys.stderr,
            )
            for error in errors:
                print(error, file=sys.stderr)
            raise SystemExit(1)
    print("Schema docs are up to date with contract/*.yaml.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--md-src", type=Path, default=DEFAULT_MD_SRC)
    parser.add_argument("--site-dir", type=Path, default=DEFAULT_SITE_DIR)
    parser.add_argument("--html-build", type=Path, default=DEFAULT_HTML_BUILD)
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=Path(os.environ.get("SCHEMA_ROOT", DEFAULT_SCHEMA_ROOT)),
    )
    parser.add_argument(
        "--skip-mkdocs",
        action="store_true",
        help="Only regenerate and post-process markdown.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed schema docs match a fresh build from contract/*.yaml.",
    )
    args = parser.parse_args()

    if args.check:
        verify_schema_docs(
            md_src=args.md_src,
            site_dir=args.site_dir,
            html_build=args.html_build,
            schema_root=args.schema_root,
        )
        return

    build_schema_docs(
        md_src=args.md_src,
        site_dir=args.site_dir,
        html_build=args.html_build,
        schema_root=args.schema_root,
        skip_mkdocs=args.skip_mkdocs,
    )
    entry = args.site_dir / "pragmatic-bim.docs.html"
    print(f"Built schema docs from live YAML in {args.site_dir}")
    print(f"Main entry point: {entry}")


if __name__ == "__main__":
    main()
