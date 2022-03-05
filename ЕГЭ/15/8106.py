def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 1000_000):
        if not ((not f(x, a)) <= (f(x,6) <= (not(f(x,4))))):
            break
    else:
        print(a)
    a += 1


