def f(x):
    l = 0
    m = 1
    while x > 0:
        l += 1
        if x % 2 > 0:
            m *= x % 8
        x = x // 8
    return m, l


x = 0
while True:
    if f(x) == (25, 3):
        print(x)
    x += 1
