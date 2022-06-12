def f(x):
    a, b, = 0, 1
    while x > 0:
        a += 1
        b = b * (x % 10)
        x //= 10
    return a, b


x = 0
c = 0
while True:
    if f(x) == (2, 24):
        c += 1
        print(c)
    x += 1
