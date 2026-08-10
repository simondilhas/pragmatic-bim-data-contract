---
search:
  boost: 2.0
---


# Enum: CostRecordRole 



<div data-search-exclude markdown="1">

URI: [pbs:CostRecordRole](https://schema.pragmaticbim.ch/CostRecordRole)

**Enum URI:** [pbs:CostRecordRole](https://schema.pragmaticbim.ch/CostRecordRole)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| cost | pbs:cost_record_role_cost | Internal or vendor cost for a catalog product. | Title: Cost<br>|
| price | pbs:cost_record_role_price | Sale or list price for a catalog product; may be customer-specific. | Title: Price<br>|
| estimate | pbs:cost_record_role_estimate | Project-side estimated cost line. | Title: Estimate<br>|
| actual | pbs:cost_record_role_actual | Project-side incurred or actual cost line. | Title: Actual<br>|




## Slots

| Name | Description |
| ---  | --- |
| [cost_record_role](cost_record_role.md) | Role of this cost record (catalog cost, catalog price, project estimate, or actual). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: CostRecordRole
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:CostRecordRole
permissible_values:
  cost:
    text: cost
    description: Internal or vendor cost for a catalog product.
    meaning: pbs:cost_record_role_cost
    alt_descriptions:
      de:
        source: de
        description: Kosten
    title: Cost
  price:
    text: price
    description: Sale or list price for a catalog product; may be customer-specific.
    meaning: pbs:cost_record_role_price
    alt_descriptions:
      de:
        source: de
        description: Preis
    title: Price
  estimate:
    text: estimate
    description: Project-side estimated cost line.
    meaning: pbs:cost_record_role_estimate
    alt_descriptions:
      de:
        source: de
        description: Schaetzung
    title: Estimate
  actual:
    text: actual
    description: Project-side incurred or actual cost line.
    meaning: pbs:cost_record_role_actual
    alt_descriptions:
      de:
        source: de
        description: Ist
    title: Actual

```
</details>

</div>