def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


for x in range(1000):
    n = 216 ** 5 + 6 ** 3 - 1 - x
    if f(n, 10, 6).count('5') == 12:
        print(x)
