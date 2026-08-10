import pandas as pd
import joblib

from src.config import RAW_DATA_DIR
from src.config import MODELS_DIR
from src.config import ARTIFACTS_DIR


class HotelLookup:

    def __init__(self):

        # Load hotel dataset
        self.df = pd.read_csv(
            RAW_DATA_DIR / "hotels.csv"
        )

        # Load recommendation artifacts
        self.user_similarity = joblib.load(
            MODELS_DIR / "user_similarity.pkl"
        )

        self.interaction_matrix = joblib.load(
            ARTIFACTS_DIR / "hotel_interaction_matrix.pkl"
        )

    # ---------------------------------------------------
    # Dropdown Data
    # ---------------------------------------------------

    def get_cities(self):

        return sorted(
            self.df["place"].dropna().unique().tolist()
        )

    def get_hotels(self):

        return sorted(
            self.df["name"].dropna().unique().tolist()
        )

    # ---------------------------------------------------
    # Recommendation System
    # ---------------------------------------------------

    def recommend_hotels(self, user_code, city="", top_n=5):

        # User not found
        if user_code not in self.interaction_matrix.index:
            return []

        # Similar users
        similar_users = (
            self.user_similarity[user_code]
            .sort_values(ascending=False)
            .drop(user_code)
        )

        # Recommendation score
        scores = pd.Series(dtype=float)

        for sim_user in similar_users.index[:10]:

            scores = scores.add(
                self.interaction_matrix.loc[sim_user],
                fill_value=0
            )

        # Remove already visited hotels
        visited = self.interaction_matrix.loc[user_code]

        scores = scores[visited == 0]

        hotels = []

        # Loop through recommended hotels
        for hotel_name in scores.sort_values(
                ascending=False
        ).index:

            hotel_rows = self.df[
                self.df["name"] == hotel_name
            ]

            # Optional city filter
            if city != "":
                hotel_rows = hotel_rows[
                    hotel_rows["place"] == city
                ]

            if hotel_rows.empty:
                continue

            row = hotel_rows.iloc[0]

            hotels.append({

                "name": row["name"],

                "place": row["place"],

                "price": round(float(row["price"]), 2),

                "days": int(row["days"]),

                "total": round(float(row["total"]), 2)

            })

            if len(hotels) >= top_n:
                break

        # ---------------------------------------------------
        # Fallback
        # ---------------------------------------------------

        if len(hotels) == 0:

            fallback = self.df.copy()

            if city != "":

                fallback = fallback[
                    fallback["place"] == city
                ]

            fallback = (
                fallback
                .sort_values(
                    by="total",
                    ascending=False
                )
                .drop_duplicates(
                    subset=["name"]
                )
                .head(top_n)
            )

            hotels = []

            for _, row in fallback.iterrows():

                hotels.append({

                    "name": row["name"],

                    "place": row["place"],

                    "price": round(float(row["price"]), 2),

                    "days": int(row["days"]),

                    "total": round(float(row["total"]), 2)

                })

        return hotels