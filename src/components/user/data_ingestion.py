import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.config import RAW_DATA_DIR


class UserDataIngestion:

    def __init__(self):

        self.data_path = RAW_DATA_DIR / "users.csv"

    def load_data(self):

        try:

            logger.info("Loading Users Dataset...")

            df = pd.read_csv(self.data_path)

            logger.info(f"Dataset Loaded Successfully: {df.shape}")

            return df

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)