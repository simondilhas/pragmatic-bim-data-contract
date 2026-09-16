---
search:
  boost: 5.0
---

# Slot: provenance_status 


_How the unit-price point estimate was sourced and validated._



<div data-search-exclude markdown="1">



URI: [cost:provenance_status](https://schema.pragmaticbim.ch/cost/provenance_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |  yes  |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProvenanceStatusEnum](ProvenanceStatusEnum.md) |
| Domain Of | [UnitPriceEntry](UnitPriceEntry.md), [PriceObservation](PriceObservation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:provenance_status |
| native | cost:provenance_status |




## LinkML Source

<details>
```yaml
name: provenance_status
description: How the unit-price point estimate was sourced and validated.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- UnitPriceEntry
- PriceObservation
range: ProvenanceStatusEnum

```
</details></div>