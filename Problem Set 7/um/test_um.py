import pytest
from um import count

def test_word():
    assert count("yummy") == 0

def test_characters():
    assert count("um, hi gummy") == 1
    assert count("UM, hi guMmy") == 1


def test_count():
    assert count("um, hello, um, world, um.") == 3
