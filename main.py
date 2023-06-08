"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from application.use_cases.feed import Feed
from application.use_cases.scan_platforms import ScanPlatforms

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()


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


@app.route('/rss', methods=['GET'])
def rss():
    """
    Return rss feed title
    """
    use_case = ScanPlatforms("platforms.json")
    if "platform" in request.args:
        result = use_case.scan_from(
            platform_title=request.args["platform"]
        )
    else:
        result = use_case.scan_all()
    return jsonify({
        "result": result
    })


def scan_all_job():
    """
    scan all platform job
    :return:
    """
    use_case = ScanPlatforms("./platforms.json")
    use_case.scan_all()


def schedule_task():
    """
    launch jobs
    :return:
    """
    print("execute scan job")
    scheduler.add_job(scan_all_job, 'cron', hour=0, minute=30)


if __name__ == '__main__':
    schedule_task()
    app.run(debug=False, host='0.0.0.0', port=5000)
