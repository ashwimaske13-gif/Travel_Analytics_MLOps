from src.components.user.data_ingestion import UserDataIngestion

ingestion = UserDataIngestion()

df = ingestion.load_data()

print(df.head())

print()

print(df.shape)