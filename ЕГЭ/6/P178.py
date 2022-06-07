def f(s):
    s = s // 15
    n = 14
    while s < 285:
        if (s + n) % 9 == 0:
            s = s + 11
        n = n + 13
    return n


s = 0
c = 0
while True:
    if f(s) == 118:
        c += 1
        print(c)
    s += 1