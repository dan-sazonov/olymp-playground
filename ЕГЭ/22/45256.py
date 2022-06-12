def f(x):
    q = 8
    p = 10
    k1 = 0
    k2 = 0
    while x <= 100:
        k1 += 1
        x += p
    while x >= q:
        k2 += 1
        x -= q
    l = x + k1
    m = x + k2
    return l, m


x = 0
while True:
    if f(x) == (12, 19):
        print(x)
    x += 1
