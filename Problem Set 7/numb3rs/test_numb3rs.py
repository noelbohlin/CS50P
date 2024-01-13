from numb3rs import validate


def test_length():
    assert validate("10.135.125.5")
    assert not validate("1.1.1")
    assert not validate("1.1.1.1.1")
    assert not validate("ipaddress")
    assert not validate("512.512.512.512.512")


def test_range():
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")
    assert not validate("256.10.10.10")
    assert not validate("999.999.999.999")
    assert not validate("-1.10.-10.10")
    assert not validate("10.10.10.256")
