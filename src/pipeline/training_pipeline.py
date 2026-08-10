from src.logger import logger

from src.components.flight.data_transformation import (
    FlightDataTransformation
)

from src.components.flight.model_trainer import (
    FlightModelTrainer
)


class TrainingPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):

        logger.info("=" * 60)
        logger.info("Flight Training Pipeline Started")
        logger.info("=" * 60)

        # Step 1
        transformer = FlightDataTransformation()

        transformer.initiate_data_transformation()

        logger.info("Data Transformation Completed")

        # Step 2
        trainer = FlightModelTrainer()

        results = trainer.train_model()

        logger.info("Model Training Completed")

        logger.info("=" * 60)
        logger.info("Pipeline Finished Successfully")
        logger.info("=" * 60)

        return results


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    results = pipeline.run_pipeline()

    print(results)