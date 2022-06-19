def f(s):
    p = 10
    q = 8
    k1 = k2 = 0

    while s <= 100:
        s = s + p
        k1 = k1 + 1

    while s >= q:
        s = s - q
        k2 = k2 + 1
    k1 += s
    k2 += s

    return k1, k2


s = 0
while True:
    if f(s) == (10, 19):
        print(s)

    s += 1
