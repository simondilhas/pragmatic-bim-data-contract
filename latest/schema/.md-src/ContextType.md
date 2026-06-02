---
search:
  boost: 2.0
---


# Enum: ContextType 



<div data-search-exclude markdown="1">

URI: [pbs:ContextType](https://schema.pragmaticbim.ch/ContextType)

**Enum URI:** [pbs:ContextType](https://schema.pragmaticbim.ch/ContextType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| project | ifcowl:IfcProject |  | Title: Project<br>|
| perimeter | ifcowl:IfcSite |  | Title: Perimeter<br>|
| legal_site | pbs:LegalSiteContext |  | Title: Legal Site<br>|
| building | bot:Building |  | Title: Building<br>|
| civil_structure | ifcowl:IfcCivilElement |  | Title: Civil Structure<br>|
| level | bot:Storey |  | Title: Level<br>|
| zone | bot:Zone |  | Title: Zone<br>|




## Slots

| Name | Description |
| ---  | --- |
| [context_type](context_type.md) | Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ContextType
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ContextType
permissible_values:
  project:
    text: project
    meaning: ifcowl:IfcProject
    alt_descriptions:
      de:
        source: de
        description: Projekt
    title: Project
  perimeter:
    text: perimeter
    meaning: ifcowl:IfcSite
    alt_descriptions:
      de:
        source: de
        description: Perimeter
    title: Perimeter
    exact_mappings:
    - bot:Site
  legal_site:
    text: legal_site
    meaning: pbs:LegalSiteContext
    alt_descriptions:
      de:
        source: de
        description: Rechtsgrundstueck
    title: Legal Site
  building:
    text: building
    meaning: bot:Building
    alt_descriptions:
      de:
        source: de
        description: Gebaeude
    title: Building
  civil_structure:
    text: civil_structure
    meaning: ifcowl:IfcCivilElement
    alt_descriptions:
      de:
        source: de
        description: Ingenieurbauwerk
    title: Civil Structure
  level:
    text: level
    meaning: bot:Storey
    alt_descriptions:
      de:
        source: de
        description: Ebene
    title: Level
  zone:
    text: zone
    meaning: bot:Zone
    alt_descriptions:
      de:
        source: de
        description: Zone
    title: Zone

```
</details>

</div>