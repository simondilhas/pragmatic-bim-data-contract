

# Slot: postal_addresses 


_Structured postal or physical addresses associated with this agent._





URI: [pbs:postal_addresses](https://example.org/pragmatic-bim-data-contract/postal_addresses)
Alias: postal_addresses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represent... |  no  |
| [Company](Company.md) | Organization, company, or legal entity participating in the project or asset ... |  no  |
| [Agent](Agent.md) | Abstract base class for people or organizations acting in workflow and commun... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PostalAddress](PostalAddress.md) |
| Domain Of | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/pragmatic-bim-data-contract




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:postal_addresses |
| native | pbs:postal_addresses |




## LinkML Source

<details>
```yaml
name: postal_addresses
description: Structured postal or physical addresses associated with this agent.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: postal_addresses
domain_of:
- Agent
range: PostalAddress
multivalued: true
inlined: true

```
</details>