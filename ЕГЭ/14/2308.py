def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


for i in range(31):
    s = f(i, 10, 5)
    if s and s[0] == '3':
        print(i)
