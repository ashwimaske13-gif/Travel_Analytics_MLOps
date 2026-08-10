from src.components.hotel.model_evaluator import HotelModelEvaluator

actual = [1, 0, 1, 1, 0, 1, 0]
predicted = [1, 0, 1, 0, 0, 1, 1]

evaluator = HotelModelEvaluator()

metrics = evaluator.evaluate(
    actual,
    predicted
)

print(metrics)