from src.components.user.data_transformation import UserDataTransformation

transform = UserDataTransformation()

X_train, X_test, y_train, y_test = transform.transform_data()

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)

print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)