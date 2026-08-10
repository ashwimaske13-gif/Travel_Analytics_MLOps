from src.utils.flight_lookup import FlightLookup


def test_get_all_from_locations():
    lookup = FlightLookup()

    locations = lookup.get_all_from_locations()

    assert isinstance(locations, list)
    assert len(locations) > 0


def test_get_all_to_locations():
    lookup = FlightLookup()

    locations = lookup.get_all_to_locations()

    assert isinstance(locations, list)
    assert len(locations) > 0


def test_get_all_airlines():
    lookup = FlightLookup()

    airlines = lookup.get_all_airlines()

    assert isinstance(airlines, list)
    assert len(airlines) > 0


def test_get_all_flight_types():
    lookup = FlightLookup()

    flight_types = lookup.get_all_flight_types()

    assert isinstance(flight_types, list)
    assert len(flight_types) > 0


def test_get_route_details():
    lookup = FlightLookup()

    result = lookup.get_route_details(
        "Recife (PE)",
        "Florianopolis (SC)",
        "FlyingDrops"
    )

    assert isinstance(result, dict)
    assert "distance" in result
    assert "time" in result