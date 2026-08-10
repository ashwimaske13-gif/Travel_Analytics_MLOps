import pandas as pd

from src.config import RAW_DATA_DIR


class FlightLookup:

    def __init__(self):

        self.df = pd.read_csv(
            RAW_DATA_DIR / "flights.csv"
        )

    # -------------------------
    # Original Methods
    # -------------------------

    def get_all_from_locations(self):

        return sorted(
            self.df["from"].unique().tolist()
        )

    def get_all_to_locations(self):

        return sorted(
            self.df["to"].unique().tolist()
        )

    def get_all_airlines(self):

        return sorted(
            self.df["agency"].unique().tolist()
        )

    def get_all_flight_types(self):

        return sorted(
            self.df["flightType"].unique().tolist()
        )

    def get_route_details(
        self,
        source,
        destination,
        agency=None
    ):

        route = self.df[
            (self.df["from"] == source)
            &
            (self.df["to"] == destination)
        ]

        if agency:

            route = route[
                route["agency"] == agency
            ]

        if route.empty:

            return {

                "distance": 0,

                "time": 0

            }

        route = route.iloc[0]

        return {

            "distance": float(route["distance"]),

            "time": float(route["time"])

        }

    # -------------------------
    # Wrapper Methods
    # -------------------------

    def get_from_cities(self):

        return self.get_all_from_locations()

    def get_to_cities(self):

        return self.get_all_to_locations()

    def get_airlines(self):

        return self.get_all_airlines()

    def get_flight_types(self):

        return self.get_all_flight_types()

    def get_route(self, source, destination):

        return self.get_route_details(
            source,
            destination
        )