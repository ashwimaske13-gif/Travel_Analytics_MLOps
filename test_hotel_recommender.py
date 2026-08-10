from src.components.hotel.recommender import HotelRecommender

recommender = HotelRecommender()

recommendations = recommender.recommend_hotels(
    user_id=25,
    top_n=5
)

print("Recommended Hotels:")
print(recommendations)