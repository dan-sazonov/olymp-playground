# F(0) = 0;
#
# F(n) = F(n / 2), если
# n > 0
# и
# при
# этом
# чётно;
#
# F(n) = 1 + F(n − 1), если
# n
# нечётно.
#
# Сколько
# существует
# таких
# чисел
# n, что
# 1 ≤ n ≤ 1000
# и
# F(n) = 3?


def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n / 2)
    elif n % 2 != 0:
        return 1 + f(n - 1)


c = 0
for i in range(1, 1001):
    if f(i) == 3:
        c += 1

print(c)
