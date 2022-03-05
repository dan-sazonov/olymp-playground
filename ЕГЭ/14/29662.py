def calc(x, a, b):
    x = int(str(x), a)
    s = ''

    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


num = 81 ** 17 + 3 ** 24 - 45
print(calc(num, 10, 9).count('8'))
