def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '10'
    else:
        s += '01'
    return int(s, 2)


n = 0
while True:
    r = f(n)
    if r > 102:
        break
    print(r)
    n += 1
