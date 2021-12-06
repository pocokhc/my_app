import logging
import random

from setting.Setting import Setting

logger = logging.getLogger(__name__)


class SimpleChoiceByWeight:
    # 重み付き乱択アルゴリズム(https://qiita.com/pocokhc/items/a8f0281d54e1de7d3a30)

    def setWeight(self, weights: list[float]) -> None:
        self.weights = weights
        self.weight_sum = sum(weights)

    def choice(self) -> int:
        r = random.random() * self.weight_sum

        num = 0
        for i, weight in enumerate(self.weights):
            num += weight
            if r <= num:
                return i

        # not comming
        return -1


class Omikuji:

    # 各おみくじの確率テーブル
    PROB_TBL = {
        "red": [
            ["大吉", 0.2],
            ["中吉", 0.2],
            ["吉", 0.2],
            ["凶", 0.2],
            ["大凶", 0.2],
        ],
        "blue": [
            ["大吉", 0.05],
            ["中吉", 0.2],
            ["吉", 0.5],
            ["凶", 0.2],
            ["大凶", 0.05],
        ],
    }

    @staticmethod
    def getKeys() -> list[str]:
        return list(Omikuji.PROB_TBL.keys())

    def __init__(self, setting: Setting, type_: str):
        self.setting = setting

        # テーブルを扱いやすいデータ形式に変換
        self.probs = [t[1] for t in Omikuji.PROB_TBL[type_]]
        self.vals = [t[0] for t in Omikuji.PROB_TBL[type_]]
        logger.debug(self.probs)
        logger.debug(self.vals)

    def getOmikuji(self) -> tuple[int, str]:
        selector = SimpleChoiceByWeight()
        selector.setWeight(self.probs)
        idx = selector.choice()
        result = self.vals[idx]
        logger.debug(f"omikuji: {idx} {result}")
        return idx, result
