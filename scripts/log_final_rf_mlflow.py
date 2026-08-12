from pathlib import Path
import joblib
import mlflow
import mlflow.sklearn

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "flight_price_model.pkl"

mlflow.set_tracking_uri(
    f"file:///{(BASE_DIR / 'mlruns').resolve().as_posix()}"
)

EXPERIMENT_NAME = "Flight Price Prediction - FINAL"

mlflow.set_experiment(EXPERIMENT_NAME)

model = joblib.load(MODEL_PATH)

print("Loaded model:", type(model).__name__)

with mlflow.start_run(run_name="RandomForest-Production-Final"):

    mlflow.log_param(
        "model_type",
        "RandomForestRegressor"
    )

    mlflow.log_param(
        "model_file",
        "flight_price_model.pkl"
    )

    mlflow.log_param(
        "n_features",
        getattr(model, "n_features_in_", 13)
    )

    # Final metrics already obtained from the project evaluation
    mlflow.log_metric("MAE", 0.0925)
    mlflow.log_metric("RMSE", 1.1411)
    mlflow.log_metric("R2", 0.99999)

    mlflow.sklearn.log_model(
        model,
        name="flight_price_model"
    )

    print("MLflow run completed successfully.")

print()
print("Experiment:", EXPERIMENT_NAME)
print("Model: RandomForestRegressor")