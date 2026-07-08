# Pragmatic BIM Classifications

SKOS vocabularies and mapping bridges for the data contract `Classification` slot.

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — sourced from [pragmatic-bim-public-rules](https://github.com/simondilhas/pragmatic-bim-public-rules).

## Vocabularies

| Vocabulary | Description |
| --- | --- |
| [Building space activity classification](room-activity.md) | `abstract-room-classification/building_space-activity-classification-en.skos.ttl` |
| [Building space name classification](room-name.md) | `abstract-room-name-classification/building-space-name-classification.skos.ttl` |
| [Separator wall role classification](separator-wall-role.md) | `abstract-separator-classification/separator-wall-role-classification-en.skos.ttl` |
| [Separator slab role classification](separator-slab-role.md) | `abstract-separator-classification/separator-slab-role-classification-en.skos.ttl` |
| [Connection functional type classification](connection-functional-type.md) | `abstract-connector-classification/connection-functional-type-en.skos.ttl` |
| [Abstract workflow participant roles](roles.md) | `abstract-roles/roles.skos.ttl` |
| [Document function classification](document-function.md) | `abstract-document-function/document-function.skos.ttl` |
| [Abstract use case classification](usecase.md) | `abstract-usecase-classification/usecase-classification.skos.ttl` |
| [Abstract material classification](material.md) | `abstract-material-classification/material-classification.skos.ttl` |
| [Abstract building metrics](building-metric.md) | `abstract-metric-definition/building-metrics.skos.ttl` |
| [Abstract building ratios](building-ratio.md) | `abstract-ratio-definition/building-ratios.skos.ttl` |
| [Abstract floor covering products](floor-covering-product.md) | `abstract-covering-product-classification/floor-covering-products.skos.ttl` |
| [Abstract wall covering products](wall-covering-product.md) | `abstract-covering-product-classification/wall-covering-products.skos.ttl` |
| [Abstract ceiling covering products](ceiling-covering-product.md) | `abstract-covering-product-classification/ceiling-covering-products.skos.ttl` |
| [Abstract facade covering products](facade-covering-product.md) | `abstract-covering-product-classification/facade-covering-products.skos.ttl` |
| [Abstract roof covering products](roof-covering-product.md) | `abstract-covering-product-classification/roof-covering-products.skos.ttl` |
| [Abstract foundation products](foundation-product.md) | `abstract-foundation-product-classification/foundation-products.skos.ttl` |
| [Abstract wall separator products](wall-separator-product.md) | `abstract-separator-product-classification/wall-separator-products.skos.ttl` |
| [KBOB ecobilans construction materials](kbob-ecobilans-baumat.md) | `mapping/kbob-ecobilans-baumat.skos.ttl` |
| [Abstract slab separator products](slab-separator-product.md) | `abstract-separator-product-classification/slab-separator-products.skos.ttl` |
| [Abstract door connector products](door-connector-product.md) | `abstract-connector-product-classification/door-connector-products.skos.ttl` |
| [Abstract window connector products](window-connector-product.md) | `abstract-connector-product-classification/window-connector-products.skos.ttl` |
| [Abstract MEP unit products](mep-unit-product.md) | `abstract-mep-product-classification/mep-unit-products.skos.ttl` |
| [Abstract MEP terminal products](mep-terminal-product.md) | `abstract-mep-product-classification/mep-terminal-products.skos.ttl` |
| [Abstract person relationship types](person-relationship-type.md) | `abstract-person-relationship-classification/person-relationship-type.skos.ttl` |
| [Abstract topic classification](topic.md) | `abstract-topic-classification/topic-classification.skos.ttl` |

## Mappings

| Mapping | Description |
| --- | --- |
| [Person relationship type to target kind mapping](mapping-person-relationship-type-to-target-kind.md) | `mapping/person-relationship-type-to-target-kind.mapping.ttl` |
| [Connection functional type to physical type mapping](mapping-connection-functional-to-physical-type.md) | `mapping/connection-functional-to-physical-type.mapping.ttl` |
| [MEP product to connection functional type mapping](mapping-mep-product-to-connection-functional-type.md) | `mapping/mep-product-to-connection-functional-type.mapping.ttl` |
| [MEP product to IFC class mapping](mapping-mep-product-to-ifc-class.md) | `mapping/mep-product-to-ifc-class.mapping.ttl` |
| [Separator role to space activity mapping](mapping-separator-role-to-space-activity.md) | `mapping/separator-role-to-space-activity.mapping.ttl` |
| [Room activity to D0165 mapping](mapping-room-activity-to-d0165.md) | `mapping/abstract-room-classification-to-d0165.mapping.ttl` |
| [D0165 to room activity mapping](mapping-d0165-to-room-activity.md) | `mapping/d0165-to-abstract-room-classification.mapping.ttl` |
| [Room activity to SIA 416 mapping](mapping-room-activity-to-sia416.md) | `mapping/abstract-room-classification-to-sia416.mapping.ttl` |
| [Room name to space activity mapping](mapping-room-name-to-activity.md) | `mapping/abstract-room-name-to-space-activity.mapping.ttl` |
| [Room name notation v1 to v2 mapping](mapping-room-name-notation-v1-to-v2.md) | `mapping/room-name-notation-v1-to-v2.mapping.ttl` |
| [armasuisse room name to abstract room name mapping](mapping-armasuisse-room-name-to-room-name.md) | `mapping/armasuisse-room-name-to-abstract-room-name.mapping.ttl` |
| [Abstract roles to BKP mapping](mapping-roles-to-bkp.md) | `mapping/abstract-roles-to-bkp.mapping.ttl` |
| [Abstract material to Uniclass Ma mapping](mapping-material-to-uniclass-ma.md) | `mapping/abstract-material-to-uniclass-ma.mapping.ttl` |
| [KBOB document types to document function mapping](mapping-kbob-document-types-to-document-function.md) | `mapping/kbob-document-types-to-document-function.mapping.ttl` |
| [Abstract building metrics to SIA 416 mapping](mapping-metric-to-sia416.md) | `mapping/abstract-metric-to-sia416.mapping.ttl` |
| [Abstract building metrics to DIN 277 mapping](mapping-metric-to-din277.md) | `mapping/abstract-metric-to-din277.mapping.ttl` |
| [Abstract building metrics to ISO 9836 mapping](mapping-metric-to-iso9836.md) | `mapping/abstract-metric-to-iso9836.mapping.ttl` |
| [Abstract building metrics to RICS IPMS mapping](mapping-metric-to-rics-ipms.md) | `mapping/abstract-metric-to-rics-ipms.mapping.ttl` |
| [Abstract building ratios to SIA 416 mapping](mapping-ratio-to-sia416.md) | `mapping/abstract-ratio-to-sia416.mapping.ttl` |
| [qto_buccaneer to abstract building metrics mapping](mapping-qto-buccaneer-to-metric.md) | `mapping/qto-buccaneer-to-abstract-metric.mapping.ttl` |
| [qto_buccaneer to abstract building ratios mapping](mapping-qto-buccaneer-to-ratio.md) | `mapping/qto-buccaneer-to-abstract-ratio.mapping.ttl` |
| [Abstract covering products to material mapping](mapping-covering-products-to-material.md) | `mapping/abstract-covering-products-to-material.mapping.ttl` |
| [Abstract covering products to BKP mapping](mapping-covering-products-to-bkp.md) | `mapping/abstract-covering-products-to-bkp.mapping.ttl` |
| [Abstract foundation products to BKP mapping](mapping-foundation-products-to-bkp.md) | `mapping/abstract-foundation-products-to-bkp.mapping.ttl` |
| [Abstract roof covering products to BKP mapping](mapping-roof-covering-products-to-bkp.md) | `mapping/abstract-roof-covering-products-to-bkp.mapping.ttl` |
| [Abstract separator products to material mapping](mapping-separator-products-to-material.md) | `mapping/abstract-separator-products-to-material.mapping.ttl` |
| [Abstract separator products to BKP mapping](mapping-separator-products-to-bkp.md) | `mapping/abstract-separator-products-to-bkp.mapping.ttl` |
| [Abstract connector products to material mapping](mapping-connector-products-to-material.md) | `mapping/abstract-connector-products-to-material.mapping.ttl` |
| [Abstract connector products to BKP mapping](mapping-connector-products-to-bkp.md) | `mapping/abstract-connector-products-to-bkp.mapping.ttl` |
| [Abstract slab separator products to KBOB ecobilans mapping](mapping-slab-separator-products-to-kbob-ecobilans.md) | `mapping/abstract-slab-separator-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract window connector products to KBOB ecobilans mapping](mapping-window-connector-products-to-kbob-ecobilans.md) | `mapping/abstract-window-connector-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract facade covering products to KBOB ecobilans mapping](mapping-facade-covering-products-to-kbob-ecobilans.md) | `mapping/abstract-facade-covering-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract roof covering products to KBOB ecobilans mapping](mapping-roof-covering-products-to-kbob-ecobilans.md) | `mapping/abstract-roof-covering-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract floor covering products to KBOB ecobilans mapping](mapping-floor-covering-products-to-kbob-ecobilans.md) | `mapping/abstract-floor-covering-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract wall covering products to KBOB ecobilans mapping](mapping-wall-covering-products-to-kbob-ecobilans.md) | `mapping/abstract-wall-covering-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract ceiling covering products to KBOB ecobilans mapping](mapping-ceiling-covering-products-to-kbob-ecobilans.md) | `mapping/abstract-ceiling-covering-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract wall separator products to KBOB ecobilans mapping](mapping-wall-separator-products-to-kbob-ecobilans.md) | `mapping/abstract-wall-separator-products-to-kbob-ecobilans.mapping.ttl` |
| [Abstract door connector products to KBOB ecobilans mapping](mapping-door-connector-products-to-kbob-ecobilans.md) | `mapping/abstract-door-connector-products-to-kbob-ecobilans.mapping.ttl` |
