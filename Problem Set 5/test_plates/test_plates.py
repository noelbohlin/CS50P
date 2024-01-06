# Från uppgiften Test Plates från CS50

from plates import is_valid

def test_beginning():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("5CSP") == False
    assert is_valid("D2SDFD") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("COMPUTER") == False
    assert is_valid("S") == False

def test_alnumcharacters():
    assert is_valid("CS50") == True
    assert is_valid("C$5@!") == False
    assert is_valid("CS.50") == False

def test_numberplacement():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("400") == False
