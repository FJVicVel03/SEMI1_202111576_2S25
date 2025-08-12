from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check')
def check():
    return '', 200

@app.route('/info')
def info():
    return jsonify({
        "api": "Fernando Vicente 202111576",
        "version": "1.0",
        "author": "Tu Nombre",
        "language": "Python",
        "framework": "Flask"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# To run the application, use the command: python app.py
