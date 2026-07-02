

# Slot: decided_by 


_Agent responsible for the decision._





URI: [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo)
Alias: decided_by

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasAttributedTo |
| native | pbs:decided_by |




## LinkML Source

<details>
```yaml
name: decided_by
description: Agent responsible for the decision.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
slot_uri: prov:wasAttributedTo
alias: decided_by
domain_of:
- Decision
range: Agent
inlined: false

```
</details>