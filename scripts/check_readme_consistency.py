#!/usr/bin/env python3
"""Validate README cross-links, layout trees, and canonical path naming.

Usage:
    python scripts/check_readme_consistency.py
    python scripts/check_readme_consistency.py --check   # exit 1 on failure (CI)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REPO_DIR_NAME = REPO_ROOT.name

README_PATHS = (
    "README.md",
    "contract/README.md",
    "classification/README.md",
    "contract/mapping/README.md",
    "contract/mappings/README.md",
)

IFC_MAPPING_ALIASES = ("contract/mappings", "contract/mapping")

# Generated or optional paths documented in READMEs but not required in git.
OPTIONAL_REPO_PATHS = frozenset(
    {
        "classification/out/",
        "classification/out",
    }
)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
REPO_BACKTICK_RE = re.compile(
    r"`((?:\.\./)*(?:contract|classification|scripts)/[^`\s#*]+)`"
)
TREE_ENTRY_RE = re.compile(r"^[│\s]*[├└]──\s+(\S+)")
LAYOUT_ROOT_RE = re.compile(r"^([a-z0-9_.-]+)/\s*$")
MAPPING_BRIDGE_RE = re.compile(
    r"^\|\s*`(mapping/[^`]+)`\s*\|", re.MULTILINE
)


def discover_readmes() -> list[Path]:
    return sorted(p for part in README_PATHS if (p := REPO_ROOT / part).is_file())


def ifc_mapping_dir_on_disk() -> Path | None:
    for alias in IFC_MAPPING_ALIASES:
        path = REPO_ROOT / alias
        if path.is_dir():
            return path
    return None


def normalize_link_target(raw: str) -> str | None:
    target = raw.strip()
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    if "#" in target:
        target = target.split("#", 1)[0]
    return target or None


def resolve_link(readme: Path, target: str) -> Path:
    rel = normalize_link_target(target)
    if rel is None:
        return readme
    path = Path(rel)
    if path.is_absolute():
        return path
    return (readme.parent / path).resolve()


def collect_ifc_mapping_mentions(text: str) -> set[str]:
    mentions: set[str] = set()
    for alias in IFC_MAPPING_ALIASES:
        if alias in text:
            mentions.add(alias)
    return mentions


def layout_blocks(text: str) -> list[tuple[str | None, list[str]]]:
    blocks: list[tuple[str | None, list[str]]] = []
    in_fence = False
    fence_lines: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("```"):
            if in_fence:
                root = None
                entries: list[str] = []
                for bl in fence_lines:
                    stripped = bl.strip()
                    m = LAYOUT_ROOT_RE.match(stripped)
                    if m and root is None:
                        root = m.group(1)
                        continue
                    tm = TREE_ENTRY_RE.match(bl)
                    if tm:
                        entries.append(tm.group(1).rstrip("/"))
                if root or entries:
                    blocks.append((root, entries))
                fence_lines = []
            in_fence = not in_fence
            continue
        if in_fence:
            fence_lines.append(line)
    return blocks


def layout_base(root: str | None, readme: Path) -> Path:
    if root in (None, REPO_DIR_NAME):
        return REPO_ROOT
    if root == "contract":
        return REPO_ROOT / "contract"
    if root == "classification":
        return REPO_ROOT / "classification"
    return REPO_ROOT / root


def check_readme_links(readme: Path, errors: list[str]) -> None:
    rel_readme = readme.relative_to(REPO_ROOT)
    for match in LINK_RE.finditer(readme.read_text(encoding="utf-8")):
        target = match.group(1)
        if normalize_link_target(target) is None:
            continue
        resolved = resolve_link(readme, target)
        if not resolved.exists():
            errors.append(f"{rel_readme}: broken link ({target})")


def check_repo_backtick_paths(readme: Path, errors: list[str]) -> None:
    rel_readme = readme.relative_to(REPO_ROOT)
    for match in REPO_BACKTICK_RE.finditer(readme.read_text(encoding="utf-8")):
        raw = match.group(1)
        if "*" in raw:
            continue
        if raw.startswith("../"):
            resolved = (readme.parent / raw).resolve()
        else:
            resolved = (REPO_ROOT / raw).resolve()
        norm = raw.rstrip("/")
        if norm in OPTIONAL_REPO_PATHS or f"{norm}/" in OPTIONAL_REPO_PATHS:
            continue
        if not resolved.exists():
            errors.append(f"{rel_readme}: missing path `{raw}`")


def check_layout_trees(readme: Path, errors: list[str]) -> None:
    rel_readme = readme.relative_to(REPO_ROOT)
    for root, entries in layout_blocks(readme.read_text(encoding="utf-8")):
        base = layout_base(root, readme)
        for entry in entries:
            if "*" in entry:
                continue
            candidate = base / entry
            if not candidate.exists():
                errors.append(f"{rel_readme}: layout entry missing `{entry}` (under {base.relative_to(REPO_ROOT)})")


def check_ifc_mapping_naming(readmes: list[Path], errors: list[str]) -> None:
    on_disk = ifc_mapping_dir_on_disk()
    if on_disk is None:
        errors.append("No IFC mapping directory (expected contract/mappings or contract/mapping)")
        return

    canonical = on_disk.relative_to(REPO_ROOT).as_posix()
    mentions: set[str] = set()
    for readme in readmes:
        mentions |= collect_ifc_mapping_mentions(readme.read_text(encoding="utf-8"))

    for alias in sorted(mentions - {canonical}):
        errors.append(
            f"IFC mapping path inconsistency: docs reference `{alias}` "
            f"but on-disk folder is `{canonical}`"
        )

    merge_script = REPO_ROOT / "scripts/merge_ifc_mapping.py"
    if merge_script.is_file():
        text = merge_script.read_text(encoding="utf-8")
        for alias in IFC_MAPPING_ALIASES:
            if alias in text and alias != canonical:
                errors.append(
                    f"scripts/merge_ifc_mapping.py references `{alias}` "
                    f"but on-disk folder is `{canonical}`"
                )
                break


def check_classification_catalog(errors: list[str]) -> None:
    readme = REPO_ROOT / "classification/README.md"
    catalog = REPO_ROOT / "classification/catalog.yaml"
    if not readme.is_file() or not catalog.is_file():
        return

    try:
        import yaml
    except ImportError:
        return

    data = yaml.safe_load(catalog.read_text(encoding="utf-8")) or {}
    text = readme.read_text(encoding="utf-8")

    for item in data.get("vocabularies", []):
        path = item.get("path", "")
        folder = path.split("/", 1)[0] if path else ""
        if folder and folder not in text:
            errors.append(
                f"classification/README.md: catalog vocabulary folder `{folder}` "
                "not mentioned in layout or tables"
            )

    documented = set(MAPPING_BRIDGE_RE.findall(text))
    for item in data.get("mappings", []):
        path = item.get("path", "")
        if path and path not in documented:
            errors.append(
                f"classification/README.md: catalog mapping `{path}` "
                "missing from Mapping bridges table"
            )


def run_checks() -> list[str]:
    errors: list[str] = []
    readmes = discover_readmes()
    if not readmes:
        errors.append("No README files found")
        return errors

    for readme in readmes:
        check_readme_links(readme, errors)
        check_repo_backtick_paths(readme, errors)
        check_layout_trees(readme, errors)

    check_ifc_mapping_naming(readmes, errors)
    check_classification_catalog(errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit 1 on failure (CI)")
    parser.parse_args()

    errors = run_checks()
    if errors:
        print("README consistency check failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"README consistency OK ({len(discover_readmes())} README files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
