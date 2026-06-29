# Pragmatic BIM Data Contract

To provide a simple, implementation-ready BIM data model for integration, querying, costing, and analysis workflows, this schema defines a pragmatic, graph-first LinkML structure that is IFC-aware and extensible across classification schemes.


URI: https://schema.pragmaticbim.ch

Name: pragmatic_bim_data_contract

## Artifacts

| Format | File |
| --- | --- |
| JSON Schema | [pragmatic-bim.schema.json](pragmatic-bim.schema.json) |
| SHACL | [pragmatic-bim.shacl.ttl](pragmatic-bim.shacl.ttl) |
| CSV | [pragmatic-bim.csv](pragmatic-bim.csv) |
| Pydantic | [pragmatic-bim.pydantic.py](pragmatic-bim.pydantic.py) |
| Docs (Markdown) | [pragmatic-bim.docs.md](pragmatic-bim.docs.md) |


## Graph classes

| Class | Description |
| --- | --- |
| [Entity](Entity.md) | Common base class for everything in the project graph. Has identity, lifecycle, and status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Agent](Agent.md) | Abstract base class for human and software actors in workflow and communication roles. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. Instances may contain personal data; privacy slots govern lawful processing, consent, retention, and redaction. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Company](Company.md) | Organization, company, or legal entity participating in the project or asset lifecycle. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SoftwareAgent](SoftwareAgent.md) | Automated actor (integration, bot, or pipeline) acting in workflow roles. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Decision](Decision.md) | Decision entity for workflow traceability and governance. Entity.status covers lifecycle; decision_status uses workflow vocabulary URIs. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Task](Task.md) | Task entity for implementation and follow-up workflows. Entity.status covers lifecycle; task_status uses action status vocabulary URIs. Links to related entities via applies_to_entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Process](Process.md) | Running BPMN process instance in the project graph. Use process_definition_uri for the BPMN definition key or artifact. When orchestration state lives in an external engine, set external_instance_uri to that system of record. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Message](Message.md) | Message entity for coordination and traceability. Links to related entities via applies_to_entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Artifact](Artifact.md) | External project artifact (text document, model, or plan) at storage_link. Used for provenance (Requirement.source_artifact). Not a modeled building element. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Contract](Contract.md) | Commercial agreement entity for project scope, parties, and governance. Links to a signed artifact and related model entities via applies_to_entities. Entity.status covers record lifecycle; contract_status uses workflow vocabulary URIs. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Project](Project.md) | Business delivery scope for spatial context, systems, and workflow entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Program](Program.md) | Portfolio or capital program scope grouping related projects. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Product](Product.md) | Commercial product or service offering sold by a company. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Deliverable](Deliverable.md) | Outcome or handover item produced within a project. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level context. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Separator](Separator.md) | Abstract base class for elements that separate spaces or zones. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SeparatorWall](SeparatorWall.md) | Wall-based separating element. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirtualEntity](VirtualEntity.md) | Abstract base class for non-physical, conceptual, or informational entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpatialContext](SpatialContext.md) | Context node used to represent perimeter, legal site, built asset, level, or zone. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structures. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[System](System.md) | Building service system grouping that serves spaces or zones. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CostRecord](CostRecord.md) | Cost record for estimation, catalog pricing, and calculation. Use cost_record_role to distinguish catalog cost/price (on Product) from project estimate/actual lines. Populate component_cost_items to act as an assembly (aggregated unit price). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Material](Material.md) | Material definition that can be associated with one or more entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Requirement](Requirement.md) | Prescriptive requirement entity (content_kind requirement). Applies to model entities via applies_to_entities. Domain is discriminated by concrete subclass (PerformanceRequirement, SpatialRequirement, DeliverableRequirement, etc.), not a separate slot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DeliverableRequirement](DeliverableRequirement.md) | Deliverable or documentation requirement (model LOD, O&M manual, export format, etc.). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ScheduleRequirement](ScheduleRequirement.md) | Schedule obligation requirement (deadline, milestone, or start/finish window). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CostRequirement](CostRequirement.md) | Cost or budget requirement (unit-cost cap, total budget limit, etc.). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialRequirement](MaterialRequirement.md) | Material or product specification requirement for matching against assigned materials. |
| [Change](Change.md) | Audit record observing the project graph moving between revisions. Not an Entity and not a graph node — it watches the graph. Use change_type together with the concrete subclass for interpretation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeometryChange](GeometryChange.md) | Geometry or representation change for a subject. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RequirementChange](RequirementChange.md) | Change to a requirement entity or its fields. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AdditionChange](AdditionChange.md) | New entity introduced in to_revision. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DeletionChange](DeletionChange.md) | Entity removed in to_revision. |

