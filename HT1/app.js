const express = require('express');
const app = express();

app.get('/check', (req, res) => {
    res.sendStatus(200);
});

app.get('/info', (req, res) => {
    res.json({
        "Instancia": "Máquina 1 - API 1 (Express)",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo 5"
        // Uncomment and modify the following lines as needed
        // "api": "API Node.js",
        // "version": "1.0",
        // "author": "Tu Nombre",
        // "language": "JavaScript",
        // "framework": "Express"
    });
});

app.listen(5000, '0.0.0.0', () => {
    console.log('API corriendo en puerto 5000');
});
// To run the application, use the command: node app.js