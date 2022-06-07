def f(s):
    s = (s + 31) // 26
    n = 813
    while s > 0:
        n = n // 3
        s = s - n
    return n

s = 0
while True:
    # print(f(s))
    if f(s) == 30:
        print(s)
        break
    s += 1
