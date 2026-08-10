import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


class UserModelEvaluator:

    def evaluate(
        self,
        model,
        X_test,
        y_test
    ):

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        precision = precision_score(
            y_test,
            prediction,
            average="weighted"
        )

        recall = recall_score(
            y_test,
            prediction,
            average="weighted"
        )

        f1 = f1_score(
            y_test,
            prediction,
            average="weighted"
        )

        cm = confusion_matrix(
            y_test,
            prediction
        )

        report = classification_report(
            y_test,
            prediction
        )

        return {

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1 Score": f1,

            "Confusion Matrix": cm,

            "Classification Report": report

        }