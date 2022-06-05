def f(n):
    s = bin(n)[2:]
    if n % 2 != 0:
        return f'11{s}11'
    else:
        return f'1{s}0'


n = 0
while True:
    r = int(f(n), 2)
    if r > 52:
        print(n)
        break
    n += 1
