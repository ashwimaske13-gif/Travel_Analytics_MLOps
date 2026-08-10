import joblib
import pandas as pd

from src.config import (
    MODELS_DIR
)


class FlightPredictionPipeline:

    def __init__(self):

        self.model = joblib.load(
            MODELS_DIR / "flight_price_model.pkl"
        )

    def predict(self, data: pd.DataFrame):

        prediction = self.model.predict(data)

        return prediction