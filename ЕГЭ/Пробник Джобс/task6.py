def f(s):
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    return n


s = 0
while True:
    if f(s) == 8:
        print(s)
        break
    s += 1
