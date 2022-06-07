def f(x):
    n = 987
    while (x + n) // 1000 < 354261:
        x = x - 5
        n = n + 8
    return n // 1000


x = -100
c = 0
while True:
    print(x, f(x))
    if f(x) == 231:
        c += 1
        print(c)
    x += 1
