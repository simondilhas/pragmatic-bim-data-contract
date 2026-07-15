#!/usr/bin/env python3
"""Publish a schema release to GitHub Pages.

Runs site sync, optionally commits, creates a version tag, and pushes.
Tag push triggers `.github/workflows/schema-pages.yml`.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from sync_site import run_build, run_check  # noqa: E402

TAG_PATTERN = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
DEFAULT_BRANCH = "main"


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=check,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def git_output(*args: str) -> str:
    result = run_git(*args)
    return result.stdout.strip()


def current_branch() -> str:
    return git_output("branch", "--show-current")


def working_tree_status() -> str:
    lines = []
    for line in git_output("status", "--short").splitlines():
        path = line[3:].strip()
        if path.startswith("scripts/__pycache__/") or "/__pycache__/" in path:
            continue
        lines.append(line)
    return "\n".join(lines)


def is_working_tree_clean() -> bool:
    return not working_tree_status()


def latest_release_tag() -> str | None:
    result = run_git("tag", "-l", "v*", "--sort=-v:refname", check=False)
    for line in result.stdout.splitlines():
        tag = line.strip()
        if TAG_PATTERN.fullmatch(tag):
            return tag
    return None


def parse_tag(tag: str) -> tuple[int, int, int]:
    match = TAG_PATTERN.fullmatch(tag)
    if not match:
        raise SystemExit(f"Invalid version tag (expected vMAJOR.MINOR.PATCH): {tag}")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def bump_tag(tag: str, bump: str) -> str:
    major, minor, patch = parse_tag(tag)
    if bump == "major":
        return f"v{major + 1}.0.0"
    if bump == "minor":
        return f"v{major}.{minor + 1}.0"
    if bump == "patch":
        return f"v{major}.{minor}.{patch + 1}"
    raise SystemExit(f"Unknown bump kind: {bump}")


def resolve_version(*, version: str | None, bump: str) -> str:
    if version:
        parse_tag(version)
        return version
    latest = latest_release_tag()
    if latest is None:
        return "v0.1.0"
    return bump_tag(latest, bump)


def tag_exists(tag: str) -> bool:
    return run_git("rev-parse", tag, check=False).returncode == 0


def commit_all(message: str) -> None:
    run_git("add", "-A")
    if run_git("diff", "--cached", "--quiet", check=False).returncode != 0:
        run_git("commit", "-m", message)


def create_annotated_tag(tag: str, message: str) -> None:
    run_git("tag", "-a", tag, "-m", message)


def push_release(*, branch: str, tag: str) -> None:
    run_git("push", "origin", branch)
    run_git("push", "origin", tag)


def print_step(label: str) -> None:
    print(f"\n==> {label}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/publish.py --dry-run\n"
            "  python scripts/publish.py --bump patch --commit 'Add family relationship concepts'\n"
            "  python scripts/publish.py --version v0.2.0 --commit 'Release v0.2.0' --push\n"
            "\n"
            "After push, GitHub Actions publishes to https://schema.pragmaticbim.ch/"
        ),
    )
    version_group = parser.add_mutually_exclusive_group()
    version_group.add_argument(
        "--version",
        metavar="vX.Y.Z",
        help="Explicit release tag (default: bump latest tag).",
    )
    version_group.add_argument(
        "--bump",
        choices=("patch", "minor", "major"),
        default="patch",
        help="Bump latest v* tag (default: patch).",
    )
    parser.add_argument(
        "--commit",
        "-m",
        metavar="MESSAGE",
        help="Commit all current changes before tagging (required if working tree is dirty).",
    )
    parser.add_argument(
        "--tag-message",
        help="Annotated tag message (default: Release <version>).",
    )
    parser.add_argument(
        "--push",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Push branch and tag to origin (default: true).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned actions without writing to git or pushing.",
    )
    parser.add_argument(
        "--branch",
        default=DEFAULT_BRANCH,
        help=f"Branch to push (default: {DEFAULT_BRANCH}).",
    )
    parser.add_argument(
        "--skip-sync",
        action="store_true",
        help="Skip site rebuild/check (not recommended).",
    )
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=None,
        help="Override schema root passed to sync_site.",
    )
    args = parser.parse_args()

    branch = current_branch()
    if branch != args.branch:
        raise SystemExit(
            f"On branch {branch!r}, expected {args.branch!r}. "
            f"Checkout {args.branch} or pass --branch {branch!r}."
        )

    release = resolve_version(version=args.version, bump=args.bump)
    tag_message = args.tag_message or f"Release {release}"

    if tag_exists(release):
        raise SystemExit(f"Tag already exists: {release}")

    print_step("Plan")
    print(f"  branch:  {branch}")
    print(f"  release: {release}")
    print(f"  push:    {args.push}")
    if not is_working_tree_clean():
        print(f"  dirty:   yes\n{working_tree_status()}")
    else:
        print("  dirty:   no")

    if not args.skip_sync:
        print_step("Sync site (build + CI check)")
        if args.dry_run:
            print("  [dry-run] would run build_site.py and check")
        else:
            run_build(schema_root=args.schema_root)
            run_check(schema_root=args.schema_root)

    status_after_sync = working_tree_status()
    if status_after_sync:
        if not args.commit and not args.dry_run:
            raise SystemExit(
                "Working tree has uncommitted changes after sync. "
                "Commit them first or rerun with --commit 'your message'.\n\n"
                f"{status_after_sync}"
            )
        if args.commit:
            print_step(f"Commit: {args.commit!r}")
        elif args.dry_run:
            print_step("Commit")
            print("  [dry-run] would require --commit 'message' (working tree is dirty)")
        if args.dry_run:
            if args.commit:
                print("  [dry-run] would git add -A && git commit")
        else:
            if not args.commit:
                raise SystemExit("Internal error: commit required but missing.")
            commit_all(args.commit)
            if not is_working_tree_clean():
                raise SystemExit(
                    "Working tree still dirty after commit:\n"
                    f"{working_tree_status()}"
                )
    elif args.commit:
        print("\nNote: --commit ignored; working tree already clean.")

    print_step(f"Create tag {release}")
    if args.dry_run:
        print(f"  [dry-run] would git tag -a {release} -m {tag_message!r}")
    else:
        create_annotated_tag(release, tag_message)
        print(f"  created {release}")

    if args.push:
        print_step("Push to origin")
        if args.dry_run:
            print(f"  [dry-run] would git push origin {branch}")
            print(f"  [dry-run] would git push origin {release}")
        else:
            push_release(branch=branch, tag=release)
            print(f"  pushed {branch} and {release}")
    else:
        print("\nSkipped push (--no-push). Publish manually with:")
        print(f"  git push origin {branch}")
        print(f"  git push origin {release}")

    print(f"\nDone. Release {release} will publish via GitHub Actions when pushed.")
    if args.dry_run:
        print("(dry-run — no changes were made)")


if __name__ == "__main__":
    main()
