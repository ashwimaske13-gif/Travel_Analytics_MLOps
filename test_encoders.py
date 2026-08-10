import joblib

from src.config import ARTIFACTS_DIR

from_encoder = joblib.load(
    ARTIFACTS_DIR / "from_encoder.pkl"
)

to_encoder = joblib.load(
    ARTIFACTS_DIR / "to_encoder.pkl"
)

flight_encoder = joblib.load(
    ARTIFACTS_DIR / "flightType_encoder.pkl"
)

agency_encoder = joblib.load(
    ARTIFACTS_DIR / "agency_encoder.pkl"
)

day_encoder = joblib.load(
    ARTIFACTS_DIR / "day_of_week_encoder.pkl"
)

print("FROM")
print(from_encoder.classes_)
print()

print("TO")
print(to_encoder.classes_)
print()

print("FLIGHT TYPE")
print(flight_encoder.classes_)
print()

print("AGENCY")
print(agency_encoder.classes_)
print()

print("DAY")
print(day_encoder.classes_)