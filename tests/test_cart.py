from unittest.mock import patch

from shop.cart import discount, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_discount():
    assert discount(100, 10) == 90
    assert discount(50, 0) == 50


def test_total_of_looked_up_prices():
    with patch("shop.prices.lookup", return_value=3):
        assert total([3, 3]) == 6