## Embedded value types

> Structured records stored inline on parent graph nodes (`inlined: true`). Not standalone project entities — no independent `id` or lifecycle.

| Class | Description |
| --- | --- |
| [Classification](Classification.md) | Generic classification entry from any scheme (for example IFC, Uniclass, OmniClass, custom). |
| [GeometryRepresentation](GeometryRepresentation.md) | Minimal geometry reference for an entity, separating representation from encoding format. |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis. |
| [MetadataEntry](MetadataEntry.md) | Generic metadata entry for storing IFC attributes, PropertySet fields, or project-specific key-value data. |
| [PerformanceProperty](PerformanceProperty.md) | Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FireProperty](FireProperty.md) | Normalized fire-related property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AcousticProperty](AcousticProperty.md) | Normalized acoustic-related property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ThermalProperty](ThermalProperty.md) | Normalized thermal-related property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StructuralProperty](StructuralProperty.md) | Normalized structural-related property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SecurityProperty](SecurityProperty.md) | Normalized security-related property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialProperty](MaterialProperty.md) | Normalized material-related property. |
| [PostalAddress](PostalAddress.md) | Structured postal or physical address for an agent. |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent. |
| [ConsentRecord](ConsentRecord.md) | Record of lawful basis, scope, and lifecycle for processing personal data on a Person. |
| [LocalizedText](LocalizedText.md) | Localized text value for a specific language tag. |
| [TimeLink](TimeLink.md) | Inline typed precedence link from a TimeRecord to one successor. Not a VirtualEntity — no id, no mixin. Owned by the predecessor record. |




## Slots

