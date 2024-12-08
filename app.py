from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hola Mundo"})

if __name__ == '__main__':
    app.run(debug=True)
