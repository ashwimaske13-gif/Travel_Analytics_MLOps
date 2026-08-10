import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.config import RAW_DATA_DIR


class FlightDataIngestion:
    """
    Reads the Flight dataset.
    """

    def __init__(self):
        self.flight_path = RAW_DATA_DIR / "flights.csv"

    def load_data(self):
        """
        Load flight dataset.
        """

        try:
            logger.info("Started Flight Data Ingestion")

            if not self.flight_path.exists():
                raise FileNotFoundError(
                    f"{self.flight_path} not found."
                )

            df = pd.read_csv(self.flight_path)

            logger.info(
                f"Flight Dataset Loaded Successfully. Shape: {df.shape}"
            )

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)