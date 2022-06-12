def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    return a, b


x = 0
c = 0
while True:
    if f(x) == (2, 0):
        c += 1
        print(c)
    x += 1
