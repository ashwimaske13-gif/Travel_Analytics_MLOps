import sys
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException
from src.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    ARTIFACTS_DIR
)


class FlightDataTransformation:

    def __init__(self):

        self.flight_path = RAW_DATA_DIR / "flights.csv"

    def initiate_data_transformation(self):

        try:

            logger.info("Starting Flight Data Transformation")

            df = pd.read_csv(self.flight_path)

            # -----------------------------
            # Date Features
            # -----------------------------

            df["date"] = pd.to_datetime(df["date"])

            df["year"] = df["date"].dt.year
            df["month"] = df["date"].dt.month
            df["day"] = df["date"].dt.day
            df["day_of_week"] = df["date"].dt.day_name()
            df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)

            df.drop(columns="date", inplace=True)

            # -----------------------------
            # Label Encoding
            # -----------------------------

            categorical_columns = [
                "from",
                "to",
                "flightType",
                "agency",
                "day_of_week"
            ]

            encoders = {}

            for column in categorical_columns:

                encoder = LabelEncoder()

                df[column] = encoder.fit_transform(df[column])

                encoders[column] = encoder

                joblib.dump(
                    encoder,
                    ARTIFACTS_DIR / f"{column}_encoder.pkl"
                )

            # -----------------------------
            # Features & Target
            # -----------------------------

            X = df.drop("price", axis=1)

            y = df["price"]

            # -----------------------------
            # Train Test Split
            # -----------------------------

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42
            )

            # -----------------------------
            # Scaling
            # -----------------------------

            scaler = StandardScaler()

            numeric_columns = [
                "time",
                "distance",
                "year",
                "month",
                "day",
                "week_of_year"
            ]

            X_train[numeric_columns] = scaler.fit_transform(
                X_train[numeric_columns]
            )

            X_test[numeric_columns] = scaler.transform(
                X_test[numeric_columns]
            )

            joblib.dump(
                scaler,
                ARTIFACTS_DIR / "flight_scaler.pkl"
            )

            # -----------------------------
            # Save Processed Data
            # -----------------------------

            X_train.to_csv(
                PROCESSED_DATA_DIR / "X_train_flight.csv",
                index=False
            )

            X_test.to_csv(
                PROCESSED_DATA_DIR / "X_test_flight.csv",
                index=False
            )

            y_train.to_csv(
                PROCESSED_DATA_DIR / "y_train_flight.csv",
                index=False
            )

            y_test.to_csv(
                PROCESSED_DATA_DIR / "y_test_flight.csv",
                index=False
            )

            logger.info("Flight Data Transformation Completed")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)