""" från uppgiften Seasons från cS50 """

from seasons import convert
import pytest


def test_seasons():
    """
    Tests the functionality of the convert function.
    """
    assert (
        convert(2003, 5, 31)
        == "Ten million, eight hundred thirty-three thousand, one hundred twenty minutes"
    )
    with pytest.raises(ValueError):
        convert(23, 23, 3233)
