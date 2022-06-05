def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        s = n + '00'
    else:
        s = n + '11'
    return int(s, 2)


n = 0
while True:
    r = f(n)
    if r > 114:
        print(r)
        break
    n += 1
