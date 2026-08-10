from src.mlops.experiment_tracker import ExperimentTracker

tracker = ExperimentTracker(
    "Travel Analytics Demo"
)

with tracker.start_run():

    tracker.log_parameters({

        "Algorithm": "Random Forest",

        "Trees": 100

    })

    tracker.log_metrics({

        "Accuracy": 0.95,

        "Precision": 0.94

    })

print("Experiment Logged Successfully")