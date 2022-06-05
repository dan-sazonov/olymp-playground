def f(n):
    n = bin(n)[2:]

    for _ in range(2):
        c_0 = n.count('0')
        c_1 = n.count('1')
        if c_0 == c_1:
            n = f'{n}{n[-1]}'
        c_0 = n.count('0')
        c_1 = n.count('1')
        n = f'{n}{"0" if c_0 < c_1 else "1"}'

    return int(n, 2)


n = 100
while True:
    r = f(n)
    if r % 4 == 0:
        print(n)
        break
    n += 1
