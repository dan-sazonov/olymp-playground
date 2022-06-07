def f(s):
    s = s // 7
    n = 11
    while s < 130:
        if (s + n) % 3 == 0:
            s = s + 7
        n = n + 13
    return n


s = 0
while True:
    if f(s) == 102:
        print(s)
        break
    s += 1
