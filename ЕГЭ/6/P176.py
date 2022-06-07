def f(s):
    s = s // 11
    n = 9
    while s < 203:
        if (s + n) % 5 == 0:
            s = s + 6
        n = n + 3
    return n


s = 0
c = 0
while True:
    if f(s) == 126:
        c += 1
        print(c)
    s += 1
