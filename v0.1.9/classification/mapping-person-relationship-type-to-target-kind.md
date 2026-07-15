# Person relationship type to target kind mapping

Source: [`person-relationship-type-to-target-kind.mapping.ttl`](sources/mapping-person-relationship-type-to-target-kind.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet Personenbeziehungs-Prädikate dem zu befüllenden PersonRelationship-Ziel-Slot zu. Pro Datensatz genau ein Ziel-Slot.
- **description (en):** Maps person relationship predicate concepts to the PersonRelationship target slot that must be populated. Exactly one target slot per record.
- **title (de):** Mapping Personenbeziehungstyp zu Ziel-Slot
- **title (en):** Person relationship type to target kind mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rel:aunt-or-uncle-of` | `relatedMatch` | `tgt:related_person` |
| `rel:child-in-law-of` | `relatedMatch` | `tgt:related_person` |
| `rel:child-of` | `relatedMatch` | `tgt:related_person` |
| `rel:client-of` | `relatedMatch` | `tgt:related_company` |
| `rel:consulted-for` | `relatedMatch` | `tgt:related_company` |
| `rel:cousin-of` | `relatedMatch` | `tgt:related_person` |
| `rel:friend-of` | `relatedMatch` | `tgt:related_person` |
| `rel:grandchild-of` | `relatedMatch` | `tgt:related_person` |
| `rel:grandparent-of` | `relatedMatch` | `tgt:related_person` |
| `rel:has-expertise-in` | `relatedMatch` | `tgt:related_topic` |
| `rel:has-interest` | `relatedMatch` | `tgt:related_topic` |
| `rel:has-key-account-manager` | `relatedMatch` | `tgt:related_person` |
| `rel:introduced-by` | `relatedMatch` | `tgt:related_person` |
| `rel:is-key-account-manager-for` | `relatedMatch` | `tgt:related_company` |
| `rel:knows` | `relatedMatch` | `tgt:related_person` |
| `rel:learning-about` | `relatedMatch` | `tgt:related_topic` |
| `rel:mentored-by` | `relatedMatch` | `tgt:related_person` |
| `rel:niece-or-nephew-of` | `relatedMatch` | `tgt:related_person` |
| `rel:parent-in-law-of` | `relatedMatch` | `tgt:related_person` |
| `rel:parent-of` | `relatedMatch` | `tgt:related_person` |
| `rel:referred-by` | `relatedMatch` | `tgt:related_person` |
| `rel:reports-to` | `relatedMatch` | `tgt:related_person` |
| `rel:sibling-of` | `relatedMatch` | `tgt:related_person` |
| `rel:spouse-of` | `relatedMatch` | `tgt:related_person` |
| `rel:studied-at` | `relatedMatch` | `tgt:related_company` |
| `rel:teaches-at` | `relatedMatch` | `tgt:related_company` |
| `rel:vendor-of` | `relatedMatch` | `tgt:related_company` |
| `rel:was-colleague-of` | `relatedMatch` | `tgt:related_person` |
| `rel:worked-at` | `relatedMatch` | `tgt:related_company` |
| `rel:works-at` | `relatedMatch` | `tgt:related_company` |
