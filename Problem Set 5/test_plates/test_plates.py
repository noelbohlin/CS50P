""" Från uppgiften Test Plates från CS50 """

from plates import is_valid


def test_beginning():
    assert is_valid("CS50")
    assert not is_valid("50CS")
    assert not is_valid("5CSP")
    assert not is_valid("D2SDFD")


def test_length():
    assert is_valid("CS50")
    assert not is_valid("COMPUTER")
    assert not is_valid("S")


def test_alnumcharacters():
    assert is_valid("CS50")
    assert not is_valid("C$5@!")
    assert not is_valid("CS.50")


def test_numberplacement():
    assert is_valid("CS50")
    assert not is_valid("CS50P")
    assert not is_valid("CS05")
    assert not is_valid("400")
