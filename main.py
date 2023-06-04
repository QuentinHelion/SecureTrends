"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify
from flask_cors import CORS
from application.interfaces.presenters.rsspresenter import RSSPresenter

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
    presenter = RSSPresenter("https://krebsonsecurity.com/feed/")
    return jsonify({
        "title": presenter.get_feed_title()
    })


if __name__ == '__main__':
    app.run(debug=True)
