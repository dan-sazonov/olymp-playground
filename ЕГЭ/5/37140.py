def f(n):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = f'1{s}0'
    else:
        s = f'11{s}11'

    return int(s, 2)


n = 0
while True:
    r = f(n)
    print(r)
    n += 1
    if r > 100:
        break