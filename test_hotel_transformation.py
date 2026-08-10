from src.components.hotel.data_transformation import HotelDataTransformation

transform = HotelDataTransformation()

interaction_matrix = transform.transform_data()

print(interaction_matrix.head())

print()

print(interaction_matrix.shape)