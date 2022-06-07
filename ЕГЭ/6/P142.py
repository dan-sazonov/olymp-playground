def f(s):
    n = 1
    while s > 200:
        s = s - 15
        n = n + 3
    return n


s = 0
while True:
    if f(s) == 46:
        print(s)
    s += 1
