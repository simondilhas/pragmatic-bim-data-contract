# Abstract model to BKP delivered-by mapping

Source: [`abstract-model-to-bkp-delivered-by.mapping.ttl`](sources/mapping-model-to-bkp-delivered-by.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jeden BIM-Fachmodelltyp BKP-Honorarpositionen der liefernden Planungsdisziplin zu. closeMatch ist die Leitdisziplin (091 Architekt, 092 Bauingenieur, 094 HLKK-Ingenieur, 095 Sanitaeringenieur). Disziplin-Honorare wiederholen sich pro Phase (091/191/…). Landschaft und Labor ergänzen relatedMatch zu Spezialisten-Honorar (096 …). Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps each BIM discipline-model type to BKP Honorar lines for the planner who delivers the model. closeMatch is the primary discipline (091 Architekt, 092 Bauingenieur, 094 HLKK-Ingenieur, 095 Sanitaeringenieur). Discipline Honorare repeat per phase (091/191/…). Landscape and laboratory add relatedMatch to Spezialisten-Honorar (096 …). Full BKP vocabulary is external; only referenced IRIs are used.
- **title (de):** Mapping abstrakter Fachmodelle nach BKP geliefert durch
- **title (en):** Abstract model to BKP delivered-by mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mod:architecture` | `closeMatch` | `bkp:091` |
| `mod:architecture` | `closeMatch` | `bkp:191` |
| `mod:architecture` | `closeMatch` | `bkp:291` |
| `mod:architecture` | `closeMatch` | `bkp:391` |
| `mod:architecture` | `closeMatch` | `bkp:491` |
| `mod:architecture` | `closeMatch` | `bkp:591` |
| `mod:architecture` | `closeMatch` | `bkp:991` |
| `mod:concrete-structure` | `closeMatch` | `bkp:092` |
| `mod:concrete-structure` | `closeMatch` | `bkp:192` |
| `mod:concrete-structure` | `closeMatch` | `bkp:292` |
| `mod:concrete-structure` | `closeMatch` | `bkp:392` |
| `mod:concrete-structure` | `closeMatch` | `bkp:492` |
| `mod:concrete-structure` | `closeMatch` | `bkp:592` |
| `mod:cooling` | `closeMatch` | `bkp:094` |
| `mod:cooling` | `closeMatch` | `bkp:194` |
| `mod:cooling` | `closeMatch` | `bkp:294` |
| `mod:cooling` | `closeMatch` | `bkp:394` |
| `mod:cooling` | `closeMatch` | `bkp:494` |
| `mod:cooling` | `closeMatch` | `bkp:594` |
| `mod:earthworks` | `closeMatch` | `bkp:092` |
| `mod:earthworks` | `closeMatch` | `bkp:192` |
| `mod:earthworks` | `closeMatch` | `bkp:292` |
| `mod:earthworks` | `closeMatch` | `bkp:392` |
| `mod:earthworks` | `closeMatch` | `bkp:492` |
| `mod:earthworks` | `closeMatch` | `bkp:592` |
| `mod:excavation-pit` | `closeMatch` | `bkp:092` |
| `mod:excavation-pit` | `closeMatch` | `bkp:192` |
| `mod:excavation-pit` | `closeMatch` | `bkp:292` |
| `mod:excavation-pit` | `closeMatch` | `bkp:392` |
| `mod:excavation-pit` | `closeMatch` | `bkp:492` |
| `mod:excavation-pit` | `closeMatch` | `bkp:592` |
| `mod:facade` | `closeMatch` | `bkp:091` |
| `mod:facade` | `closeMatch` | `bkp:191` |
| `mod:facade` | `closeMatch` | `bkp:291` |
| `mod:facade` | `closeMatch` | `bkp:391` |
| `mod:facade` | `closeMatch` | `bkp:491` |
| `mod:facade` | `closeMatch` | `bkp:591` |
| `mod:facade` | `closeMatch` | `bkp:991` |
| `mod:furniture` | `closeMatch` | `bkp:091` |
| `mod:furniture` | `closeMatch` | `bkp:191` |
| `mod:furniture` | `closeMatch` | `bkp:291` |
| `mod:furniture` | `closeMatch` | `bkp:391` |
| `mod:furniture` | `closeMatch` | `bkp:491` |
| `mod:furniture` | `closeMatch` | `bkp:591` |
| `mod:furniture` | `closeMatch` | `bkp:991` |
| `mod:heating` | `closeMatch` | `bkp:094` |
| `mod:heating` | `closeMatch` | `bkp:194` |
| `mod:heating` | `closeMatch` | `bkp:294` |
| `mod:heating` | `closeMatch` | `bkp:394` |
| `mod:heating` | `closeMatch` | `bkp:494` |
| `mod:heating` | `closeMatch` | `bkp:594` |
| `mod:laboratory` | `closeMatch` | `bkp:091` |
| `mod:laboratory` | `closeMatch` | `bkp:191` |
| `mod:laboratory` | `closeMatch` | `bkp:291` |
| `mod:laboratory` | `closeMatch` | `bkp:391` |
| `mod:laboratory` | `closeMatch` | `bkp:491` |
| `mod:laboratory` | `closeMatch` | `bkp:591` |
| `mod:laboratory` | `closeMatch` | `bkp:991` |
| `mod:laboratory` | `relatedMatch` | `bkp:096` |
| `mod:laboratory` | `relatedMatch` | `bkp:196` |
| `mod:laboratory` | `relatedMatch` | `bkp:296` |
| `mod:laboratory` | `relatedMatch` | `bkp:396` |
| `mod:laboratory` | `relatedMatch` | `bkp:496` |
| `mod:laboratory` | `relatedMatch` | `bkp:596` |
| `mod:laboratory` | `relatedMatch` | `bkp:996` |
| `mod:landscape` | `closeMatch` | `bkp:091` |
| `mod:landscape` | `closeMatch` | `bkp:191` |
| `mod:landscape` | `closeMatch` | `bkp:291` |
| `mod:landscape` | `closeMatch` | `bkp:391` |
| `mod:landscape` | `closeMatch` | `bkp:491` |
| `mod:landscape` | `closeMatch` | `bkp:591` |
| `mod:landscape` | `closeMatch` | `bkp:991` |
| `mod:landscape` | `relatedMatch` | `bkp:096` |
| `mod:landscape` | `relatedMatch` | `bkp:196` |
| `mod:landscape` | `relatedMatch` | `bkp:296` |
| `mod:landscape` | `relatedMatch` | `bkp:396` |
| `mod:landscape` | `relatedMatch` | `bkp:496` |
| `mod:landscape` | `relatedMatch` | `bkp:596` |
| `mod:landscape` | `relatedMatch` | `bkp:996` |
| `mod:plumbing` | `closeMatch` | `bkp:095` |
| `mod:plumbing` | `closeMatch` | `bkp:195` |
| `mod:plumbing` | `closeMatch` | `bkp:295` |
| `mod:plumbing` | `closeMatch` | `bkp:395` |
| `mod:plumbing` | `closeMatch` | `bkp:495` |
| `mod:plumbing` | `closeMatch` | `bkp:595` |
| `mod:reinforcement` | `closeMatch` | `bkp:092` |
| `mod:reinforcement` | `closeMatch` | `bkp:192` |
| `mod:reinforcement` | `closeMatch` | `bkp:292` |
| `mod:reinforcement` | `closeMatch` | `bkp:392` |
| `mod:reinforcement` | `closeMatch` | `bkp:492` |
| `mod:reinforcement` | `closeMatch` | `bkp:592` |
| `mod:steel-structure` | `closeMatch` | `bkp:092` |
| `mod:steel-structure` | `closeMatch` | `bkp:192` |
| `mod:steel-structure` | `closeMatch` | `bkp:292` |
| `mod:steel-structure` | `closeMatch` | `bkp:392` |
| `mod:steel-structure` | `closeMatch` | `bkp:492` |
| `mod:steel-structure` | `closeMatch` | `bkp:592` |
| `mod:storey-volume` | `closeMatch` | `bkp:091` |
| `mod:storey-volume` | `closeMatch` | `bkp:191` |
| `mod:storey-volume` | `closeMatch` | `bkp:291` |
| `mod:storey-volume` | `closeMatch` | `bkp:391` |
| `mod:storey-volume` | `closeMatch` | `bkp:491` |
| `mod:storey-volume` | `closeMatch` | `bkp:591` |
| `mod:storey-volume` | `closeMatch` | `bkp:991` |
| `mod:surroundings` | `closeMatch` | `bkp:091` |
| `mod:surroundings` | `closeMatch` | `bkp:191` |
| `mod:surroundings` | `closeMatch` | `bkp:291` |
| `mod:surroundings` | `closeMatch` | `bkp:391` |
| `mod:surroundings` | `closeMatch` | `bkp:491` |
| `mod:surroundings` | `closeMatch` | `bkp:591` |
| `mod:surroundings` | `closeMatch` | `bkp:991` |
| `mod:timber-structure` | `closeMatch` | `bkp:092` |
| `mod:timber-structure` | `closeMatch` | `bkp:192` |
| `mod:timber-structure` | `closeMatch` | `bkp:292` |
| `mod:timber-structure` | `closeMatch` | `bkp:392` |
| `mod:timber-structure` | `closeMatch` | `bkp:492` |
| `mod:timber-structure` | `closeMatch` | `bkp:592` |
| `mod:underground-services` | `closeMatch` | `bkp:095` |
| `mod:underground-services` | `closeMatch` | `bkp:195` |
| `mod:underground-services` | `closeMatch` | `bkp:295` |
| `mod:underground-services` | `closeMatch` | `bkp:395` |
| `mod:underground-services` | `closeMatch` | `bkp:495` |
| `mod:underground-services` | `closeMatch` | `bkp:595` |
| `mod:ventilation` | `closeMatch` | `bkp:094` |
| `mod:ventilation` | `closeMatch` | `bkp:194` |
| `mod:ventilation` | `closeMatch` | `bkp:294` |
| `mod:ventilation` | `closeMatch` | `bkp:394` |
| `mod:ventilation` | `closeMatch` | `bkp:494` |
| `mod:ventilation` | `closeMatch` | `bkp:594` |
