

# Slot: contact_points 


_Structured communication channels and profiles associated with this agent._





URI: [pbs:contact_points](https://example.org/pragmatic-bim-data-contract/contact_points)
Alias: contact_points

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
| Range | [ContactPoint](ContactPoint.md) |
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
| self | pbs:contact_points |
| native | pbs:contact_points |




## LinkML Source

<details>
```yaml
name: contact_points
description: Structured communication channels and profiles associated with this agent.
from_schema: https://example.org/pragmatic-bim-data-contract
rank: 1000
alias: contact_points
domain_of:
- Agent
range: ContactPoint
multivalued: true
inlined: true

```
</details>