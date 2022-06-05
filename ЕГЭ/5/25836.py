def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '00'
    else:
        s += '11'
    return int(s, 2)


n = 0
while True:
    r = f(n)
    if r >= 134:
        break
    print(n)
    n += 1
