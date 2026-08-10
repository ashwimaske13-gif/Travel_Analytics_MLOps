import sys
import joblib
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.config import (
    RAW_DATA_DIR,
    ARTIFACTS_DIR
)


class HotelDataTransformation:

    def transform_data(self):

        try:

            logger.info("Loading Hotel Dataset...")

            df = pd.read_csv(
                RAW_DATA_DIR / "hotels.csv"
            )

            logger.info(f"Dataset Shape : {df.shape}")

            # remove duplicate bookings if any
            df = df.drop_duplicates()

            logger.info("Creating User-Hotel Interaction Matrix")

            interaction_matrix = df.pivot_table(

                index="userCode",

                columns="name",

                values="total",

                aggfunc="sum",

                fill_value=0

            )

            logger.info(f"Interaction Matrix Shape : {interaction_matrix.shape}")

            joblib.dump(

                interaction_matrix,

                ARTIFACTS_DIR / "hotel_interaction_matrix.pkl"

            )

            logger.info("Interaction Matrix Saved Successfully")

            return interaction_matrix

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)