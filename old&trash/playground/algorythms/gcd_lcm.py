import math


def gcd_iter(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd_recursion(a, b):
    if b == 0:
        return a
    return gcd_recursion(b, a % b)


def lcm_bike(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


print(gcd_iter(36, 24))  # 12
print(gcd_recursion(36, 24))  # 12
print(lcm_bike(36, 24))  # 72
print(lcm(36, 24))  # 72
