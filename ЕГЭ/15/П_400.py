def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 100_000):
        if not (f(120, a) and ((not f(x, a)) <= (f(x, 36) <= (not f(x, 15))))):
            break
    else:
        print(a)
    a += 1
