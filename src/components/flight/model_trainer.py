import sys
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from src.logger import logger
from src.exception import CustomException

from src.config import (
    PROCESSED_DATA_DIR,
    MODELS_DIR
)

from src.constants import (
    FLIGHT_EXPERIMENT,
    FLIGHT_MODEL_NAME,
    RANDOM_STATE
)

from src.components.flight.model_evaluator import (
    FlightModelEvaluator
)

from src.mlops.experiment_tracker import (
    ExperimentTracker
)

from src.utils.common import CommonUtils


class FlightModelTrainer:

    def __init__(self):

        self.models = {

            "Linear Regression":
                LinearRegression(),

            "Decision Tree":
                DecisionTreeRegressor(
                    random_state=RANDOM_STATE
                ),

            "Random Forest":
                RandomForestRegressor(
                    random_state=RANDOM_STATE
                ),

            "Gradient Boosting":
                GradientBoostingRegressor(
                    random_state=RANDOM_STATE
                )

        }

    def train_model(self):

        try:

            logger.info("Loading processed dataset...")

            X_train = pd.read_csv(
                PROCESSED_DATA_DIR / "X_train_flight.csv"
            )

            X_test = pd.read_csv(
                PROCESSED_DATA_DIR / "X_test_flight.csv"
            )

            y_train = pd.read_csv(
                PROCESSED_DATA_DIR / "y_train_flight.csv"
            ).squeeze()

            y_test = pd.read_csv(
                PROCESSED_DATA_DIR / "y_test_flight.csv"
            ).squeeze()

            logger.info("Dataset loaded successfully.")

            evaluator = FlightModelEvaluator()

            tracker = ExperimentTracker(
                FLIGHT_EXPERIMENT
            )

            results = []

            best_model = None

            best_score = float("-inf")

            for model_name, model in self.models.items():

                logger.info(
                    f"Training {model_name}"
                )

                with tracker.start_run(
                    run_name=model_name
                ):

                    model.fit(
                        X_train,
                        y_train
                    )

                    metrics = evaluator.evaluate(
                        model,
                        X_test,
                        y_test
                    )

                    tracker.log_parameters({

                        "Model": model_name

                    })

                    tracker.log_metrics(metrics)

                    tracker.log_model(
                        model,
                        model_name
                    )

                    results.append([

                        model_name,

                        metrics["MAE"],

                        metrics["MSE"],

                        metrics["RMSE"],

                        metrics["R2 Score"]

                    ])

                    if metrics["R2 Score"] > best_score:

                        best_score = metrics["R2 Score"]

                        best_model = model

            results_df = pd.DataFrame(

                results,

                columns=[

                    "Model",

                    "MAE",

                    "MSE",

                    "RMSE",

                    "R2 Score"

                ]

            )

            results_df = results_df.sort_values(

                by="R2 Score",

                ascending=False

            )

            CommonUtils.save_model(

                best_model,

                MODELS_DIR / FLIGHT_MODEL_NAME

            )

            logger.info(

                "Best Flight Model Saved Successfully."

            )

            return results_df

        except Exception as e:

            logger.error(e)

            raise CustomException(
                e,
                sys
            )