""" Från uppgiften Um från CS50 """

import pytest
from um import count


def test_word():
    """
    This function tests the count function with the word "yummy".
    """
    assert count("yummy") == 0


def test_characters():
    """
    This function tests the count function with different cases of characters.
    """
    assert count("um, hi gummy") == 1
    assert count("UM, hi guMmy") == 1


def test_count():
    """
    This function tests the count function with a string containing multiple instances of "um".
    """
    assert count("um, hello, um, world, um.") == 3
