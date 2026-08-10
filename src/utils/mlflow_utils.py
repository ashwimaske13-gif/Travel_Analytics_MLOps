import mlflow
import mlflow.sklearn

from src.logger import logger


class MLflowManager:

    @staticmethod
    def set_experiment(experiment_name):

        mlflow.set_experiment(experiment_name)

        logger.info(
            f"MLflow Experiment : {experiment_name}"
        )

    @staticmethod
    def start_run(run_name=None):

        return mlflow.start_run(
            run_name=run_name
        )

    @staticmethod
    def log_params(params: dict):

        mlflow.log_params(params)

    @staticmethod
    def log_metrics(metrics: dict):

        mlflow.log_metrics(metrics)

    @staticmethod
    def log_model(model, artifact_name):

        mlflow.sklearn.log_model(
            model,
            artifact_name
        )

    @staticmethod
    def end_run():

        mlflow.end_run()