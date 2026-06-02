#!/usr/bin/env python3
"""Generate schema markdown documentation from live LinkML YAML."""

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
DEFAULT_MD_SRC = REPO_ROOT / "site" / ".md-src" / "schema"
INDEX_NAME = "pragmatic-bim.docs.md"


def find_gen_doc() -> str:
    for cmd in ("gen-doc", "gen-docs", "gen-markdown"):
        if shutil.which(cmd):
            return cmd
    raise SystemExit("No gen-doc command found; install linkml from requirements-docs.txt")


def clear_markdown_source(md_src: Path) -> None:
    if md_src.exists():
        shutil.rmtree(md_src)
    md_src.mkdir(parents=True, exist_ok=True)


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


def generate_schema_markdown(*, md_src: Path, schema_root: Path) -> None:
    run_gen_doc(md_src, schema_root)
    postprocess_md_dir(md_src, schema_root=schema_root)


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
    schema_root: Path,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        tmp_md_src = tmp_root / "schema"
        generate_schema_markdown(md_src=tmp_md_src, schema_root=schema_root)
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
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=Path(os.environ.get("SCHEMA_ROOT", DEFAULT_SCHEMA_ROOT)),
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed schema docs match a fresh build from contract/*.yaml.",
    )
    args = parser.parse_args()

    if args.check:
        verify_schema_docs(md_src=args.md_src, schema_root=args.schema_root)
        return

    generate_schema_markdown(md_src=args.md_src, schema_root=args.schema_root)
    print(f"Generated schema markdown in {args.md_src}")


if __name__ == "__main__":
    main()
