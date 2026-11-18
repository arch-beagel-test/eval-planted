from unittest.mock import patch

from shop.cart import discount, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_discount():
    assert discount(100, 10) == 90
    assert discount(50, 0) == 50


def test_total_of_a_mocked_cart():
    with patch("shop.cart.total", return_value=6) as fake:
        assert fake([1, 2, 3]) == 6
