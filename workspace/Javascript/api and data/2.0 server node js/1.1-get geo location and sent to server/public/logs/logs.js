getData();
async function getData() {
    const response = await fetch("/api");
    const data = await response.json();

    for (item of data) {
        const main = document.createElement("div");
        const geolocation = document.createElement("div");
        const name = document.createElement("div");
        const time = document.createElement("div");
        const linebreak = document.createElement("br");
        const image = document.createElement("img");
        image.src = item.image64;

        geolocation.textContent = `${item.latitude}, ${item.longitude}`;
        name.textContent = `name : ${item.name}`;
        const timestring = new Date(item.timestamp).toLocaleString();
        time.textContent = timestring;
        main.append(image, linebreak, geolocation, name, time);
        document.body.append(main);
    }
}