#!/usr/bin/env python3
"""Post-process LinkML gen-doc markdown before MkDocs build."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

import yaml

INDEX_NAME = "pragmatic-bim.docs.md"
ARTIFACTS = (
    ("JSON Schema", "pragmatic-bim.schema.json"),
    ("SHACL", "pragmatic-bim.shacl.ttl"),
    ("CSV", "pragmatic-bim.csv"),
    ("Pydantic", "pragmatic-bim.pydantic.py"),
    ("Docs (Markdown)", "pragmatic-bim.docs.md"),
)


def load_class_metadata(schema_root: Path) -> tuple[dict[str, int], dict[str, str], dict[str, str]]:
    root = yaml.safe_load(schema_root.read_text(encoding="utf-8")) or {}
    imports = root.get("imports", [])
    order: dict[str, int] = {}
    descriptions: dict[str, str] = {}
    parents: dict[str, str] = {}
    idx = 0
    schema_dir = schema_root.parent
    for item in imports:
        if not isinstance(item, str) or item.startswith("linkml:"):
            continue
        schema_file = schema_dir / f"{item}.yaml"
        if not schema_file.exists():
            continue
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        classes = doc.get("classes", {})
        if not isinstance(classes, dict):
            continue
        for class_name, class_body in classes.items():
            if class_name not in order:
                order[class_name] = idx
                idx += 1
            if class_name not in descriptions and isinstance(class_body, dict):
                desc = class_body.get("description")
                if isinstance(desc, str) and desc.strip():
                    descriptions[class_name] = " ".join(desc.split())
                parent = class_body.get("is_a")
                if isinstance(parent, str) and parent.strip():
                    parents[class_name] = parent.strip()
    return order, descriptions, parents


def build_class_hierarchy_order(
    class_order: dict[str, int],
    class_parents: dict[str, str],
) -> dict[str, int]:
    children: dict[str, list[str]] = {}
    for class_name, parent_name in class_parents.items():
        if parent_name in class_order:
            children.setdefault(parent_name, []).append(class_name)

    for parent_name in children:
        children[parent_name].sort(key=lambda child: class_order.get(child, 10_000_000))

    roots = [
        class_name
        for class_name in sorted(class_order, key=lambda c: class_order[c])
        if class_parents.get(class_name) not in class_order
    ]

    ordered: list[str] = []
    visited: set[str] = set()

    def visit(class_name: str) -> None:
        if class_name in visited:
            return
        visited.add(class_name)
        ordered.append(class_name)
        for child_name in children.get(class_name, []):
            visit(child_name)

    for root_name in roots:
        visit(root_name)

    for class_name in sorted(class_order, key=lambda c: class_order[c]):
        visit(class_name)

    return {class_name: idx for idx, class_name in enumerate(ordered)}


def normalize_desc(value: str) -> str:
    return " ".join(value.split()).strip()


def render_artifacts_section() -> str:
    rows = "\n".join(
        f"| {label} | [{filename}]({filename}) |"
        for label, filename in ARTIFACTS
    )
    return f"## Artifacts\n\n| Format | File |\n| --- | --- |\n{rows}"


def inject_artifacts_section(index_text: str) -> str:
    if "## Artifacts" in index_text:
        return index_text
    match = re.search(r"^## Classes\s*$", index_text, re.MULTILINE)
    if not match:
        raise SystemExit("Expected ## Classes section in gen-doc index markdown")
    prefix = index_text[: match.start()].rstrip()
    suffix = index_text[match.start() :].lstrip()
    return f"{prefix}\n\n{render_artifacts_section()}\n\n{suffix}"


def reorder_classes_table(
    text: str,
    class_order: dict[str, int],
    class_descriptions: dict[str, str],
    class_hierarchy_order: dict[str, int],
) -> str:
    if "## Classes" not in text:
        return text
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Classes":
            start = i
            break
    if start is None:
        return text

    table_start = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("| Class |"):
            table_start = i
            break
        if lines[i].startswith("## "):
            return text
    if table_start is None or table_start + 1 >= len(lines):
        return text

    rows_start = table_start + 2
    rows_end = rows_start
    while rows_end < len(lines) and lines[rows_end].startswith("| "):
        rows_end += 1

    rows = lines[rows_start:rows_end]
    if not rows:
        return text

    fixed_rows = []
    for row in rows:
        match = re.search(r"\[([A-Za-z0-9_]+)\]\([^)]+\.md\)", row)
        if not match:
            fixed_rows.append(row)
            continue
        class_name = match.group(1)
        parts = row.split("|")
        if len(parts) >= 4:
            current_desc = normalize_desc(parts[2])
            full_desc = class_descriptions.get(class_name)
            if full_desc and (current_desc.endswith("...") or current_desc.endswith("…")):
                parts[2] = f" {full_desc} "
                row = "|".join(parts)
        fixed_rows.append(row)

    def row_key(row: str) -> tuple[int, str, str]:
        match = re.search(r"\[([A-Za-z0-9_]+)\]\([^)]+\.md\)", row)
        class_name = match.group(1) if match else ""
        order_idx = class_hierarchy_order.get(class_name, class_order.get(class_name, 10_000_000))
        return (order_idx, class_name.lower(), row.lower())

    rows_sorted = sorted(fixed_rows, key=row_key)
    return "\n".join(lines[:rows_start] + rows_sorted + lines[rows_end:])


def normalize_mermaid_blocks(text: str) -> str:
    pattern = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)

    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        compact_lines = [line.rstrip() for line in body.splitlines() if line.strip()]
        normalized = "\n".join(compact_lines)
        normalized = re.sub(
            r'(click\s+([A-Za-z0-9_]+)\s+href\s+")\.\./([A-Za-z0-9_]+)/?(")',
            lambda m: f'{m.group(1)}./{m.group(3)}.html{m.group(4)}',
            normalized,
        )
        normalized = re.sub(
            r"(click\s+([A-Za-z0-9_]+)\s+href\s+')\.\./([A-Za-z0-9_]+)/?(')",
            lambda m: f"{m.group(1)}./{m.group(3)}.html{m.group(4)}",
            normalized,
        )
        normalized = re.sub(
            r'^(click\s+[A-Za-z0-9_]+\s+href\s+["\'][^"\']+["\'](?:\s+["\'][^"\']*["\'])?)(\s+_[A-Za-z0-9]+)?\s*$',
            lambda m: f"{m.group(1)} _blank",
            normalized,
            flags=re.MULTILINE,
        )
        return "```mermaid\n" + normalized + "\n```"

    return pattern.sub(repl, text)


def postprocess_md_dir(
    md_dir: Path,
    *,
    schema_root: Path,
) -> None:
    if not md_dir.is_dir():
        raise SystemExit(f"Markdown source directory not found: {md_dir}")

    class_order, class_descriptions, class_parents = load_class_metadata(schema_root)
    class_hierarchy_order = build_class_hierarchy_order(class_order, class_parents)

    for md_file in sorted(md_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        if md_file.name == INDEX_NAME:
            text = inject_artifacts_section(text)
            text = reorder_classes_table(
                text,
                class_order,
                class_descriptions,
                class_hierarchy_order,
            )
        text = normalize_mermaid_blocks(text)
        md_file.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--md-dir",
        type=Path,
        default=Path("site/.md-src/schema"),
        help="Directory containing gen-doc markdown output.",
    )
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=Path(os.environ.get("SCHEMA_ROOT", "contract/00_pragmatic_bim_data_contract.yaml")),
    )
    args = parser.parse_args()

    postprocess_md_dir(args.md_dir, schema_root=args.schema_root)
    print(f"Post-processed markdown in {args.md_dir}")


if __name__ == "__main__":
    main()
