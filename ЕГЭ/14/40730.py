def calc(x, a, b):
    x = int(str(x), a)
    s = ''

    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1].lstrip('0')


num = 3 * 125 ** 6 + 2 * 25 ** 9 + 5 ** 12 - 625
print(calc(num, 10, 5).count('0'))
