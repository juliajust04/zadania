import pytest

from zad_4 import calculate_discount


@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 0.2, 80.0),
        (50, 0, 50.0),
        (200, 1, 0.0),
    ]
)
def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == expected


@pytest.mark.parametrize("discount", [-0.1, 1.5])
def test_invalid_discount(discount):
    with pytest.raises(ValueError):
        calculate_discount(100, discount)