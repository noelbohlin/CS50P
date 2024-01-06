
from project import get_billboard_hot_100, get_imdb_top250, today, difficulty, get_word
from datetime import date


def test_get_billboard_hot_100():
    assert isinstance(get_billboard_hot_100(2013), list)

def test_get_imdb_top250():
    assert isinstance(get_imdb_top250(), list)

def test_today():
    assert today() == date.today().year


