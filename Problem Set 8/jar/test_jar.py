""" Från uppgiften jar från cs50 """

from jar import Jar
import pytest


def test_init():
    """
    This function tests the initialization of the Jar class.
    """
    jar = Jar(344)
    assert jar.size == 344
    with pytest.raises(ValueError):
        jar = Jar(-42)


def test_str():
    """
    This function tests the string representation of the Jar class.
    """
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    """
    Test the deposit method of the Jar class.
    """
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1337)


def test_withdraw():
    """
    Test the withdraw method of the Jar class.
    """
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(420)
