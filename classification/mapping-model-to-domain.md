# Abstract model to domain mapping

Source: [`abstract-model-to-domain.mapping.ttl`](sources/mapping-model-to-domain.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jeden BIM-Fachmodelltyp seinem Fachbereich zu (Architektur ARC, Tragwerk STR, Gebäudetechnik MEP). closeMatch ist der Fachbereich im Dateinamen-Präfix `{DOMAIN}-{MODEL}`.
- **description (en):** Maps each BIM discipline-model type to its domain (architecture ARC, structural STR, MEP). closeMatch is the owning domain used in the file-name prefix `{DOMAIN}-{MODEL}`.
- **title (de):** Mapping abstrakter Fachmodelle zu Fachbereichen
- **title (en):** Abstract model to domain mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mod:architecture` | `closeMatch` | `dom:architecture` |
| `mod:concrete-structure` | `closeMatch` | `dom:structural` |
| `mod:cooling` | `closeMatch` | `dom:mep` |
| `mod:earthworks` | `closeMatch` | `dom:structural` |
| `mod:excavation-pit` | `closeMatch` | `dom:structural` |
| `mod:facade` | `closeMatch` | `dom:architecture` |
| `mod:furniture` | `closeMatch` | `dom:architecture` |
| `mod:heating` | `closeMatch` | `dom:mep` |
| `mod:laboratory` | `closeMatch` | `dom:architecture` |
| `mod:landscape` | `closeMatch` | `dom:architecture` |
| `mod:plumbing` | `closeMatch` | `dom:mep` |
| `mod:reinforcement` | `closeMatch` | `dom:structural` |
| `mod:steel-structure` | `closeMatch` | `dom:structural` |
| `mod:storey-volume` | `closeMatch` | `dom:architecture` |
| `mod:surroundings` | `closeMatch` | `dom:architecture` |
| `mod:timber-structure` | `closeMatch` | `dom:structural` |
| `mod:underground-services` | `closeMatch` | `dom:mep` |
| `mod:ventilation` | `closeMatch` | `dom:mep` |
