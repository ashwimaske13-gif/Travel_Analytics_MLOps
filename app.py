from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify

from src.utils.flight_lookup import FlightLookup
from src.utils.hotel_lookup import HotelLookup
from src.utils.user_lookup import UserLookup
from src.utils.gender_lookup import GenderLookup
from src.config import RAW_DATA_DIR

import pandas as pd
import joblib
from datetime import datetime

from src.config import MODELS_DIR
from src.config import ARTIFACTS_DIR

from src.utils.flight_lookup import FlightLookup

app = Flask(__name__)

app.secret_key = "travel_partner_secret"


# ----------------------------------------------------
# LOGIN
# ----------------------------------------------------

USERNAME = "admin"
PASSWORD = "admin123"


# ----------------------------------------------------
# LOAD MODEL
# ----------------------------------------------------

model = joblib.load(
    MODELS_DIR / "flight_price_model.pkl"
)

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

scaler = joblib.load(
    ARTIFACTS_DIR / "flight_scaler.pkl"
)


lookup = FlightLookup()
hotel_lookup = HotelLookup()
user_lookup = UserLookup()
gender_lookup = GenderLookup()

# =====================================================
# LOGIN
# =====================================================
@app.route("/route-info")
def route_info():

    source = request.args.get("from")

    destination = request.args.get("to")

    result = lookup.get_route(source, destination)

    return jsonify(result)

@app.route("/")
def root():

    if "user" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username

            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")

# =====================================================
# GENDER PREDICTION
# =====================================================

@app.route("/gender", methods=["GET", "POST"])
def gender():

    if "user" not in session:
        return redirect(url_for("login"))

    prediction = None

    if request.method == "POST":

        name = request.form["name"]

        company = request.form["company"]

        age = int(
            request.form["age"]
        )

        prediction = gender_lookup.predict_gender(
            name,
            company,
            age
        )

    return render_template(
        "gender.html",
        companies=gender_lookup.get_companies(),
        prediction=prediction
    )

# =====================================================
# FLIGHT PAGE
# =====================================================

@app.route("/flight")
def flight():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
    "flight.html",
    from_cities=lookup.get_from_cities(),
    to_cities=lookup.get_to_cities(),
    airlines=lookup.get_airlines(),
    flight_types=lookup.get_flight_types()
)


# =====================================================
# HOTEL PAGE
# =====================================================

@app.route("/hotel")
def hotel():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
    "hotel.html",
    cities=hotel_lookup.get_cities(),
    hotels=hotel_lookup.get_hotels()
    )

# =====================================================
# USER ANALYTICS
# =====================================================

@app.route("/user", methods=["GET", "POST"])
def user():

    if "user" not in session:
        return redirect(url_for("login"))

    summary = None

    if request.method == "POST":

        user_code = int(request.form["userCode"])

        summary = user_lookup.get_user_summary(
            user_code
        )

    return render_template(
        "user.html",
        summary=summary
    )

# =====================================================
# MLFLOW
# =====================================================

@app.route("/mlflow")
def mlflow_dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "mlflow.html"
    )
    
    
# =====================================================
# MLOPS PIPELINE
# =====================================================

@app.route("/pipeline")
def mlops_pipeline():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "pipeline.html"
    )

# =====================================================
# PRICE PREDICTION
# =====================================================

@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect(url_for("login"))

    travel_code = int(request.form["travelCode"])

    user_code = int(request.form["userCode"])

    source = request.form["from"]

    destination = request.form["to"]

    flight_type = request.form["flightType"]

    agency = request.form["agency"]


    # ---------------------------------------
    # Automatically Calculate
    # ---------------------------------------

    route = lookup.get_route_details(
        source,
        destination
    )

    distance = route["distance"]

    time = route["time"]

    today = datetime.today()

    year = today.year

    month = today.month

    day = today.day

    weekday = today.strftime("%A")

    week = today.isocalendar()[1]


    # ---------------------------------------

    encoded_source = from_encoder.transform([source])[0]

    encoded_destination = to_encoder.transform([destination])[0]

    encoded_type = flight_encoder.transform([flight_type])[0]

    encoded_agency = agency_encoder.transform([agency])[0]

    encoded_day = day_encoder.transform([weekday])[0]


    data = pd.DataFrame([[
        travel_code,
        user_code,
        encoded_source,
        encoded_destination,
        encoded_type,
        time,
        distance,
        encoded_agency,
        year,
        month,
        day,
        encoded_day,
        week
    ]],

    columns=[
        "travelCode",
        "userCode",
        "from",
        "to",
        "flightType",
        "time",
        "distance",
        "agency",
        "year",
        "month",
        "day",
        "day_of_week",
        "week_of_year"
    ])

    numeric = [
        "time",
        "distance",
        "year",
        "month",
        "day",
        "week_of_year"
    ]

    data[numeric] = scaler.transform(data[numeric])

    prediction = round(model.predict(data)[0], 2)

    return render_template(

        "flight.html",

        prediction=prediction,

        distance=distance,

        time=time,

        booking_id=f"TP-{travel_code}{user_code}",

        from_cities=lookup.get_from_cities(),

        to_cities=lookup.get_to_cities(),

        airlines=lookup.get_airlines(),

        flight_types=lookup.get_flight_types()

    )

# =====================================================
# HOTEL RECOMMENDATION
# =====================================================

@app.route("/hotel-recommend", methods=["POST"])
def hotel_recommend():

    if "user" not in session:
        return redirect(url_for("login"))

    user_code = int(request.form["userCode"])

    city = request.form["city"]

    top_n = int(request.form["top_n"])

    recommendations = hotel_lookup.recommend_hotels(
        user_code=user_code,
        city=city,
        top_n=top_n
    )

    return render_template(

        "hotel.html",

        cities=hotel_lookup.get_cities(),

        recommendations=recommendations

    )

# =====================================================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )