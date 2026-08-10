import mlflow
import mlflow.sklearn

from src.logger import logger


class ExperimentTracker:

    def __init__(self, experiment_name):

        self.experiment_name = experiment_name

        mlflow.set_experiment(
            experiment_name
        )

    def start_run(self, run_name=None):

        return mlflow.start_run(
            run_name=run_name
        )

    def log_parameters(self, parameters):

        mlflow.log_params(parameters)

    def log_metrics(self, metrics):

        mlflow.log_metrics(metrics)

    def log_model(self, model, artifact_name):

        mlflow.sklearn.log_model(
            sk_model=model,
            name=artifact_name
        )

    def end_run(self):

        mlflow.end_run()