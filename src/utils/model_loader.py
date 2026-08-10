from src.config import (
    MODELS_DIR,
    ARTIFACTS_DIR
)

from src.utils.common import CommonUtils


class ModelLoader:

    @staticmethod
    def load_flight_model():

        return CommonUtils.load_model(
            MODELS_DIR / "flight_price_model.pkl"
        )

    @staticmethod
    def load_user_model():

        return CommonUtils.load_model(
            MODELS_DIR / "gender_classifier.pkl"
        )

    @staticmethod
    def load_hotel_matrix():

        return CommonUtils.load_artifact(
            ARTIFACTS_DIR / "hotel_interaction_matrix.pkl"
        )

    @staticmethod
    def load_flight_scaler():

        return CommonUtils.load_artifact(
            ARTIFACTS_DIR / "flight_scaler.pkl"
        )

    @staticmethod
    def load_user_scaler():

        return CommonUtils.load_artifact(
            ARTIFACTS_DIR / "user_scaler.pkl"
        )

    @staticmethod
    def load_encoder(name):

        return CommonUtils.load_artifact(
            ARTIFACTS_DIR / f"{name}_encoder.pkl"
        )