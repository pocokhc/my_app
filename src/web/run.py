import logging
import os
from logging import FileHandler, StreamHandler
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, send_from_directory

from .index import module1

DEBUG = True

# ------------------
# ログの設定
# ------------------
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(lineno)d [%(levelname)s] %(message)s")

if DEBUG:
    # debugはコンソールとファイルに出力、ファイルは都度初期化
    ch = StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logfile = os.path.join(os.path.dirname(__file__), "../../log/web/debug.log")
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    ch = FileHandler(logfile)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

else:
    # 本番はファイルをローテーションで保存
    # when=D,backupCount=30 は、過去1か月分のログを保存する
    logfile = os.path.join(os.path.dirname(__file__), "../../log/web/web.log")
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    ch = TimedRotatingFileHandler(logfile, when="D", backupCount=30)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


# ------------------
# flask
# ------------------
app = Flask(__name__)

app.register_blueprint(module1)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )
