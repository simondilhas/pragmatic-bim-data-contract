

# Slot: belongs_to_company 


_Optional company that the person belongs to._





URI: [pbs:belongs_to_company](https://example.org/pragmatic-bim-data-contract/belongs_to_company)
Alias: belongs_to_company

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represent... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
| Domain Of | [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:belongs_to_company |
| native | pbs:belongs_to_company |




## LinkML Source

<details>
```yaml
name: belongs_to_company
description: Optional company that the person belongs to.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: belongs_to_company
domain_of:
- Person
range: Company
inlined: false

```
</details>