# 49**7 · 7**20 − 7**8 − 28

def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


x = 49 ** 7 * 7 ** 20 - 7 ** 8 - 28
s = f(x, 10, 7).count('6')
print(s)