| Slot | Description |
| --- | --- |
| [acceptance_criteria](acceptance_criteria.md) | Criteria that define when the deliverable is accepted. |
| [actual_finish_at](actual_finish_at.md) | Actual finish timestamp for the time record where known. |
| [actual_start_at](actual_start_at.md) | Actual start timestamp for the time record where known. |
| [address_country](address_country.md) | Country name. |
| [address_country_code](address_country_code.md) | Optional ISO 3166-1 alpha-2 or alpha-3 country code. |
| [address_locality](address_locality.md) | Locality, city, or town. |
| [address_region](address_region.md) | Region, state, canton, or province. |
| [adjacency_kind](adjacency_kind.md) | Adjacency semantics when this spatial requirement involves another subject. |
| [affected_geometry_role](affected_geometry_role.md) | Geometry role affected for GeometryChange records. |
| [affected_requirement](affected_requirement.md) | Requirement entity affected by this change. |
| [affected_subject](affected_subject.md) | Optional typed reference to the changed graph entity when the subject is in the project graph. |
| [affected_subject_id](affected_subject_id.md) | Identifier of the changed subject (entity id, document id, or external key). |
| [affected_subject_path](affected_subject_path.md) | Optional JSON-pointer-style path for nested targets (for example localized_descriptions[de], section.4.2.paragraph_1). |
| [affected_subject_type](affected_subject_type.md) | LinkML class name of the changed subject (for example Space, SeparatorWall, Artifact). |
| [applies_to_entities](applies_to_entities.md) | Model entities this record applies to (requirements, cost items, schedule items, etc.). |
| [artifact_kind](artifact_kind.md) | Kind of external artifact (text document, model, or plan). |
| [artifact_storage_link](artifact_storage_link.md) | Artifact location when the subject is an Artifact entity or embedded field diff. |
| [assignee](assignee.md) | Responsible agent. |
| [availability_notes](availability_notes.md) | Optional notes about availability, office hours, or response expectations. |
| [belongs_to_company](belongs_to_company.md) | Optional company that the person belongs to. |
| [boundary_type](boundary_type.md) | Classification of boundary element (e.g., covering). |
| [bounded_by](bounded_by.md) | Physical elements that bound a space. |
| [bounded_space](bounded_space.md) | Space bounded by this boundary element. |
| [catalog_cost_records](catalog_cost_records.md) | Catalog cost and price records for this product (cost_record_role cost or price). |
| [change_severity](change_severity.md) | Optional severity independent of change type. |
| [change_source](change_source.md) | URI identifying the tool or pipeline that produced this change record. |
| [change_type](change_type.md) | Category of change detected between two revisions. |
| [classification_code](classification_code.md) | Classification code inside the scheme. |
| [classification_label](classification_label.md) | Optional human-readable classification label. |
| [classification_scheme](classification_scheme.md) | Name of the classification scheme (for example ifc, uniclass, omniclass, custom). |
| [classification_source](classification_source.md) | Source authority or dataset for this classification. |
| [classification_uri](classification_uri.md) | Optional URI/CURIE that identifies the classification concept in an external registry. |
| [classification_version](classification_version.md) | Optional scheme/version identifier. |
| [classifications](classifications.md) | Classification entries from IFC and other schemes. |
| [clause_ref](clause_ref.md) | Clause, article, or section reference within the norm. |
| [client](client.md) | Owning client organization. |
| [completed_at](completed_at.md) | Timestamp when the process instance completed or terminated, when applicable. |
| [component_cost_items](component_cost_items.md) | Cost records aggregated into this assembly record. |
| [component_time_items](component_time_items.md) | Time records contained in this plan; set milestone_at on a record to mark it as a checkpoint. |
| [connection_physical_requirement_drivers](connection_physical_requirement_drivers.md) | Performance requirement drivers for this physical connection element. Multiple values are allowed because one connection may need to satisfy several requirements. |
| [connection_physical_type](connection_physical_type.md) | Classification of physical connector type (for example door, window, duct, pipe, cable). |
| [connection_virtual_requirement_drivers](connection_virtual_requirement_drivers.md) | Main requirement drivers for this virtual connection. |
| [connection_virtual_type](connection_virtual_type.md) | Classification of virtual connection semantics (for example structural_joint, adjacency, access). |
| [connects_physical_elements](connects_physical_elements.md) | Physical elements connected by this virtual connection (for example wall-wall, wall-slab). |
| [connects_spaces](connects_spaces.md) | Spaces connected by this virtual connection. |
| [consent_notes](consent_notes.md) | Optional notes about how or where consent was captured. |
| [consent_records](consent_records.md) | Audit trail of lawful basis and consent for processing personal data. When lawful_basis is consent and state is active, at least one non-withdrawn record should be present. |
| [contact_channel_type](contact_channel_type.md) | Communication channel type such as email, phone, website, linkedin, whatsapp, signal, slack, teams, or telegram. |
| [contact_points](contact_points.md) | Structured communication channels and profiles associated with this agent. |
| [contact_uri](contact_uri.md) | URI for the contact endpoint or profile where applicable. |
| [contact_value](contact_value.md) | Human-readable contact value such as an email address, phone number, handle, or username. |
| [contained_entities](contained_entities.md) | Generic containment for associated entities. |
| [content_kind](content_kind.md) | Entity type discriminator for adapter projection and querying. Must be a ContentKind value. |
| [context_type](context_type.md) | Classification of context entity (perimeter, legal_site, building, civil_structure, level, zone). |
| [contract_parties](contract_parties.md) | Agents party to the contract (for example client, contractor, consultant). |
| [contract_reference](contract_reference.md) | Human-readable contract number or external reference. |
| [contract_status](contract_status.md) | Contract status expressed as a URI/CURIE (for example draft, signed, active, terminated, superseded). |
| [contract_type](contract_type.md) | Contract type expressed as a URI/CURIE from a controlled vocabulary (for example design, construction, supply). |
| [cost_category](cost_category.md) | Cost category label kept intentionally open pending classification-backed modeling. |
| [cost_quantity_type](cost_quantity_type.md) | Quantity type used as basis for this cost calculation. |
| [cost_quantity_unit](cost_quantity_unit.md) | Unit of the cost quantity value. |
| [cost_quantity_value](cost_quantity_value.md) | Quantity magnitude used as basis for this cost calculation. |
| [cost_record_role](cost_record_role.md) | Role of this cost record (catalog cost, catalog price, project estimate, or actual). |
| [cost_records](cost_records.md) | Cost records associated with this entity. |
| [created_at](created_at.md) | Creation timestamp for this entity record. |
| [currency](currency.md) | ISO 4217 currency code (for example EUR, USD). |
| [data_categories](data_categories.md) | Personal data categories covered by this consent or processing record. |
| [data_controller](data_controller.md) | Organization accountable as data controller for this person record. |
| [decided_at](decided_at.md) | Timestamp when the decision was made. |
| [decided_by](decided_by.md) | Agent responsible for the decision. |
| [decision_status](decision_status.md) | Decision status expressed as a URI/CURIE (for example proposed, accepted, rejected, superseded). |
| [decision_type](decision_type.md) | Decision type expressed as a URI/CURIE from a controlled vocabulary. |
| [deliverable_code](deliverable_code.md) | External or internal deliverable identifier within a project. |
| [deliverable_format](deliverable_format.md) | Required deliverable format or encoding (for example IFC4, PDF, COBie). |
| [deliverable_kind](deliverable_kind.md) | Deliverable type label (for example coordination model, O&M manual, as-built record). |
| [dependency_type](dependency_type.md) | FS | SS | FF | SF |
| [description](description.md) | Default description text. |
| [detected_at](detected_at.md) | Timestamp when this change was detected. |
| [due_at](due_at.md) | Due timestamp for task completion. |
| [earliest_start_at](earliest_start_at.md) | Earliest permitted start when a schedule requirement defines a start window. |
| [effective_from](effective_from.md) | Start of contractual validity. |
| [effective_until](effective_until.md) | End of contractual validity when applicable. |
| [equipment_type](equipment_type.md) | Classification of equipment (for example HVAC, electrical, plumbing). |
| [external_instance_uri](external_instance_uri.md) | URI of the corresponding process instance in an external workflow engine when applicable. |
| [frame_material](frame_material.md) | Material of the frame or casing surrounding the opening. Applies to opening-type connectors (door, window). |
| [from_revision](from_revision.md) | Source revision number for this change. |
| [from_value](from_value.md) | Prior value serialized as text. Absent or null for new subjects or fields. |
| [geometry_format](geometry_format.md) | Optional serialization/encoding format (for example ifc, gltf, wkt, geojson), independent of representation kind. |
| [geometry_reference](geometry_reference.md) | URI/path/hash/pointer to geometry payload. |
| [geometry_representation](geometry_representation.md) | Representation kind/dimension (for example body_3d, footprint_2d, point), independent of file format. |
| [geometry_representations](geometry_representations.md) | Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself. |
| [granted_at](granted_at.md) | Timestamp when consent was given. Required when lawful_basis is consent. |
| [group_members](group_members.md) | Zone members; may include spaces, separations, systems, etc. |
| [id](id.md) | Unique local identifier. |
| [ifc_attribute_name](ifc_attribute_name.md) | IFC attribute name when property_path_kind is ifc_attribute (for example Name, GlobalId). |
| [ifc_global_id](ifc_global_id.md) | IFC GlobalId of the mapped entity. |
| [infill_material](infill_material.md) | Material of the opening infill within the frame (for example glazing for windows, door leaf or panel for doors). Applies to opening-type connectors (door, window). |
| [intent_verdict](intent_verdict.md) | Intent stability verdict from an automated judge (for example iterthink STABLE/NEW). |
| [is_preferred](is_preferred.md) | Indicates whether this is the preferred contact point. |
| [jurisdiction](jurisdiction.md) | Jurisdiction or authority scope for the regulatory requirement. |
| [lag_days](lag_days.md) |  |
| [language_tag](language_tag.md) | IETF BCP 47 language tag (for example en, de, pt-BR). |
| [lawful_basis](lawful_basis.md) | Lawful basis for processing the scoped personal data categories. |
| [localized_descriptions](localized_descriptions.md) | Localized variants of description. |
| [localized_names](localized_names.md) | Localized variants of name. |
| [mapping_version](mapping_version.md) | Mapping specification version used to derive the normalized property. |
| [match_status](match_status.md) | Whether the subject met the requirement at the target revision. |
| [material_category](material_category.md) | Material category label kept intentionally open pending classification-backed modeling. |
| [material_specification](material_specification.md) | Material grade, specification, or product description. |
| [materials](materials.md) | Material definitions associated with this entity. |
| [meaning_uri](meaning_uri.md) | Optional semantic URI for linking the entity instance to an external ontology concept. |
| [media_format](media_format.md) | Encoding or format label (for example IFC4, PDF, DWG). |
| [message_body](message_body.md) | Human-readable message content. |
| [message_subject](message_subject.md) | Optional subject or headline for the message. |
| [message_type](message_type.md) | Message type expressed as a URI/CURIE from a controlled vocabulary. |
| [metadata](metadata.md) | Generic metadata container for IFC attributes/properties and project-specific extensions. |
| [metadata_key](metadata_key.md) | Metadata key, for example IfcWall.FireRating or Pset_WallCommon.Reference. |
| [metadata_value](metadata_value.md) | Metadata value serialized as text. |
| [milestone_at](milestone_at.md) | Target timestamp for a zero-duration milestone checkpoint. |
| [min_area](min_area.md) | Minimum required area in square metres. |
| [min_clear_distance](min_clear_distance.md) | Minimum clear distance in metres when adjacency_kind is min_clear_distance. |
| [min_height](min_height.md) | Minimum required height or clear height in metres. |
| [modified_at](modified_at.md) | Last modification timestamp for this entity record. |
| [name](name.md) | Default display name. |
| [norm_uri](norm_uri.md) | URI identifying the norm, standard, or building code. |
| [operated_by](operated_by.md) | Organization accountable for this software agent. |
| [parent_building](parent_building.md) | Parent building context reference. |
| [parent_legal_site](parent_legal_site.md) | Parent legal site context reference. |
| [parent_level](parent_level.md) | Parent level/storey context reference. |
| [parent_perimeter](parent_perimeter.md) | Parent perimeter context reference. |
| [parent_process](parent_process.md) | Optional BPMN process instance that owns or spawned this task. |
| [parent_program](parent_program.md) | Parent program reference. |
| [parent_project](parent_project.md) | Parent project reference. |
| [parent_space](parent_space.md) | Parent space where the equipment is located. |
| [parent_system](parent_system.md) | Parent systems that the equipment belongs to. |
| [parent_zone](parent_zone.md) | Parent zone context reference. |
| [performance_properties](performance_properties.md) | Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values. |
| [personal_data_processing_state](personal_data_processing_state.md) | Privacy handling state for personal data on this person, orthogonal to workflow QA status. |
| [planned_finish_at](planned_finish_at.md) | Planned finish timestamp for the time record. |
| [planned_start_at](planned_start_at.md) | Planned start timestamp for the time record. |
| [post_office_box_number](post_office_box_number.md) | Post office box number where applicable. |
| [postal_addresses](postal_addresses.md) | Structured postal or physical addresses associated with this agent. |
| [postal_code](postal_code.md) | Postal or ZIP code. |
| [priced_for_customer](priced_for_customer.md) | Optional customer for a customer-specific catalog price when cost_record_role is price. |
| [privacy_policy_uri](privacy_policy_uri.md) | URI of the current or default privacy policy or notice applicable to this person record. |
| [process_definition_uri](process_definition_uri.md) | URI identifying the BPMN process definition (for example engine definition key or BPMN artifact URI). |
| [process_participants](process_participants.md) | Agents participating in this BPMN process instance (for example assignees mapped from lane roles). |
| [process_status](process_status.md) | Process instance status expressed as a URI/CURIE (for example active, suspended, completed, terminated). |
| [processing_purpose](processing_purpose.md) | Human-readable purpose for which the personal data categories are processed. |
| [processing_purposes](processing_purposes.md) | High-level purposes for processing personal data (for example project coordination, contract administration). |
| [product_code](product_code.md) | External or internal product catalog identifier. |
| [program_code](program_code.md) | External or internal program identifier. |
| [programme_ref](programme_ref.md) | URI or identifier for a programme or brief document. |
| [project_code](project_code.md) | External or internal project identifier. |
| [property_key](property_key.md) | Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum. |
| [property_path](property_path.md) | Canonical path to the changed field. Examples: Pset_WallCommon.FireRating, IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389. |
| [property_path_kind](property_path_kind.md) | Classification of the property path for downstream diff interpretation. |
| [property_unit](property_unit.md) | Normalized unit where applicable (for example min, dB, W/m2K). |
| [property_unit_uri](property_unit_uri.md) | Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT. |
| [property_value_boolean](property_value_boolean.md) | Boolean value when property_value_type is boolean. |
| [property_value_number](property_value_number.md) | Numeric value when property_value_type is number. |
| [property_value_string](property_value_string.md) | String value when property_value_type is string. |
| [property_value_type](property_value_type.md) | Value type discriminator for normalized storage (for example string, number, boolean). |
| [quantity_type](quantity_type.md) | Controlled quantity type. |
| [quantity_unit](quantity_unit.md) | Unit of the quantity value. |
| [quantity_unit_uri](quantity_unit_uri.md) | Optional URI that identifies the quantity unit in an external vocabulary such as QUDT. |
| [quantity_value](quantity_value.md) | Numeric quantity value. |
| [quantity_values](quantity_values.md) | Quantities associated with the entity. |
| [rationale](rationale.md) | Human-readable rationale that explains why the decision was made. |
| [recipients](recipients.md) | Agents that received the message. |
| [redacted_at](redacted_at.md) | Timestamp when identifying personal data was redacted on this record. |
| [redaction_reason](redaction_reason.md) | Reason for redaction (for example external model export, erasure request, retention expired). |
| [related_decision](related_decision.md) | Optional reference to a decision that informs or drives this task. |
| [related_entity](related_entity.md) | Entity or space subject for adjacency or distance constraints. |
| [related_material](related_material.md) | Optional Material entity template this requirement must match or satisfy. |
| [related_product](related_product.md) | Optional catalog product this deliverable implements or this cost record is priced from. |
| [related_requirement](related_requirement.md) | Requirement entity for match_change records. |
| [related_time_record](related_time_record.md) | Optional TimeRecord plan item this schedule requirement aligns with or must satisfy. |
| [requirement_property_key](requirement_property_key.md) | Canonical performance key for the target (for example u_value, resistance_rating). Aligns with performance property keys where applicable. |
| [retain_until](retain_until.md) | Storage-limit deadline after which personal data should be deleted or redacted. |
| [revision](revision.md) | Integer revision counter for change tracking. |
| [sender](sender.md) | Agent that sent the message. |
| [sent_at](sent_at.md) | Timestamp when the message was sent. |
| [separates_levels](separates_levels.md) | Level context nodes separated by this slab separator. |
| [separates_spaces](separates_spaces.md) | Spaces separated by this separator element. |
| [separator_requirement_drivers](separator_requirement_drivers.md) | Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements. |
| [separator_slab_type](separator_slab_type.md) | Classification of slab-based separator element (for example floor/roof/base slab). |
| [separator_wall_type](separator_wall_type.md) | Classification of wall-based separator element. |
| [serves_spaces](serves_spaces.md) | Spaces served by this system. |
| [serves_zones](serves_zones.md) | Zone context nodes served by this system. |
| [service_endpoint](service_endpoint.md) | Optional URI of the running service or integration endpoint. |
| [signed_artifact](signed_artifact.md) | Optional signed contract artifact at storage_link. |
| [signed_at](signed_at.md) | Timestamp when the contract was signed. |
| [software_version](software_version.md) | Optional deployed version label for the software agent. |
| [source_artifact](source_artifact.md) | Optional source artifact backing this requirement. |
| [source_property](source_property.md) | Original property name inside the source PropertySet (for example FireRating). |
| [source_pset](source_pset.md) | Original IFC PropertySet name (for example Pset_WallCommon). |
| [source_value_raw](source_value_raw.md) | Raw source value before normalization. |
| [space_name_type](space_name_type.md) | Normalized abstract room name type (for example office, kitchen, corridor). Project-specific labels remain on name. When set, adapters may derive a BuildingSpaceActivityClassification entry in classifications[] via the room-name-to-activity mapping bridge. |
| [space_type](space_type.md) | Classification of space (void, circulation, usable, service). |
| [started_at](started_at.md) | Timestamp when the process instance started. |
| [statement](statement.md) | Free-text requirement statement from client or programme. |
| [status](status.md) | Lifecycle or QA status. |
| [storage_link](storage_link.md) | URI/URL/path to the stored artifact location. |
| [street_address](street_address.md) | Street name and house number or equivalent address line. |
| [substitutes_allowed](substitutes_allowed.md) | Whether equivalent or substitute materials are permitted. |
| [successors](successors.md) | Forward precedence links to successor records. Reverse lookup (find all predecessors of X) requires scanning all TimeRecord.successors — acceptable for document exchange, not for live graph queries. |
| [system_discipline](system_discipline.md) | Classification of system discipline (electrical, sanitary, ventilation, heating). |
| [system_type](system_type.md) | Classification of system role (unit, network, terminal). |
| [tags](tags.md) | Optional free-form labels for filtering/grouping. |
| [target_item](target_item.md) | The successor TimeRecord. |
| [target_operator](target_operator.md) | Comparison operator for the requirement target. |
| [target_unit](target_unit.md) | Unit for numeric targets (for example W/m2K, min, dB). |
| [target_unit_uri](target_unit_uri.md) | Optional URI identifying the target unit (for example QUDT). |
| [target_value_boolean](target_value_boolean.md) | Boolean target value when applicable. |
| [target_value_number](target_value_number.md) | Numeric target value when applicable. |
| [target_value_string](target_value_string.md) | Textual target value when applicable. |
| [task_notes](task_notes.md) | Additional notes or implementation details for the task. |
| [task_status](task_status.md) | Task status URI/CURIE aligned with action status vocabularies. |
| [task_type](task_type.md) | Task type expressed as a URI/CURIE from a controlled vocabulary. |
| [text_value](text_value.md) | Localized text value. |
| [time_plan](time_plan.md) | Parent time plan this record belongs to. |
| [time_records](time_records.md) | Time records associated with this entity. |
| [to_revision](to_revision.md) | Target revision number for this change. |
| [to_value](to_value.md) | New value serialized as text. Absent or null for deleted subjects or fields. |
| [transport_medium](transport_medium.md) | Primary transport medium carried or enabled by the connector (for example human_access, air, liquid, electricity). |
| [triggered_process](triggered_process.md) | BPMN process instance that this change triggered or should trigger. |
| [triggered_task](triggered_task.md) | Task entity that this change triggered or should trigger. |
| [unit_cost](unit_cost.md) | Unit cost for this cost item. |
| [usage_context](usage_context.md) | Optional usage context such as work, personal, support, billing, or emergency. |
| [vendor](vendor.md) | Company that sells or offers this product. |
| [withdrawn_at](withdrawn_at.md) | Timestamp when consent was withdrawn, if applicable. |
| [zone_type](zone_type.md) | Optional zone classification; intended for SpatialContext nodes where context_type is zone. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AcousticPropertyKey](AcousticPropertyKey.md) | Canonical acoustic-related keys derived from IFC PropertySets. |
| [ArtifactKind](ArtifactKind.md) | Kind of external project artifact referenced by storage_link. |
| [BoundaryType](BoundaryType.md) |  |
| [ChangeIntentVerdict](ChangeIntentVerdict.md) | Intent stability verdict from an automated judge (for example iterthink STABLE/NEW). |
| [ChangeSeverity](ChangeSeverity.md) | Optional severity of a change independent of change type. |
| [ChangeType](ChangeType.md) | Category of change detected between two revisions. |
| [ConnectionPhysicalType](ConnectionPhysicalType.md) | Classification of physical connector elements that connect spaces. |
| [ConnectionRequirementDriver](ConnectionRequirementDriver.md) | Main requirement drivers for connection element performance. |
| [ConnectionVirtualType](ConnectionVirtualType.md) | Classification of virtual connection semantics using schema-internal meanings because no stable 1:1 IFC mapping exists for these concepts. |
| [ContentKind](ContentKind.md) | Entity type discriminator for adapter projection and querying — not a module router. |
| [ContextType](ContextType.md) |  |
| [CostRecordRole](CostRecordRole.md) |  |
| [DependencyType](DependencyType.md) | Precedence logic between two time records (FS finish-to-start, SS start-to-start, FF finish-to-finish, SF start-to-finish). |
| [EquipmentType](EquipmentType.md) |  |
| [FirePropertyKey](FirePropertyKey.md) | Canonical fire-related keys derived from IFC PropertySets. |
| [GeometryRepresentationType](GeometryRepresentationType.md) | Classification of geometric representation dimension/style. |
| [LawfulBasis](LawfulBasis.md) | Lawful basis for processing personal data, aligned with GDPR Article 6 and similar regimes. |
| [MatchStatus](MatchStatus.md) | Whether an entity satisfies a related requirement at the target revision. |
| [MaterialPropertyKey](MaterialPropertyKey.md) | Canonical material-related keys derived from IFC PropertySets and material metadata. |
| [PerformancePropertyValueType](PerformancePropertyValueType.md) | Type discriminator for normalized performance property values. |
| [PersonalDataCategory](PersonalDataCategory.md) | Category of personal data covered by consent or processing scope. |
| [PersonalDataProcessingState](PersonalDataProcessingState.md) | Privacy handling state for personal data on a Person record, orthogonal to workflow QA status. |
| [PropertyPathKind](PropertyPathKind.md) | Classification of a property path for diff interpretation across IFC and text sources. |
| [QuantityType](QuantityType.md) |  |
| [RequirementTargetOperator](RequirementTargetOperator.md) | Comparison operator for numeric or textual requirement targets. |
| [SecurityPropertyKey](SecurityPropertyKey.md) | Canonical security-related keys derived from IFC PropertySets. |
| [SeparatorRequirementDriver](SeparatorRequirementDriver.md) | Main requirement drivers for separator performance. |
| [SeparatorSlabType](SeparatorSlabType.md) | Classification of slab-based separator elements. |
| [SeparatorWallType](SeparatorWallType.md) | Classification of wall-based separator elements. |
| [SpaceNameType](SpaceNameType.md) | Normalized abstract room name type for IfcSpace; finer-grained than space activity classification. |
| [SpaceType](SpaceType.md) | Classification of space semantics used by modeling and downstream conversion. |
| [SpatialAdjacencyKind](SpatialAdjacencyKind.md) | Spatial adjacency semantics for spatial requirements. |
| [StatusType](StatusType.md) | Lifecycle or QA gate status used for model progression and approvals. |
| [StructuralPropertyKey](StructuralPropertyKey.md) | Canonical structural-related keys derived from IFC PropertySets. |
| [SystemDiscipline](SystemDiscipline.md) | Discipline of a building service system. |
| [SystemType](SystemType.md) | Role of an MEP-related element or grouping in the service chain. |
| [ThermalPropertyKey](ThermalPropertyKey.md) | Canonical thermal-related keys derived from IFC PropertySets. |
| [TransportMedium](TransportMedium.md) | Primary medium transported through or enabled by a physical connector. |
| [ZoneType](ZoneType.md) | Classification of zone purpose and organizational intent. |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |