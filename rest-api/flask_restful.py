from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        "id": 1,
        "name": "Rafael Marques",
        "lang": "python"
    },
    {
        "id": 2,
        "name": "John Doe",
        "lang": "node.js"
    },
    {
        "id": 3,
        "name": "Robert Baratheon",
        "lang": "javascript"
    },
    {
        "id": 4,
        "name": "John Snow",
        "lang": "python"
    }
]
@app.route("/devs", methods=['GET'])
def home():
    return jsonify(devs), 200

@app.route("/devs/<string:lang>", methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200

@app.route("/devs/<int:id>", methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({'error': 'not found'}), 404

@app.route("/devs", methods=['POST'])
def save_dev():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)