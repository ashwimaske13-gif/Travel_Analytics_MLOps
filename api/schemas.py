from dataclasses import dataclass


@dataclass
class FlightPredictionRequest:

    travel_code: int
    user_code: int

    source: str
    destination: str

    flight_type: str
    agency: str

    day_of_week: str

    time: float
    distance: float

    year: int
    month: int
    day: int
    week_of_year: int


def validate_flight_request(data: dict):

    required_fields = [
        "travel_code",
        "user_code",
        "source",
        "destination",
        "flight_type",
        "agency",
        "day_of_week",
        "time",
        "distance",
        "year",
        "month",
        "day",
        "week_of_year"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing_fields:

        raise ValueError(
            "Missing required fields: "
            + ", ".join(missing_fields)
        )

    try:

        return FlightPredictionRequest(

            travel_code=int(
                data["travel_code"]
            ),

            user_code=int(
                data["user_code"]
            ),

            source=str(
                data["source"]
            ),

            destination=str(
                data["destination"]
            ),

            flight_type=str(
                data["flight_type"]
            ),

            agency=str(
                data["agency"]
            ),

            day_of_week=str(
                data["day_of_week"]
            ),

            time=float(
                data["time"]
            ),

            distance=float(
                data["distance"]
            ),

            year=int(
                data["year"]
            ),

            month=int(
                data["month"]
            ),

            day=int(
                data["day"]
            ),

            week_of_year=int(
                data["week_of_year"]
            )
        )

    except (TypeError, ValueError) as exc:

        raise ValueError(
            f"Invalid flight input: {exc}"
        )