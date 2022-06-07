def f(s):
    n = 6
    while s <= 154:
        s = s + 12
        n = n + 3
    return n


s = 0
while True:
    if f(s) == 42:
        print(s)
    s += 1
