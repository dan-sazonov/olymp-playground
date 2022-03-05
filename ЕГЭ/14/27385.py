def calc(x, a, b):
    x = int(str(x), a)
    s = ''

    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1].lstrip('0')


num = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21

print(len(set(calc(num, 10, 7))))
