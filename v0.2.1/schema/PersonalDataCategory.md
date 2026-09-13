---
search:
  boost: 2.0
---


# Enum: PersonalDataCategory 




_Category of personal data covered by consent or processing scope._



<div data-search-exclude markdown="1">

URI: [pbs:PersonalDataCategory](https://schema.pragmaticbim.ch/PersonalDataCategory)

**Enum URI:** [pbs:PersonalDataCategory](https://schema.pragmaticbim.ch/PersonalDataCategory)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| identity | pbs:personal_data_category_identity | Name, role labels, and other identity-related fields. | Title: Identity<br>|
| contact | pbs:personal_data_category_contact | Email, phone, handles, and other communication endpoints. | Title: Contact<br>|
| address | pbs:personal_data_category_address | Postal or physical addresses. | Title: Address<br>|
| affiliation | pbs:personal_data_category_affiliation | Company membership and organizational affiliation. | Title: Affiliation<br>|




## Slots

| Name | Description |
| ---  | --- |
| [data_categories](data_categories.md) | Personal data categories covered by this consent or processing record. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: PersonalDataCategory
description: Category of personal data covered by consent or processing scope.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:PersonalDataCategory
permissible_values:
  identity:
    text: identity
    description: Name, role labels, and other identity-related fields.
    meaning: pbs:personal_data_category_identity
    alt_descriptions:
      de:
        source: de
        description: Identität
    title: Identity
  contact:
    text: contact
    description: Email, phone, handles, and other communication endpoints.
    meaning: pbs:personal_data_category_contact
    alt_descriptions:
      de:
        source: de
        description: Kontakt
    title: Contact
  address:
    text: address
    description: Postal or physical addresses.
    meaning: pbs:personal_data_category_address
    alt_descriptions:
      de:
        source: de
        description: Adresse
    title: Address
  affiliation:
    text: affiliation
    description: Company membership and organizational affiliation.
    meaning: pbs:personal_data_category_affiliation
    alt_descriptions:
      de:
        source: de
        description: Zugehörigkeit
    title: Affiliation

```
</details>

</div>