const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const fetch = require("node-fetch");
const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.post("/submit", (req, res) => {
  const { name, email } = req.body;

  fetch("http://backend-host:8080/process", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email }),
  })
    .then((response) => response.json())
    .then((data) => {
      res.send(`<h1>${data.message}</h1>`);
    })
    .catch((err) => {
      console.error("Error submitting form:", err);
      res.status(500).send("Something went wrong!");
    });
});

app.listen(PORT, () => {
  console.log(`Frontend server running at http://localhost:${PORT}`);
});
