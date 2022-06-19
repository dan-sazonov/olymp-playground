def f(n, from_base, to_base):
    n = int(str(n), from_base)
    s = ''
    while n > 0:
        s += str(n % to_base)
        n //= to_base
    return s[::-1]


n = 3 * 16**2018 - 2*8**1028 - 3*4**1100 - 2**1050 - 2022
print(f(n, 10, 4).count('3'))
