import pandas as pd

from src.pipeline.prediction_pipeline import (
    FlightPredictionPipeline
)

# Load sample processed data
X_test = pd.read_csv(
    "data/processed/X_test_flight.csv"
)

pipeline = FlightPredictionPipeline()

prediction = pipeline.predict(
    X_test.head()
)

print(prediction)
