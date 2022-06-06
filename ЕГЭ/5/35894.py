def f(n):
    s = bin(n)[2:]

    for _ in range(3):
        if s.count('0') == s.count('1'):
            s += s[-1]
        elif s.count('0') > s.count('1'):
            s += '1'
        else:
            s += '0'

    return int(s, 2)


n = 105
while True:
    r = f(n)
    if r % 4 == 0:
        print(n)
        break
    n += 1
