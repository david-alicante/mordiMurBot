import time
import sys
import git
import os
import messages
from flask import Flask, jsonify, make_response, request


app = Flask(__name__)
port = int(os.environ["PORT"])


def logger(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    sys.stdout.write("{} | {}\n".format(timestamp, text))


@app.route("/status", methods=["GET"])
def get_status():
    return "Up and running", 201


@app.route("/webhook/<webhook>", methods=["GET", "POST"])
def get_webhook(webhook):
    logger(webhook)
    if os.environ["WEBHOOK"] != webhook:
        return "KO", 404
    try:
        if request.method == "GET" or not request.json:
            return "OK", 200
    except Exception:
        return "OK", 200
    messages.message_received(request.json)
    return "OK", 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./mordiMurBot")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "", 200


if __name__ == '__main__':
    app.run(debug=True, port=port)


