from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent


MODEL_PATH = (
    BASE_DIR
    / "models"
    / "flight_price_model.pkl"
)

SCALER_PATH = (
    BASE_DIR
    / "artifacts"
    / "flight_scaler.pkl"
)

FROM_ENCODER_PATH = (
    BASE_DIR
    / "artifacts"
    / "from_encoder.pkl"
)

TO_ENCODER_PATH = (
    BASE_DIR
    / "artifacts"
    / "to_encoder.pkl"
)

FLIGHT_TYPE_ENCODER_PATH = (
    BASE_DIR
    / "artifacts"
    / "flightType_encoder.pkl"
)

AGENCY_ENCODER_PATH = (
    BASE_DIR
    / "artifacts"
    / "agency_encoder.pkl"
)

DAY_OF_WEEK_ENCODER_PATH = (
    BASE_DIR
    / "artifacts"
    / "day_of_week_encoder.pkl"
)


class FlightPricePredictor:

    def __init__(self):

        self.model = joblib.load(
            MODEL_PATH
        )

        self.scaler = joblib.load(
            SCALER_PATH
        )

        self.from_encoder = joblib.load(
            FROM_ENCODER_PATH
        )

        self.to_encoder = joblib.load(
            TO_ENCODER_PATH
        )

        self.flight_type_encoder = joblib.load(
            FLIGHT_TYPE_ENCODER_PATH
        )

        self.agency_encoder = joblib.load(
            AGENCY_ENCODER_PATH
        )

        self.day_of_week_encoder = joblib.load(
            DAY_OF_WEEK_ENCODER_PATH
        )

    def encode_value(
        self,
        encoder,
        value
    ):

        try:

            return int(
                encoder.transform([value])[0]
            )

        except ValueError:

            raise ValueError(
                f"Unknown value '{value}'. "
                f"Allowed values: "
                f"{list(encoder.classes_)}"
            )

    def predict(
        self,
        travel_code,
        user_code,
        source,
        destination,
        flight_type,
        agency,
        day_of_week,
        time,
        distance,
        year,
        month,
        day,
        week_of_year
    ):

        source_encoded = self.encode_value(
            self.from_encoder,
            source
        )

        destination_encoded = self.encode_value(
            self.to_encoder,
            destination
        )

        flight_type_encoded = self.encode_value(
            self.flight_type_encoder,
            flight_type
        )

        agency_encoded = self.encode_value(
            self.agency_encoder,
            agency
        )

        day_of_week_encoded = self.encode_value(
            self.day_of_week_encoder,
            day_of_week
        )

        data = pd.DataFrame(
            [[
                travel_code,
                user_code,
                source_encoded,
                destination_encoded,
                flight_type_encoded,
                time,
                distance,
                agency_encoded,
                year,
                month,
                day,
                day_of_week_encoded,
                week_of_year
            ]],
            columns=[
                "travelCode",
                "userCode",
                "from",
                "to",
                "flightType",
                "time",
                "distance",
                "agency",
                "year",
                "month",
                "day",
                "day_of_week",
                "week_of_year"
            ]
        )

        numeric_columns = [
            "time",
            "distance",
            "year",
            "month",
            "day",
            "week_of_year"
        ]

        data[numeric_columns] = (
            self.scaler.transform(
                data[numeric_columns]
            )
        )

        prediction = self.model.predict(
            data
        )

        return float(
            prediction[0]
        )