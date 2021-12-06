import pytest
from setting.Setting import Setting


@pytest.fixture(scope="class", autouse=True)
def setup():
    setting = Setting("test")
    print()
    yield (setting,)


def test_ok(setup):
    setting = setup[0]
    assert True


def test_ng(setup):
    setting = setup[0]
    assert False
