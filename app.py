from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check')
def check():
    return '', 200

@app.route('/info')
def info():
    return jsonify({
        "Instancia": "Máquina 1 - API 1 (Flask)",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo 5"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# To run the application, use the command: python app.py
