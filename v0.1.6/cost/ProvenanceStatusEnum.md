---
search:
  boost: 2.0
---


# Enum: ProvenanceStatusEnum 




_How the unit-price point estimate was sourced and validated._



<div data-search-exclude markdown="1">

URI: [cost:ProvenanceStatusEnum](https://schema.pragmaticbim.ch/cost/ProvenanceStatusEnum)

**Enum URI:** [cost:ProvenanceStatusEnum](https://schema.pragmaticbim.ch/cost/ProvenanceStatusEnum)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| estimated | None | First fill — not yet checked against anything. | Title: Estimated<br>|
| expert_reviewed | None | A person with domain knowledge sanity-checked the value. | Title: Expert reviewed<br>|
| reference_calibrated | None | Cross-checked against KBOB, CWICR, ÖKOBAUDAT, or similar reference data. | Title: Reference calibrated<br>|
| project_validated | None | Held up against realised cost on a real project. | Title: Project validated<br>|




## Slots

| Name | Description |
| ---  | --- |
| [provenance_status](provenance_status.md) | How the unit-price point estimate was sourced and validated. |
| [provenance_status](provenance_status.md) |  |
| [provenance_status](provenance_status.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch/cost/baseline-cost






## LinkML Source

<details>
```yaml
name: ProvenanceStatusEnum
description: How the unit-price point estimate was sourced and validated.
from_schema: https://schema.pragmaticbim.ch/cost/baseline-cost
rank: 1000
enum_uri: cost:ProvenanceStatusEnum
permissible_values:
  estimated:
    text: estimated
    description: First fill — not yet checked against anything.
    title: Estimated
  expert_reviewed:
    text: expert_reviewed
    description: A person with domain knowledge sanity-checked the value.
    title: Expert reviewed
  reference_calibrated:
    text: reference_calibrated
    description: Cross-checked against KBOB, CWICR, ÖKOBAUDAT, or similar reference
      data.
    title: Reference calibrated
  project_validated:
    text: project_validated
    description: Held up against realised cost on a real project.
    title: Project validated

```
</details>

</div>