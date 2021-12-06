import logging

from flask import Blueprint, abort, render_template, request
from omikuji.Omikuji import Omikuji
from setting.Setting import Setting

logger = logging.getLogger(__name__)


module1 = Blueprint("module1", __name__)


@module1.route("/")
def index():
    return render_template("index.html")


@module1.route("/omikuji", methods=["POST"])
def omikuji():
    logger.debug(request.form)
    setting = Setting("web")

    # omikuji_type
    omikuji_type = request.form.get("type", "")
    if omikuji_type not in Omikuji.PROB_TBL:
        logger.warning(f"Unkown omikuji_type: {omikuji_type}")
        abort(410)

    # おみくじを引く
    omikuji = Omikuji(setting, omikuji_type)
    _, result = omikuji.getOmikuji()
    logger.debug(f"omikuji result: {result}")

    return result
