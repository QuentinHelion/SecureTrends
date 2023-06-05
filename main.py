"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify
from flask_cors import CORS
from application.use_cases.krebon_sec import KrebonSec

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


@app.route('/rss', methods=['GET'])
def rss():
    """
    Return rss feed title
    """
    use_case = KrebonSec()
    return jsonify({
        "title": use_case.get_title(),
        "entries": use_case.get_feed()
    })


if __name__ == '__main__':
    app.run(debug=True)
