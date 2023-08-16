import logger
import git
import os
import messages
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/')
def root():
    logger.info("Alive and kicking!")
    return 'Alive and kicking!'


@app.route("/webhook/<webhook>", methods=["GET", "POST"])
def get_webhook(webhook):
    if os.environ["WEBHOOK"] != webhook:
        logger.error("Incorrect webhook")
        return "KO", 404
    try:
        if request.method == "GET" or not request.json:
            logger.warning("Correct webhook but without post")
            return "OK", 200
    except Exception:
        return "OK", 200

    logger.info("Correct webhook with post")
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


if __name__ == '__main__':
    app.run(debug=True, port=443)