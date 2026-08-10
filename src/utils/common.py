import joblib
import pandas as pd

from pathlib import Path

from src.logger import logger


class CommonUtils:

    @staticmethod
    def load_csv(file_path: Path):

        logger.info(f"Loading CSV : {file_path}")

        return pd.read_csv(file_path)

    @staticmethod
    def save_csv(df, file_path: Path):

        logger.info(f"Saving CSV : {file_path}")

        df.to_csv(file_path, index=False)

    @staticmethod
    def save_model(model, file_path: Path):

        logger.info(f"Saving Model : {file_path}")

        joblib.dump(model, file_path)

    @staticmethod
    def load_model(file_path: Path):

        logger.info(f"Loading Model : {file_path}")

        return joblib.load(file_path)

    @staticmethod
    def save_artifact(obj, file_path: Path):

        logger.info(f"Saving Artifact : {file_path}")

        joblib.dump(obj, file_path)

    @staticmethod
    def load_artifact(file_path: Path):

        logger.info(f"Loading Artifact : {file_path}")

        return joblib.load(file_path)