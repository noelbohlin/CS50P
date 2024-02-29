""" Från uppgiften jar från cs50 """

from jar import Jar
import pytest


def test_init():
    jar = Jar(344)
    assert jar.size == 344
    with pytest.raises(ValueError):
        jar = Jar(-42)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1337)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(420)
