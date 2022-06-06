def f(n):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    return int(s, 2)


n = 0
while True:
    r = f(n)
    if r > 83:
        print(r)
        break
    n += 1
