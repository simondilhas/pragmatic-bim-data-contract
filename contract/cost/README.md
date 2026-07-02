# Baseline cost schema

LinkML module for baseline unit prices and regional cost benchmarks.

**Schema license:** MIT (same as [`contract/`](../README.md)).

**Data license:** [CC BY 4.0](../../baseline-unit-prices/LICENSE) for generated benchmark JSON.

## Module

| File | Role |
|------|------|
| `baseline_cost_schema.yaml` | `BaselinePriceBook`, `UnitPriceEntry`, `RegionalCostBenchmarkBook` |
| `baseline_cost_schema_enums.yaml` | `CurrencyEnum`, `PriceUnitEnum`, KBOB/carbon enums |

Module URI: `https://schema.pragmaticbim.ch/cost/baseline-cost`

Not imported by [`00_pragmatic_bim_data_contract.yaml`](../00_pragmatic_bim_data_contract.yaml). Published as a sibling artifact under `site/cost/`.

## Currency model

- **Price book:** all `material_cost` and demolition disposal values are **EUR**, **net (VAT excluded)** (schema invariant).
- **Labor on price book:** hours only (`onsite_labor_hours_per_unit`, `offsite_labor_hours_per_unit`).
- **Regional book:** `labor_unit_price` and `offsite_labor_unit_price` in regional `currency` (net, VAT excluded).

**Cost scope:** VAT and contingency are excluded from all benchmark amounts. See [`baseline-unit-prices/NOTICE.md`](../../baseline-unit-prices/NOTICE.md).

Installed cost in regional currency:

```
material_local = (delivered_eur / fx_to_eur) × material_factor
labor_local    = onsite_hours × labor_unit_price × labor_factor
               + offsite_hours × offsite_labor_unit_price × labor_factor
installed_local = material_local + labor_local
```

Source of truth is one JSON file per SKOS top concept in
[`baseline-unit-prices/entries/`](../../baseline-unit-prices/entries/). Category
defaults and the installed-rate `material_share` split assumption live in
[`baseline-unit-prices/cost-adjustments.json`](../../baseline-unit-prices/cost-adjustments.json).

## Uncertainty bands

Each `UnitPriceEntry` may include an inlined `uncertainty` object (`PriceUncertainty`):

- **Relative bands:** `material_low_pct`, `material_high_pct`, `labor_low_pct`, `labor_high_pct` — signed fractions relative to the point estimate (for example `-0.12` → low = point × 0.88).
- **Derived bounds:** `material_cost_low` / `_high`, `delivered_material_cost_low` / `_high`, `onsite_labor_hours_low` / `_high` (and offsite when applicable) are computed at generation time.

Each entry also carries **`provenance_status`** (`ProvenanceStatusEnum`):

| Value | Meaning |
|-------|---------|
| `estimated` | First fill — not yet checked against anything |
| `expert_reviewed` | Sanity-checked by someone with domain knowledge |
| `reference_calibrated` | Cross-checked against KBOB, CWICR, ÖKOBAUDAT, or similar |
| `project_validated` | Held up against realised cost on a real project |

Default is `estimated` (`default_provenance_status` in `cost-adjustments.json`; override per product in `product_overrides`).

## Observations (multi-contributor inputs)

Each `UnitPriceEntry` keeps **one canonical scalar** per costing slot (`material_cost`, labor hours, …) for deterministic lookup. Optional **`observations[]`** record alternative or supporting values with provenance:

| Field | Role |
|-------|------|
| `aspect` | Which canonical slot (`material_cost`, `onsite_labor_hours_per_unit`, …) |
| `value` | Observed number in the same unit as that slot |
| `reference_source` | Reference dataset, organisation, or document (required) |
| `contributor` | Person or team (optional) |
| `contributed_at` | When recorded (optional) |
| `provenance_status` | Validation level for this observation (optional) |
| `notes` | Scope, region, assumptions (optional) |
| `selects_canonical` | `true` if this observation was chosen for the parent canonical value |

Authoring workflow: contributors append observations to the per-code entry files in [`baseline-unit-prices/entries/`](../../baseline-unit-prices/entries/) and mark the chosen one with `selects_canonical: true`; the build carries observations through unchanged. Validation requires at least one observation with `selects_canonical` and a non-empty `reference_source` per entry.

Default uncertainty bands are authored in `cost-adjustments.json` (`default_uncertainty` and optional per-category `uncertainty` overrides) and applied by the build.

## Carbon geometry

`CarbonEstimate` stores unit-conversion basis in typed slots (`density_kg_m3`, `mass_per_area_kg_m2`, `area_per_piece_m2`, optional `thickness_m`). Defaults are authored in [`kbob-ecobilans-price-unit-defaults.json`](../../classification/mapping/kbob-ecobilans-price-unit-defaults.json). The generator must not use KBOB kg/m³ density as kg/m² mass.

**Subsystem pricing:** baseline `UnitPriceEntry` rows are keyed by **parent** SKOS notation (`FaCP-*`, `RCP-*`, `FDP-*`, …). Layer notations (`*-INS`, `*-MEM`, …) are recipe-only for `layer_recipe_sum` carbon unless explicitly given their own baseline row. See [Subsystem product classification](../../classification/README.md#subsystem-product-classification).

## Regenerate data

Source of truth is `baseline-unit-prices/entries/*.json`. Rebuild the merged
`BaselinePriceBook` and `RegionalCostBenchmarkBook`:

```bash
python scripts/list_baseline_products.py --scaffold   # sync entries with SKOS
python scripts/build_baseline_products.py             # entries → merged JSON
python scripts/export_baseline_prices_csv.py          # flat CSV exports
```

Carbon/KBOB enrichment is deferred; `scripts/generate_baseline_unit_prices.py`
remains for that later pass.

## Validate

```bash
python scripts/validate_baseline_prices.py
```

Runs manifest coverage, LinkML schema validation for both books, and the
uncertainty / observation / data-quality gates.
