from src.utils.flight_lookup import FlightLookup

lookup = FlightLookup()

print()

print("FROM Cities")
print("----------------")
print(lookup.get_all_from_locations())

print()

print("TO Cities")
print("----------------")
print(lookup.get_all_to_locations())

print()

print("Airlines")
print("----------------")
print(lookup.get_all_airlines())

print()

print("Flight Types")
print("----------------")
print(lookup.get_all_flight_types())

print()

print("Sample Route")
print("----------------")

print(

    lookup.get_route_information(

        "Recife (PE)",

        "Florianopolis (SC)",

        "FlyingDrops"

    )

)