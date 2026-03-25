

# Slot: language_tag 


_IETF BCP 47 language tag (for example en, de, pt-BR)._





URI: [pbs:language_tag](https://example.org/pragmatic-bim-data-contract/language_tag)
Alias: language_tag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocalizedText](LocalizedText.md) | Localized text value for a specific language tag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LocalizedText](LocalizedText.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:language_tag |
| native | pbs:language_tag |




## LinkML Source

<details>
```yaml
name: language_tag
description: IETF BCP 47 language tag (for example en, de, pt-BR).
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: language_tag
domain_of:
- LocalizedText
range: string
required: true

```
</details>