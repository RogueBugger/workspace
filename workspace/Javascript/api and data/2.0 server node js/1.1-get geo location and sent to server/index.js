const express = require("express");
const app = express();
const Datastore = require("nedb");

app.listen(8080, () => console.log("listening at 8080"));
app.use(express.static("public"));
app.use(express.json({ limit: "1mb" }));

const database = new Datastore("database.db");
database.loadDatabase();

app.get("/api", (request, response) => {
    database.find({}, (error, data) => {
        response.json(data);
    });
});

app.post("/api", (request, response) => {
    const timestamp = Date.now();
    const data = request.body;
    data.timestamp = timestamp;
    console.log("got a request");
    database.insert(data);
    response.json(data);
});