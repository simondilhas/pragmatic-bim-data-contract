---
search:
  boost: 5.0
---

# Slot: reference_source 


_Reference dataset, organisation, or document for this observation._



<div data-search-exclude markdown="1">



URI: [cost:reference_source](https://schema.pragmaticbim.ch/cost/reference_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PriceObservation](PriceObservation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:reference_source |
| native | cost:reference_source |




## LinkML Source

<details>
```yaml
name: reference_source
description: Reference dataset, organisation, or document for this observation.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
domain_of:
- PriceObservation
range: string

```
</details></div>