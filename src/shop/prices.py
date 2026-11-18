PRICES = {"apple": 3, "pear": 4}


def lookup(name):
    return PRICES[name]


def in_dollars(name):
    return lookup(name) / 100
