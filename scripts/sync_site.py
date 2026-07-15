#!/usr/bin/env python3
"""Regenerate site docs from sources and verify CI will pass.

One command to run after editing classification TTL, catalog.yaml, or contract YAML.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILD_SITE = REPO_ROOT / "scripts" / "build_site.py"

# Paths touched by `build_site.py` that must be committed with source edits.
SITE_SYNC_PATHS = (
    "site/.md-src",
    "site/classification",
    "site/schema",
    "site/cost",
    "site/mapping",
    "site/index.html",
    "site/404.html",
    "site/sitemap.xml",
    "site/sitemap.xml.gz",
    "site/search",
    "site/stylesheets",
    "site/javascripts",
    "site/assets",
    "site/entity",
    "site/modules.json",
)


def run_build(*, schema_root: Path | None) -> None:
    cmd = [sys.executable, str(BUILD_SITE)]
    if schema_root is not None:
        cmd.extend(["--schema-root", str(schema_root)])
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def run_check(*, schema_root: Path | None) -> None:
    cmd = [sys.executable, str(BUILD_SITE), "check"]
    if schema_root is not None:
        cmd.extend(["--schema-root", str(schema_root)])
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def git_status_paths() -> str:
    result = subprocess.run(
        ["git", "status", "--short", "--", *SITE_SYNC_PATHS],
        check=True,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_stage_paths() -> None:
    subprocess.run(
        ["git", "add", "--", *SITE_SYNC_PATHS],
        check=True,
        cwd=REPO_ROOT,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Typical workflow after editing classification/*.ttl or contract/*.yaml:\n"
            "  python scripts/sync_site.py\n"
            "  python scripts/sync_site.py --stage\n"
            "  git commit -m '...'\n"
            "\n"
            "Publishing a release: python scripts/publish.py --commit '...'"
        ),
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Skip build; run CI check only (same as build_site.py check).",
    )
    parser.add_argument(
        "--stage",
        action="store_true",
        help="git add site outputs after a successful build+check.",
    )
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=None,
        help="Override schema root (default: contract/00_pragmatic_bim_data_contract.yaml).",
    )
    args = parser.parse_args()

    if not args.check_only:
        print("Regenerating site from sources…")
        run_build(schema_root=args.schema_root)

    print("Verifying site docs match sources (CI check)…")
    run_check(schema_root=args.schema_root)

    status = git_status_paths()
    if status:
        print("\nUncommitted site changes:")
        print(status)
        if args.stage:
            git_stage_paths()
            print("\nStaged site outputs. Review with: git diff --cached")
        else:
            print("\nStage with: python scripts/sync_site.py --stage")
    else:
        print("\nSite outputs are in sync; nothing to commit under site/.")

    print("\nOK — CI site check would pass.")


if __name__ == "__main__":
    main()
