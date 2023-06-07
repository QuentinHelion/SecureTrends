"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from application.use_cases.save_article import SaveArticle
from application.use_cases.feed import Feed
from application.use_cases.scan_platforms import ScanPlatforms

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
    use_case = ScanPlatforms("platforms.json")
    return jsonify({
        "result": "ok"
    })



if __name__ == '__main__':
    app.run(debug=True)
