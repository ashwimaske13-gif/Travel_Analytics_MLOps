from flask import (
    Blueprint,
    request,
    jsonify
)

from api.schemas import (
    validate_flight_request
)

from api.predict import (
    FlightPricePredictor
)


api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


predictor = FlightPricePredictor()


@api.route(
    "/health",
    methods=["GET"]
)
def health_check():

    return jsonify({

        "status": "success",

        "message":
            "Travel Analytics REST API is running"

    }), 200


@api.route(
    "/predict/flight-price",
    methods=["POST"]
)
def predict_flight_price():

    try:

        data = request.get_json()

        if not data:

            return jsonify({

                "status": "error",

                "message":
                    "Request body must contain JSON data"

            }), 400

        flight_request = (
            validate_flight_request(data)
        )

        prediction = predictor.predict(

            travel_code=
                flight_request.travel_code,

            user_code=
                flight_request.user_code,

            source=
                flight_request.source,

            destination=
                flight_request.destination,

            flight_type=
                flight_request.flight_type,

            agency=
                flight_request.agency,

            day_of_week=
                flight_request.day_of_week,

            time=
                flight_request.time,

            distance=
                flight_request.distance,

            year=
                flight_request.year,

            month=
                flight_request.month,

            day=
                flight_request.day,

            week_of_year=
                flight_request.week_of_year
        )

        return jsonify({

            "status": "success",

            "prediction":
                round(prediction, 2),

            "currency": "USD"

        }), 200

    except ValueError as exc:

        return jsonify({

            "status": "error",

            "message": str(exc)

        }), 400

    except Exception as exc:

        return jsonify({

            "status": "error",

            "message":
                "Prediction failed",

            "details": str(exc)

        }), 500