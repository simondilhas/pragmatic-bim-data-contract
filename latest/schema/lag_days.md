---
search:
  boost: 5.0
---

# Slot: lag_days 


_Optional lag or lead offset in days applied to the dependency relation._



<div data-search-exclude markdown="1">



URI: [pbs:lag_days](https://schema.pragmaticbim.ch/lag_days)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleDependency](ScheduleDependency.md) | Precedence relationship between two schedule items, optionally with lag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [ScheduleDependency](ScheduleDependency.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:lag_days |
| native | pbs:lag_days |




## LinkML Source

<details>
```yaml
name: lag_days
description: Optional lag or lead offset in days applied to the dependency relation.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ScheduleDependency
range: double

```
</details></div>