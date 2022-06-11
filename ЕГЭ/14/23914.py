def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


n = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
print(f(n, 10, 3).count('2'))
