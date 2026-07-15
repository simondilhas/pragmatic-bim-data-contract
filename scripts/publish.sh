#!/usr/bin/env bash
# Publish: sync site, commit, tag, push.
# Usage:
#   ./scripts/publish.sh "commit message"           # bump patch (v0.1.7 -> v0.1.8)
#   ./scripts/publish.sh "commit message" v0.1.8    # explicit tag
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

COMMIT_MSG="${1:-}"
TAG="${2:-}"

if [[ "$(git branch --show-current)" != "main" ]]; then
  echo "Must be on main (currently on $(git branch --show-current))." >&2
  exit 1
fi

echo "==> Sync site"
python scripts/build_site.py
python scripts/build_site.py check

if [[ -n "$(git status --porcelain)" ]]; then
  if [[ -z "$COMMIT_MSG" ]]; then
    echo "Uncommitted changes. Pass a commit message:" >&2
    echo "  ./scripts/publish.sh \"your message\"" >&2
    exit 1
  fi
  echo "==> Commit"
  git add -A
  git commit -m "$COMMIT_MSG"
fi

if [[ -z "$TAG" ]]; then
  LATEST="$(git tag -l 'v*' --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1 || true)"
  if [[ -z "$LATEST" ]]; then
    TAG="v0.1.0"
  else
    VER="${LATEST#v}"
    IFS=. read -r MAJOR MINOR PATCH <<< "$VER"
    TAG="v${MAJOR}.${MINOR}.$((PATCH + 1))"
  fi
fi

if [[ ! "$TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid tag (use vMAJOR.MINOR.PATCH): $TAG" >&2
  exit 1
fi

if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "Tag already exists locally: $TAG" >&2
  exit 1
fi

if git ls-remote --exit-code --tags origin "refs/tags/${TAG}" >/dev/null 2>&1; then
  echo "Tag already exists on origin: $TAG" >&2
  exit 1
fi

echo "==> Tag $TAG"
git tag -a "$TAG" -m "Release $TAG"

echo "==> Push"
git push origin main
git push origin "$TAG"

echo "Done. GitHub Actions will publish $TAG to https://schema.pragmaticbim.ch/"
