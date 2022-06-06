def f(n):
    s = bin(n)[2:]
    s = f"{'0' * (8 - len(s))}{s}"

    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')

    d = int(s, 2)
    return d - n


n = 0
while True:
    r = f(n)
    if r == 133:
        print(n)
        break
    n += 1
