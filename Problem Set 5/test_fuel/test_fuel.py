""" Från uppgiften Refuel från CS50 """

from fuel import convert, gauge
import pytest


def test_convert():
    """
    Tests the convert function with various inputs.

    Asserts that the function correctly converts fractions to percentages.
    """
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/34234") == 0


def test_gauge():
    """
    Tests the gauge function with various inputs.

    Asserts that the function correctly converts percentage values to string representations.
    """    
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_valueerror():
    """
    Tests the convert function with invalid inputs.

    Asserts that the function raises a ValueError when given invalid inputs.
    """
    with pytest.raises(ValueError):
        convert("5/4")
        convert("cat/dog")


def test_zerodivisionerror():
    """
    Tests the convert function with division by zero.

    Asserts that the function raises a ZeroDivisionError when trying to divide by zero.
    """
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
