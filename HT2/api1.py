from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    data = {
        "api_name": "API 1",  # Este valor lo puedes personalizar
        "data": {
            "id": 1,
            "nombre": "Grupo 5 - Semi 1 - Api 1"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
