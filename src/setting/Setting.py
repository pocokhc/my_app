import os
import random

import yaml


class Setting:
    def __init__(self, name: str):
        if name == "test":
            fn = "setting_test.yml"
        elif name == "web":
            fn = "setting_web.yml"
        else:
            raise ValueError()

        path = os.path.join(os.path.dirname(__file__), "../../setting", fn)
        with open(path) as f:
            self.data = yaml.safe_load(f)

        # データルートディレクトリ
        self.data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))

        # tmp
        self.tmp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tmp"))

        # 乱数の初期化
        if self.data["SEED"] is not None:
            random.seed(self.data["SEED"])
