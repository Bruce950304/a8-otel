import logging

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger("checkout")
logger.setLevel(logging.INFO)


@app.route("/checkout")
def checkout():
    logger.info("Payment started")
    logger.warning("Payment provider response was slow")
    return "paid\n"