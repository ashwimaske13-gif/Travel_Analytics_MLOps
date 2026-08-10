from src.components.hotel.data_ingestion import HotelDataIngestion

ingestion = HotelDataIngestion()

df = ingestion.load_data()

print(df.head())

print()

print(df.shape)