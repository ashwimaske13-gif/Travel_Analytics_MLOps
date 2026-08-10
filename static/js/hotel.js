document.addEventListener("DOMContentLoaded", function(){

    const city=document.getElementById("city");
    const hotel=document.getElementById("hotel");

    function update(){

        if(city.value=="" || hotel.value=="")
            return;

        fetch(`/hotel-info?city=${encodeURIComponent(city.value)}&hotel=${encodeURIComponent(hotel.value)}`)

        .then(res=>res.json())

        .then(data=>{

            document.getElementById("stars").value=data.stars;

            document.getElementById("reviews").value=data.reviews;

        });

    }

    city.addEventListener("change",update);

    hotel.addEventListener("change",update);

    update();

});