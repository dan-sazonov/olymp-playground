def f(x):
    s = 5 * (x // 10)
    n = 1
    while s < 300:
        s = s + 28
        n = n * 3
    return n


x = 1
c = 0
while True:
    if f(x) == 243:
        c += 1
        print(c)
    x += 1
