def d(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 10000):
        if not ((d(x, 3) <= (not (d(x, 5)))) or (x + a >= 70)):
            break
    else:
        print(a)
        break
    a += 1
