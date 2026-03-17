# Converter

IFC converter and persistence layer for the Pragmatic BIM schema.

## What it does

- Parses IFC input.
- Maps IFC entities/relations to Pragmatic BIM entities/relations.
- Validates required slots and enum values using:
  - `schema/enums_schema.yaml`
  - `schema/performance_enums_schema.yaml`
  - `schema/requirements_enums_schema.yaml`
- Writes to a SQLAlchemy-backed DB using one codepath for:
  - SQLite (`sqlite:///...`)
  - PostgreSQL (`postgresql+psycopg://...`)
- Exports canonical `entities.ndjson` and `relations.ndjson`.

## Setup

```bash
cd converter
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Quickstart

```bash
cd converter
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
PYTHONPATH=src pytest -q
pbs-converter init-db --database-url "sqlite:///converter/pragmatic_bim.db"
pbs-converter convert-ifc --ifc-file /absolute/path/model.ifc --database-url "sqlite:///converter/pragmatic_bim.db"
pbs-converter export-ndjson --database-url "sqlite:///converter/pragmatic_bim.db" --out-dir /absolute/path/out
```

## CLI

### 1) Initialize / migrate DB

```bash
pbs-converter init-db --database-url "sqlite:///converter/pragmatic_bim.db"
```

PostgreSQL example:

```bash
pbs-converter init-db --database-url "postgresql+psycopg://user:pass@localhost:5432/pragmatic_bim"
```

PostgreSQL conversion/export example:

```bash
pbs-converter convert-ifc --ifc-file /absolute/path/model.ifc --database-url "postgresql+psycopg://user:pass@localhost:5432/pragmatic_bim"
pbs-converter export-ndjson --database-url "postgresql+psycopg://user:pass@localhost:5432/pragmatic_bim" --out-dir /absolute/path/out
```

### 2) Convert IFC into DB

```bash
pbs-converter convert-ifc \
  --ifc-file /absolute/path/to/model.ifc \
  --database-url "sqlite:///converter/pragmatic_bim.db"
```

Use strict mode to fail on validation errors:

```bash
pbs-converter convert-ifc --ifc-file /absolute/path/to/model.ifc --strict
```

### 3) Export DB to NDJSON

```bash
pbs-converter export-ndjson \
  --database-url "sqlite:///converter/pragmatic_bim.db" \
  --out-dir /absolute/path/to/out
```

## Data model in DB

- `entities`
  - `id` (PK)
  - `type`
  - `name`
  - `ifc_global_id`
  - `payload` (JSON)
- `relations`
  - `from_id` (FK -> entities.id)
  - `relation_type`
  - `to_id` (FK -> entities.id)
  - `payload` (JSON)
  - `source`
