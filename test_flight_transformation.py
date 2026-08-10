from src.components.flight.data_transformation import FlightDataTransformation

transform = FlightDataTransformation()

X_train, X_test, y_train, y_test = (
    transform.initiate_data_transformation()
)

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)