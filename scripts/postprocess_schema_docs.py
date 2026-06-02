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
EMBEDDED_CLASS_BOOST = 2.0
EMBEDDED_SLOT_BOOST = 3.0
EMBEDDED_NOTE_MARKER = "**Embedded value type**"
EMBEDDED_SECTION_INTRO = (
    "> Structured records stored inline on parent graph nodes (`inlined: true`). "
    "Not standalone project entities — no independent `id` or lifecycle.\n"
)
CLASS_ROW_RE = re.compile(r"\[([A-Za-z0-9_]+)\]\([^)]+\.md\)")


def iter_imported_schema_docs(schema_root: Path):
    root = yaml.safe_load(schema_root.read_text(encoding="utf-8")) or {}
    imports = root.get("imports", [])
    schema_dir = schema_root.parent
    for item in imports:
        if not isinstance(item, str) or item.startswith("linkml:"):
            continue
        schema_file = schema_dir / f"{item}.yaml"
        if not schema_file.exists():
            continue
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        yield schema_file, doc


def load_class_metadata(schema_root: Path) -> tuple[dict[str, int], dict[str, str], dict[str, str]]:
    order: dict[str, int] = {}
    descriptions: dict[str, str] = {}
    parents: dict[str, str] = {}
    idx = 0
    for _schema_file, doc in iter_imported_schema_docs(schema_root):
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


def _collect_inlined_ranges(body: dict) -> set[str]:
    ranges: set[str] = set()
    range_name = body.get("range")
    if body.get("inlined") is True and isinstance(range_name, str) and range_name.strip():
        ranges.add(range_name.strip())
    return ranges


def load_embedded_value_classes(schema_root: Path, class_parents: dict[str, str]) -> set[str]:
    embedded_ranges: set[str] = set()
    for _schema_file, doc in iter_imported_schema_docs(schema_root):
        slots = doc.get("slots", {})
        if isinstance(slots, dict):
            for slot_body in slots.values():
                if isinstance(slot_body, dict):
                    embedded_ranges.update(_collect_inlined_ranges(slot_body))

        classes = doc.get("classes", {})
        if not isinstance(classes, dict):
            continue
        for class_body in classes.values():
            if not isinstance(class_body, dict):
                continue
            attributes = class_body.get("attributes", {})
            if isinstance(attributes, dict):
                for attr_body in attributes.values():
                    if isinstance(attr_body, dict):
                        embedded_ranges.update(_collect_inlined_ranges(attr_body))

    embedded = set(embedded_ranges)
    changed = True
    while changed:
        changed = False
        for class_name, parent_name in class_parents.items():
            if parent_name in embedded and class_name not in embedded:
                embedded.add(class_name)
                changed = True
    return embedded


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


def extract_class_name_from_row(row: str) -> str | None:
    match = CLASS_ROW_RE.search(row)
    return match.group(1) if match else None


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


def fix_row_descriptions(rows: list[str], class_descriptions: dict[str, str]) -> list[str]:
    fixed_rows: list[str] = []
    for row in rows:
        class_name = extract_class_name_from_row(row)
        if not class_name:
            fixed_rows.append(row)
            continue
        parts = row.split("|")
        if len(parts) >= 4:
            current_desc = normalize_desc(parts[2])
            full_desc = class_descriptions.get(class_name)
            if full_desc and (current_desc.endswith("...") or current_desc.endswith("…")):
                parts[2] = f" {full_desc} "
                row = "|".join(parts)
        fixed_rows.append(row)
    return fixed_rows


def sort_class_rows(
    rows: list[str],
    class_order: dict[str, int],
    class_hierarchy_order: dict[str, int],
) -> list[str]:
    def row_key(row: str) -> tuple[int, str, str]:
        class_name = extract_class_name_from_row(row) or ""
        order_idx = class_hierarchy_order.get(class_name, class_order.get(class_name, 10_000_000))
        return (order_idx, class_name.lower(), row.lower())

    return sorted(rows, key=row_key)


def parse_classes_table(text: str) -> tuple[list[str], list[str], list[str], list[str]] | None:
    if "## Classes" not in text:
        return None
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Classes":
            start = i
            break
    if start is None:
        return None

    table_start = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("| Class |"):
            table_start = i
            break
        if lines[i].startswith("## "):
            return None
    if table_start is None or table_start + 1 >= len(lines):
        return None

    rows_start = table_start + 2
    rows_end = rows_start
    while rows_end < len(lines) and lines[rows_end].startswith("| "):
        rows_end += 1

    rows = lines[rows_start:rows_end]
    if not rows:
        return None

    return lines[:start], lines[start : table_start], rows, lines[rows_end:]


