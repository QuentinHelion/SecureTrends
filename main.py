"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from application.use_cases.krebon_sec import KrebonSec
from application.interfaces.controllers.platform_rss_controller import PlatformRssController
from application.use_cases.hacker_news import HackerNews
from application.use_cases.threat_post import ThreatPost
from application.use_cases.security_week import SecurityWeek
from application.use_cases.save_article import SaveArticle
from application.use_cases.feed import Feed

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


@app.route('/feed', methods=['GET'])
def feed():
    """
    Return feed of last day
    """
    use_case = Feed()
    if "platform" in request.args and "interval" in request.args:
        return jsonify({
            "result": use_case.get_feed_from_to(
                interval=request.args["interval"],
                platform=request.args["platform"]
            )
        })
    if "platform" in request.args:
        return jsonify({
            "result": use_case.get_feed_from(
                platform=request.args["platform"]
            )
        })
    if "interval" in request.args:
        return jsonify({
            "result": use_case.get_feed_to(
                interval=request.args["interval"]
            )
        })
    return jsonify({
        "result": use_case.get_feed()
    })


@app.route('/test', methods=['GET'])
def test():
    """
    Return rss feed title
    """
    use_case = SaveArticle()
    return jsonify({
        "result": use_case.save({
            "title": "t_title_4",
            "platform": "t_platform",
            "link": "t_link",
            "summary": "t_summary"
        })
    })


@app.route('/rm', methods=['GET'])
def remove_article():
    """
    Return rss feed title
    """
    use_case = SaveArticle()
    return jsonify({
        "result": use_case.remove({
            "title": "t_title_4",
            "platform": "t_platform"
        })
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
