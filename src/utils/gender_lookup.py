import pandas as pd
import joblib

from src.config import RAW_DATA_DIR
from src.config import MODELS_DIR


class GenderLookup:

    def __init__(self):

        self.users = pd.read_csv(
            RAW_DATA_DIR / "users.csv"
        )

        self.model = joblib.load(
            MODELS_DIR / "gender_classifier.pkl"
        )

    def get_companies(self):

        return sorted(
            self.users["company"]
            .dropna()
            .unique()
            .tolist()
        )

    def predict_gender(
        self,
        name,
        company,
        age
    ):

        first_name = (
            str(name)
            .strip()
            .split()[0]
        )

        data = pd.DataFrame(
            [{
                "first_name": first_name,
                "company": company,
                "age": age
            }]
        )

        prediction = self.model.predict(
            data
        )[0]

        if prediction == "none":
            return "Not Specified"

        return prediction.title()