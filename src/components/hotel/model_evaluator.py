import sys

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from src.logger import logger
from src.exception import CustomException


class HotelModelEvaluator:

    def __init__(self):
        pass

    def evaluate(self, actual, predicted):

        try:

            precision = precision_score(
                actual,
                predicted,
                average="macro",
                zero_division=0
            )

            recall = recall_score(
                actual,
                predicted,
                average="macro",
                zero_division=0
            )

            f1 = f1_score(
                actual,
                predicted,
                average="macro",
                zero_division=0
            )

            logger.info("Hotel Recommendation Model Evaluated Successfully")

            return {

                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1

            }

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)