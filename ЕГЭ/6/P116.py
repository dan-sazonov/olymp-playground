def f(d):
    n = 1
    while d // n > 0:
        d = d - 2
        n = n + 3
    return n


d = 0
while True:
    if f(d) == 46:
        print(d)
    d += 1
