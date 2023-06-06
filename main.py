"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify
from flask_cors import CORS
from application.use_cases.krebon_sec import KrebonSec
from application.use_cases.dark_reading import DarkReading
from application.use_cases.hacker_news import HackerNews
from application.use_cases.threat_post import ThreatPost
from application.use_cases.security_week import SecurityWeek

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


@app.route('/darkreading', methods=['GET'])
def darkreading():
    """
    Return rss feed title
    """
    use_case = DarkReading()
    return jsonify({
        "title": use_case.get_title(),
        "entries": use_case.get_feed()
    })


@app.route('/hackernews', methods=['GET'])
def hackernews():
    """
    Return rss feed title
    """
    use_case = HackerNews()
    return jsonify({
        "title": use_case.get_title(),
        "entries": use_case.get_feed()
    })


@app.route('/threatpost', methods=['GET'])
def threatpost():
    """
    Return rss feed title
    """
    use_case = ThreatPost()
    return jsonify({
        "title": use_case.get_title(),
        "entries": use_case.get_feed()
    })


@app.route('/securityweek', methods=['GET'])
def securityweek():
    """
    Return rss feed title
    """
    use_case = SecurityWeek()
    return jsonify({
        "title": use_case.get_title(),
        "entries": use_case.get_feed()
    })


if __name__ == '__main__':
    app.run(debug=True)
