---
search:
  boost: 10.0
---

# Class: BaselinePriceBook 


_Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark._



<div data-search-exclude markdown="1">



URI: [cost:BaselinePriceBook](https://schema.pragmaticbim.ch/cost/BaselinePriceBook)





```mermaid
classDiagram
direction TB
class BaselinePriceBook
click BaselinePriceBook href "./BaselinePriceBook.html" _blank
click UnitPriceEntry href "./UnitPriceEntry.html" _blank
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [cost:BaselinePriceBook](https://schema.pragmaticbim.ch/cost/BaselinePriceBook) |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [version](version.md) | 0..1 <br/> [String](String.md) | Edition label (for example v12). | direct |
| [issued](issued.md) | 1 <br/> [Date](Date.md) | Publication date of this dataset edition. | direct |
| [anchor_region](anchor_region.md) | 1 <br/> [String](String.md) | Region code where material_factor and labor_factor are 1.0 (for example DE_MU). | direct |
| [source](source.md) | 0..1 <br/> [String](String.md) | Path or URI of the editorial source workbook. | direct |
| [license](license.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | License URI for the dataset (CC BY 4.0 for benchmark data). | direct |
| [disclaimer](disclaimer.md) | 0..1 <br/> [String](String.md) | Pointer to notice/disclaimer text. | direct |
| [carbon_source](carbon_source.md) | 0..1 <br/> [String](String.md) | Human-readable name of the carbon reference database. | direct |
| [carbon_source_version](carbon_source_version.md) | 0..1 <br/> [String](String.md) | Version of the carbon reference database (for example 8.02). | direct |
| [entries](entries.md) | * <br/> [UnitPriceEntry](UnitPriceEntry.md) | Baseline unit-price entries keyed by product notation. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cost:BaselinePriceBook |
| native | cost:BaselinePriceBook |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BaselinePriceBook
description: Container for baseline unit-price entries. Monetary values on entries
  are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours
  only; labor money lives on RegionalBenchmark.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
slots:
- version
- issued
- anchor_region
- source
- license
- disclaimer
- carbon_source
- carbon_source_version
- entries
slot_usage:
  issued:
    name: issued
    required: true
  anchor_region:
    name: anchor_region
    required: true
  entries:
    name: entries
    range: UnitPriceEntry
    multivalued: true
    inlined: true
class_uri: cost:BaselinePriceBook
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: BaselinePriceBook
description: Container for baseline unit-price entries. Monetary values on entries
  are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours
  only; labor money lives on RegionalBenchmark.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
slot_usage:
  issued:
    name: issued
    required: true
  anchor_region:
    name: anchor_region
    required: true
  entries:
    name: entries
    range: UnitPriceEntry
    multivalued: true
    inlined: true
attributes:
  version:
    name: version
    description: Edition label (for example v12).
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: string
  issued:
    name: issued
    description: Publication date of this dataset edition.
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: date
    required: true
  anchor_region:
    name: anchor_region
    description: Region code where material_factor and labor_factor are 1.0 (for example
      DE_MU).
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: string
    required: true
  source:
    name: source
    description: Path or URI of the editorial source workbook.
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: string
  license:
    name: license
    description: License URI for the dataset (CC BY 4.0 for benchmark data).
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: uriorcurie
  disclaimer:
    name: disclaimer
    description: Pointer to notice/disclaimer text.
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    - RegionalCostBenchmarkBook
    range: string
  carbon_source:
    name: carbon_source
    description: Human-readable name of the carbon reference database.
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    range: string
  carbon_source_version:
    name: carbon_source_version
    description: Version of the carbon reference database (for example 8.02).
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    range: string
  entries:
    name: entries
    description: Baseline unit-price entries keyed by product notation.
    from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
    rank: 1000
    owner: BaselinePriceBook
    domain_of:
    - BaselinePriceBook
    range: UnitPriceEntry
    multivalued: true
    inlined: true
class_uri: cost:BaselinePriceBook
tree_root: true

```
</details></div>