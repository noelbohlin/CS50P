""" från uppgiften working från cs50 """

from working import convert
import pytest


def test_conversion():
    """
    Tests the conversion of time strings from 12-hour format to 24-hour format.
    """
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 8:45 PM") == "00:00 to 20:45"
    assert convert("12 PM to 1 AM") == "12:00 to 01:00"


def test_valueerror():
    """
    Tests if ValueError is raised correctly.
    """
    with pytest.raises(ValueError):
        convert("14 AM to 3 PM")
    with pytest.raises(ValueError):
        convert("10 AM 3 PM")
