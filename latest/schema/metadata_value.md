

# Slot: metadata_value 


_Metadata value serialized as text._





URI: [pbs:metadata_value](https://example.org/pragmatic-bim-data-contract/metadata_value)
Alias: metadata_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetadataEntry](MetadataEntry.md) | Generic metadata entry for storing IFC attributes, PropertySet fields, or pro... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MetadataEntry](MetadataEntry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:metadata_value |
| native | pbs:metadata_value |




## LinkML Source

<details>
```yaml
name: metadata_value
description: Metadata value serialized as text.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: metadata_value
domain_of:
- MetadataEntry
range: string

```
</details>