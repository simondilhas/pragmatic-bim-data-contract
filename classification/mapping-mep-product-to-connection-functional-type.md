# MEP product to connection functional type mapping

Source: [`mep-product-to-connection-functional-type.mapping.ttl`](sources/mapping-mep-product-to-connection-functional-type.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet zuweisbare TGA-Erzeuger- und Endgeraeteprodukte ConnectionFunctionalType-Disziplinen zu. MTP-FIRE-* Querschnitts-Endgeraete verwenden relatedMatch zu anwendbaren Host-Disziplinen; die Disziplin wird bei Zuweisung vom Inline-Hostsystem aufgeloest.
- **description (en):** Maps assignable MEP unit and terminal product concepts to ConnectionFunctionalType disciplines. MTP-FIRE-* cross-cutting terminals use relatedMatch to applicable host disciplines; discipline is resolved from the inline host system at assignment time.
- **title (de):** Mapping TGA-Produkte zu funktionalen Verbindungstypen
- **title (en):** MEP product to connection functional type mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `relatedMatch` | `func:cooling` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `relatedMatch` | `func:heating` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `relatedMatch` | `func:ventilation` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `relatedMatch` | `func:cooling` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `relatedMatch` | `func:heating` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `relatedMatch` | `func:ventilation` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `relatedMatch` | `func:data` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `relatedMatch` | `func:electrical` |
