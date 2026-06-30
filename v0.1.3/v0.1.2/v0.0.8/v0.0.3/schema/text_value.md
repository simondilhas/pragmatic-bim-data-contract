

# Slot: text_value 


_Localized text value._





URI: [pbs:text_value](https://example.org/pragmatic-bim-data-contract/text_value)
Alias: text_value

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
| self | pbs:text_value |
| native | pbs:text_value |




## LinkML Source

<details>
```yaml
name: text_value
description: Localized text value.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: text_value
domain_of:
- LocalizedText
range: string
required: true

```
</details>