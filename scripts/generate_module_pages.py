#!/usr/bin/env python3
"""Generate JSON descriptors for schema module URIs."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlparse

import yaml

ARTIFACTS = (
    ("json_schema", "JSON Schema", "pragmatic-bim.schema.json", "application/json"),
    ("shacl", "SHACL", "pragmatic-bim.shacl.ttl", "text/turtle"),
    ("csv", "CSV", "pragmatic-bim.csv", "text/csv"),
    ("pydantic", "Pydantic", "pragmatic-bim.pydantic.py", "text/x-python"),
    ("docs_md", "Docs (Markdown)", "pragmatic-bim.docs.md", "text/markdown"),
)


def normalize_description(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def slug_from_id(module_id: str, base_url: str) -> str | None:
    base = base_url.rstrip("/")
    if module_id.rstrip("/") == base:
        return None
    parsed = urlparse(module_id)
    path = parsed.path.strip("/")
    if not path:
        return None
    return path


def pick_primary_doc(doc: dict) -> str | None:
    classes = doc.get("classes")
    if isinstance(classes, dict) and classes:
        for name, body in classes.items():
            if isinstance(body, dict) and body.get("abstract"):
                return name
        for name, body in classes.items():
            if isinstance(body, dict) and body.get("tree_root"):
                return name
        for name, body in classes.items():
            if isinstance(body, dict):
                slots = body.get("slots", [])
                if isinstance(slots, list) and "id" in slots:
                    return name
        for name, body in classes.items():
            if isinstance(body, dict) and not body.get("abstract"):
                return name
        return next(iter(classes.keys()))
    enums = doc.get("enums")
    if isinstance(enums, dict) and enums:
        return next(iter(enums.keys()))
    return None


def load_modules(schema_dir: Path, base_url: str) -> list[dict]:
    modules: list[dict] = []
    for schema_file in sorted(schema_dir.glob("*_schema.yaml")):
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        module_id = doc.get("id")
        if not isinstance(module_id, str) or not module_id.strip():
            continue
        slug = slug_from_id(module_id.strip(), base_url)
        if slug is None:
            continue
        primary = pick_primary_doc(doc)
        modules.append(
            {
                "slug": slug,
                "id": module_id.strip(),
                "title": doc.get("title") or slug,
                "description": normalize_description(doc.get("description")),
                "source_file": schema_file.name,
                "primary_doc": primary,
            }
        )
    return modules


def artifact_urls(base_url: str) -> dict[str, str]:
    schema_base = f"{base_url.rstrip('/')}/schema"
    urls = {"docs_index": f"{schema_base}/pragmatic-bim.docs.html"}
    for key, _, filename, _ in ARTIFACTS:
        urls[key] = f"{schema_base}/{filename}"
    return urls


def build_descriptor(module: dict, base_url: str) -> dict:
    urls = artifact_urls(base_url)
    descriptor = {
        "id": module["id"],
        "title": module["title"],
        "description": module["description"],
        "source_file": module["source_file"],
        "docs_index": urls["docs_index"],
        "json_schema": urls["json_schema"],
        "shacl": urls["shacl"],
        "csv": urls["csv"],
        "pydantic": urls["pydantic"],
        "docs_md": urls["docs_md"],
    }
    primary = module.get("primary_doc")
    if primary:
        descriptor["html"] = f"{urls['docs_index'].rsplit('/', 1)[0]}/{primary}.html"
        descriptor["primary_doc"] = primary
    return descriptor


def render_root_redirect(base_url: str) -> str:
    docs_index = f"{base_url.rstrip('/')}/schema/pragmatic-bim.docs.html"
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="0; url=./schema/pragmatic-bim.docs.html">
    <link rel="canonical" href="{html.escape(docs_index)}">
    <title>Pragmatic BIM Data Contract</title>
  </head>
  <body>
    <p><a href="./schema/pragmatic-bim.docs.html">Pragmatic BIM Data Contract</a></p>
  </body>
</html>
"""


def write_module_descriptors(
    site_dir: Path,
    modules: list[dict],
    base_url: str,
) -> None:
    site_dir.mkdir(parents=True, exist_ok=True)
    for module in modules:
        slug = module["slug"]
        descriptor = build_descriptor(module, base_url)
        slug_dir = site_dir / slug
        slug_dir.mkdir(parents=True, exist_ok=True)
        (slug_dir / "descriptor.json").write_text(
            json.dumps(descriptor, indent=2) + "\n",
            encoding="utf-8",
        )
        for stale in (slug_dir / "index.html", site_dir / f"{slug}.html"):
            if stale.is_file():
                stale.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--schema-dir", type=Path, default=Path("schema"))
    parser.add_argument("--base-url", default="https://schema.pragmaticbim.ch")
    parser.add_argument(
        "--write-root-index",
        action="store_true",
        help="Write site/index.html redirecting to the main schema docs page.",
    )
    args = parser.parse_args()

    modules = load_modules(args.schema_dir, args.base_url)
    if not modules:
        raise SystemExit(f"No modules found in {args.schema_dir}")

    write_module_descriptors(
        args.site_dir,
        modules,
        args.base_url.rstrip("/"),
    )
    manifest = {
        "base_url": args.base_url.rstrip("/"),
        "docs_index": f"{args.base_url.rstrip('/')}/schema/pragmatic-bim.docs.html",
        "modules": [
            {
                "slug": module["slug"],
                "id": module["id"],
                "title": module["title"],
                "descriptor": f"{args.base_url.rstrip('/')}/{module['slug']}/descriptor.json",
            }
            for module in modules
        ],
    }
    args.site_dir.mkdir(parents=True, exist_ok=True)
    (args.site_dir / "modules.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    if args.write_root_index:
        (args.site_dir / "index.html").write_text(
            render_root_redirect(args.base_url.rstrip("/")),
            encoding="utf-8",
        )

    print(f"Generated descriptors for {len(modules)} modules in {args.site_dir}")


if __name__ == "__main__":
    main()
