from math import gcd

m, a = map(int, input().split())


def phi(n):
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            res -= res // p
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        res -= res // n
    return res


print(pow(a, phi(m) - 1, m) if gcd(m, a) == 1 else -1)
