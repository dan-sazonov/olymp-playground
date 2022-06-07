def f(s):
    s = s // 5
    n = 8
    while s < 156:
        if (s + n) % 3 == 0:
            s = s + 6
        n = n + 11
    return n


s = 0
while True:
    if f(s) == 140:
        print(s)
    s += 1
