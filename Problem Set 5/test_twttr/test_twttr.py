""" från uppgiften testing my twitter från Cs50 """

from twttr import shorten


def test_string():
    """
    Tests the shorten function with various inputs.
    """
    assert shorten("twitter") == "twttr"
    assert shorten("Just sEtting up my Twitter") == "Jst sttng p my Twttr"
    assert shorten("2024") == "2024"
    assert shorten("hE!!0") == "h!!0"
    assert shorten(",.-hej,.-") == ",.-hj,.-"
