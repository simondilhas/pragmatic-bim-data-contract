# Baseline unit prices

Indicative material unit costs, labor hours, and disassembly/demolition costs
for the abstract SKOS product classifications used in Pragmatic BIM workflows.

Material costs are anchored to a **EUR (DE-level) baseline** (`anchor_region:
DE_MU`) and are **net** — **VAT** and contingency are **excluded**. Regional
installed cost is computed at use time from `regional-benchmarks.json`.

Values are researched from public references (BKI Baukosten element cost values,
manufacturer/trade list prices) keyed to the reference area / price unit of each
product; they are estimates, not quotations. Embodied-carbon (KBOB) enrichment
is deferred and added in a later pass.

**License:** [CC BY 4.0](LICENSE) · **Disclaimer:** [NOTICE.md](NOTICE.md)

**Schema:** [Baseline cost module](../contract/cost/README.md) — LinkML module at
`contract/cost/`; JSON validates against `BaselinePriceBook` and
`RegionalCostBenchmarkBook`.

## Source of truth

One JSON file per assignable SKOS top concept lives in
[`entries/`](entries/) and is the **git source of truth** (125 codes). Each file
is minimal authored input; the build derives the rest.

Scope is limited to concepts whose notation prefix has a category in
`NOTATION_PREFIX_CATEGORIES` (`scripts/baseline_prices_common.py`), because the
category resolves the waste, transport, and demolition defaults an entry needs.
MEP product concepts (`MTP-*`, `MUP-*`) are outside the book for that reason.

```json
{
  "product": "SWP-ORTBETON",
  "material_cost": 150.0,
  "price_unit": "m3",
  "onsite_labor_hours_per_unit": 9.5,
  "provenance_status": "reference_calibrated",
  "observations": [
    {
      "aspect": "material_cost",
      "value": 150.0,
      "reference_source": "BKI Baukosten Bauelemente Neubau 2026 ...",
      "contributed_at": "2026-07-01",
      "provenance_status": "reference_calibrated",
      "selects_canonical": true
    }
  ]
}
```

The build derives `product_uri`, `delivered_material_cost`, `demolition`,
`uncertainty`, and category defaults (`waste_pct`, `transport_pct`) from
`cost-adjustments.json`.

## Files

| File | In git | Description |
|------|:------:|-------------|
| `entries/{NOTATION}.json` | yes | **Source of truth** — one authored entry per SKOS top concept |
| `cost-adjustments.json` | yes | Authored: per-category waste/transport/demolition/uncertainty defaults + `material_share` |
| `regional-material-benchmarks.json` | yes | Authored: regional `material_factor` + `fx_to_eur` (DE_MU = 1.00 anchor) |
| `regional-labor-benchmarks.json` | yes | Authored: regional onsite/offsite labor rates (net, local currency) |
| `labor-overrides.json` | yes | Legacy/reference prefab labor-hour notes (not read by the build) |
| `product-manifest.json` | yes | Generated code list from SKOS (committed for diff visibility) |
| `baseline-products.json` | no | Generated: `BaselinePriceBook` (CI artifact) |
| `regional-benchmarks.json` | no | Generated: `RegionalCostBenchmarkBook` (CI artifact) |
| `baseline-products.csv`, `*.csv` | no | Generated flat exports for review |

## Pipeline

```bash
# 1. Refresh the manifest and scaffold any missing entry templates
python scripts/list_baseline_products.py --scaffold

# 2. Build the merged price book + regional benchmarks from entries/
python scripts/build_baseline_products.py

# 3. Export flat CSVs for review
python scripts/export_baseline_prices_csv.py

# 4. Validate coverage, schema, uncertainty, observations, and data quality
python scripts/validate_baseline_prices.py
```

Requires `rdflib` (SKOS parsing) and `linkml` (validation).

`list_baseline_products.py --check` fails when `entries/` and the SKOS top
concepts disagree; the build refuses to run unless every code has a positive
`material_cost`, a valid `price_unit`, and an `onsite_labor_hours_per_unit`.

## Edit workflow

1. Research a net-EUR material cost and onsite labor hours for the product,
   keyed to its price unit. The price unit is **not a free choice**: it is the
   unit of the reference quantity that the Elementplan element declares for the
   scheme this product belongs to (m² face, m³ member or concrete volume, m of
   running length for beams and railings). `validate_element_classification.py`
   fails when an entry is priced in another unit than its element.
