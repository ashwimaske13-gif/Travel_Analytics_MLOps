import sys
import joblib
import mlflow
import pandas as pd

from src.logger import logger
from src.exception import CustomException

from src.config import (
    ARTIFACTS_DIR,
    PROCESSED_DATA_DIR
)

from src.constants import (
    HOTEL_MATRIX_NAME,
    HOTEL_EXPERIMENT
)

from src.mlops.experiment_tracker import ExperimentTracker

from src.utils.common import CommonUtils


class HotelModelTrainer:

    def train_model(self):

        try:

            logger.info("Loading Hotel Interaction Matrix")

            interaction_matrix = CommonUtils.load_artifact(

                ARTIFACTS_DIR / HOTEL_MATRIX_NAME

            )

            logger.info("Interaction Matrix Loaded Successfully")

            tracker = ExperimentTracker(

                HOTEL_EXPERIMENT

            )

            with tracker.start_run(

                run_name="Hotel Recommendation"

            ):

                tracker.log_parameters({

                    "Algorithm": "User-Based Collaborative Filtering",

                    "Similarity": "Cosine Similarity",

                    "Users": interaction_matrix.shape[0],

                    "Hotels": interaction_matrix.shape[1]

                })

                sparsity = (
                    (interaction_matrix == 0).sum().sum()
                    /
                    interaction_matrix.size
                )

                tracker.log_metrics({

                    "Users": interaction_matrix.shape[0],

                    "Hotels": interaction_matrix.shape[1],

                    "Sparsity": sparsity

                })
                import mlflow

                mlflow.log_artifact(

                str(ARTIFACTS_DIR / HOTEL_MATRIX_NAME)

)

                # tracker.log_model(

                #     interaction_matrix,

                #     "hotel_interaction_matrix"

                

            logger.info(

                "Hotel Recommendation Experiment Logged Successfully."

            )

            return interaction_matrix.head()

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)