from seasons import convert
import pytest

def test_seasons():
    assert convert(2003, 5, 31) == "Ten million, eight hundred thirty-three thousand, one hundred twenty minutes"

    with pytest.raises(ValueError):
        convert(23, 23, 3233)
