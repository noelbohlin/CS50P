""" från uppgiften Back to the Bank från CS50 """

from bank import value

def test_hello():
    """
    This function tests the case where the input string starts with "hEllO".
    """
    assert value("hEllO, Newman!!") == 0

def test_startwith_h():
    """
    This function tests the case where the input string starts with "Hooja".
    """
    assert value("Hooja, Newman!!") == 20

def test_no_greeting():
    """
    This function tests the case where there is no greeting in the input string.
    """
    assert value("Good Day, Newman") == 100
