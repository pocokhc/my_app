import logging
import warnings


def set_logger(name: str = "", level=logging.DEBUG) -> None:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(lineno)d [%(levelname)s] %(message)s")

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # ライブラリ別にログレベルを調整
    # logging.getLogger("matplotlib").setLevel(logging.INFO)

    # 余分なwarningを非表示
    warnings.simplefilter("ignore")
