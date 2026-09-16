# Abstract model to BKP delivered-from mapping

Source: [`abstract-model-to-bkp-delivered-from.mapping.ttl`](sources/mapping-model-to-bkp-delivered-from.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jeden BIM-Fachmodelltyp BKP-Baukostengruppen zu, aus denen der Modellinhalt stammt. closeMatch ist das Leitgewerk; relatedMatch eine sekundäre Hauptgruppe. Codes folgen dem BKP-IRI-Satz dieses Repositories (211 Baumeisterarbeiten, 213 Stahlbau, 214 Holzbau, 216 Fundamente, 221/215.5/226/227 Fassade, 24 HLK, 25 Sanitaer, 27/28 Ausbau, 3 Betriebseinrichtungen, 4 Umgebung, 9 Ausstattung). Vollstaendiges BKP-Vokabular extern.
- **description (en):** Maps each BIM discipline-model type to BKP construction cost groups the model content is taken from. closeMatch is the primary works package; relatedMatch is a secondary chapter. Codes follow this repository's BKP IRI set (211 Baumeisterarbeiten, 213 Stahlbau, 214 Holzbau, 216 Fundamente, 221/215.5/226/227 Fassade, 24 HLK, 25 Sanitaer, 27/28 Ausbau, 3 Betriebseinrichtungen, 4 Umgebung, 9 Ausstattung). Full BKP vocabulary is external; only referenced IRIs are used.
- **title (de):** Mapping abstrakter Fachmodelle nach BKP geliefert aus
- **title (en):** Abstract model to BKP delivered-from mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mod:architecture` | `closeMatch` | `bkp:27` |
| `mod:architecture` | `closeMatch` | `bkp:28` |
| `mod:architecture` | `relatedMatch` | `bkp:21` |
| `mod:architecture` | `relatedMatch` | `bkp:22` |
| `mod:concrete-structure` | `closeMatch` | `bkp:211` |
| `mod:concrete-structure` | `closeMatch` | `bkp:216` |
| `mod:concrete-structure` | `relatedMatch` | `bkp:21` |
| `mod:cooling` | `closeMatch` | `bkp:24` |
| `mod:earthworks` | `closeMatch` | `bkp:1` |
| `mod:earthworks` | `relatedMatch` | `bkp:21` |
| `mod:excavation-pit` | `closeMatch` | `bkp:21` |
| `mod:facade` | `closeMatch` | `bkp:215-5` |
| `mod:facade` | `closeMatch` | `bkp:221` |
| `mod:facade` | `closeMatch` | `bkp:226` |
| `mod:facade` | `closeMatch` | `bkp:227` |
| `mod:facade` | `relatedMatch` | `bkp:22` |
| `mod:furniture` | `closeMatch` | `bkp:9` |
| `mod:furniture` | `relatedMatch` | `bkp:28` |
| `mod:heating` | `closeMatch` | `bkp:24` |
| `mod:laboratory` | `closeMatch` | `bkp:3` |
| `mod:landscape` | `closeMatch` | `bkp:4` |
| `mod:plumbing` | `closeMatch` | `bkp:25` |
| `mod:reinforcement` | `closeMatch` | `bkp:211` |
| `mod:reinforcement` | `relatedMatch` | `bkp:21` |
| `mod:steel-structure` | `closeMatch` | `bkp:213` |
| `mod:steel-structure` | `relatedMatch` | `bkp:21` |
| `mod:storey-volume` | `relatedMatch` | `bkp:2` |
| `mod:surroundings` | `relatedMatch` | `bkp:4` |
| `mod:timber-structure` | `closeMatch` | `bkp:214` |
| `mod:timber-structure` | `relatedMatch` | `bkp:21` |
| `mod:underground-services` | `closeMatch` | `bkp:25` |
| `mod:underground-services` | `relatedMatch` | `bkp:4` |
| `mod:ventilation` | `closeMatch` | `bkp:24` |
