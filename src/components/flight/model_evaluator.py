import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class FlightModelEvaluator:

    def evaluate(self, model, X_test, y_test):

        prediction = model.predict(X_test)

        mae = mean_absolute_error(y_test, prediction)

        mse = mean_squared_error(y_test, prediction)

        rmse = np.sqrt(mse)

        r2 = r2_score(y_test, prediction)

        return {

            "MAE": mae,

            "MSE": mse,

            "RMSE": rmse,

            "R2 Score": r2

        }