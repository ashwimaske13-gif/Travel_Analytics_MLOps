from src.utils.mlflow_utils import MLflowManager

MLflowManager.set_experiment(
    "Test Experiment"
)

with MLflowManager.start_run():

    MLflowManager.log_params({

        "Model":"RandomForest",

        "Trees":100

    })

    MLflowManager.log_metrics({

        "Accuracy":0.95

    })

print("MLflow Test Successful")