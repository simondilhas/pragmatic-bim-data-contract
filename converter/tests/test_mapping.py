from pbs_converter.mapping import map_ifc_product_to_entity


def test_map_ifc_wall_to_separator_wall() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcWall",
        global_id="3H7gK7S6v3A8mM2f1ABC12",
        name="WALL-01",
    )
    assert entity is not None
    assert entity.type == "SeparatorWall"
    assert entity.payload["separator_wall_type"] == "unit_boundary"


def test_map_ifc_door_to_connection_physical_defaults() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcDoor",
        global_id="2H7gK7S6v3A8mM2f1ABC34",
        name="DOOR-01",
    )
    assert entity is not None
    assert entity.type == "ConnectionPhysical"
    assert entity.payload["connection_physical_type"] == "door"
    assert entity.payload["transport_medium"] == "human_access"


def test_map_ifc_window_to_connection_physical_defaults() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcWindow",
        global_id="2H7gK7S6v3A8mM2f1ABC35",
        name="WINDOW-01",
    )
    assert entity is not None
    assert entity.type == "ConnectionPhysical"
    assert entity.payload["connection_physical_type"] == "window"
    assert entity.payload["transport_medium"] == "daylight_view"


def test_map_ifc_duct_to_connection_physical_defaults() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcDuctSegment",
        global_id="2H7gK7S6v3A8mM2f1ABC36",
        name="DUCT-01",
    )
    assert entity is not None
    assert entity.type == "ConnectionPhysical"
    assert entity.payload["connection_physical_type"] == "duct"
    assert entity.payload["transport_medium"] == "air"


def test_map_ifc_distribution_control_to_equipment() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcDistributionControlElement",
        global_id="2H7gK7S6v3A8mM2f1ABC37",
        name="SENSOR-01",
    )
    assert entity is not None
    assert entity.type == "Equipment"
    assert entity.payload["equipment_type"] == "other"


def test_map_ifc_distribution_element_no_longer_mapped() -> None:
    entity = map_ifc_product_to_entity(
        ifc_class_name="IfcDistributionElement",
        global_id="2H7gK7S6v3A8mM2f1ABC38",
        name="DISTR-01",
    )
    assert entity is None
