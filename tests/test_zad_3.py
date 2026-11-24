import pytest

from zad_3 import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python", 2),
        ("AEIOUY", 6),
        ("bcd", 0),
        ("", 0),
        ("Próba żółwia", 5),
    ]
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
