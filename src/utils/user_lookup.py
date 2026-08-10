import pandas as pd

from src.config import RAW_DATA_DIR


class UserLookup:

    def __init__(self):

        self.users = pd.read_csv(
            RAW_DATA_DIR / "users.csv"
        )

        self.flights = pd.read_csv(
            RAW_DATA_DIR / "flights.csv"
        )

        self.hotels = pd.read_csv(
            RAW_DATA_DIR / "hotels.csv"
        )

    def get_user_summary(self, user_code):

        user = self.users[
            self.users["code"] == user_code
        ]

        flights = self.flights[
            self.flights["userCode"] == user_code
        ]

        hotels = self.hotels[
            self.hotels["userCode"] == user_code
        ]

        if user.empty:

            return None

        user = user.iloc[0]

        gender = user["gender"]

        age = int(user["age"])

        company = user["company"]

        name = user["name"]

        # -----------------------

        flight_count = len(flights)

        hotel_count = len(hotels)

        # -----------------------

        if flight_count > 0:

            fav_airline = flights["agency"].mode()[0]

            fav_destination = flights["to"].mode()[0]

            avg_flight_price = round(

                flights["price"].mean(),

                2

            )

            total_flight = round(

                flights["price"].sum(),

                2

            )

        else:

            fav_airline = "-"

            fav_destination = "-"

            avg_flight_price = 0

            total_flight = 0

        # -----------------------

        if hotel_count > 0:

            fav_hotel = hotels["name"].mode()[0]

            avg_hotel_price = round(

                hotels["price"].mean(),

                2

            )

            total_hotel = round(

                hotels["total"].sum(),

                2

            )

        else:

            fav_hotel = "-"

            avg_hotel_price = 0

            total_hotel = 0

        total_spend = round(

            total_flight + total_hotel,

            2

        )

        return {

            "userCode": user_code,

            "name": name,

            "company": company,

            "gender": gender,

            "age": age,

            "flight_count": flight_count,

            "hotel_count": hotel_count,

            "fav_airline": fav_airline,

            "fav_destination": fav_destination,

            "fav_hotel": fav_hotel,

            "avg_flight": avg_flight_price,

            "avg_hotel": avg_hotel_price,

            "total_spend": total_spend

        }