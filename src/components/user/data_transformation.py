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


class UserDataTransformation:

    def __init__(self):

        self.company_encoder = LabelEncoder()
        self.gender_encoder = LabelEncoder()
        self.scaler = StandardScaler()

    def transform_data(self):

        try:

            logger.info("Loading Users Dataset...")

            df = pd.read_csv(
                RAW_DATA_DIR / "users.csv"
            )

            logger.info(f"Dataset Shape : {df.shape}")

            # Remove unnecessary column
            df.drop(
                columns=["name"],
                inplace=True
            )

            logger.info("Encoding Company")

            df["company"] = self.company_encoder.fit_transform(
                df["company"]
            )

            logger.info("Encoding Gender")

            df["gender"] = self.gender_encoder.fit_transform(
                df["gender"]
            )

            X = df.drop(
                columns=["gender"]
            )

            y = df["gender"]

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42,
                stratify=y
            )

            logger.info("Scaling Age")

            X_train["age"] = self.scaler.fit_transform(
                X_train[["age"]]
            )

            X_test["age"] = self.scaler.transform(
                X_test[["age"]]
            )

            logger.info("Saving Processed Data")

            X_train.to_csv(
                PROCESSED_DATA_DIR / "X_train_user.csv",
                index=False
            )

            X_test.to_csv(
                PROCESSED_DATA_DIR / "X_test_user.csv",
                index=False
            )

            y_train.to_csv(
                PROCESSED_DATA_DIR / "y_train_user.csv",
                index=False
            )

            y_test.to_csv(
                PROCESSED_DATA_DIR / "y_test_user.csv",
                index=False
            )

            logger.info("Saving Encoders")

            joblib.dump(
                self.company_encoder,
                ARTIFACTS_DIR / "company_encoder.pkl"
            )

            joblib.dump(
                self.gender_encoder,
                ARTIFACTS_DIR / "gender_encoder.pkl"
            )

            joblib.dump(
                self.scaler,
                ARTIFACTS_DIR / "user_scaler.pkl"
            )

            logger.info("Transformation Completed Successfully")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)