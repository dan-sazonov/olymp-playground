from functools import lru_cache


# F(0) = 0;
#
# F(n) = F(n / 2), если n > 0 и при этом n чётно;
#
# F(n) = 1 + F(n − 1), если n нечётно.

@lru_cache
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    if n % 2 != 0:
        return 1 + f(n - 1)


n = 0
while True:
    if f(n) == 12:
        print(n)
        break
    n += 1
