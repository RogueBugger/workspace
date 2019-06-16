function setup() {
    let latitude, longitude;
    const video = createCapture(VIDEO);
    video.size(320, 240);
    const button = document.getElementById("submit");
    button.addEventListener("click", async event => {
        video.loadPixels();
        const image64 = video.canvas.toDataURL();
        const name = document.getElementById("name").value;
        const data = {
            latitude,
            longitude,
            name,
            image64
        };
        const options = {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(data)
        };
        console.log(data);

        const response = await fetch("/api", options);
        const jsonData = await response.json();
    });
    if ("geolocation" in navigator) {
        console.log("geolocation is available");
        navigator.geolocation.getCurrentPosition(async position => {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            document.getElementById("latitude").textContent = latitude;
            document.getElementById("longitude").textContent = longitude;
        });
    } else {
        console.log("geolocation is unavailable");
    }
    noCanvas();
}