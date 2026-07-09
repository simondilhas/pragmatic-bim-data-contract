---
search:
  boost: 2.0
---


# Enum: PriceObservationAspectEnum 




_Which canonical UnitPriceEntry slot an observation records. Monetary aspects are EUR net (VAT excluded); labor aspects are person-hours per price_unit; waste_pct and transport_pct are fractions (0–1)._



<div data-search-exclude markdown="1">

URI: [cost:PriceObservationAspectEnum](https://schema.pragmaticbim.ch/cost/PriceObservationAspectEnum)

**Enum URI:** [cost:PriceObservationAspectEnum](https://schema.pragmaticbim.ch/cost/PriceObservationAspectEnum)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| material_cost | None | Ex-works material cost per price_unit in EUR. | Title: Material cost<br>|
| waste_pct | None | Waste allowance as a fraction of material cost. | Title: Waste allowance<br>|
| transport_pct | None | Transport-to-site allowance as a fraction of material cost. | Title: Transport allowance<br>|
| onsite_labor_hours_per_unit | None | Onsite installation labor in person-hours per price_unit. | Title: Onsite labor hours<br>|
| offsite_labor_hours_per_unit | None | Factory/offsite labor in person-hours per price_unit. | Title: Offsite labor hours<br>|
| demolition_hours_per_unit | None | Demolition labor hours per price unit. | Title: Demolition labor hours<br>|
| demolition_disposal_cost | None | Disposal cost per price unit in EUR. | Title: Demolition disposal cost<br>|




## Slots

| Name | Description |
| ---  | --- |
| [aspect](aspect.md) | Canonical slot this observation applies to. |
| [aspect](aspect.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost






## LinkML Source

<details>
```yaml
name: PriceObservationAspectEnum
description: Which canonical UnitPriceEntry slot an observation records. Monetary
  aspects are EUR net (VAT excluded); labor aspects are person-hours per price_unit;
  waste_pct and transport_pct are fractions (0–1).
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
enum_uri: cost:PriceObservationAspectEnum
permissible_values:
  material_cost:
    text: material_cost
    description: Ex-works material cost per price_unit in EUR.
    title: Material cost
  waste_pct:
    text: waste_pct
    description: Waste allowance as a fraction of material cost.
    title: Waste allowance
  transport_pct:
    text: transport_pct
    description: Transport-to-site allowance as a fraction of material cost.
    title: Transport allowance
  onsite_labor_hours_per_unit:
    text: onsite_labor_hours_per_unit
    description: Onsite installation labor in person-hours per price_unit.
    title: Onsite labor hours
  offsite_labor_hours_per_unit:
    text: offsite_labor_hours_per_unit
    description: Factory/offsite labor in person-hours per price_unit.
    title: Offsite labor hours
  demolition_hours_per_unit:
    text: demolition_hours_per_unit
    description: Demolition labor hours per price unit.
    title: Demolition labor hours
  demolition_disposal_cost:
    text: demolition_disposal_cost
    description: Disposal cost per price unit in EUR.
    title: Demolition disposal cost

```
</details>

</div>