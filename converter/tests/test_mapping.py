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
