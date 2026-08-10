document.addEventListener("DOMContentLoaded", function () {

    const fromCity = document.getElementById("from");
    const toCity = document.getElementById("to");

    const time = document.getElementById("time");
    const distance = document.getElementById("distance");

    const departure = document.getElementById("departureDate");

    function updateRoute() {

        const from = fromCity.value;
        const to = toCity.value;

        if (!from || !to)
            return;

        fetch(`/route-info?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}`)
            .then(response => response.json())
            .then(data => {

                time.value = data.time;
                distance.value = data.distance;

            });

    }

    fromCity.addEventListener("change", updateRoute);
    toCity.addEventListener("change", updateRoute);

    departure.addEventListener("change", function () {

        const date = new Date(this.value);

        if (!this.value)
            return;

        document.getElementById("year").value = date.getFullYear();

        document.getElementById("month").value = date.getMonth() + 1;

        document.getElementById("day").value = date.getDate();

        const days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ];

        document.getElementById("day_of_week").value =
            days[date.getDay()];

        const start = new Date(date.getFullYear(), 0, 1);

        const diff = date - start;

        const week =
            Math.ceil(diff / (1000 * 60 * 60 * 24 * 7));

        document.getElementById("week_of_year").value = week;

    });

    updateRoute();

});