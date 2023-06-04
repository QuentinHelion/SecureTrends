"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost"]}})


@app.route('/ping', methods=['GET'])
def ping():
    """
    Return pong
    """
    return jsonify({
        "result": "pong"
    })


if __name__ == '__main__':
    app.run(debug=True)
