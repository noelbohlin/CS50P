""" Från uppgiften Test Plates från CS50 """

from plates import is_valid


def test_beginning():
    """
    This function tests the beginning of the plate number.
    """
    assert is_valid("CS50")
    assert not is_valid("50CS")
    assert not is_valid("5CSP")
    assert not is_valid("D2SDFD")


def test_length():
    """
    This function tests the length of the plate number.
    """
    assert is_valid("CS50")
    assert not is_valid("COMPUTER")
    assert not is_valid("S")


def test_alnumcharacters():
    """
    This function tests whether the characters in the plate number are alphanumeric.
    """
    assert is_valid("CS50")
    assert not is_valid("C$5@!")
    assert not is_valid("CS.50")


def test_numberplacement():
    """
    This function tests the placement of numbers in the plate number.
    """
    assert is_valid("CS50")
    assert not is_valid("CS50P")
    assert not is_valid("CS05")
    assert not is_valid("400")
