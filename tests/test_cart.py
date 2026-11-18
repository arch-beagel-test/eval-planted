from shop.cart import discount, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_discount():
    assert discount(100, 10) == 90
    assert discount(50, 0) == 50
