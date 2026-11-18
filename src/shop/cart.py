def total(prices):
    return sum(p for p in prices if p > 0)


def discount(amount, percent):
    return amount - amount * percent / 100
