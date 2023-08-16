import time
import git
import os
import messages
import logging
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


def logger(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print("{} | {}\n".format(timestamp, text))


@app.route('/')
def root():
    logging.info("Alive and kicking!")
    return 'Alive and kicking!'


@app.route("/webhook/<webhook>", methods=["GET", "POST"])
def get_webhook(webhook):
    if os.environ["WEBHOOK"] != webhook:
        logging.error("Incorrect webhook")
        return "KO", 404
    try:
        if request.method == "GET" or not request.json:
            logging.warning("Correct webhook but without post")
            return "OK", 200
    except Exception:
        return "OK", 200

    logging.info("Correct webhook with post")
    messages.message_received(request.json)
    return "OK", 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./mordiMurBot")
    origin = repo.remotes.origin
    repo.create_head("main",
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "", 200