def split_and_render_classes_sections(
    text: str,
    embedded_classes: set[str],
    class_order: dict[str, int],
    class_descriptions: dict[str, str],
    class_hierarchy_order: dict[str, int],
) -> str:
    parsed = parse_classes_table(text)
    if parsed is None:
        return text

    prefix_lines, _section_header, rows, suffix_lines = parsed
    rows = fix_row_descriptions(rows, class_descriptions)

    graph_rows: list[str] = []
    embedded_rows: list[str] = []
    for row in rows:
        class_name = extract_class_name_from_row(row)
        if class_name and class_name in embedded_classes:
            embedded_rows.append(row)
        else:
            graph_rows.append(row)

    graph_rows = sort_class_rows(graph_rows, class_order, class_hierarchy_order)
    embedded_rows = sort_class_rows(embedded_rows, class_order, class_hierarchy_order)

    graph_section = "\n".join(
        [
            "## Graph classes",
            "",
            "| Class | Description |",
            "| --- | --- |",
            *graph_rows,
        ]
    )
    embedded_section = "\n".join(
        [
            "## Embedded value types",
            "",
            EMBEDDED_SECTION_INTRO,
            "| Class | Description |",
            "| --- | --- |",
            *embedded_rows,
        ]
    )

    return "\n".join(prefix_lines + ["", graph_section, "", embedded_section, ""] + suffix_lines)


def simplify_class_diagram(body: str) -> str:
    """Keep inheritance structure only; drop slots and associations."""
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("classDiagram"):
            lines.append(stripped)
            lines.append("direction TB")
            continue
        if stripped.startswith("direction "):
            continue
        if "<|--" in stripped:
            lines.append(stripped)
            continue
        if stripped.startswith("click "):
            lines.append(stripped)
            continue
        if re.match(r"^class [A-Za-z0-9_]+$", stripped):
            lines.append(stripped)
    return "\n".join(lines)


def normalize_mermaid_blocks(text: str) -> str:
    pattern = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)

    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        if body.lstrip().startswith("classDiagram"):
            normalized = simplify_class_diagram(body)
        else:
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


def set_search_boost(text: str, boost: float) -> str:
    if "boost:" not in text:
        return text
    return re.sub(r"(boost:\s*)[\d.]+", rf"\g<1>{boost}", text, count=1)


def parse_slot_domains(text: str) -> set[str] | None:
    if not re.search(r"^# Slot:", text, re.MULTILINE):
        return None
    match = re.search(r"^\| Domain Of \| (.+) \|$", text, re.MULTILINE)
    if not match:
        return set()
    return set(CLASS_ROW_RE.findall(match.group(1)))


def adjust_search_boost(text: str, md_stem: str, embedded_classes: set[str]) -> str:
    if md_stem in embedded_classes:
        return set_search_boost(text, EMBEDDED_CLASS_BOOST)

    domains = parse_slot_domains(text)
    if domains is not None and domains and domains <= embedded_classes:
        return set_search_boost(text, EMBEDDED_SLOT_BOOST)
    return text


def inject_embedded_class_note(text: str, class_name: str, embedded_classes: set[str]) -> str:
    if class_name not in embedded_classes or EMBEDDED_NOTE_MARKER in text:
        return text
    if not re.search(rf"^# Class: {re.escape(class_name)}\s*$", text, re.MULTILINE):
        return text
    note = "> **Embedded value type** — nested inside a parent record, not a graph node.\n\n"
    pattern = rf"(# Class: {re.escape(class_name)}\s*\n\n\n_[^\n]+_\n)(\n+)"
    return re.sub(pattern, rf"\1\n{note}", text, count=1)


def postprocess_md_dir(
    md_dir: Path,
    *,
    schema_root: Path,
) -> None:
    if not md_dir.is_dir():
        raise SystemExit(f"Markdown source directory not found: {md_dir}")

    class_order, class_descriptions, class_parents = load_class_metadata(schema_root)
    class_hierarchy_order = build_class_hierarchy_order(class_order, class_parents)
    embedded_classes = load_embedded_value_classes(schema_root, class_parents)

    for md_file in sorted(md_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        if md_file.name == INDEX_NAME:
            text = inject_artifacts_section(text)
            text = split_and_render_classes_sections(
                text,
                embedded_classes,
                class_order,
                class_descriptions,
                class_hierarchy_order,
            )
        else:
            stem = md_file.stem
            if stem in class_order:
                text = inject_embedded_class_note(text, stem, embedded_classes)
            text = adjust_search_boost(text, stem, embedded_classes)
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
