getData();
async function getData() {
    const response = await fetch("/api");
    const data = await response.json();

    for (item of data) {
        const main = document.createElement("p");
        const geolocation = document.createElement("div");
        const time = document.createElement("div");
        const weather = document.createElement('div');
        const summary = document.createElement('div');
        weather.textContent = `Humidity = ${item.humidity}, temperature = ${item.temperature}`
        summary.textContent = `summary = ${item.summary}`;
        geolocation.textContent = `latitude = ${item.latitude}, longitude = ${item.longitude}`;
        const timestring = new Date(item.timestamp).toLocaleString();
        time.textContent = `Time =  ${timestring}`;
        main.append(time, geolocation, weather, summary);
        document.body.append(main);
    }
}