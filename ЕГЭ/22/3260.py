def f(x):
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if (M < x) and ((x % 2) == 0):
            M = x % 10
        x = x // 10
    return L, M


x = 0
while True:
    if f(x) == (3, 8):
        print(x)
        break
    x += 1
