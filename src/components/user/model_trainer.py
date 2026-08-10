import sys
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from src.logger import logger
from src.exception import CustomException

from src.config import (
    PROCESSED_DATA_DIR,
    MODELS_DIR
)

from src.constants import (
    USER_EXPERIMENT,
    RANDOM_STATE
)

from src.mlops.experiment_tracker import ExperimentTracker

from src.components.user.model_evaluator import UserModelEvaluator

from src.utils.common import CommonUtils


class UserModelTrainer:

    def __init__(self):

        self.models = {

            "Logistic Regression":
            LogisticRegression(
                max_iter=1000,
                random_state=RANDOM_STATE
            ),

            "Decision Tree":
            DecisionTreeClassifier(
                random_state=RANDOM_STATE
            ),

            "Random Forest":
            RandomForestClassifier(
                random_state=RANDOM_STATE,
                n_estimators=100,
                n_jobs=-1
            )

        }

    def train_model(self):

        try:

            logger.info("Loading Processed User Dataset")

            X_train = pd.read_csv(
                PROCESSED_DATA_DIR / "X_train_user.csv"
            )

            X_test = pd.read_csv(
                PROCESSED_DATA_DIR / "X_test_user.csv"
            )

            y_train = pd.read_csv(
                PROCESSED_DATA_DIR / "y_train_user.csv"
            ).squeeze()

            y_test = pd.read_csv(
                PROCESSED_DATA_DIR / "y_test_user.csv"
            ).squeeze()

            logger.info("Dataset Loaded Successfully")

            evaluator = UserModelEvaluator()

            tracker = ExperimentTracker(
                USER_EXPERIMENT
            )

            results = []

            best_model = None

            best_accuracy = float("-inf")

            for model_name, model in self.models.items():

                logger.info(f"Training {model_name}")

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

                    tracker.log_metrics({

                        "Accuracy": metrics["Accuracy"],
                        "Precision": metrics["Precision"],
                        "Recall": metrics["Recall"],
                        "F1 Score": metrics["F1 Score"]

                    })

                    tracker.log_model(
                        model,
                        model_name
                    )

                    results.append([

                        model_name,

                        metrics["Accuracy"],

                        metrics["Precision"],

                        metrics["Recall"],

                        metrics["F1 Score"]

                    ])

                    if metrics["Accuracy"] > best_accuracy:

                        best_accuracy = metrics["Accuracy"]

                        best_model = model

            results_df = pd.DataFrame(

                results,

                columns=[

                    "Model",

                    "Accuracy",

                    "Precision",

                    "Recall",

                    "F1 Score"

                ]

            )

            results_df = results_df.sort_values(

                by="Accuracy",

                ascending=False

            )

            CommonUtils.save_model(

                best_model,

                MODELS_DIR / "user_classifier.pkl"

            )

            logger.info("Best User Model Saved Successfully")

            return results_df

        except Exception as e:

            logger.error(e)

            raise CustomException(
                e,
                sys
            )