import logging
import os

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger("checkout")
logger.setLevel(logging.INFO)


@app.route("/checkout")
def checkout():
    logger.info("Payment started")
    logger.warning("Payment provider response was slow")
    return "paid\n"


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="127.0.0.1", port=5000, debug=True)
