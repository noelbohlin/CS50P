# Från uppgiften Refuel från CS50

from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/34234") == 0


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_valueerror():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("cat/dog")


def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
