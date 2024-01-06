# från uppgiften Back to the Bank från CS50

from bank import value


def test_hello():
    assert value("hEllO, Newman!!") == 0
def test_startwith_h():
    assert value("Hooja, Newman!!") == 20
def test_no_greeting():
    assert value("Good Day, Newman") == 100