2. Edit `entries/{NOTATION}.json`: set `material_cost`,
   `onsite_labor_hours_per_unit` (and `offsite_labor_hours_per_unit` for
   prefab), and add at least one `observation` with `reference_source` and
   `selects_canonical: true`.
3. Adjust category defaults in `cost-adjustments.json` if needed.
4. Run the pipeline above.

## Currency and installed cost

**Price book (EUR invariant, net):** all `material_cost` and demolition disposal
values are EUR excluding VAT. Labor on the book is **hours only**.

**Regional book (net):** `labor_unit_price` and `offsite_labor_unit_price` in
local `currency`, excluding VAT.

```
delivered_eur = material_cost × (1 + waste_pct) × (1 + transport_pct)

material_local = (delivered_eur / fx_to_eur) × material_factor

labor_local = onsite_hours × labor_unit_price × labor_factor
            + offsite_hours × offsite_labor_unit_price × labor_factor

installed_local = material_local + labor_local
```

## Estimation method

Public references (e.g. BKI Baukosten Bauelemente) typically give **installed,
gross** element rates. To reach the schema shape:

1. Remove VAT to reach net EUR.
2. Split the installed rate into ex-works `material_cost` (EUR) and
   `onsite_labor_hours_per_unit` using the per-category `material_share` in
   `cost-adjustments.json` and the DE_MU `labor_unit_price`.
3. Record the source and split assumption in `observations[]`; set
   `provenance_status: reference_calibrated` when tied to a named reference,
   otherwise `estimated`.

## JSON schema (summary)

See [`contract/cost/README.md`](../contract/cost/README.md) for the LinkML module.

**baseline-products.json** (`BaselinePriceBook`)

- `anchor_region` — e.g. `DE_MU`
- `entries` — dict keyed by SKOS `product` notation
- `entries[].material_cost`, `price_unit`, `waste_pct`, `transport_pct` (EUR net)
- `entries[].onsite_labor_hours_per_unit`, `offsite_labor_hours_per_unit`
- `entries[].uncertainty`, `demolition`, `provenance_status`, `observations`

**regional-benchmarks.json** (`RegionalCostBenchmarkBook`)

- `regions` — dict keyed by `code`
- `regions[].material_factor`, `fx_to_eur`, `labor_factor`
- `regions[].labor_unit_price`, `offsite_labor_unit_price`, `currency`

Product labels and definitions remain in
`classification/**/*-products.skos.ttl`.

## Element binding

Which product applies to which building element is resolved by
[`classification/mapping/elementplan-elements-to-products.mapping.ttl`](../classification/mapping/elementplan-elements-to-products.mapping.ttl).
Each element declares one reference quantity and price unit, and every product
of the linked scheme shares them, so an element resolves to exactly one quantity
basis, enforced by `validate_element_classification.py`.

Where a researched reference came in another unit than the element declares, the
entry was rebased on a nominal geometry recorded in its observation notes:

| Products | Reference basis | Priced as | Nominal geometry |
|----------|-----------------|-----------|------------------|
| `DCP-*` | per door leaf | m² of opening (`Qto_DoorBaseQuantities.Area`) | 1.89 m² opening |
| `WICP-SKYLIGHT` | per rooflight | m² of opening (`Qto_WindowBaseQuantities.Area`) | 1.20 m² rooflight |
| `SWP-ORTBETON`, `SWP-PREFAB-CONC` | per m³ concrete | m² wall face (`Qto_WallBaseQuantities.NetSideArea`) | 0.20 m wall thickness |
| `SSP-INSITU` | per m³ concrete | m² slab area (`Qto_SlabBaseQuantities.GrossArea`) | 0.28 m slab thickness |
| `FDP-DRAINAGE`, `FDP-WATERPROOF` | per m² layer | m³ foundation volume (`Qto_FootingBaseQuantities.GrossVolume`) | 0.30 m foundation thickness |
| `BMP-*` | per m³ member | m of beam length (`Qto_BeamBaseQuantities.Length`) | HEA 300, 200×400 mm, 300×600 mm per material |

Rebased entries carry `provenance_status: estimated`, since the unit basis is
derived rather than sourced.
