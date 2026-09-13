---
search:
  boost: 2.0
---


# Enum: LawfulBasis 




_Lawful basis for processing personal data, aligned with GDPR Article 6 and similar regimes._



<div data-search-exclude markdown="1">

URI: [pbs:LawfulBasis](https://schema.pragmaticbim.ch/LawfulBasis)

**Enum URI:** [pbs:LawfulBasis](https://schema.pragmaticbim.ch/LawfulBasis)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| consent | pbs:lawful_basis_consent | Data subject has given consent for one or more specific purposes. | Title: Consent<br>|
| contract | pbs:lawful_basis_contract | Processing is necessary for the performance of a contract or pre-contractual steps. | Title: Contract<br>|
| legal_obligation | pbs:lawful_basis_legal_obligation | Processing is necessary to comply with a legal obligation. | Title: Legal obligation<br>|
| vital_interest | pbs:lawful_basis_vital_interest | Processing is necessary to protect vital interests of the data subject or another person. | Title: Vital interest<br>|
| public_task | pbs:lawful_basis_public_task | Processing is necessary for the performance of a task carried out in the public interest. | Title: Public task<br>|
| legitimate_interest | pbs:lawful_basis_legitimate_interest | Processing is necessary for legitimate interests pursued by the controller or a third party. | Title: Legitimate interest<br>|




## Slots

| Name | Description |
| ---  | --- |
| [lawful_basis](lawful_basis.md) | Lawful basis for processing the scoped personal data categories. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: LawfulBasis
description: Lawful basis for processing personal data, aligned with GDPR Article
  6 and similar regimes.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:LawfulBasis
permissible_values:
  consent:
    text: consent
    description: Data subject has given consent for one or more specific purposes.
    meaning: pbs:lawful_basis_consent
    alt_descriptions:
      de:
        source: de
        description: Einwilligung
    title: Consent
  contract:
    text: contract
    description: Processing is necessary for the performance of a contract or pre-contractual
      steps.
    meaning: pbs:lawful_basis_contract
    alt_descriptions:
      de:
        source: de
        description: Vertrag
    title: Contract
  legal_obligation:
    text: legal_obligation
    description: Processing is necessary to comply with a legal obligation.
    meaning: pbs:lawful_basis_legal_obligation
    alt_descriptions:
      de:
        source: de
        description: Rechtliche Verpflichtung
    title: Legal obligation
  vital_interest:
    text: vital_interest
    description: Processing is necessary to protect vital interests of the data subject
      or another person.
    meaning: pbs:lawful_basis_vital_interest
    alt_descriptions:
      de:
        source: de
        description: Lebenswichtiges Interesse
    title: Vital interest
  public_task:
    text: public_task
    description: Processing is necessary for the performance of a task carried out
      in the public interest.
    meaning: pbs:lawful_basis_public_task
    alt_descriptions:
      de:
        source: de
        description: Öffentliche Aufgabe
    title: Public task
  legitimate_interest:
    text: legitimate_interest
    description: Processing is necessary for legitimate interests pursued by the controller
      or a third party.
    meaning: pbs:lawful_basis_legitimate_interest
    alt_descriptions:
      de:
        source: de
        description: Berechtigtes Interesse
    title: Legitimate interest

```
</details>

</div>