from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para todas las rutas

@app.route('/get-data', methods=['GET'])
def get_data():
    data = {
        "api_name": "API 2",
        "data": {
            "id": 1,
            "nombre": "Grupo 5 - Semi 1 - Api 2"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
