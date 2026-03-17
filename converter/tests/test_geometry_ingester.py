from types import SimpleNamespace

from pbs_converter.geometry_ingester import build_geometry_records


def _product_with_coordinates(*coords: float) -> SimpleNamespace:
    location = SimpleNamespace(Coordinates=list(coords))
    relative = SimpleNamespace(Location=location)
    placement = SimpleNamespace(RelativePlacement=relative, PlacementRelTo=None)
    return SimpleNamespace(ObjectPlacement=placement)


def test_build_geometry_records_with_centroid() -> None:
    product = _product_with_coordinates(1.5, 2.5, 3.5)
    records, warnings = build_geometry_records(product, "3H7gK7S6v3A8mM2f1ABC12")

    assert len(records) == 4
    assert warnings == []
    assert records[0].geometry_representation == "point"
    assert records[0].payload == {"x": 1.5, "y": 2.5, "z": 3.5}
    assert {record.geometry_representation for record in records[1:]} == {"axis", "body_3d", "footprint_2d"}


def test_build_geometry_records_centroid_fallback() -> None:
    product = SimpleNamespace(ObjectPlacement=None)
    records, warnings = build_geometry_records(product, "3H7gK7S6v3A8mM2f1ABC12")

    assert len(records) == 4
    assert len(warnings) == 1
    assert "Centroid fallback to origin" in warnings[0]
    assert records[0].payload == {"x": 0.0, "y": 0.0, "z": 0.0}
