from src.components.flight.data_ingestion import FlightDataIngestion

ingestion = FlightDataIngestion()

df = ingestion.load_data()

print(df.head())

print()

print(df.shape)