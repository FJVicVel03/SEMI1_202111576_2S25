const express = require('express');
const app = express();

app.get('/check', (req, res) => {
    res.sendStatus(200);
});

app.get('/info', (req, res) => {
    res.json({
        api: "API Node.js",
        version: "1.0",
        author: "Tu Nombre",
        language: "JavaScript",
        framework: "Express"
    });
});

app.listen(5000, '0.0.0.0', () => {
    console.log('API corriendo en puerto 5000');
});
// To run the application, use the command: node app.js