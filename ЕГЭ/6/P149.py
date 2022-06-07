def f(x):
    s = 12 * (x // 10)
    n = 1
    while s < 300:
        s = s + 25
        n = n * 2
    return n


x = 1
c = 0
while True:
    if f(x) > 500:
        c += 1
        print(c)
    x += 1
