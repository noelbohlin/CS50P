from datetime import date
from project import get_billboard_hot_100, get_imdb_top250, today


def test_get_billboard_hot_100():
    """ test that list is returned at all"""
    assert isinstance(get_billboard_hot_100(2013), list)


def test_get_imdb_top250():
    """ test that list is returned at all"""
    assert isinstance(get_imdb_top250(), list)


def test_today():
    """ test that date is returned at all"""
    assert today() == date.today().year


