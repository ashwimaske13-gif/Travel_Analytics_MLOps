import sys
import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from src.logger import logger
from src.exception import CustomException
from src.config import ARTIFACTS_DIR


class HotelRecommender:

    def __init__(self):

        self.interaction_matrix = joblib.load(
            ARTIFACTS_DIR / "hotel_interaction_matrix.pkl"
        )

        logger.info("Interaction Matrix Loaded Successfully")

        self.user_similarity = pd.DataFrame(
            cosine_similarity(self.interaction_matrix),
            index=self.interaction_matrix.index,
            columns=self.interaction_matrix.index
        )

        logger.info("User Similarity Matrix Created Successfully")

    def recommend_hotels(self, user_id, top_n=5):

        try:

            if user_id not in self.interaction_matrix.index:
                return []

            similar_users = self.user_similarity[user_id].sort_values(
                ascending=False
            )[1:11]

            recommendations = {}

            for similar_user in similar_users.index:

                hotels = self.interaction_matrix.loc[similar_user]

                for hotel, value in hotels.items():

                    if value > 0:
                        recommendations[hotel] = (
                            recommendations.get(hotel, 0) + value
                        )

            booked_hotels = self.interaction_matrix.loc[user_id]

            for hotel in booked_hotels.index:

                if booked_hotels[hotel] > 0:
                    recommendations.pop(hotel, None)

            recommended = sorted(
                recommendations.items(),
                key=lambda x: x[1],
                reverse=True
            )

            # Normal recommendation
            if recommended:
                return [
                    hotel
                    for hotel, _ in recommended[:top_n]
                ]

            # Fallback if user has booked all hotels
            logger.info(
                "User has already booked all hotels. Returning favourite hotels."
            )

            visited = self.interaction_matrix.loc[user_id]

            visited = visited.sort_values(
                ascending=False
            )

            return visited.head(top_n).index.tolist()

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)