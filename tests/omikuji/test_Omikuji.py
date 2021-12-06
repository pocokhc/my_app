import pytest
from setting.Setting import Setting

from omikuji.Omikuji import Omikuji


@pytest.fixture(scope="class", autouse=True)
def setup():
    setting = Setting("test")
    print()
    yield (setting,)


def _Omikuji(omikuji):
    counter = [0 for _ in range(len(omikuji.probs))]
    N = 10000
    for _ in range(N):
        idx, _ = omikuji.getOmikuji()
        counter[idx] += 1
    counter = [x / N for x in counter]
    weights = [w / sum(omikuji.probs) for w in omikuji.probs]

    for k in range(len(weights)):
        r2 = abs(weights[k] - counter[k])
        assert r2 < 0.05, "{} weight:{} counter:{}".format(k, weights, counter)


def test_red(setup):
    setting = setup[0]
    _Omikuji(Omikuji(setting, "red"))


def test_blue(setup):
    setting = setup[0]
    _Omikuji(Omikuji(setting, "blue"))
