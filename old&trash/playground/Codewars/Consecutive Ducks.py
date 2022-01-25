from math import log2


def consecutive_ducks(n):
    return int(log2(n)) != log2(n)
