def f(x):
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if (x % 2) != 0:
            M = M + x % 8
        x = x // 8
    return (L, M)


x = 0
while True:
    x += 1
    if f(x) == (3, 6):
        print(x)
