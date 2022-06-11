def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


for i in range(2, 10):
    if len(f(30, 10, i)) == 3:
        print(f(30, 10, i), i)
